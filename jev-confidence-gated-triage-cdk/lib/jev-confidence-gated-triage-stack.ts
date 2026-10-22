// Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

import { Stack, StackProps, Duration, CfnOutput, RemovalPolicy, Aws } from "aws-cdk-lib";
import { Construct } from "constructs";
import * as apigateway from "aws-cdk-lib/aws-apigateway";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as sfn from "aws-cdk-lib/aws-stepfunctions";
import * as tasks from "aws-cdk-lib/aws-stepfunctions-tasks";
import * as sqs from "aws-cdk-lib/aws-sqs";
import * as sns from "aws-cdk-lib/aws-sns";
import * as secretsmanager from "aws-cdk-lib/aws-secretsmanager";
import * as logs from "aws-cdk-lib/aws-logs";
import * as iam from "aws-cdk-lib/aws-iam";

/**
 * Confidence-gated ticket triage with TypeSafe Jev.
 *
 * Amazon API Gateway ingests a ticket. AWS Lambda sends the ticket state plus
 * three typed questions to the TypeSafe Jev System One model in one HTTPS call
 * and reads back typed decisions, each with a calibrated 0-1 confidence. The
 * AWS Lambda function starts an AWS Step Functions execution; a Choice state branches on the
 * confidence per action type. When every decision clears its threshold the
 * workflow auto-routes the ticket; when any decision is uncertain the ticket is
 * sent to an Amazon SQS human-review queue with the full Jev output attached.
 */
export class JevConfidenceGatedTriageStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // --- Amazon Secrets Manager: TypeSafe Jev API key ---------------------
    // The key value is NOT set here. Populate it after deployment (see README).
    const jevApiKeySecret = new secretsmanager.Secret(this, "JevApiKeySecret", {
      secretName: `${Aws.STACK_NAME}-jev-api-key`,
      description: "TypeSafe Jev API key for the confidence-gated triage pattern",
    });

    // --- Amazon SQS: human-review escape hatch (+ dead-letter queue) ------
    const humanReviewDlq = new sqs.Queue(this, "HumanReviewDlq", {
      queueName: `${Aws.STACK_NAME}-human-review-dlq`,
      enforceSSL: true,
      retentionPeriod: Duration.days(14),
    });

    const humanReviewQueue = new sqs.Queue(this, "HumanReviewQueue", {
      queueName: `${Aws.STACK_NAME}-human-review`,
      enforceSSL: true,
      visibilityTimeout: Duration.seconds(60),
      deadLetterQueue: { queue: humanReviewDlq, maxReceiveCount: 3 },
    });

    // --- Amazon SNS: security-incident paging topic -----------------------
    const securityPagingTopic = new sns.Topic(this, "SecurityPagingTopic", {
      topicName: `${Aws.STACK_NAME}-security-paging`,
      displayName: "Confidence-gated triage - security paging",
    });

    // --- AWS Lambda: the Jev decision function ----------------------------
    const decisionFn = new lambda.Function(this, "JevDecisionFunction", {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: "decision.handler",
      code: lambda.Code.fromAsset("src"),
      timeout: Duration.seconds(15),
      memorySize: 256,
      logRetention: logs.RetentionDays.ONE_WEEK,
      environment: {
        JEV_API_KEY_SECRET_ARN: jevApiKeySecret.secretArn,
        JEV_ENDPOINT: "https://api.typesafe.ai/v1/systemone",
      },
    });

    // Least-privilege: read only this one secret.
    jevApiKeySecret.grantRead(decisionFn);

    // --- AWS Step Functions: the confidence gate --------------------------
    // Terminal states for each routing outcome.
    const autoRoute = new sfn.Pass(this, "AutoRoute", {
      comment: "All decisions cleared their confidence thresholds - auto-route.",
      result: sfn.Result.fromObject({ outcome: "auto_routed" }),
      resultPath: "$.triage",
    });

    const pageSecurity = new tasks.SnsPublish(this, "PageSecurityOnCall", {
      topic: securityPagingTopic,
      message: sfn.TaskInput.fromJsonPathAt("$"),
      subject: "High-confidence security incident detected by triage",
      resultPath: "$.paging",
    }).next(autoRoute);

    const sendToHumanReview = new tasks.SqsSendMessage(this, "SendToHumanReview", {
      queue: humanReviewQueue,
      // Attach the full ticket + Jev output so a human sees the distribution.
      messageBody: sfn.TaskInput.fromJsonPathAt("$"),
      resultPath: "$.review",
    });

    // Confidence thresholds differ by stakes:
    //  - department routing is low-stakes  -> 0.6
    //  - urgency scoring                    -> 0.7
    //  - paging on-call for a security noul -> 0.9 (highest bar)
    const isConfidentSecurity = sfn.Condition.and(
      sfn.Condition.booleanEquals("$.decision.security.value", true),
      sfn.Condition.numberGreaterThanEquals("$.decision.security.confidence", 0.9)
    );

    const isConfidentRouting = sfn.Condition.and(
      sfn.Condition.numberGreaterThanEquals("$.decision.department.confidence", 0.6),
      sfn.Condition.numberGreaterThanEquals("$.decision.urgency.confidence", 0.7)
    );

    // Choice state IS the confidence gate - the headline of this pattern.
    const confidenceGate = new sfn.Choice(this, "ConfidenceGate", {
      comment: "Branch on Jev calibrated confidence per action type.",
    })
      .when(isConfidentSecurity, pageSecurity)
      .when(isConfidentRouting, autoRoute)
      .otherwise(sendToHumanReview);

    const stateMachine = new sfn.StateMachine(this, "TriageStateMachine", {
      stateMachineName: `${Aws.STACK_NAME}-triage`,
      definitionBody: sfn.DefinitionBody.fromChainable(confidenceGate),
      stateMachineType: sfn.StateMachineType.EXPRESS,
      timeout: Duration.minutes(5),
      tracingEnabled: true,
      logs: {
        destination: new logs.LogGroup(this, "TriageStateMachineLogs", {
          logGroupName: `/aws/vendedlogs/states/${Aws.STACK_NAME}-triage`,
          retention: logs.RetentionDays.ONE_WEEK,
          removalPolicy: RemovalPolicy.DESTROY,
        }),
        level: sfn.LogLevel.ALL,
      },
    });

    // Least-privilege: the AWS Lambda function may start ONLY this state machine (sync).
    decisionFn.addEnvironment("STATE_MACHINE_ARN", stateMachine.stateMachineArn);
    stateMachine.grantStartSyncExecution(decisionFn);

    // --- Amazon API Gateway: ingest endpoint ------------------------------
    const accessLogGroup = new logs.LogGroup(this, "ApiAccessLogs", {
      logGroupName: `/aws/apigateway/${Aws.STACK_NAME}-triage`,
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    const api = new apigateway.RestApi(this, "TriageApi", {
      restApiName: `${Aws.STACK_NAME}-triage`,
      description: "Confidence-gated ticket triage ingest endpoint",
      deployOptions: {
        stageName: "prod",
        accessLogDestination: new apigateway.LogGroupLogDestination(accessLogGroup),
        accessLogFormat: apigateway.AccessLogFormat.jsonWithStandardFields(),
        loggingLevel: apigateway.MethodLoggingLevel.INFO,
        metricsEnabled: true,
      },
    });

    const tickets = api.root.addResource("tickets");
    tickets.addMethod("POST", new apigateway.LambdaIntegration(decisionFn), {
      // Require an API key so the paid TypeSafe Jev calls and security pages
      // behind this endpoint cannot be driven anonymously.
      apiKeyRequired: true,
    });

    // --- API key + usage plan --------------------------------------------
    // The endpoint drives paid third-party (TypeSafe Jev) calls and can page
    // on-call, so it must not be publicly invokable. Callers present the key
    // in the `x-api-key` header. The usage plan also rate-limits abuse.
    const apiKey = api.addApiKey("TriageApiKey", {
      apiKeyName: `${Aws.STACK_NAME}-triage-key`,
      description: "Required to call POST /tickets",
    });

    const usagePlan = api.addUsagePlan("TriageUsagePlan", {
      name: `${Aws.STACK_NAME}-triage-usage-plan`,
      throttle: { rateLimit: 20, burstLimit: 40 },
    });
    usagePlan.addApiKey(apiKey);
    usagePlan.addApiStage({ stage: api.deploymentStage });

    // --- Outputs ----------------------------------------------------------
    new CfnOutput(this, "TicketsEndpoint", {
      description: "POST a ticket here to trigger confidence-gated triage",
      value: `${api.url}tickets`,
    });
    new CfnOutput(this, "JevApiKeySecretArn", {
      description: "Set the TypeSafe Jev API key on this Secrets Manager secret",
      value: jevApiKeySecret.secretArn,
    });
    new CfnOutput(this, "HumanReviewQueueUrl", {
      description: "Low-confidence tickets land here for human review",
      value: humanReviewQueue.queueUrl,
    });
    new CfnOutput(this, "SecurityPagingTopicArn", {
      description: "Subscribe to receive high-confidence security pages",
      value: securityPagingTopic.topicArn,
    });
    new CfnOutput(this, "TriageApiKeyId", {
      description:
        "API key id for POST /tickets. Retrieve the key value with: aws apigateway get-api-key --api-key <this-id> --include-value",
      value: apiKey.keyId,
    });
  }
}

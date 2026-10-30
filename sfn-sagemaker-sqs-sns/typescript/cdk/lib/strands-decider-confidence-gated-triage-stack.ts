// Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

import * as fs from "fs";
import * as path from "path";
import { Stack, StackProps, Duration, CfnOutput, RemovalPolicy, Aws } from "aws-cdk-lib";
import { Construct } from "constructs";
import * as ecrAssets from "aws-cdk-lib/aws-ecr-assets";
import * as iam from "aws-cdk-lib/aws-iam";
import * as logs from "aws-cdk-lib/aws-logs";
import * as sagemaker from "aws-cdk-lib/aws-sagemaker";
import * as sns from "aws-cdk-lib/aws-sns";
import * as sqs from "aws-cdk-lib/aws-sqs";
import * as sfn from "aws-cdk-lib/aws-stepfunctions";
import * as tasks from "aws-cdk-lib/aws-stepfunctions-tasks";

/**
 * Confidence-gated ticket triage with Strands Decider.
 *
 * An AWS Step Functions Express workflow calls an Amazon SageMaker AI endpoint that serves the
 * open-weight Strands Decider model, directly through the AWS SDK integration (no Lambda function).
 * The request holds three typed questions (questions.json): a `choice` for the owning department,
 * a `score` for urgency and a `noul` (yes/no) for "active security incident". A Choice state is
 * the confidence gate. It evaluates its rules in order and fails toward a person:
 *
 *   - no usable security answer (call failed, malformed)     -> human review
 *   - P(security incident) >= securityPageThreshold          -> page on-call (SNS) AND human review
 *                                                               (if the page fails: human review, with the reason)
 *   - no usable department answer                            -> human review
 *   - P(security incident) >  securityClearThreshold         -> human review (uncertain)
 *   - department confidence >= departmentThreshold           -> auto-route
 *   - anything else                                          -> human review
 *
 * The urgency score travels with the answers as a priority hint but does not gate: on the 30
 * synthetic tickets recorded for this pattern its confidence stayed between 0.2 and 0.5 whatever
 * the ticket. The thresholds are starting points. Measure them on your own traffic.
 */

const DEFAULTS = {
  // Hugging Face repo holding the Strands Decider adapter + head, pinned to a commit.
  checkpoint: "StrandsAgents/strands-decider-2B-hobson-v19",
  revision: "bb282d786bc251fd4e3068de3ada9ddbb38127cd",
  // The base model the adapter was trained on (Qwen/Qwen3.5-2B-Base), pinned to the commit that the
  // adapter's provenance.json records. The checkpoint itself names no revision.
  baseRevision: "b1485b2fa6dfa1287294f269f5fb618e03d52d7c",
  instanceType: "ml.m5.2xlarge",
  // Strands Decider's own routing convention: 0.9 or above acts without a check.
  departmentThreshold: 0.9,
  // Probability that the ticket reports an active security incident.
  securityPageThreshold: 0.7,
  securityClearThreshold: 0.3,
};

function numberContext(scope: Construct, key: keyof typeof DEFAULTS): number {
  const raw = scope.node.tryGetContext(key);
  const value = raw === undefined ? (DEFAULTS[key] as number) : Number(raw);
  if (!Number.isFinite(value) || value < 0 || value > 1) {
    throw new Error(`Context value "${key}" must be a number between 0 and 1 (got "${raw}")`);
  }
  return value;
}

function stringContext(scope: Construct, key: keyof typeof DEFAULTS): string {
  const raw = scope.node.tryGetContext(key);
  return raw === undefined ? (DEFAULTS[key] as string) : String(raw);
}

export class StrandsDeciderConfidenceGatedTriageStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // --- Gate configuration (override with `cdk deploy -c departmentThreshold=0.8`) -------------
    const departmentThreshold = numberContext(this, "departmentThreshold");
    const securityPageThreshold = numberContext(this, "securityPageThreshold");
    const securityClearThreshold = numberContext(this, "securityClearThreshold");
    if (securityClearThreshold >= securityPageThreshold) {
      throw new Error("securityClearThreshold must be lower than securityPageThreshold");
    }
    const checkpoint = stringContext(this, "checkpoint");
    const revision = stringContext(this, "revision");
    const baseRevision = stringContext(this, "baseRevision");
    const instanceType = stringContext(this, "instanceType");

    // --- Amazon SageMaker AI: the Strands Decider real-time endpoint ----------------------------
    // The container (./model) serves Strands Decider on CPU and downloads the model weights from
    // Hugging Face at startup. See the README for the trade-offs and the GPU note.
    const deciderImage = new ecrAssets.DockerImageAsset(this, "DeciderImage", {
      directory: path.join(__dirname, "..", "model"),
      platform: ecrAssets.Platform.LINUX_AMD64,
    });

    const sagemakerRole = new iam.Role(this, "DeciderExecutionRole", {
      assumedBy: new iam.ServicePrincipal("sagemaker.amazonaws.com"),
      description: "Execution role for the Strands Decider SageMaker endpoint",
    });
    deciderImage.repository.grantPull(sagemakerRole);
    sagemakerRole.addToPolicy(
      new iam.PolicyStatement({
        actions: ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents", "logs:DescribeLogStreams"],
        resources: [
          `arn:${Aws.PARTITION}:logs:${Aws.REGION}:${Aws.ACCOUNT_ID}:log-group:/aws/sagemaker/Endpoints/*`,
        ],
      })
    );

    const deciderModel = new sagemaker.CfnModel(this, "DeciderModel", {
      executionRoleArn: sagemakerRole.roleArn,
      primaryContainer: {
        image: deciderImage.imageUri,
        environment: {
          DECIDER_CHECKPOINT: checkpoint,
          DECIDER_REVISION: revision,
          DECIDER_BASE_REVISION: baseRevision,
          DECIDER_DEVICE: "cpu",
        },
      },
    });
    deciderModel.node.addDependency(sagemakerRole);

    const deciderEndpointConfig = new sagemaker.CfnEndpointConfig(this, "DeciderEndpointConfig", {
      productionVariants: [
        {
          variantName: "AllTraffic",
          modelName: deciderModel.attrModelName,
          instanceType,
          initialInstanceCount: 1,
          initialVariantWeight: 1,
          // Downloading ~4.5 GB of weights and loading them takes minutes on every start.
          containerStartupHealthCheckTimeoutInSeconds: 1800,
          volumeSizeInGb: 50,
        },
      ],
    });

    const deciderEndpoint = new sagemaker.CfnEndpoint(this, "DeciderEndpoint", {
      endpointConfigName: deciderEndpointConfig.attrEndpointConfigName,
    });

    // --- Amazon SQS: human-review queue (+ dead-letter queue) -----------------------------------
    // The dead-letter queue keeps messages longer than the queue they came from, as SQS recommends:
    // a message's retention clock starts when it is first enqueued, not when it is moved.
    const humanReviewDlq = new sqs.Queue(this, "HumanReviewDlq", {
      encryption: sqs.QueueEncryption.SQS_MANAGED,
      enforceSSL: true,
      retentionPeriod: Duration.days(14),
    });

    const humanReviewQueue = new sqs.Queue(this, "HumanReviewQueue", {
      encryption: sqs.QueueEncryption.SQS_MANAGED,
      enforceSSL: true,
      visibilityTimeout: Duration.seconds(60),
      retentionPeriod: Duration.days(7),
      deadLetterQueue: { queue: humanReviewDlq, maxReceiveCount: 3 },
    });

    // --- Amazon SNS: security-incident paging topic ---------------------------------------------
    const securityPagingTopic = new sns.Topic(this, "SecurityPagingTopic", {
      displayName: "Confidence-gated triage - security paging",
      enforceSSL: true,
    });

    // --- AWS Step Functions: ask the model, then apply the confidence gate -----------------------
    const questions = JSON.parse(fs.readFileSync(path.join(__dirname, "..", "questions.json"), "utf-8"));

    const tag = (name: string, outcome: string, reason: string) =>
      new sfn.Pass(this, name, {
        result: sfn.Result.fromObject({ outcome, reason }),
        resultPath: "$.gate",
      });

    const sendToHumanReview = new tasks.SqsSendMessage(this, "SendToHumanReview", {
      queue: humanReviewQueue,
      // The message carries the ticket, the model's full answers (every probability) and why the
      // gate escalated it, so the reviewer sees exactly which confidence fell short.
      messageBody: sfn.TaskInput.fromJsonPathAt("$"),
      resultPath: "$.review",
    });

    const pageOnCall = new tasks.SnsPublish(this, "PageSecurityOnCall", {
      topic: securityPagingTopic,
      subject: "Suspected security incident in a support ticket",
      // Ticket text is deliberately not in the page. The reviewer reads it from the review queue.
      message: sfn.TaskInput.fromObject({
        "ticket_id.$": "$.id",
        "security_probability.$": "$.model.response.answers.security_incident.noul",
      }),
      resultPath: "$.page",
    });

    // The error names of the SQS and SNS integrations do not separate transient from permanent causes (an
    // invalid parameter raises the generic SQS.AmazonSQSException), so the first retrier lists the errors that
    // a retry cannot fix (no permission, queue or topic missing) with no attempts, and everything else is
    // retried. States.TaskFailed matches every known error except States.Timeout. If the review queue stays
    // unreachable the execution fails, which the caller sees, rather than the ticket silently going nowhere.
    const retryOthers = { errors: ["States.TaskFailed"], interval: Duration.seconds(1), maxAttempts: 3, backoffRate: 2 };
    sendToHumanReview.addRetry({ errors: ["States.Permissions", "SQS.QueueDoesNotExistException"], maxAttempts: 0 });
    sendToHumanReview.addRetry(retryOthers);
    pageOnCall.addRetry({ errors: ["States.Permissions", "SNS.NotFoundException"], maxAttempts: 0 });
    pageOnCall.addRetry(retryOthers);

    const reviewUnavailable = tag("ReasonDecisionUnavailable", "review", "decision_unavailable").next(sendToHumanReview);
    // If the page cannot be published the ticket still goes to a person, and says why.
    const reviewPageFailed = tag("ReasonPageFailed", "review", "security_incident_page_failed").next(sendToHumanReview);
    pageOnCall.addCatch(reviewPageFailed, { errors: ["States.ALL"], resultPath: "$.page_error" });
    const reviewSecurity = tag("ReasonSecurityIncident", "paged_and_review", "security_incident_suspected")
      .next(pageOnCall)
      .next(sendToHumanReview);
    const reviewSecurityUncertain = tag("ReasonSecurityUncertain", "review", "security_uncertain").next(sendToHumanReview);
    const reviewLowConfidence = tag("ReasonLowConfidence", "review", "low_confidence").next(sendToHumanReview);
    const autoRoute = tag("AutoRoute", "auto_routed", "confident");

    // Direct AWS SDK integration: Step Functions serialises Body to JSON, calls InvokeEndpoint and
    // returns the response body as a string. This one state uses the JSONata query language (the rest
    // of the workflow is JSONPath, which a state machine may mix) because JSONata is the one that
    // lets the Catch below see an unparsable body. In JSONPath, States.StringToJson on a body that is
    // not JSON raises States.Runtime, which no Catch can handle, so the whole execution would fail and
    // the ticket would never reach the review queue. JSONata's $parse raises
    // States.QueryEvaluationError instead, which States.ALL catches.
    // The output keeps the shape the gate reads: the ticket fields plus model.response.
    const askDecider = tasks.CallAwsService.jsonata(this, "AskDecider", {
      service: "sagemakerruntime",
      action: "invokeEndpoint",
      // Rendered as Arguments in a JSONata state.
      parameters: {
        EndpointName: deciderEndpoint.attrEndpointName,
        ContentType: "application/json",
        Accept: "application/json",
        Body: { state: "{% $states.input.text %}", questions },
      },
      // The IAM action for InvokeEndpoint is in the sagemaker namespace. Ref returns the endpoint ARN.
      iamAction: "sagemaker:InvokeEndpoint",
      iamResources: [deciderEndpoint.ref],
      outputs: "{% $merge([$states.input, {'model': {'response': $parse($states.result.Body)}}]) %}",
      taskTimeout: sfn.Timeout.duration(Duration.seconds(60)),
    });
    // Retry throttling and the transient service errors. A ModelError (the container itself answered
    // with an error, for example 503 when it is busy) is not retried: a struggling container should
    // not be given more work.
    askDecider.addRetry({
      errors: [
        "SageMakerRuntime.ThrottlingException",
        "SageMakerRuntime.ServiceUnavailableException",
        "SageMakerRuntime.InternalFailureException",
      ],
      interval: Duration.seconds(2),
      maxAttempts: 2,
      backoffRate: 2,
    });
    // Fail closed: any other failure (model error, timeout, unparsable body) goes to a person.
    // The ticket fields travel on with the error added at $.error, as {Error, Cause}.
    askDecider.addCatch(reviewUnavailable, {
      errors: ["States.ALL"],
      outputs: "{% $merge([$states.input, {'error': $states.errorOutput}]) %}",
    });

    const answer = (field: string) => `$.model.response.answers.${field}`;
    const department = answer("department.confidence");
    const incident = answer("security_incident.noul");

    // The gate only trusts numbers it can see: present, numeric and inside [0, 1]. The security answer
    // is checked first and on its own, so a page never depends on another answer being well formed.
    const usable = (path: string) =>
      sfn.Condition.and(
        sfn.Condition.isPresent(path),
        sfn.Condition.isNumeric(path),
        sfn.Condition.numberGreaterThanEquals(path, 0),
        sfn.Condition.numberLessThanEquals(path, 1)
      );

    const confidenceGate = new sfn.Choice(this, "ConfidenceGate", {
      comment: "Fail closed: anything that is not clearly safe to automate goes to a person.",
    })
      .when(sfn.Condition.not(usable(incident)), reviewUnavailable)
      .when(sfn.Condition.numberGreaterThanEquals(incident, securityPageThreshold), reviewSecurity)
      .when(sfn.Condition.not(usable(department)), reviewUnavailable)
      .when(sfn.Condition.numberGreaterThan(incident, securityClearThreshold), reviewSecurityUncertain)
      .when(sfn.Condition.numberGreaterThanEquals(department, departmentThreshold), autoRoute)
      .otherwise(reviewLowConfidence);

    const invalidTicket = new sfn.Fail(this, "InvalidTicket", {
      error: "InvalidTicket",
      cause: 'The input must be {"id": "<string>", "text": "<string>"}',
    });

    const validateInput = new sfn.Choice(this, "ValidateInput")
      .when(
        sfn.Condition.and(
          sfn.Condition.isPresent("$.id"),
          sfn.Condition.isString("$.id"),
          sfn.Condition.isPresent("$.text"),
          sfn.Condition.isString("$.text")
        ),
        askDecider.next(confidenceGate)
      )
      .otherwise(invalidTicket);

    const stateMachine = new sfn.StateMachine(this, "TriageStateMachine", {
      definitionBody: sfn.DefinitionBody.fromChainable(validateInput),
      stateMachineType: sfn.StateMachineType.EXPRESS,
      timeout: Duration.minutes(3),
      logs: {
        destination: new logs.LogGroup(this, "TriageStateMachineLogs", {
          retention: logs.RetentionDays.ONE_WEEK,
          removalPolicy: RemovalPolicy.DESTROY,
        }),
        // Errors only, and never the execution data: the input carries ticket text.
        level: sfn.LogLevel.ERROR,
        includeExecutionData: false,
      },
    });

    // --- Outputs ---------------------------------------------------------------------------------
    new CfnOutput(this, "StateMachineArn", {
      description: "Start an execution with {\"id\": \"T-1\", \"text\": \"...\"}",
      value: stateMachine.stateMachineArn,
    });
    new CfnOutput(this, "DeciderEndpointName", {
      description: "SageMaker endpoint hosting Strands Decider (billed per hour while it exists)",
      value: deciderEndpoint.attrEndpointName,
    });
    new CfnOutput(this, "HumanReviewQueueUrl", {
      description: "Tickets the gate did not automate land here",
      value: humanReviewQueue.queueUrl,
    });
    new CfnOutput(this, "SecurityPagingTopicArn", {
      description: "Subscribe to receive security pages",
      value: securityPagingTopic.topicArn,
    });
  }
}

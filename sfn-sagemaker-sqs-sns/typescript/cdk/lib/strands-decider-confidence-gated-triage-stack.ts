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
 * The urgency score travels with the answers as a priority hint but does not gate. The thresholds
 * are starting points. Measure them on your own traffic.
 */

const DEFAULTS = {
  // Hugging Face repo holding the Strands Decider adapter + head. The repo has no tags, so it is
  // pinned to a commit. Strands Decider 0.2.0 takes the base model revision from the checkpoint's
  // provenance.json.
  checkpoint: "StrandsAgents/strands-decider-2B-hobson-v19",
  revision: "bb282d786bc251fd4e3068de3ada9ddbb38127cd",
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
    const instanceType = stringContext(this, "instanceType");

    // --- Amazon SageMaker AI: the Strands Decider real-time endpoint ----------------------------
    // The container (./model) serves Strands Decider on CPU and downloads the model weights from
    // Hugging Face at startup. See the Important Notes in the README.
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
    // The whole state machine uses the JSONata query language (queryLanguage on the StateMachine), so
    // every state reads its input as $states.input and writes its output with an `outputs` expression.
    const questions = JSON.parse(fs.readFileSync(path.join(__dirname, "..", "questions.json"), "utf-8"));

    // Add a value to the state: the output is the input plus one new top-level field.
    const withField = (field: string, value: string) => `{% $merge([$states.input, {'${field}': ${value}}]) %}`;

    const tag = (name: string, outcome: string, reason: string) =>
      sfn.Pass.jsonata(this, name, {
        outputs: withField("gate", `{'outcome': '${outcome}', 'reason': '${reason}'}`),
      });

    const sendToHumanReview = tasks.SqsSendMessage.jsonata(this, "SendToHumanReview", {
      queue: humanReviewQueue,
      // The message carries the ticket, the model's full answers (every probability) and why the
      // gate escalated it, so the reviewer sees exactly which confidence fell short.
      messageBody: sfn.TaskInput.fromText("{% $states.input %}"),
      outputs: withField("review", "$states.result"),
    });

    const pageOnCall = tasks.SnsPublish.jsonata(this, "PageSecurityOnCall", {
      topic: securityPagingTopic,
      subject: "Suspected security incident in a support ticket",
      // Ticket text is deliberately not in the page. The reviewer reads it from the review queue.
      message: sfn.TaskInput.fromObject({
        ticket_id: "{% $states.input.id %}",
        security_probability: "{% $states.input.model.response.answers.security_incident.noul %}",
      }),
      outputs: withField("page", "$states.result"),
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
    pageOnCall.addCatch(reviewPageFailed, {
      errors: ["States.ALL"],
      outputs: withField("page_error", "$states.errorOutput"),
    });
    const reviewSecurity = tag("ReasonSecurityIncident", "paged_and_review", "security_incident_suspected")
      .next(pageOnCall)
      .next(sendToHumanReview);
    const reviewSecurityUncertain = tag("ReasonSecurityUncertain", "review", "security_uncertain").next(sendToHumanReview);
    const reviewLowConfidence = tag("ReasonLowConfidence", "review", "low_confidence").next(sendToHumanReview);
    const autoRoute = tag("AutoRoute", "auto_routed", "confident");

    // Direct AWS SDK integration: Step Functions serialises Body to JSON, calls InvokeEndpoint and
    // returns the response body as a string. JSONata's $parse raises States.QueryEvaluationError on a
    // body that is not JSON, which the Catch below handles. (In JSONPath, States.StringToJson on such a
    // body raises States.Runtime, which no Catch can handle, so the execution would fail and the ticket
    // would never reach the review queue.)
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
      outputs: withField("model", "{'response': $parse($states.result.Body)}"),
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
    // The ticket fields travel on with the error added at `error`, as {Error, Cause}.
    askDecider.addCatch(reviewUnavailable, {
      errors: ["States.ALL"],
      outputs: withField("error", "$states.errorOutput"),
    });

    // The gate only trusts numbers it can see: a JSON number inside [0, 1]. Each condition is written so
    // that it is always true or false and never throws. A comparison on a missing field returns nothing
    // (not false), `$not()` of nothing is nothing, and a comparison on a non-number throws. Any of these
    // would end the execution with States.QueryEvaluationError, which a Choice state cannot catch. So the
    // test is `$type(x) = 'number'` first (a missing field gives nothing, and `nothing = 'number'` is
    // false), then the range, and "not usable" is the $not() of that always-boolean expression.
    // JSONata also looks inside an array at every step of a path (JSONPath does not), so each step down to
    // the number must be an object. A rule is only reached once the rules above it did not match, so the
    // plain comparisons below can rely on the answers they use being numbers in [0, 1].
    const response = "$states.input.model.response";
    const answer = (question: string, key: string) => `${response}.answers.${question}.${key}`;
    const usable = (question: string, key: string) =>
      [response, `${response}.answers`, `${response}.answers.${question}`]
        .map((step) => `$type(${step}) = 'object'`)
        .concat(
          `$type(${answer(question, key)}) = 'number'`,
          `${answer(question, key)} >= 0`,
          `${answer(question, key)} <= 1`
        )
        .join(" and ");
    const incident = answer("security_incident", "noul");
    const department = answer("department", "confidence");
    const when = (expression: string) => sfn.Condition.jsonata(`{% ${expression} %}`);

    // The security answer is checked first and on its own, so a page never depends on another answer
    // being well formed.
    const confidenceGate = sfn.Choice.jsonata(this, "ConfidenceGate", {
      comment: "Fail closed: anything that is not clearly safe to automate goes to a person.",
    })
      .when(when(`$not(${usable("security_incident", "noul")})`), reviewUnavailable)
      .when(when(`${incident} >= ${securityPageThreshold}`), reviewSecurity)
      .when(when(`$not(${usable("department", "confidence")})`), reviewUnavailable)
      .when(when(`${incident} > ${securityClearThreshold}`), reviewSecurityUncertain)
      .when(when(`${department} >= ${departmentThreshold}`), autoRoute)
      .otherwise(reviewLowConfidence);

    const invalidTicket = new sfn.Fail(this, "InvalidTicket", {
      error: "InvalidTicket",
      cause: 'The input must be {"id": "<string>", "text": "<string>"}',
    });

    // $type() is 'string' only for a string, so a missing, null or non-string field is refused. The
    // input must also be an object: for an array holding one ticket, `$states.input.id` would find the
    // id inside the array.
    const validateInput = sfn.Choice.jsonata(this, "ValidateInput")
      .when(
        sfn.Condition.jsonata(
          "{% $type($states.input) = 'object' and $type($states.input.id) = 'string' and $type($states.input.text) = 'string' %}"
        ),
        askDecider.next(confidenceGate)
      )
      .otherwise(invalidTicket);

    const stateMachine = new sfn.StateMachine(this, "TriageStateMachine", {
      definitionBody: sfn.DefinitionBody.fromChainable(validateInput),
      queryLanguage: sfn.QueryLanguage.JSONATA,
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

// Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

import { Stack, StackProps, Duration, CfnOutput, CfnParameter, Fn, RemovalPolicy, SecretValue } from "aws-cdk-lib";
import { Construct } from "constructs";
import * as apigateway from "aws-cdk-lib/aws-apigateway";
import * as events from "aws-cdk-lib/aws-events";
import * as logs from "aws-cdk-lib/aws-logs";
import * as sns from "aws-cdk-lib/aws-sns";
import * as sqs from "aws-cdk-lib/aws-sqs";
import * as sfn from "aws-cdk-lib/aws-stepfunctions";
import * as tasks from "aws-cdk-lib/aws-stepfunctions-tasks";

/**
 * Confidence-gated ticket triage with TypeSafe Jev.
 *
 * Amazon API Gateway starts an AWS Step Functions Express workflow synchronously. An HTTP Task
 * calls the TypeSafe Jev System One API through an Amazon EventBridge connection (the connection
 * holds the API key), so there is no AWS Lambda function. A Choice state is the confidence gate.
 * It evaluates its rules in order and fails toward a person:
 *
 *   1. no usable security answer (call failed, malformed)      -> review (decision_unavailable)
 *   2. security incident, confidence >= SECURITY_MIN           -> page (Amazon SNS), then review
 *                                                                 (if the page fails: review, with the reason)
 *   3. no usable department or urgency answer                  -> review (decision_unavailable)
 *   4. department >= DEPARTMENT_MIN and urgency >= URGENCY_MIN
 *      and the security value is false                         -> auto_routed
 *   5. anything else                                           -> review (low_confidence)
 */

// Confidence thresholds differ by stakes. They are written into the Choice state as fixed numbers,
// so a caller cannot change them; changing one is a stack update that touches only the state machine.
const DEPARTMENT_MIN = 0.6; // department routing is low stakes
const URGENCY_MIN = 0.7;
const SECURITY_MIN = 0.9; // paging on-call has the highest bar

const JEV_MODEL = "jev-latest";
const DEFAULT_JEV_API_ROOT = "https://api.typesafe.ai";

export class SfnChoiceJevStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // --- Configuration ------------------------------------------------------------------------
    // The Jev API key is a NoEcho parameter (npx cdk deploy --parameters JevApiKey=...). It never
    // appears in the synthesized template. The EventBridge connection stores it.
    const jevApiKey = new CfnParameter(this, "JevApiKey", {
      type: "String",
      noEcho: true,
      minLength: 1,
      maxLength: 500,
      description: "TypeSafe Jev API key (sent as 'Authorization: Bearer <key>')",
    });
    // Point the HTTP Task at another endpoint, for example a test double: -c jevApiRoot=https://...
    const jevApiRoot = String(this.node.tryGetContext("jevApiRoot") ?? DEFAULT_JEV_API_ROOT).replace(/\/+$/, "");
    if (!jevApiRoot.startsWith("https://")) {
      throw new Error(`Context value "jevApiRoot" must start with https:// (got "${jevApiRoot}")`);
    }

    // --- Amazon EventBridge: connection that holds the Jev API key -----------------------------
    // EventBridge keeps the credentials in a secret that it manages and sends them as a header on
    // every call. The HTTP Task may not set an Authorization header itself, but a connection may.
    const jevConnection = new events.Connection(this, "JevConnection", {
      description: "TypeSafe Jev API key",
      authorization: events.Authorization.apiKey(
        "Authorization",
        SecretValue.unsafePlainText(Fn.join(" ", ["Bearer", jevApiKey.valueAsString]))
      ),
    });

    // --- Amazon SQS: human-review queue (+ dead-letter queue) ----------------------------------
    // The dead-letter queue keeps messages longer than the queue they came from: a message's
    // retention clock starts when it is first enqueued, not when it is moved.
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

    // --- Amazon SNS: security-incident paging topic --------------------------------------------
    const securityPagingTopic = new sns.Topic(this, "SecurityPagingTopic", {
      displayName: "Confidence-gated triage - security paging",
      enforceSSL: true,
    });

    // --- AWS Step Functions: ask Jev, normalize the answers, apply the confidence gate ----------
    // The whole state machine uses JSONata (queryLanguage on the StateMachine), so every state reads
    // its input as $states.input. API Gateway starts the execution with {"body": <the ticket>, ...}.
    const withField = (field: string, value: string) => `{% $merge([$states.input, {'${field}': ${value}}]) %}`;

    const tag = (name: string, outcome: string, reason: string) =>
      sfn.Pass.jsonata(this, name, {
        outputs: withField("gate", `{'outcome': '${outcome}', 'reason': '${reason}'}`),
      });

    // The message carries the ticket, the Jev answers (when there are any) and why the gate sent it
    // here. The execution output, which API Gateway returns to the caller, leaves the ticket out.
    const sendToHumanReview = tasks.SqsSendMessage.jsonata(this, "SendToHumanReview", {
      queue: humanReviewQueue,
      messageBody: sfn.TaskInput.fromText("{% $string($states.input) %}"),
      outputs: `{% {
        'gate': $states.input.gate,
        'decision': $states.input.decision,
        'error': $states.input.error.Error,
        'page_message_id': $states.input.page.MessageId,
        'review_message_id': $states.result.MessageId
      } %}`,
    });

    // Ticket text stays out of the page: only the ticket id (when it is a string or a number) and the
    // probability. The reviewer reads the ticket from the review queue.
    const pageOnCall = tasks.SnsPublish.jsonata(this, "PageSecurityOnCall", {
      topic: securityPagingTopic,
      subject: "Suspected security incident in a support ticket",
      message: sfn.TaskInput.fromText(`{% $string({
        'ticket_id': $type($states.input.ticket.id) = 'string' or $type($states.input.ticket.id) = 'number'
          ? $string($states.input.ticket.id) : 'none',
        'security_probability': $states.input.jev.answers.security.noul
      }) %}`),
      outputs: withField("page", "$states.result"),
    });

    // The error names of the SQS and SNS integrations do not separate transient from permanent causes
    // (an invalid parameter raises the generic SQS.AmazonSQSException), so the first retrier lists the
    // errors that a retry cannot fix with no attempts, and everything else is retried. If the review
    // queue stays unreachable the execution fails, which the caller sees, instead of the ticket
    // silently going nowhere.
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
    const reviewLowConfidence = tag("ReasonLowConfidence", "review", "low_confidence").next(sendToHumanReview);
    const autoRoute = sfn.Pass.jsonata(this, "AutoRoute", {
      comment: "Replace with your own action, for example a call that assigns the ticket to the department.",
      outputs: `{% {
        'gate': {'outcome': 'auto_routed', 'reason': 'confident'},
        'decision': $states.input.decision
      } %}`,
    });

    // HTTP Task: POST the ticket and the three typed questions to Jev. The state is the ticket as a
    // JSON string. HTTP Task responses carry ResponseBody (a parsed object for a JSON response, a
    // string otherwise) and StatusCode; a non-2xx status raises States.Http.StatusCode.<code>.
    const askJev = tasks.HttpInvoke.jsonata(this, "AskJev", {
      apiRoot: jevApiRoot,
      apiEndpoint: sfn.TaskInput.fromText("v1/systemone"),
      method: sfn.TaskInput.fromText("POST"),
      connection: jevConnection,
      headers: sfn.TaskInput.fromObject({ "Content-Type": "application/json" }),
      body: sfn.TaskInput.fromObject({
        model: JEV_MODEL,
        state: "{% $string($states.input.body) %}",
        questions: {
          department: {
            type: "choice",
            instructions: "Which team should own this ticket",
            criteria: {
              billing: "Payment, invoicing, or subscription issues",
              technical_support: "Bugs, errors, or integration problems",
              account_security: "Compromised accounts, unauthorized access, or abuse",
              general: "Anything that does not fit the other categories",
            },
          },
          urgency: {
            type: "score",
            instructions: "How urgent is this ticket",
            criteria: [
              "Not time-sensitive; can wait",
              "Mildly time-sensitive",
              "Time-sensitive; should be handled today",
              "Urgent; actively blocking the customer",
              "Critical; severe or escalating business impact",
            ],
          },
          security: {
            type: "noul",
            instructions: "The ticket reports an active security incident",
          },
        },
      }),
      // $parse raises States.QueryEvaluationError on a body that is not JSON; the Catch below handles it.
      outputs:
        "{% {'ticket': $states.input.body, " +
        "'jev': $type($states.result.ResponseBody) = 'string' ? $parse($states.result.ResponseBody) : $states.result.ResponseBody} %}",
      // API Gateway waits at most 29 seconds for the synchronous execution, so one short attempt plus
      // one retry must fit inside that.
      taskTimeout: sfn.Timeout.duration(Duration.seconds(10)),
    });
    askJev.addRetry({
      errors: ["States.Http.StatusCode.429", "States.Http.StatusCode.502", "States.Http.StatusCode.503", "States.Http.StatusCode.504"],
      interval: Duration.seconds(1),
      maxAttempts: 1,
    });
    // Fail closed: any other failure (wrong key, 4xx, timeout, unparsable body) goes to a person.
    askJev.addCatch(reviewUnavailable, {
      errors: ["States.ALL"],
      outputs: "{% {'ticket': $states.input.body, 'error': $states.errorOutput} %}",
    });

    // Normalize the typed answers into {value, confidence} per question (null when an answer is not
    // usable). A usable confidence is a JSON number in [0, 1]. A noul answer is only a probability p:
    // value = p >= 0.5 and confidence = |p - 0.5| * 2, rounded to 6 places so 0.95 gives exactly 0.9.
    // Every step down to a number is checked to be an object, because JSONata looks inside arrays at
    // each step of a path and an unchecked path could read a value out of an array.
    const normalize = sfn.Pass.jsonata(this, "Normalize", {
      outputs: `{% (
        $num := function($v) { $type($v) = 'number' and $v >= 0 and $v <= 1 };
        $obj := function($v) { $type($v) = 'object' };
        $a := $obj($states.input.jev) and $obj($states.input.jev.answers) ? $states.input.jev.answers : {};
        $d := $obj($a.department) ? $a.department : {};
        $u := $obj($a.urgency) ? $a.urgency : {};
        $s := $obj($a.security) ? $a.security : {};
        $merge([$states.input, {'decision': {
          'department': $type($d.choice) = 'string' and $num($d.confidence)
            ? {'value': $d.choice, 'confidence': $d.confidence} : null,
          'urgency': $type($u.score) = 'number' and $num($u.confidence)
            ? {'value': $u.score, 'confidence': $u.confidence} : null,
          'security': $num($s.noul)
            ? {'value': $s.noul >= 0.5, 'confidence': $round($abs($s.noul - 0.5) * 2, 6)} : null
        }}])
      ) %}`,
    });

    const decision = "$states.input.decision";
    const when = (expression: string) => sfn.Condition.jsonata(`{% ${expression} %}`);
    const confidenceGate = sfn.Choice.jsonata(this, "ConfidenceGate", {
      comment: "Fail closed: anything that is not clearly safe to automate goes to a person.",
    })
      .when(when(`$type(${decision}.security) != 'object'`), reviewUnavailable)
      .when(when(`${decision}.security.value = true and ${decision}.security.confidence >= ${SECURITY_MIN}`), reviewSecurity)
      .when(when(`$type(${decision}.department) != 'object' or $type(${decision}.urgency) != 'object'`), reviewUnavailable)
      .when(
        when(
          `${decision}.department.confidence >= ${DEPARTMENT_MIN} and ${decision}.urgency.confidence >= ${URGENCY_MIN} ` +
            `and ${decision}.security.value = false`
        ),
        autoRoute
      )
      .otherwise(reviewLowConfidence);

    const stateMachineLogs = new logs.LogGroup(this, "TriageStateMachineLogs", {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY,
    });
    const stateMachine = new sfn.StateMachine(this, "TriageStateMachine", {
      definitionBody: sfn.DefinitionBody.fromChainable(askJev.next(normalize).next(confidenceGate)),
      queryLanguage: sfn.QueryLanguage.JSONATA,
      stateMachineType: sfn.StateMachineType.EXPRESS,
      timeout: Duration.minutes(2),
      logs: {
        destination: stateMachineLogs,
        // Errors only, and never the execution data: the input carries ticket text.
        level: sfn.LogLevel.ERROR,
        includeExecutionData: false,
      },
    });

    // --- Amazon API Gateway: synchronous front door ---------------------------------------------
    // The integration calls StartSyncExecution and returns the execution output as the response body
    // (HTTP 200), or HTTP 500 with the error and cause when the execution fails.
    const api = new apigateway.RestApi(this, "TriageApi", {
      description: "Confidence-gated ticket triage",
      cloudWatchRole: false,
      deployOptions: { stageName: "prod" },
    });
    api.root.addResource("tickets").addMethod(
      "POST",
      apigateway.StepFunctionsIntegration.startExecution(stateMachine, { querystring: false, path: false }),
      // The endpoint drives paid third-party calls and can page on-call, so callers must send an API key.
      { apiKeyRequired: true }
    );
    const apiKey = api.addApiKey("TriageApiKey", { description: "Required to call POST /tickets" });
    const usagePlan = api.addUsagePlan("TriageUsagePlan", { throttle: { rateLimit: 20, burstLimit: 40 } });
    usagePlan.addApiKey(apiKey);
    usagePlan.addApiStage({ stage: api.deploymentStage });
    api.node.tryRemoveChild("Endpoint"); // the stack outputs below replace the default URL output

    // --- Outputs --------------------------------------------------------------------------------
    new CfnOutput(this, "TicketsEndpoint", {
      description: "POST a ticket here (send the API key in the x-api-key header)",
      value: `${api.url}tickets`,
    });
    new CfnOutput(this, "TriageApiKeyId", {
      description: "Read the key value with: aws apigateway get-api-key --api-key <this id> --include-value",
      value: apiKey.keyId,
    });
    new CfnOutput(this, "HumanReviewQueueUrl", {
      description: "Tickets the gate did not automate land here",
      value: humanReviewQueue.queueUrl,
    });
    new CfnOutput(this, "SecurityPagingTopicArn", {
      description: "Subscribe to receive security pages",
      value: securityPagingTopic.topicArn,
    });
    new CfnOutput(this, "StateMachineArn", {
      description: "The Express workflow behind POST /tickets",
      value: stateMachine.stateMachineArn,
    });
    new CfnOutput(this, "StateMachineLogGroupName", {
      description: "Execution errors are logged here (execution data is off)",
      value: stateMachineLogs.logGroupName,
    });
  }
}

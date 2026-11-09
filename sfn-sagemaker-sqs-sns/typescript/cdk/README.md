# AWS Step Functions to Amazon SageMaker AI: confidence-gated decisions with Strands Decider

This pattern lets an AWS Step Functions Choice state decide whether to act on a model's answer. An AWS Step Functions Express workflow calls an Amazon SageMaker AI endpoint that serves [Strands Decider](https://github.com/strands-labs/strands-decider), an open-weight decision model that runs in your own AWS account, through the AWS SDK integration, with no AWS Lambda function in between. The example triages support tickets: the model answers three typed questions about a ticket, a Choice state auto-routes the ticket only when the model is confident, a suspected security incident pages on-call through Amazon SNS and still goes to a person, and everything else goes to an Amazon SQS human-review queue.

Strands Decider is a "system one" (decision) model. It does not generate text: you send it a `state` (here, the ticket) and typed questions, and it returns typed answers (the probability of a yes/no question, the chosen option of a `choice` with a confidence, or the level of an ordered `score`). Because the answers are numbers, they map directly onto a Choice state.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-sagemaker-sqs-sns-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example. The Amazon SageMaker AI endpoint is billed for every hour it exists, whether or not it serves requests, so delete the stack when you are done ([Cleanup](#cleanup)).

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 22 or later](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html), with your account and Region bootstrapped (`npx cdk bootstrap`). The commands below use `npx cdk`, which runs the CDK CLI version this project installs. An older global `cdk` can fail with "Cloud assembly schema version mismatch".
* A container builder that the AWS CDK can use (Docker, or [Finch](https://github.com/runfinch/finch) with `CDK_DOCKER=finch`). `npx cdk deploy` builds the model container for `linux/amd64`, which is slow on Apple silicon.
* Amazon SageMaker AI quota for one endpoint instance of the instance type you choose (default `ml.m5.2xlarge`; check Service Quotas, "ml.m5.2xlarge for endpoint usage")

## Supported Regions

The stack has no Region-specific values: it deploys to the Region of your AWS CLI profile or `AWS_REGION`, and its ARNs use the partition, Region and account of the stack. It was deployed and tested in us-west-2 only. In another Region, check that you have endpoint quota for the instance type there. The endpoint also needs outbound internet access to download the model (see Important Notes).

## Architecture

```
Ticket {"id": "...", "text": "..."}
        |
        v
AWS Step Functions Express workflow
  ValidateInput ---- invalid input ----> Fail: InvalidTicket
        |
  AskDecider (Amazon SageMaker AI endpoint: Strands Decider)
        |          call failed or unusable answer -------------------------+
        v                                                                   |
  ConfidenceGate (Choice state)                                             |
        |-- suspected security incident --> Amazon SNS page --+             |
        |                                                     v             v
        |-- uncertain or low confidence ----------------> Amazon SQS human-review queue --> dead-letter queue
        '-- confident ----------------------------------> auto-route (the workflow ends)
```

## How it works

1. `ValidateInput` fails the execution with `InvalidTicket` unless the input is `{"id": "<string>", "text": "<string>"}`.
2. `AskDecider` calls `InvokeEndpoint` on the Amazon SageMaker AI endpoint through the AWS SDK integration (`arn:aws:states:::aws-sdk:sagemakerruntime:invokeEndpoint`). Throttling and the transient service errors `ServiceUnavailable` and `InternalFailure` are retried twice. An error returned by the container itself (`SageMakerRuntime.ModelErrorException`) is not retried. Any other failure, including the 60-second timeout, is caught and the ticket goes to review as `decision_unavailable`.
3. `ConfidenceGate` is the Choice state (see [The gate](#the-gate)).
4. The outcome states tag the execution with `gate.outcome` and `gate.reason`. Tickets that need a person are sent to the Amazon SQS queue, and a suspected security incident is first published to the Amazon SNS topic. Both calls are retried up to three times, except for errors that a retry cannot fix (a missing queue or topic, or missing permission), which fail at once. If the page still fails, the ticket goes to the queue with the reason `security_incident_page_failed`. If the queue itself stays unreachable, the execution fails, so the caller knows the ticket was not queued.

Step Functions serialises the request `Body` to JSON and returns the response body as a string. The container is asked for JSON, and `AskDecider` parses the body with the JSONata `$parse` function. This one state uses the JSONata query language (the other states use JSONPath, and a state machine may mix them). A body that is not valid JSON raises `States.QueryEvaluationError`, which is caught and treated as "no usable answer". The equivalent JSONPath intrinsic function `States.StringToJson` raises `States.Runtime` for such a body, an error that no `Catch` can handle, so the whole execution would fail and the ticket would never reach the review queue (seen in a check with the Step Functions TestState API).

### The questions

The request holds the ticket as `state` and the three questions in `questions.json`:

```json
{
  "state": "<the ticket text>",
  "questions": {
    "department": {"type": "choice", "instructions": "Which team should handle this support ticket?",
                   "criteria": {"billing": "...", "technical": "...", "account_access": "...", "sales": "..."}},
    "urgency": {"type": "score", "instructions": "How urgent is this ticket for the customer?",
                "criteria": ["Low", "Medium", "High", "Critical"]},
    "security_incident": {"type": "noul", "instructions": "Does this ticket report an active security incident such as a compromised account or data being exfiltrated?"}
  }
}
```

The model reads the ticket once and answers all questions over the shared text. Labels and options are part of the request, so you can change the questions without retraining. A ticket longer than the model's window (4,096 tokens) is shortened; the questions keep their options.

### Model output

| Question type | Answer | Confidence |
|---|---|---|
| `choice` | the chosen option and a probability per option | top probability rescaled so an even split is 0 and a certain answer is 1 |
| `score` | an expected level and a probability per level | one minus the normalised spread of the distribution |
| `noul` | the probability that the statement is true | none returned; the gate uses the probability itself |

### The gate

The Choice state evaluates its rules in order and fails toward a person. An answer must be present, numeric and between 0 and 1. The security answer is checked first and on its own, so a paging decision never depends on another answer being well formed. A failed model call is caught earlier and goes to review directly as `decision_unavailable`.

| # | Rule | Outcome | Reason |
|---|---|---|---|
| 1 | no usable security answer (missing, not a number, or outside 0 to 1) | `review` | `decision_unavailable` |
| 2 | P(security incident) >= `securityPageThreshold` (default 0.7) | `paged_and_review`: SNS page, then the review queue (`review` / `security_incident_page_failed` if the page cannot be published) | `security_incident_suspected` |
| 3 | no usable department answer | `review` | `decision_unavailable` |
| 4 | P(security incident) > `securityClearThreshold` (default 0.3) | `review` | `security_uncertain` |
| 5 | department confidence >= `departmentThreshold` (default 0.9) | `auto_routed` | `confident` |
| 6 | anything else | `review` | `low_confidence` |

`auto_routed` ends the workflow: the `AutoRoute` state only tags the result. Replace it with your own action, for example a call that assigns the ticket to the chosen department.

The gate thresholds, the model revision and the instance type are AWS CDK context values, for example `npx cdk deploy -c departmentThreshold=0.8 -c securityPageThreshold=0.6 -c instanceType=ml.m5.4xlarge`. The thresholds are compiled into the state machine definition, so changing one is a stack update.

## Important Notes

* **Treat ticket text as untrusted.** The model reads it as part of its input. Do not let the model's answer be the only control on an irreversible action.
* **The container downloads weights from Hugging Face at startup,** about 4.6 GB each time the endpoint starts. To remove the runtime dependency, bake the weights into the image or stage them in Amazon S3.
* **Logs:** the state machine logs errors only and turns execution data off. An error message written by Step Functions can still quote part of the state, so treat the log group as sensitive. The page leaves the ticket text out. The review queue and the execution output contain the ticket; treat them accordingly.
* **One endpoint instance, one model worker, no autoscaling.** Requests are answered one at a time, so tickets sent together wait for each other. A request that waits more than 30 seconds for the model is refused with HTTP 503 and goes to review as `decision_unavailable`. Limit the number of concurrent tickets at the caller.
* **CPU only.** On CPU the upstream engine runs the model in float32 (about 7 GiB for the weights), much slower than on a GPU. GPU instances need a CUDA image and are not covered.
* **The model is an experiment.** It has 1.9 billion parameters. Upstream's [data/sources.md](https://github.com/strands-labs/strands-decider/blob/main/data/sources.md) lists every training source with its licence, and several state non-commercial terms or an unknown licence, so read it and the model card before you use the model commercially. Measure the model on your tickets.
* **Cap the ticket size at the caller.** Step Functions limits the data of a state to 256 KiB (a larger input fails the execution), and the model reads about 4,096 tokens whatever you send, so the rest of a long ticket is ignored. A long ticket also takes longer to answer: on `ml.m5.2xlarge` in us-west-2 a one-line ticket took about 3 seconds in the model and a ticket of about 8,000 characters about 19.5 seconds. A call that passes 60 seconds is cut off and the ticket goes to review, but the container keeps computing it, so later tickets wait behind it.
* **Updates need spare quota.** Changing the model revision or the instance type updates the endpoint: SageMaker AI starts the new instance before it deletes the old one, so you need quota for two instances while the update runs.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/sfn-sagemaker-sqs-sns/typescript/cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy the stack to your default AWS account and Region:
    ```bash
    npx cdk deploy
    ```
    The stack is ready when the Amazon SageMaker AI endpoint is `InService`. The container downloads and loads the model before it reports healthy, and the endpoint waits up to 30 minutes for that. In a test deployment to us-west-2 the endpoint was `InService` about 3.5 minutes after it was created, and the container needed about 50 seconds of that to download and load the model; building the `linux/amd64` image on an Apple silicon laptop with Finch took about 13 minutes. If the endpoint does not reach `InService`, the container logs to the log group `/aws/sagemaker/Endpoints/<endpoint name>`. Find it with `aws logs describe-log-groups --log-group-name-prefix /aws/sagemaker/Endpoints/`.

4. Note the outputs from the deployment: `StateMachineArn`, `DeciderEndpointName`, `HumanReviewQueueUrl`, `SecurityPagingTopicArn`. They are used for testing.

## Testing

1. Read the stack outputs into variables:
    ```bash
    out() { aws cloudformation describe-stacks --stack-name StrandsDeciderConfidenceGatedTriageStack --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
    SM=$(out StateMachineArn); QUEUE=$(out HumanReviewQueueUrl); TOPIC=$(out SecurityPagingTopicArn)
    ```

2. Subscribe to the paging topic before you send the security sample, for example by email (click the confirmation link in the message that Amazon SNS sends first, or no page arrives):
    ```bash
    aws sns subscribe --topic-arn $TOPIC --protocol email --notification-endpoint you@example.com
    ```

3. Start an execution with each sample ticket in `events/` and read the result:
    ```bash
    aws stepfunctions start-sync-execution --cli-read-timeout 0 --state-machine-arn $SM --input file://events/clear-ticket.json --query output --output text
    aws stepfunctions start-sync-execution --cli-read-timeout 0 --state-machine-arn $SM --input file://events/ambiguous-ticket.json --query output --output text
    aws stepfunctions start-sync-execution --cli-read-timeout 0 --state-machine-arn $SM --input file://events/security-ticket.json --query output --output text
    ```
    `--cli-read-timeout 0` stops the AWS CLI from giving up after its default 60 seconds and sending the request again, which would start a second execution. The output is the final state. `gate.outcome` and `gate.reason` tell you what the gate did, and `model.response.answers` holds the model's answers. If every ticket is `review` / `decision_unavailable`, read `error.Error` and `error.Cause` in the output: they hold the reason the model call failed. On the deployed endpoint (`ml.m5.2xlarge`, us-west-2) the three samples gave the values below, and the model needed about 3 seconds for each; yours can differ slightly.

    | Sample | `gate.outcome` / `gate.reason` | Model answers |
    |---|---|---|
    | `clear-ticket.json` | `auto_routed` / `confident` | department `account_access` (0.94), urgency score 1.80, P(security incident) 0.22 |
    | `ambiguous-ticket.json` | `review` / `low_confidence` | department `billing` (0.67), urgency score 1.85, P(security incident) 0.16 |
    | `security-ticket.json` | `paged_and_review` / `security_incident_suspected` | department `account_access` (0.80), urgency score 2.30, P(security incident) 0.91 |

4. Read the review queue. The ambiguous and security samples are there, with the full answers:
    ```bash
    aws sqs receive-message --queue-url $QUEUE --max-number-of-messages 10 --wait-time-seconds 10
    ```
    A call can return fewer messages than the queue holds, even with long polling (`--wait-time-seconds 10`): in a test the first call returned only the security ticket, and a call a minute later returned the ambiguous one, so call it again until you have seen both. A message that you receive is hidden from further receives for 60 seconds (the visibility timeout). Every receive without a delete counts toward the queue's `maxReceiveCount` of 3, after which the message moves to the dead-letter queue.

5. Send an invalid input to see the workflow refuse it. Expected: status `FAILED` and the error `InvalidTicket`:
    ```bash
    aws stepfunctions start-sync-execution --state-machine-arn $SM --input '{"text": "no id"}' --query '[status,error]' --output text
    ```

## Cleanup

1. Read the endpoint name before you delete the stack, because the stack outputs are gone afterwards:
    ```bash
    ENDPOINT=$(aws cloudformation describe-stacks --stack-name StrandsDeciderConfidenceGatedTriageStack --query "Stacks[0].Outputs[?OutputKey=='DeciderEndpointName'].OutputValue" --output text)
    ```

2. Delete the stack. This removes the endpoint, so the hourly charge stops. It also deletes the review and dead-letter queues and any tickets still in them, so read or move those first:
    ```bash
    npx cdk destroy
    ```

3. Amazon SageMaker AI creates the endpoint's log group itself, and the stack does not delete it. Delete it:
    ```bash
    aws logs delete-log-group --log-group-name /aws/sagemaker/Endpoints/$ENDPOINT
    ```

4. The container image stays in the AWS CDK bootstrap repository in Amazon ECR. Delete it there if you no longer need it.

5. Confirm the stack has been deleted:
    ```bash
    aws cloudformation describe-stacks --stack-name StrandsDeciderConfidenceGatedTriageStack
    ```
    Expected: an error that the stack does not exist.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

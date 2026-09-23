# Confidence-gated ticket triage with TypeSafe Jev

This pattern auto-triages inbound support tickets and acts on its own only when the model is genuinely sure. Amazon API Gateway ingests a ticket, an AWS Lambda function asks the TypeSafe Jev model three typed questions in one call, and an AWS Step Functions Choice state branches on the calibrated confidence of each answer. High-confidence tickets are routed automatically (and page on-call for a security incident); low-confidence tickets fall through to an Amazon SQS human-review queue.

TypeSafe Jev is a third-party "System One" model. You send it a state (any string or JSON) plus typed questions and it returns typed decisions, each with a calibrated 0-1 confidence, in a single HTTPS call. Because the confidence is a number your code can branch on, it maps one-to-one onto an AWS Step Functions Choice state. The model decides *what*, and its confidence decides *whether to act*.

> Important: this pattern calls a third-party service (TypeSafe Jev) that is not an AWS service. You need a TypeSafe account and API key, and Jev usage is billed by TypeSafe, separately from AWS.

TypeSafe documentation:
* [Introduction](https://docs.typesafe.ai/introduction) and [API reference](https://docs.typesafe.ai/api) - the System One endpoint, authentication, and the request/response contract this pattern uses.
* [Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) - TypeSafe's own write-up of the pattern this sample implements on AWS serverless.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/jev-confidence-gated-triage-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Architecture

```
                                           +--> (auto-route)
Amazon           AWS Lambda                |
API Gateway ---> (TypeSafe Jev  ---> AWS Step Functions --+--> Amazon SNS (page security on-call)
(POST /tickets)   decision)          Choice: confidence   |
                                     gate per action      +--> Amazon SQS (human review) --> DLQ
```

1. **Amazon API Gateway** exposes `POST /tickets` (protected by an API key and a usage plan) and forwards the ticket to the AWS Lambda function.
2. **AWS Lambda** reads the TypeSafe Jev API key from AWS Secrets Manager, sends the ticket state plus three typed questions (a `choice` for the owning department, a `score` for urgency, and a `noul` for the statement "the ticket reports an active security incident") to Jev in one HTTPS call, and normalizes the typed answers into `{ value, confidence }` per question.
3. The AWS Lambda function starts a synchronous **AWS Step Functions** Express execution.
4. The **Choice state** is the confidence gate. It auto-routes only when the department and urgency confidences clear their thresholds, pages on-call through **Amazon SNS** only when the security answer is `true` with confidence >= 0.9, and otherwise sends the ticket to the **Amazon SQS** human-review queue (backed by a dead-letter queue) with the full Jev output attached.

Confidence thresholds differ by stakes: low-stakes department routing uses 0.6, urgency scoring uses 0.7, and paging on-call for a security incident uses the highest bar, 0.9.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git installed](https://git-scm.com/downloads)
* [Node.js 20+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed and bootstrapped in your account and Region
* A [TypeSafe account](https://typesafe.ai/) and a Jev API key

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal, and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns/jev-confidence-gated-triage-cdk
    ```
3. Install dependencies:
    ```
    npm install
    ```
4. Deploy the stack to your default AWS account and Region:
    ```
    cdk deploy
    ```
5. Note the `TicketsEndpoint`, `JevApiKeySecretArn`, `HumanReviewQueueUrl`, `SecurityPagingTopicArn`, and `TriageApiKeyId` values from the stack outputs.
6. Set your TypeSafe Jev API key on the created AWS Secrets Manager secret (replace the ARN and key with your own):
    ```
    aws secretsmanager put-secret-value \
      --secret-id <JevApiKeySecretArn> \
      --secret-string "<your-typesafe-jev-api-key>"
    ```
7. Retrieve the Amazon API Gateway API key value (callers must send it in the `x-api-key` header):
    ```
    aws apigateway get-api-key --api-key <TriageApiKeyId> --include-value \
      --query value --output text
    ```

## How it works

A ticket lands on `POST /tickets`. The AWS Lambda function turns the ticket into the Jev `state`, asks three typed questions in a single call, and reads back a calibrated confidence for each answer. It starts a synchronous AWS Step Functions execution, and the Choice state decides the outcome purely from those confidences: auto-route, page security on-call, or hand off to a human. No text parsing, no malformed-JSON retries - the confidence number is the only thing gating autonomy.

### The Jev call

The AWS Lambda function calls the TypeSafe-native System One endpoint, `POST https://api.typesafe.ai/v1/systemone`, with the API key as a bearer token. (Jev is also reachable through OpenAI-compatible gateways such as OpenRouter by swapping the base URL and using their chat-completions shape; this pattern uses the native TypeSafe API directly, which is set in the `JEV_ENDPOINT` environment variable.)

The request sends the ticket as the `state` plus three typed questions - a `choice` for the owning department, a `score` for urgency, and a `noul` for whether the ticket reports a security incident:

```json
{
  "model": "jev-latest",
  "state": "{\"subject\":\"Cannot log in\",\"body\":\"Every reset email lands but the new password is rejected.\"}",
  "questions": {
    "department": {
      "type": "choice",
      "instructions": "Which team should own this ticket",
      "criteria": {
        "billing": "Payment, invoicing, or subscription issues",
        "technical_support": "Bugs, errors, or integration problems",
        "account_security": "Compromised accounts, unauthorized access, or abuse",
        "general": "Anything that does not fit the other categories"
      }
    },
    "urgency": {
      "type": "score",
      "instructions": "How urgent is this ticket",
      "criteria": [
        "Not time-sensitive; can wait",
        "Mildly time-sensitive",
        "Time-sensitive; should be handled today",
        "Urgent; actively blocking the customer",
        "Critical; severe or escalating business impact"
      ]
    },
    "security": {
      "type": "noul",
      "instructions": "The ticket reports an active security incident"
    }
  }
}
```

Jev returns an `answers` object keyed by question name, with type-specific fields:

```json
{
  "model": "jev-1.13.0",
  "answers": {
    "department": {
      "type": "choice",
      "choice": "technical_support",
      "confidence": 0.94,
      "probabilities": { "technical_support": 0.94, "billing": 0.04, "general": 0.02, "account_security": 0.0 }
    },
    "urgency": {
      "type": "score",
      "score": 3,
      "confidence": 0.81,
      "legend": { "0": "Not time-sensitive; can wait", "3": "Urgent; actively blocking the customer" },
      "probabilities": { "0": 0.02, "3": 0.81 }
    },
    "security": { "type": "noul", "noul": 0.03 }
  }
}
```

The AWS Lambda function normalizes each answer into `{ value, confidence }` for the Choice state to branch on:

* **choice** - `value` is `choice`, `confidence` is `confidence`.
* **score** - `value` is `score` (the level index), `confidence` is `confidence`.
* **noul** - Jev returns only a probability (`noul`), not a separate confidence. The function derives `value = noul >= 0.5` and `confidence = |noul - 0.5| * 2`, so a probability near 1.0 or 0.0 is a high-confidence decision and one near 0.5 is genuinely uncertain and falls to human review.

## Testing

The headline of this pattern is the confidence gate. These tests prove that the same ticket is handled differently based on Jev's confidence.

1. Confirm the Jev API key is set (Deployment step 6) and that you have the Amazon API Gateway API key value (Deployment step 7). The requests below send it in the `x-api-key` header.

2. Send a clear, high-confidence ticket and confirm it is auto-routed:
    ```
    curl -s -X POST <TicketsEndpoint> \
      -H "Content-Type: application/json" \
      -H "x-api-key: <your-api-key-value>" \
      -d '{"subject":"Cannot log in - password reset loop","body":"Every reset email lands but the new password is rejected."}'
    ```
   Expect an HTTP 200 response whose body includes `"status": "SUCCEEDED"` and a `triage` object with `"outcome": "auto_routed"`.

3. Send an ambiguous, low-confidence ticket and confirm it is escalated to human review:
    ```
    curl -s -X POST <TicketsEndpoint> \
      -H "Content-Type: application/json" \
      -H "x-api-key: <your-api-key-value>" \
      -d '{"subject":"question","body":"hi"}'
    ```
   The Choice state falls through to the Amazon SQS human-review queue. Confirm the message arrived:
    ```
    aws sqs receive-message --queue-url <HumanReviewQueueUrl>
    ```
   The message body contains the original ticket and the full Jev decision, including the low confidence that caused the escalation.

4. (Optional) Subscribe an email address to `<SecurityPagingTopicArn>` and send a ticket that clearly describes an active security incident to see the high-confidence security path page on-call through Amazon SNS.

## Cleanup

1. Delete the stack. This removes the Amazon API Gateway REST API, the AWS Lambda function, the AWS Step Functions state machine, the Amazon SQS queues, and the Amazon SNS topic:
    ```
    cdk destroy
    ```
   Warning: this permanently deletes the Amazon SQS queues (including any tickets still awaiting human review) and the AWS Secrets Manager secret holding your API key. Drain anything you need from the human-review queue first.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

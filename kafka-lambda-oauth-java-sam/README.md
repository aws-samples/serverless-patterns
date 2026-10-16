# Java AWS Lambda consumers for Apache Kafka with OAuth and IAM authentication

This serverless pattern collection shows how to deploy and run an AWS Lambda function, written in Java, with an Apache Kafka event source that authenticates without a username and password. Each of the three patterns uses a different authentication method: AWS Identity and Access Management (IAM) against Amazon Managed Streaming for Apache Kafka (Amazon MSK), OAuth 2.0 through an external identity provider, and OAuth with tokens issued by IAM.

All three use the same Java consumer: the AWS Lambda function decodes each Kafka record, logs it to Amazon CloudWatch Logs, and stores its fields in an Amazon DynamoDB table. Only the Kafka cluster, the authentication method, and the event source configuration differ.

## Patterns

| Pattern | Kafka cluster | Client authentication | Event source auth type | AWS Lambda credentials |
|---|---|---|---|---|
| [`iam_auth`](iam_auth/README.md) | Amazon MSK provisioned cluster | AWS IAM (`SASL/AWS_MSK_IAM`) | `IAM_AUTH` | The function's execution role. No secrets. |
| [`oauthbearer_auth`](oauthbearer_auth/README.md) | Self-managed Apache Kafka on Amazon EC2 | SASL/OAUTHBEARER, Amazon Cognito access tokens | `OAUTHBEARER_AUTH` | An OAuth 2.0 client ID and secret in AWS Secrets Manager. |
| [`iam_oauthbearer_auth`](iam_oauthbearer_auth/README.md) | Self-managed Apache Kafka on Amazon EC2 | SASL/OAUTHBEARER, AWS STS web identity tokens | `IAM_OAUTHBEARER_AUTH` | The function's execution role. No secrets. |

### [Amazon MSK with IAM authentication](iam_auth/README.md)

The function consumes from an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster that uses IAM access control. The cluster is attached as a self-managed Apache Kafka event source with the `IAM_AUTH` authentication type, so the event source mapping signs each connection with the function's execution role, and IAM policies grant access to the cluster, topic, and consumer group.

Use this pattern when your Kafka runs on Amazon MSK and you want IAM to handle both authentication and authorization.

### [Apache Kafka with OAuth through an external identity provider](oauthbearer_auth/README.md)

The function consumes from a self-managed Apache Kafka cluster on Amazon EC2 that authenticates clients with SASL/OAUTHBEARER. Amazon Cognito stands in for any OAuth 2.0 identity provider: the event source mapping obtains access tokens with the client credentials grant (`OAUTHBEARER_AUTH`), and the brokers validate them against the user pool's JSON Web Key Set.

Use this pattern when you already have an OAuth 2.0 identity provider, or clients outside AWS also need access to the cluster.

### [Apache Kafka with OAuth through AWS IAM](iam_oauthbearer_auth/README.md)

The function consumes from a self-managed Apache Kafka cluster on Amazon EC2 that authenticates clients with SASL/OAUTHBEARER, using tokens issued by AWS Identity and Access Management (IAM). With IAM outbound identity federation, the event source mapping obtains a signed web identity token for the function's execution role (`IAM_OAUTHBEARER_AUTH`); the brokers validate it against the account's AWS STS issuer and authorize the role through Kafka ACLs.

Use this pattern when your clients run on AWS and you want OAuth tokens on the Kafka side without operating an identity provider or storing secrets.

## How the patterns are deployed

Every pattern follows the same steps, described in detail in its README:

1. Deploy the pattern's AWS CloudFormation template. It creates the Kafka cluster, the supporting resources, and an Amazon EC2 client instance with the Kafka tools, the AWS SAM CLI, and the Java toolchain installed. The `JavaVersion` parameter selects the AWS Lambda runtime.
2. Connect to the client instance, **KafkaClientInstance**, with EC2 Instance Connect.
3. Deploy the AWS Lambda function and its event source with AWS SAM (`sam build`, then `sam deploy --guided`) or with the AWS CLI script in the pattern's `scripts` folder. `sam local invoke` tests the function locally against DynamoDB Local.
4. Send messages with `producer_send.sh`, then verify them in Amazon CloudWatch Logs and Amazon DynamoDB.
5. Delete the function with `sam delete` or the teardown script, then delete the AWS CloudFormation stack.

## Requirements

- An AWS account and an IAM principal with permissions to create the resources in the pattern's AWS CloudFormation template, including named IAM roles.
- The [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), if you deploy the templates from the command line.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

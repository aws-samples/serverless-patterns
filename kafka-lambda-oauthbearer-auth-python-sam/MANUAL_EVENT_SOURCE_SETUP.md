# Setting up the event source by hand — OAuth with an external identity provider

This is the plain-language version of what `scripts/deploy_lambda_oauth_cli.sh` does when it
creates the Lambda event source. Read this if you want to click through the console or type the
CLI command yourself instead of running the script.

## What you're actually configuring

An **event source mapping** (ESM) is the piece of Lambda that does the polling for you. You never
write consumer code that connects to Kafka — you tell Lambda "here are my brokers, here is my
topic, and here is how to prove who I am," and Lambda's poller logs in, reads messages, and hands
them to your function in batches.

In this pattern the poller logs in the way a machine-to-machine app logs into any OAuth 2.0 system:
it exchanges a **client ID and client secret** for a short-lived access token, then presents that
token to the brokers. Kafka calls this SASL/OAUTHBEARER.

## Before you start

You need four things ready. The CloudFormation stack in this pattern creates all of them, but if
you're doing it manually somewhere else, check them off:

1. **Brokers listening for encrypted OAuth connections** — SASL_SSL with the OAUTHBEARER
   mechanism, and the brokers must be set up to validate tokens from your identity provider.
2. **An OAuth app client that supports the client-credentials grant** — in this pattern it's an
   Amazon Cognito app client, but Okta, Keycloak, or anything else that issues JWTs works the same
   way. Note its client ID, client secret, token endpoint URL, and scope.
3. **Two secrets in AWS Secrets Manager** (details below).
4. **Your account allowlisted** for the new self-managed Kafka authentication types. Without this,
   creating the mapping fails outright.

## The two secrets

Lambda will not accept a client secret or a certificate typed into the mapping directly. You put
them in Secrets Manager and give Lambda the ARNs.

**Secret 1 — the OAuth credentials.** A JSON blob with exactly these three keys:

```json
{
  "oauthClientId": "1a2b3c4d5e6f7g8h9i0j",
  "oauthClientSecret": "the-app-client-secret",
  "oauthTokenEndpointUrl": "https://your-domain.auth.us-west-2.amazoncognito.com/oauth2/token"
}
```

**Secret 2 — the broker's certificate authority.** The poller connects over TLS and checks the
broker's certificate, so it needs the CA certificate that signed it. One key, `certificate`, whose
value is the PEM text:

```json
{ "certificate": "-----BEGIN CERTIFICATE-----\nMIID...\n-----END CERTIFICATE-----" }
```

If your brokers use a certificate from a well-known public CA, you can skip this secret. Self-signed
or private-CA certificates — which is what this pattern's brokers use — require it.

## What goes into the mapping

Six settings, then a list of "source access configurations" that carry the networking and auth bits.

| Setting | Value | Why |
|---|---|---|
| Event source type | Self-managed Apache Kafka | Not the MSK type, even if the brokers happen to be on EC2 |
| Bootstrap servers | `10.0.1.10:9092,10.0.2.10:9092,10.0.3.10:9092` | The SASL_SSL/OAUTHBEARER port, not a plaintext port |
| Topic name | `KafkaOAuthBearerLambdaTopic` | Exactly one topic per mapping |
| Consumer group ID | `lambda-oauth-consumer` | Lambda joins Kafka as this consumer group |
| Batch size | `10` | How many messages your function gets per invocation |
| Starting position | `TRIM_HORIZON` | Start from the oldest message the broker still has. Use `LATEST` to only get new messages |

The source access configurations are a list of type/value pairs. You need seven:

```
VPC_SUBNET                 subnet:subnet-0aaa...      <- one per subnet, three here
VPC_SUBNET                 subnet:subnet-0bbb...
VPC_SUBNET                 subnet:subnet-0ccc...
VPC_SECURITY_GROUP         security_group:sg-0ddd...  <- must be allowed to reach the brokers
OAUTHBEARER_AUTH           arn:aws:secretsmanager:...:secret:...-oauth-creds
OAUTHBEARER_SCOPE          kafka/consume
SERVER_ROOT_CA_CERTIFICATE arn:aws:secretsmanager:...:secret:...-broker-ca
```

The subnets and security group are how Lambda's poller gets network access to your private brokers —
Lambda creates network interfaces in those subnets on your behalf. The scope is the OAuth scope the
poller asks for; the brokers use it to decide what the token is allowed to do.

## Permissions the function's role needs

The poller borrows your function's execution role to do its work, so the role — not the function
code — needs these:

- **Read the two secrets**: `secretsmanager:GetSecretValue` on both ARNs.
- **Manage network interfaces**: `ec2:CreateNetworkInterface`, `ec2:DescribeNetworkInterfaces`,
  `ec2:DeleteNetworkInterface`, plus `ec2:DescribeSecurityGroups`, `ec2:DescribeSubnets`,
  `ec2:DescribeVpcs`.
- Whatever your own code needs. Here that's `dynamodb:PutItem` and `dynamodb:BatchWriteItem` on the
  target table.

Also grant the OAuth principal READ on the topic in Kafka itself. IAM controls what the role can do
in AWS; **Kafka ACLs** control what the authenticated principal can do on the cluster. They are two
separate systems and you need both.

## Provisioned pollers

This pattern sets a provisioned poller config:

```json
{ "PollerGroupName": "lambda-oauth-consumer-cell1", "MinimumPollers": 1, "MaximumPollers": 1 }
```

One dedicated poller, always running. Two things to know: the group name has to be fresh for each
VPC and event source type combination, and provisioned pollers bill by the hour whether messages
arrive or not.

## Checking that it worked

Watch for `State: Enabled`:

```bash
aws lambda list-event-source-mappings --function-name kafka-oauth-selfmanaged-consumer \
  --query 'EventSourceMappings[].[UUID,State,LastProcessingResult]' --output table
```

`Creating` for a minute or two is normal. If it lands in `Disabled` or `LastProcessingResult` shows
an error, the usual causes are: the security group can't reach the broker port, the broker rejects
the token (scope or issuer mismatch), the CA certificate doesn't match what the brokers present, or
the role can't read a secret. The function's CloudWatch log group is empty in all of those cases —
the failure happens before your code runs, so check the mapping's state first, not the logs.

# Setting up the event source by hand — IAM outbound identity federation

This is the plain-language version of what `scripts/deploy_lambda_oauth_cli.sh` does when it creates
the Lambda event source. Read this if you'd rather click through the console or type the CLI command
yourself.

## What you're actually configuring

An **event source mapping** (ESM) is the piece of Lambda that polls Kafka for you. You don't write
code that connects to the cluster — you tell Lambda where the brokers are, which topic to read, and
how to prove who it is. Lambda's poller logs in, reads messages, and hands them to your function in
batches.

What makes this pattern different from the plain OAuth one: **there is no identity provider and no
client secret**. AWS itself mints the token. The poller asks AWS STS for a signed OIDC token that
says "I am this Lambda execution role," and presents that to the brokers over SASL/OAUTHBEARER. The
brokers validate it against AWS STS's public keys, the same way they'd validate a token from Okta or
Cognito.

So you get OAuth-style authentication without running an identity provider or rotating a secret.
The trade-off is that the brokers have to be configured to trust AWS STS as an issuer.

## Before you start

1. **Outbound web identity federation enabled on your account.** One call, and it's safe to repeat:
   ```bash
   aws iam enable-outbound-web-identity-federation
   ```
2. **Brokers listening for encrypted OAuth connections** (SASL_SSL + OAUTHBEARER), configured to
   trust the AWS STS OIDC issuer — issuer URL of the form `https://<uuid>.tokens.sts.global.api.aws`
   with JWKS at `/.well-known/jwks.json` — and to require the audience value you pick below.
3. **One secret in Secrets Manager** holding the broker's CA certificate (details below).
4. **Your account allowlisted** for the new self-managed Kafka authentication types. Without this,
   creating the mapping fails outright.

## The one secret

The connection is still TLS, so the poller needs the CA certificate that signed the broker's
certificate. Put the PEM text in a Secrets Manager secret under the key `certificate`:

```json
{ "certificate": "-----BEGIN CERTIFICATE-----\nMIID...\n-----END CERTIFICATE-----" }
```

If your brokers present a certificate from a well-known public CA, you can skip this. Self-signed or
private-CA certificates — what this pattern's brokers use — require it.

## What goes into the mapping

| Setting | Value | Why |
|---|---|---|
| Event source type | Self-managed Apache Kafka | Not the MSK type |
| Bootstrap servers | `10.0.1.10:9092,10.0.2.10:9092,10.0.3.10:9092` | The SASL_SSL/OAUTHBEARER port |
| Topic name | `KafkaIamOAuthBearerLambdaTopic` | One topic per mapping |
| Consumer group ID | `lambda-iam-oauth-consumer` | Lambda joins Kafka as this consumer group |
| Batch size | `10` | Messages per invocation of your function |
| Starting position | `TRIM_HORIZON` | Oldest available message. `LATEST` for new messages only |

Then the source access configurations — six entries:

```
VPC_SUBNET                 subnet:subnet-0aaa...      <- one per subnet, three here
VPC_SUBNET                 subnet:subnet-0bbb...
VPC_SUBNET                 subnet:subnet-0ccc...
VPC_SECURITY_GROUP         security_group:sg-0ddd...  <- must be allowed to reach the brokers
IAM_OAUTHBEARER_AUTH       (no value)
OAUTHBEARER_AUDIENCE       kafka-cluster
SERVER_ROOT_CA_CERTIFICATE arn:aws:secretsmanager:...:secret:...-broker-ca
```

Two things that trip people up:

- **`IAM_OAUTHBEARER_AUTH` has no value.** It's a flag, not a pointer to a secret. In the CLI you
  write `{"Type":"IAM_OAUTHBEARER_AUTH"}` with no `URI` field at all.
- **`OAUTHBEARER_AUDIENCE` is required here** (it isn't used in the external-IdP pattern). The value
  is a label that you choose and that must match what the brokers are configured to expect. Get it
  wrong and the brokers reject an otherwise valid token.

The subnets and security group are how the poller reaches your private brokers — Lambda creates
network interfaces in those subnets for you.

## Permissions the function's role needs

The poller uses your function's execution role, so the role needs:

- **`sts:GetWebIdentityToken`** — this is the one that makes the whole pattern work. It's what lets
  the poller mint its own login token.
- **Read the CA secret**: `secretsmanager:GetSecretValue` on that ARN.
- **Manage network interfaces**: `ec2:CreateNetworkInterface`, `ec2:DescribeNetworkInterfaces`,
  `ec2:DeleteNetworkInterface`, `ec2:DescribeSecurityGroups`, `ec2:DescribeSubnets`,
  `ec2:DescribeVpcs`.
- Whatever your code needs — here, `dynamodb:PutItem` and `dynamodb:BatchWriteItem` on the table.

## Grant the role READ in Kafka too

IAM says what the role can do in AWS. **Kafka ACLs** say what the authenticated principal can do on
the cluster. You need both, and the Kafka half is easy to forget.

The principal name is the token's `sub` claim, which for this pattern is **the execution role's ARN**.
So the ACL looks like:

```bash
kafka-acls.sh --bootstrap-server <internal-listener> --add \
  --allow-principal "User:arn:aws:iam::123456789012:role/kafka-iam-oauth-consumer-role" \
  --operation Read --topic KafkaIamOAuthBearerLambdaTopic

kafka-acls.sh --bootstrap-server <internal-listener> --add \
  --allow-principal "User:arn:aws:iam::123456789012:role/kafka-iam-oauth-consumer-role" \
  --operation Read --group '*'
```

The consumer-group ACL matters as much as the topic one. A consumer that can read the topic but
can't join a group still fails.

## Provisioned pollers

```json
{ "PollerGroupName": "lambda-iam-oauth-consumer-cell1", "MinimumPollers": 1, "MaximumPollers": 1 }
```

One dedicated poller, always on. The group name must be fresh per VPC and event source type
combination, and provisioned pollers bill hourly whether or not messages arrive.

## Checking that it worked

```bash
aws lambda list-event-source-mappings --function-name kafka-iam-oauth-consumer \
  --query 'EventSourceMappings[].[UUID,State,LastProcessingResult]' --output table
```

Wait for `State: Enabled`. A couple of minutes in `Creating` is normal.

**One quirk worth knowing about.** The token AWS mints is valid for 300 seconds, and Kafka brokers
tie each authenticated session to the token's expiry. The poller re-authenticates on schedule, but
if a re-authentication lands late you'll see `Token expired at: ...` in the broker logs, and after
enough of those the mapping can flip to `Disabled`. Re-enable it with:

```bash
aws lambda update-event-source-mapping --uuid <uuid> --enabled
```

It isn't a mistake in your configuration.
The other two patterns in this set don't have it.

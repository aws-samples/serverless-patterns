# Setting up the event source by hand — Amazon MSK with IAM authentication

This is the plain-language version of what `scripts/deploy_lambda_iam_cli.sh` does when it creates
the Lambda event source. Read this if you'd rather click through the console or type the CLI command
yourself.

## What you're actually configuring

An **event source mapping** (ESM) is the piece of Lambda that polls Kafka for you. You don't write
code that connects to the cluster — you tell Lambda where the brokers are, which topic to read, and
how to prove who it is. Lambda's poller logs in, reads messages, and hands them to your function in
batches.

This is the simplest of the three patterns by a wide margin. There's **no secret, no certificate, and
no identity provider**. The poller signs its connection with the function's execution role using
SigV4 — the same signing every AWS API call uses — and MSK checks IAM to decide what that role may
do. Kafka calls the mechanism `AWS_MSK_IAM`.

## The one confusing bit, up front

Even though you're pointing at an Amazon MSK cluster, you configure this as a **self-managed Kafka**
event source, not the MSK event source type. You point it at MSK's IAM bootstrap endpoint and add an
`IAM_AUTH` flag.

That looks wrong the first time you see it. It's correct.

## Before you start

1. **An MSK cluster with IAM authentication turned on.**
2. **Your account allowlisted** for the new self-managed Kafka authentication types.

That's the whole list. Compare that to the certificate and secret juggling the other two patterns
need.

## Get the right bootstrap endpoint

MSK exposes several endpoints on different ports, and only one of them speaks IAM. Port **9098** is
the IAM one. Ask for it by name rather than copying a broker string from the console:

```bash
aws kafka get-bootstrap-brokers --cluster-arn <your-cluster-arn> \
  --query 'BootstrapBrokerStringSaslIam' --output text
```

Using port 9092 or 9096 here is the single most common mistake. The mapping will be created happily
and then fail to authenticate.

## What goes into the mapping

| Setting | Value | Why |
|---|---|---|
| Event source type | Self-managed Apache Kafka | Yes, even for MSK — see above |
| Bootstrap servers | The `BootstrapBrokerStringSaslIam` value | Port 9098 |
| Topic name | `KafkaIamLambdaTopic` | One topic per mapping |
| Consumer group ID | `lambda-iam-consumer` | Lambda joins Kafka as this consumer group |
| Batch size | `10` | Messages per invocation of your function |
| Starting position | `TRIM_HORIZON` | Oldest available message. `LATEST` for new messages only |

Then the source access configurations — five entries, and notice how short the list is:

```
VPC_SUBNET         subnet:subnet-0aaa...      <- one per subnet, three here
VPC_SUBNET         subnet:subnet-0bbb...
VPC_SUBNET         subnet:subnet-0ccc...
VPC_SECURITY_GROUP security_group:sg-0ddd...  <- must be allowed to reach the brokers on 9098
IAM_AUTH           (no value)
```

`IAM_AUTH` is a flag with no value — in the CLI, `{"Type":"IAM_AUTH"}` with no `URI` field. There's
no secret ARN and no `SERVER_ROOT_CA_CERTIFICATE` entry, because MSK's brokers use certificates from
a public CA that the poller already trusts.

The subnets and security group are how the poller reaches your cluster; Lambda creates network
interfaces in those subnets for you.

## Permissions the function's role needs

Here's where the interesting part moved. In the other two patterns, IAM handled AWS access and Kafka
ACLs handled cluster access. With MSK IAM auth, **IAM does both** — there are no ACLs to manage.

The `kafka-cluster:` actions are scoped to three different ARN shapes, and it matters which action
goes with which:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["kafka-cluster:Connect", "kafka-cluster:DescribeCluster"],
      "Resource": "arn:aws:kafka:us-west-2:123456789012:cluster/kafka-iam-cluster/*"
    },
    {
      "Effect": "Allow",
      "Action": ["kafka-cluster:DescribeTopic", "kafka-cluster:ReadData"],
      "Resource": "arn:aws:kafka:us-west-2:123456789012:topic/kafka-iam-cluster/*"
    },
    {
      "Effect": "Allow",
      "Action": ["kafka-cluster:AlterGroup", "kafka-cluster:DescribeGroup"],
      "Resource": "arn:aws:kafka:us-west-2:123456789012:group/kafka-iam-cluster/*"
    }
  ]
}
```

Three ARN prefixes — `cluster/`, `topic/`, `group/` — all built from the same cluster name. Topic
actions on a cluster ARN won't work, and vice versa.

`AlterGroup` sounds alarming for a read-only consumer, but joining a consumer group *is* altering it.
Without that permission the poller connects, reads nothing, and reports a group authorization error.

You also need the usual VPC networking permissions on the role — `ec2:CreateNetworkInterface`,
`ec2:DescribeNetworkInterfaces`, `ec2:DeleteNetworkInterface`, `ec2:DescribeSecurityGroups`,
`ec2:DescribeSubnets`, `ec2:DescribeVpcs` — plus whatever your own code does. Here that's
`dynamodb:PutItem` and `dynamodb:BatchWriteItem` on the target table.

To tighten this up for production, replace the `/*` wildcards with the specific topic and group
names instead of granting the whole cluster.

## Provisioned pollers

```json
{ "PollerGroupName": "lambda-iam-consumer-cell1", "MinimumPollers": 1, "MaximumPollers": 1 }
```

One dedicated poller, always on. The group name must be fresh per VPC and event source type
combination, and provisioned pollers bill hourly whether or not messages arrive.

## Checking that it worked

```bash
aws lambda list-event-source-mappings --function-name kafka-iam-consumer \
  --query 'EventSourceMappings[].[UUID,State,LastProcessingResult]' --output table
```

Wait for `State: Enabled`; a couple of minutes in `Creating` is normal.

When something's wrong, the error message tells you which permission is missing:

| What you see | What's missing |
|---|---|
| `Access denied` at connect time | `kafka-cluster:Connect` on the cluster ARN, or you're on the wrong port |
| `TopicAuthorizationException` | `kafka-cluster:ReadData` / `DescribeTopic` on the topic ARN |
| `GroupAuthorizationException` | `kafka-cluster:AlterGroup` / `DescribeGroup` on the group ARN |
| Nothing at all, mapping stuck | Security group can't reach the brokers on 9098 |

IAM changes can take a few seconds to take effect. If you just fixed a policy and the mapping still
complains, wait and look again before changing anything else.

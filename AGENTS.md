# Agent instructions

This repo holds serverless patterns published on [Serverless Land](https://serverlessland.com/patterns). New patterns use family folders that group variants of the same services, e.g. `sqs-lambda/python/sam`; older patterns use single top-level folders such as `sqs-lambda-python-sam`. See [folder structure](PUBLISHING.md#folder-structure) in PUBLISHING.md for the naming rules. Folders starting with `_` and `.github/` are repo tooling.

To create or change a pattern, follow the [pattern checklist](PUBLISHING.md#pattern-checklist) in PUBLISHING.md. These rules apply on top of it:

- Before writing a new pattern, search the repo for one with the same services, in both folder styles. If one exists, add a variant to its family instead of a duplicate.
- Work in one pattern variant folder only. Start from `_pattern-model/` or a similar existing pattern. If you copy a pattern, update every reference to the original: `example-pattern.json`, README, and resource and stack names.
- Don't edit `_scripts/pattern-schema.mjs`. It's generated from serverless-land. Don't edit other files in `_scripts/`, `_pattern-model/` or `.github/` unless asked.
- Before you finish, run the pattern file check and the framework's build or synth:

    ```bash
    cd _scripts && npm i && cd ..
    node _scripts/validate.js {pattern-folder}/example-pattern.json
    ```

- Use least-privilege IAM, e.g. SAM policy templates, instead of `*` actions or resources.
- Don't hardcode account IDs, Regions, ARNs or secrets. Use parameters, pseudo parameters or environment variables.
- Keep custom code short. A pattern shows how services connect.
- Stage files by name, e.g. `git add {pattern-folder}`. Don't use `git add .` or `git add -A`.

## Helper EC2 instances

Some patterns need a client inside a VPC to produce test data or reach a private resource, for example a Kafka producer for Amazon MSK, an Amazon MQ client or a database shell. When a pattern adds a helper EC2 instance:

- Put it in a private subnet and use the existing NAT for outbound access. Don't give it a public IP.
- Take the AMI from SSM, e.g. `/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64`, instead of a hardcoded AMI ID.
- Connect with Session Manager: attach `AmazonSSMManagedInstanceCore` to the instance role. Don't add a key pair, SSH ingress rules or Cloud9.
- Scope the instance role to the resources the pattern creates. Don't attach `*FullAccess`, `PowerUser` or admin managed policies.
- Include the stack name in resource names (secrets, configurations, log groups) so two stacks can deploy in the same Region.
- Describe how to connect and run the test in the README: `aws ssm start-session --target <instance-id>` or the EC2 console's Connect button.

See `rabbitmq-private-lambda-python-sam` for a scoped instance role.

### Kafka clients (Amazon MSK)

- Use a Kafka version that the [MSK supported versions page](https://docs.aws.amazon.com/msk/latest/developerguide/supported-kafka-versions.html) lists as supported for the broker type, for the cluster and the client.
- Download the client from the Apache archive with the Scala 2.13 build of that version: `https://archive.apache.org/dist/kafka/<version>/kafka_2.13-<version>.tgz`.
- For IAM auth, add the [aws-msk-iam-auth](https://github.com/aws/aws-msk-iam-auth/releases) jar and scope `kafka-cluster` actions to the pattern's cluster, topics and groups.
- Kafka 4 dropped `--zookeeper` and `--broker-list`. Use `--bootstrap-server` in README commands.

See `msk-lambda-iam-python-sam` for a full example.

### AWS IP ranges

If a pattern needs AWS IP ranges, for example to restrict a security group to a service's addresses, read the official list from `https://ip-ranges.amazonaws.com/ip-ranges.json`. Don't clone third-party copies of it.

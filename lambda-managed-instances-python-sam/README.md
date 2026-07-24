# Lambda Managed Instances with SAM (Python)

This pattern deploys a Python Lambda function running on AWS Lambda Managed Instances using CloudFormation. Lambda Managed Instances enables you to run functions on EC2 instances while AWS handles lifecycle management, patching, routing, and scaling. You benefit from EC2 pricing (Savings Plans, Reserved Instances) and multi-concurrency support.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/lambda-managed-instances-python-sam](https://serverlessland.com/patterns/lambda-managed-instances-python-sam)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

**Note**: Lambda Managed Instances provision EC2 instances that are **NOT eligible for the AWS Free Tier**. Instances incur charges immediately upon deployment.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) installed (v1.164.0+)
- [Python 3.13](https://www.python.org/downloads/) installed and available in your PATH

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```
   cd lambda-managed-instances-python-sam
   ```
1. From the command line, use AWS SAM to build and deploy:
   ```
   sam build
   sam deploy --guided
   ```
1. During the prompts:
   - Enter a stack name
   - Enter the desired AWS Region
   - Allow SAM CLI to create IAM roles with the required permissions.

   Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern creates:

1. **VPC with private subnets**: Two private subnets across availability zones for the capacity provider.

2. **Capacity Provider Operator IAM Role**: An IAM role with the `AWSLambdaManagedEC2ResourceOperator` managed policy that Lambda uses to provision and manage EC2 instances.

3. **Lambda Capacity Provider**: Defines where functions run — VPC config, instance architecture (ARM64/Graviton4), and the operator role for instance management.

4. **Lambda function on Managed Instances**: A Python function attached to the capacity provider via `CapacityProviderConfig`. Once a version is published, Lambda provisions instances and starts execution environments.

5. **Multi-concurrency**: Unlike default Lambda (1 invocation per environment), Managed Instances support multiple concurrent invocations per environment. The example uses thread-safe patterns to demonstrate this.

### When to use Managed Instances

- High-volume, predictable workloads (steady-state traffic)
- Cost optimization via EC2 Savings Plans or Reserved Instances
- Performance-critical apps needing specific CPU/network characteristics
- Regulatory requirements needing VPC placement control

### Key constraints

- Minimum `MemorySize` is 2048 MB (2 GB)
- A published version or alias is required for invocation
- Capacity provider scales within 5 minutes for traffic doubling

## Testing

1. Invoke the function via the `live` alias:

   ```bash
   aws lambda invoke \
     --function-name '<STACK_NAME>-api-handler' \
     --qualifier live \
     --cli-binary-format raw-in-base64-out \
     --payload '{"name": "Serverless Land"}' \
     /tmp/response.json && cat /tmp/response.json
   ```

2. Expected response:

   ```json
   {
     "statusCode": 200,
     "body": "{\"message\": \"Hello, Serverless Land!\", \"invocation\": 1, \"timestamp\": \"...\", \"version\": \"1\"}"
   }
   ```

3. Test multi-concurrency by invoking in parallel:
   ```bash
   for i in $(seq 1 10); do
     aws lambda invoke \
       --function-name '<STACK_NAME>-api-handler' \
       --qualifier live \
       --cli-binary-format raw-in-base64-out \
       --payload "{\"name\": \"Request-$i\"}" \
       /tmp/response-$i.json &
   done
   wait
   ```

## Cleanup

```bash
sam delete
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

# Amazon Bedrock IAM Cost Allocation with Lambda

This pattern deploys two Lambda functions with separately tagged IAM roles that invoke Amazon Bedrock. Costs are automatically attributed to each IAM principal in AWS Cost and Usage Report (CUR 2.0) and Cost Explorer.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/bedrock-iam-cost-allocation-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed

## How it works

Amazon Bedrock now supports cost allocation by IAM principal (April 2026). This pattern demonstrates:

- **Two Lambda functions** with separate IAM roles, each tagged with `team` and `cost-center`
- **Team A** (data-science, cost-center 10001) and **Team B** (engineering, cost-center 10002)
- Both invoke Bedrock — costs are automatically attributed to the calling IAM role in CUR 2.0
- After activating cost allocation tags in AWS Billing, you can filter by team in Cost Explorer

```
Team A Lambda (role: team=data-science) → Bedrock → CUR 2.0: attributed to Team A role
Team B Lambda (role: team=engineering)  → Bedrock → CUR 2.0: attributed to Team B role
```

## Deployment Instructions

1. Clone the repository and navigate to the pattern directory:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/bedrock-iam-cost-allocation-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy the stack:
    ```bash
    cdk deploy
    ```

## Testing

Invoke each team's function and compare costs in CUR 2.0:

```bash
# Team A invocation
aws lambda invoke --function-name <TeamAFunctionName> \
  --payload '{"prompt":"Explain serverless cost optimization in 2 sentences"}' \
  --cli-binary-format raw-in-base64-out output.json && cat output.json | python3 -m json.tool

# Team B invocation
aws lambda invoke --function-name <TeamBFunctionName> \
  --payload '{"prompt":"What is Amazon Bedrock? Answer in 2 sentences"}' \
  --cli-binary-format raw-in-base64-out output.json && cat output.json | python3 -m json.tool
```

## Activating Cost Allocation Tags

1. Open the [AWS Billing console](https://console.aws.amazon.com/billing/)
2. Navigate to **Cost allocation tags**
3. Find tags `team` and `cost-center` under the **IAM** category
4. Select and **Activate** them
5. Costs appear in Cost Explorer and CUR 2.0 within 24-48 hours

## Cleanup

```bash
cdk destroy
```

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

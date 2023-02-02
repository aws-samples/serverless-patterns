# Java REST API with Amazon API Gateway, RDS Postgres and AWS Lambda with SnapStart 

![Architecture diagram](./architecture.png)

A pattern to show how to use Lambda SnapStart with relational databases.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-lambda-rds-snapstart

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_install) (AWS CDK) installed
- jq

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```
   cd apigw-lambda-rds-snapstart
   ```
3. Build the database setup and unicorn functions
   ```
   ./mvnw clean package -f infrastructure/db-setup/pom.xml
   ./mvnw clean package -f software/unicorn-store/pom.xml
   ```
4. Deploy the infrastructure
   ```
   cd infrastructure/cdk
   cdk bootstrap
   cdk deploy UnicornStoreInfrastructure --require-approval never --outputs-file target/output.json
   ```
5. Execute the DB setup function to create the table
   ```
   aws lambda invoke --function-name $(cat target/output.json | jq -r '.UnicornStoreInfrastructure.DbSetupArn') /dev/stdout | cat;
   ```
6. Deploy the unicorn store
   ```
   cdk deploy UnicornStoreApp --outputs-file target/output.json --require-approval never
   ```

## Testing 

Create a new unicorn

```
curl --location --request POST $(cat target/output.json | jq -r '.UnicornStoreApp.ApiEndpoint')'/unicorns' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "name": "Something",
    "age": "Older",
    "type": "Animal",
    "size": "Very big"
}' | jq
```

## How it works



## Delete stack

```bash
cd infrastructure/cdk
cdk destroy --all
```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
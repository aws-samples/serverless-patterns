# AWS WAF to Appsync

This pattern creates an AppSync graphql API with dynamodb resolvers and protects the api with associating AWS WAF WebACL including managed rules for IP reputation lists and custom rule for blocking graphql schema introspections.

Learn more about this pattern at Serverless Land Patterns: [Serverless Land Pattern](https://serverlessland/patterns)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Cloud Development Kit](https://aws.amazon.com/cdk/) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```
   cd waf-appsync-cdk
   ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```
   cdk deploy --all
   ```

## How it works

This CDK application creates an AppSync graphql API, a demo DynamoDB table, a WAF WebACL with two rules, and associates the WebACL with the API.

## Testing

1. Deploy the stack and use a graphql client to query demos. 

```
query MyQuery {
  getDemos {
    id
    version
  }
}
```

2. Try to run an introspection query to see WAF WebACL rule in action.

```
query MyQuery {
  __schema {
    types {
      name
    }
  }
}
```

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```

---

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

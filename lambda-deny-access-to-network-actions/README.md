# Deny access to networking management from function code

[AWS Lambda](https://aws.amazon.com/lambda/) functions that require access to VPC resources utilize [private networking](https://docs.aws.amazon.com/lambda/latest/dg/foundation-networking.html) to access resources only accessible from a customer-owned VPC. The Lambda *service* requires AWS IAM permissions via the [Lambda function execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) to create elastic network interface(s) (ENI) and other networking components.

In this pattern, we explore an approach to deny access to those same networking management operations from Lambda *function* code. Customers who utilize Lambda to operate software-as-a-service platforms and those in highly-regulated industries may utilize this approach.

Begin by creating a Lambda function. [AWS SAM](https://aws.amazon.com/serverless/sam/) is used here but other infrastructure as code options can also be used.

``` yaml
TestFunction:
  Type: AWS::Serverless::Function
  Properties:
    Handler: test.handler
    Policies: 
      - VPCAccessPolicy:
          {}
    ...
```

The `VPCAccessPolicy` is a [SAM policy template](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-policy-templates.html) that provides the permissions needed for the Lambda service to create networking resources in the customer-owned VPC. The template is expanded on deployment (see docs for details).

A separate AWS IAM policy is then created and attached to the function execution role that includes a `DENY` statement and condition using the `lambda:SourceFunctionArn` key. Metadata is attached to AWS API calls from Lambda function code automatically that identify the ARN of the function. By using a deny policy, we prevent the actions included in the policy from being called *from* function code, but not the service itself.

> **Why a separate a policy?** A separate policy was created to avoid a circular dependency in the SAM template as the ARN of the function is used in the policy condition (though a wild card may also be acceptable).

``` yaml
DenyNetworkActionsFromFunctionPolicy:
  Type: AWS::IAM::Policy
  Properties:
    Roles:
      - !Ref TestFunctionRole
    PolicyName: DenyNetworkActionsFromFunctionPolicy
    PolicyDocument:
      Version: "2012-10-17"
      Statement:
        Effect: Deny
        Action:
          - "ec2:CreateNetworkInterface"
          - "ec2:DeleteNetworkInterface"
          - "ec2:DescribeNetworkInterfaces"
          - "ec2:DetachNetworkInterface"
          - "ec2:AssignPrivateIpAddresses"
          - "ec2:UnassignPrivateIpAddresses"
        Resource: "*"
        Condition:
          ArnEquals:
            lambda:SourceFunctionArn:
              - !GetAtt TestFunction.Arn
```

By adding the above poilcy to the function execution role, you effectively prevent function code from accessing the identified actions, such as deleting a networking interface (ENI) while allowing the Lambda service to perform necessary actions.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deploy

1. Clone the project to your local working directory

   ```sh
   git clone https://github.com/aws-samples/serverless-patterns
   ```

1. Change the working directory to this pattern's directory

   ```sh
   cd lambda-deny-access-to-network-actions
   ```

1. From the command line, use AWS SAM to build the serverless application with its dependencies

    ```
    sam build
    ```

1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:

    ```
    sam deploy --guided
    ```

1. At prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. This contains the Lambda function name for testing

## Testing

Use the AWS Console to create a new elastic network interface. Note the ENI ID and update the Lambda function environment variable configuration with that ENI ID.

Invoke the Lambda function.

## Cleanup

Delete the resources created in this pattern:

```sh
sam delete
```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

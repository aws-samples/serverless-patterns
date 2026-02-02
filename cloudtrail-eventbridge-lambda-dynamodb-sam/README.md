# Automated BYOIP Route Advertisement Removal

This pattern uses Amazon EventBridge to monitor for `AdvertiseByoipCidr` events and triggers an AWS Lambda Function to remove the route advertisement if the CIDR is not listed in an Amazon DynamoDB Table item configured by the end user.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/cloudtrail-eventbridge-lambda-dynamodb-sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the workflow as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name.
    * Enter the desired AWS Region.
    * Enter an email address for notifications when an IP address space has been advertised unexpectedly.
    * Allow SAM CLI to create IAM roles with the required permissions.
    * Accept all other defaults.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.
    ```
    Stack Name [sam-app]: byoip-advertisement-removal
    AWS Region [us-east-1]:
    Parameter NotificationEmail []: jrdwyer@amazon.com
    #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
    Confirm changes before deploy [y/N]: 
    #SAM needs permission to be able to create roles to connect to the resources in your template
    Allow SAM CLI IAM role creation [Y/n]: 
    #Preserves the state of previously provisioned resources when an operation fails
    Disable rollback [y/N]: 
    Save arguments to configuration file [Y/n]: 
    SAM configuration file [samconfig.toml]:
    SAM configuration environment [default]:
    ```

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

1. The list of IP ranges that are allowed to be advertised will need to be configured by the user by creating an item in the DynamoDB table created by the template.  The item should be entered in the following format:
```
{
  "id": {
    "S": "Allowed_CIDRs"
  },
  "CIDRs": {
    "L": [
      {
        "S": "CIDR1"
      },
      {
        "S": "CIDR2"
      },
      {
        "S": "CIDR3"
      },
      ...
    ]
  }
}
```


## How it works

EventBridge will trigger a rule any time the `AdvertiseByoipCidr` API call is logged via CloudTrail.  The Lambda function will check items in a DynamoDB table to determine if the BYOIP range is permitted to be publicly advertised and withdraw the advertisement if it is not permitted. 


## Testing

In Amazon VPC IP Address Manager (IPAM), enable advertisement of a BYOIP space that is not permitted to be advertised via the list of allowed IP ranges in DynamoDB.  If working as expected, the advertisement should be withdrawn within a few seconds after the CIDR has been advertised.

The following command can be used to advertise a CIDR that is not permitted to be advertised.

```aws ec2 advertise-byoip-cidr --cidr <value>```

After a few seconds, the following command should show a ```State``` of ```provisioned``` rather than ```advertised``` indicating that the advertisement has been removed.

```aws ec2 describe-byoip-cidrs --max-results 10```


## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
1. During the prompts:
    ```bash
        Are you sure you want to delete the stack byoip-advertisement-removal in the region us-east-1 ? [y/N]: y
        Are you sure you want to delete the folder byoip-advertisement-removal in S3 which contains the artifacts? [y/N]: y
    ```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

Amazon EventBridge to trigger AWS Lambda function to replicate FSx-OpenZFS volumes across file systems

The AWS SAM template deploys an Amazon EventBridge Scheduler to trigger an AWS Lambda function based on a user schedule to copy the snapshot of the volume and copy it to the target FSx system available in different AWS account and/or region.

For FSx-OpenZFS periodic volume replication in same account and same region, please refer to the Serverless Land Pattern <https://serverlessland.com/patterns/eventbridge-lambda-fsx-openzfs-periodic-replication>

The template contains a sample Lambda function that creates a snapshot of the source FSx VolumeID. Once the snapshot becomes available, it invokes another Lambda function in the destination AWS account or region, which will initiate the replication by calling copy_snapshot_and_update_volume API call. This solution will also notify users using a SNS topic for any errors and snapshot creation details.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create two AWS accounts for cross account setup](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have, create them and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) iinstalled and configure two profiles with credentials for the individual accounts as below:

    ```
    [default]
    [crossaccount]
    ```


- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
- Make sure that you have the ID of the source and destination volumes that you would like to initiate the replication between. For more information on these resources, see [Creating FSx for OpenZFS file systems](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/creating-file-systems.html), [Creating a volume](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/creating-volumes.html), [Creating a snapshot](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/snapshots-openzfs.html#creating-snapshots), and [Using on-demand data replication](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/on-demand-replication.html#how-to-use-data-replication).

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```
   cd eventbridge-lambda-fsx-openzfs-cross-account-region-periodic-replication
   ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```
   sam deploy --guided --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM CAPABILITY_NAMED_IAM -t destination-template.yaml --profile crossaccount
   ```
1. During the prompts:

   - Enter a target stack name
   - Enter the desired AWS Region
   - Enter a TargetVolumeID
   - Enter a CopySnapshotAndUpdateVolume - "Options" parameter. Comma (,) separated values
   - Enter a CopySnapshotAndUpdateVolume - "CopyStrategy" parameter (Default = INCREMENTAL_COPY)
   - Enter Source AWS Acctount Id
   - Allow SAM CLI to create IAM roles with the required permissions.
   - Save arguments to configuration file [Y/n]: Y
	- SAM configuration file [samconfig.toml]:
	- SAM configuration environment [default]: crossacct

   Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file, you can use `sam deploy` in future to use these defaults by adding `--config-env crossacct`.


1. Once the above stack is deployed in the target account/region, use AWS SAM to deploy the resources in source account using the source-template.yaml file.
   ```
   sam deploy --guided --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM CAPABILITY_NAMED_IAM -t source-template.yaml
   ```
1. During the prompts:

   - Enter a source stack name
   - Enter the desired AWS Region
   - Enter a SourceVolumeID
   - Enter a CRON schedule for snapshots (Default = [0 0/6 * * ? *] every six hours)
   - Enter a Value of snapshot Name (Default = fsx_scheduled_snapshot)
   - Enter an Email for notifications
   - Allow Success Notification (Default = Yes)
   - Enter Number of days to retain custom-scheduled snapshots (Default = 7 days)
   - Enter Target AWS Acctount Id
   - Enter Target Region
   - Enter Target stack name used previously

   Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file, you can use `sam deploy` in future to use these defaults.

2. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for later review.

## How it works

This pattern sets up the following resources:

- An Amazon EventBridge Scheduler that triggers a Lambda function based on the schedule defined by the customer to create snapshots of the provided FSx Source VolumeID.
- A sample [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function that creates snapshots of the source FSx VolumeID and invokes another Lambda function in the destination AWS account and/or region, which will initiate the replication by calling copy_snapshot_and_update_volume API call.
- The function also deletes the older snapshots in source and destination AWS account/region based on the retaintion period configured.
- An SNS topic that notifies for any success / failure notifications while creating snapshots.


## Testing

1. In the Outputs tab of the AWS CloudFormation console, note the `SNSTopic` , `EventBridgeScheduler` , `EventBridgeSchedulerRole` , `LambdaExecutionRole`, `LambdaFunction` outputs. Kindly provide all the requested details.
2. Based on the provided schedule, monitor the CloudWatch logs and the FSx snapshots that are created. 
3. The Lambda will automatically send notifications for any kinds of success/failure within the API calls to the configured email ID.


## Cleanup

 
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/eventbridge-lambda-fsx-openzfs-cross-account-region-periodic-replication
    ```
1. Delete all created resources in same account.
    ```
    sam delete --stack-name <stackname>
    ```
    
1. If API is deployed in cross account then run the same command again with the stackname that is deployed in different account along with --profile crossaccount
    ```
    sam delete --stack-name <stackname> --profile crossaccount --config-env crossacct
   ``````
1. During the prompts:
    * Enter all details as per requirement.

---

Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0


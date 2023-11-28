# Amazon EventBridge to trigger Lambda to perform volume replication across file systems

The SAM template deploys an Amazon EventBridge to trigger a Lambda function which will get periodic invocations based on user schedule to copy the snapshot of the volume and replicate them to the target FSx system. Users are also notified for snapshot creations and for any errors via SNS.

The template contains a sample Lambda function that receives the user input for source and target VolumeId. The Lambda function creates snapshots of the source FSx VolumeID and replicates them by performing copy_snapshot_and_update_volume call to the target VolumeId in same account and same region. The function also deletes the older snapshots. With the help of the SNS topic, the users will be notified for any errors and snapshot creation details.


Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
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
   cd eventbridge-lambda-fsx-openzfs-periodic-replication
   ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```
   sam deploy --guided --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM CAPABILITY_NAMED_IAM
   ```
1. During the prompts:

   - Enter a stack name
   - Enter the desired AWS Region
   - Enter a SourceVolumeID
   - Enter a TargetVolumeID
   - Enter a CRON schedule for snapshots (Default = [0 0/6 **?*] every six hours)
   - Enter a Value of snapshot Name (Default = fsx_scheduled_snapshot)
   - Enter a CopySnapshotAndUpdateVolume - "CopyStrategy" parameter (Default = INCREMENTAL_COPY)
   - Enter a CopySnapshotAndUpdateVolume - "Options" parameter. Comma (,) separated values
   - Enter an Email for notifications
   - Enter Number of days to retain custom-scheduled snapshots (Default = 7 days)
   - Allow SAM CLI to create IAM roles with the required permissions.

   Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for later review.

## How it works

This pattern sets up the following resources:

- An Amazon EventBridge rule that triggers a Lambda function based on the schedule defined by the customer to take create snapshots of the provided FSx VolumeID.
- A sample [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function that creates snapshots of the source FSx VolumeID and replicates them by performing copy_snapshot_and_update_volume call to the target VolumeId in same account and same region (https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/custom-snapshot-schedule.html).
- The function also deletes the older snapshots based on the retaintion period configured.
- An SNS topic that notifies for any failures while creating snapshots.
  

## Testing

1. In the Outputs tab of the AWS CloudFormation console, note the `SNSTopic` , `EventBridgeRule` , `LambdaExecutionRole`, `LambdaFunction` outputs. Kindly provide all the requested details.
2. Based on the provided schedule, monitor the CloudWatch logs and the FSx snapshots that are created. 
3. The Lambda will automatically send notifications for any kinds of failures within the API calls to the configured email ID.


## Cleanup

Delete the stack:

```bash
sam delete
```

---

Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

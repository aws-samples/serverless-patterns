# AWS EventBridge to AWS Systems Manager - State Manager Associations

This SAM template deploys a custom scheduled EventBridge task that triggers a SSM association that runs a custom 'Hello World!' SSM document. The EventBridge rule uses a cron schedule to run the SSM association every 15 minutes. The EC2 instances are deployed as targets for the SSM association using tag based rules. 

Learn more about this pattern at Serverless Land Patterns: https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html

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
    cd EventBridge-schedule-to-ssm-sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This SAM template deploys the resources and the IAM permissions required to run the application, including: an EventBridge Scheduler Task, SSM Document, SSM Association, two EC2 instances (Windows and Linux), and a S3 bucket to store the SSM association output. IAM execution roles are also created for EC2, SSM and EventBridge Scheduler.

The EventBridge Scheduler uses a cron expression to define how often the SSM association is executed. When run, the SSM association will run the custom 'Hello World!' SSM document, which executes simple echo commands on the Windows and Linux EC2 instances created by the SAM template. The SSM State Manager Association uses tag based rules to target the EC2 instance. Output of each Association execution is captured in the S3 bucket this template creates. The Cloud Formation output provides the names of the created resources.

When building the EventBridge Scheduler Task, we are using a universal target since SSM Associations do not have a pre-defined template. With universal targets you can target hundreds of AWS services APIs, a full list can be found within the [EventBridge Scheduler User Guide](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-targets-universal.html). Input for the universal target is well formatted JSON string containing the required keys and values for the API method being invoked.  Refer to the [AWS services' SDK documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html) to understand which information 'Input' requires as each API method contains different parameters.

## Testing

1.  Within the AWS console, navigate the [CloudFormation Stack](https://console.aws.amazon.com/cloudformation/home) that this SAM template created and make note of the names of the resources it created in the 'Outputs' 

2. Let's view the EventBridge Schedule, browse to EventBridge within the console

3. Select 'Schedules' under 'Scheduler' in the navigation pane

4. Select the schedule the SAM template created

5. Review the 'Schedule' section to see how often the task will run and when the next execution is scheduled for. The next 10 trigger dates should be displayed below the cron expression.

6. Next, click on the 'Target' section within the schedule to view the type of target we are invoking, the service, method (API) and the payload (Input)

7. Wait until the next scheduled time passes to validate the SSM State Manager Association is successfully run

8. Once the schedule task runs, you can verify it ran by browsing to [AWS Systems Manager](https://console.aws.amazon.com/systems-manager/home) within the console

9. Then click on 'State Manager' under 'Node Management' within the navigation pane

10. Select the association ID for the 'Cross-platform-Hello-World' association

11. Select 'Execution history' and verify the document ran successfully

12. Finally, navigate to the 'logs' folder within the S3 bucket. Each time the SSM Association runs it creates a new folder with the results of the execution. Select one of the runs, then select either of the instances it ran on, click on document task (awsrunPowerShellScript/awsrunShellScript) and name (runCommandsWindows/runCommandsLinux), then stdout file. 

*__Note:__ If you don't see any folder/files within the logs directory yet, the cron schedule may have not executed yet since the deployment. Wait 15 mins and check again.*


## Cleanup
 
1. Delete all objects in the S3 log bucket
     ```bash
    aws s3 rm s3://<bucket-name> --recursive
    ```

2. Delete the stack and SAM artifacts
    ```bash
    sam delete
    ```

    Select 'Y' to delete the stack and folder containing the artifacts


----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

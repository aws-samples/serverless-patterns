# Creating Slack subscription in SNS topic via Chatbot

This project contains source code and supporting files for a serverless application that you can deploy with the AWS Cloudformation or SAM. It includes the following files and folders.
​
The project creates a chatbot slack channel configuration which will be automatically subscribed to the SNS topic of your selection. 

## Pre-requisite:

--> Slack Channel ID (To get the ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ABCBBLZZZ.)
--> Workspace ID (To get the workspace ID, you must perform the initial authorization flow with Slack in the AWS Chatbot console. Then you can copy and paste the workspace ID from the console.)
--> IAM role that needs to be used
--> Topic(s) ARN
--> Name of the ChatBot channel configured

For more details, check the following documention on Setting Up AWS Chatbot with Slack in the AWS Chatbot User Guide.

[+] https://docs.aws.amazon.com/chatbot/latest/adminguide/slack-setup.html

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
```
git clone https://github.com/aws-samples/serverless-patterns
```
1. Change directory to the pattern directory:
```
cd Chat-with-slack-channel/
```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
```
sam deploy --guided
```
1. During the prompts:

    * Enter a stack name
    * Enter the desired AWS Region
    * Parameter ChannelName
    * Parameter IamRole
    * Parameter ChannelID
    * Parameter WorkspaceID
    * Parameter TopicARN

Once you have run sam deploy --guided mode once and saved arguments to a configuration file (samconfig.toml), you can use sam deploy in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Cleanup

1. Delete the stack
```
aws cloudformation delete-stack --stack-name STACK_NAME
```
2. Confirm the stack has been deleted
```
aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
```
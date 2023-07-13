This project contains source code and supporting files for a serverless application that you can deploy with the AWS Cloudformation. It includes the following files and folders.
​
The project creates a chatbot slack channel configuration which will be automatically subscribed to the SNS topic of your selection. 

Pre-requisite:
--> Slack Channel ID (To get the ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ABCBBLZZZ.)
--> Workspace ID (To get the workspace ID, you must perform the initial authorization flow with Slack in the AWS Chatbot console. Then you can copy and paste the workspace ID from the console.)
--> IAM role that needs to be used
--> Topic(s) ARN
--> Name of the ChatBot channel configured

For more details, check the following documention on Setting Up AWS Chatbot with Slack in the AWS Chatbot User Guide.

[+] https://docs.aws.amazon.com/chatbot/latest/adminguide/slack-setup.html


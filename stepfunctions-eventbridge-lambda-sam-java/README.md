## Description
## Step Functions - EventBridge - Lambda

This pattern creates two Lambda functions, an EventBridge custom event bus and event Rule, 
and a Step Functions Workflow using AWS SAM and Java 11.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred.

## Language:
#### This is a Maven project which uses Java 11 and AWS SDK

## Framework

The framework used to deploy the infrastructure is SAM

## Services used

The AWS services used in this pattern are
#### Step Functions - EventBridge - Lambda

Topology

<img src="topology.png" alt="topology" width="70%"/>


## Description
The SAM template contains all the information to deploy AWS resources(the Lambda functions, the EventBridge and the Step Functions workflow)
and also the permission required by these service to communicate.

You will be able to create and delete the CloudFormation stack using the CLI commands.

To test this pattern you need to start the State Machine ProcessOrder from your terminal or from AWS Console Step Function.
The state machine will invoke the OrderState Lambda function which will create a OrderCreated object which will be sent to a custom EventBridge Bus
and intercepted by an Event Pattern Rule.

The event pattern Rule will invoke the ProcessOrder Lambda function with the EventBridge message as a Payload.

You can see the event in the CloudWatch Logs - Log Group of the ProcessOrder Lambda function.

This is fully functional example implemented in Java 11.

## Deployment commands

````
mvn clean package

# create an S3 bucket where the source code will be stored:
aws s3 mb s3://poplkjs8392ksjii92ijsjs

# copy the source code located in the target folder:
aws s3 cp target/sourceCode.zip s3://poplkjs8392ksjii92ijsjs

# SAM will deploy the CloudFormation stack described in the template.yml file:
sam deploy --s3-bucket poplkjs8392ksjii92ijsjs --stack-name orders-stack --capabilities CAPABILITY_IAM

````

## Testing

Start the Step Functions state machine from your terminal and replace the AWS Region and Account with your details
```
aws stepfunctions start-execution --state-machine-arn arn:aws:states:YOUR_REGION:YOUR_AWS_ACCOUNT:stateMachine:ProcessOrders

```

In CloudWatch Logs - Log Groups you will see the output from the ProcessOrder lambda and the event.
```
i.e.:
Processing Order Event{version=0, id=f5c4cdcb-1c4d-ac11-c528-0c6da3be9fee, detail-type=OrderCreated, source=com.example.orders,
 account=YOUR_AWS_ACCOUNT, time=2022-02-13T14:28:18Z, region=YOUR_REGION, resources=[], detail={data=OrderId:123456789}}

```

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
aws cloudformation delete-stack --stack-name orders-stack

aws s3 rm s3://poplkjs8392ksjii92ijsjs --recursive

aws s3 rb s3://poplkjs8392ksjii92ijsjs
```

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed



## Author bio
Name: Razvan Minciuna
Linkedin: https://www.linkedin.com/in/razvanminciuna/
Description: Software Architect

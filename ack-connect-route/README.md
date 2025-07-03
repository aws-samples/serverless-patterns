## Websocket API Gateway acknowledgement for $connect route.

The SAM template deploys a websocket API Gateway and two Lambda functions required to run the application. This pattern deploys an Amazon API Gateway WebSocket API with a $connect route with a Lambda proxy integration which will invoke another Lambda function asynchronously and pass the Connection Id and the API Gateway stage URL to it. Then the Lambda function which got invoked asynchronously will check the validity of the connection. If the Connection Id is valid it will make an SDK API call to post a greeting to the client.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-lambda

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.


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
2. Change directory to the pattern directory:
    ```
    cd ack-connect-route
    ```
3. From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the template.yml file:

    ```
    sam build
    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.
          
         Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

Once the application is deployed, retrieve the WebSocketURL value from CloudFormation Outputs. To test the WebSocket API, you can use [wscat](https://github.com/websockets/wscat) which is an open-source command line tool.

1. [Install NPM](https://www.npmjs.com/get-npm).

2. Install wscat:
    ```
    $ npm install -g wscat
    ```

3. Connect to your WebSocketURL by executing the following command:
    ```
    $ wscat -c <YOUR WEBSOCKET URL>
    ```

4. To test the custom route and its associated function, send a JSON-formatted request like the following example. The Lambda function sends back the value of the "data" key using the callback URL:
```
$ wscat -c <YOUR WEBSOCKET URL>
connected (press CTRL+C to quit)
```
## Cleanup

1. Delete the stack
    ```
    aws cloudformation delete-stack --stack-name <YOUR STACK NAME>
    ```

2. Confirm the stack has been deleted
    ```
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'<YOUR STACK NAME>')].StackStatus"
    ```



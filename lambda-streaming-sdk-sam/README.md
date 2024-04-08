# Lambda Response streaming: Invoking a function with response streaming using the AWS SDK

This pattern shows how to use the AWS SDK to stream responses directly from the Lambda `InvokeWithResponseStream` API. This provides additional functionality compared to using an API such as handling midstream errors. For more information on the feature, see the [launch blog post](https://aws.amazon.com/blogs/compute/introducing-aws-lambda-response-streaming/).

Learn more about this pattern at Serverless Land Patterns: [lambda-streaming-sdk-sam](https://github.com/aws-samples/serverless-patterns/tree/main/lambda-streaming-sdk-sam)

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
    cd lambda-streaming-sdk-sam
    ```

1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:

    ```
    sam deploy -g --stack-name lambda-streaming-sdk-sam
    ```

1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region - AWS CLI default region is recommended if you are planning to run the test (test.sh) script
    * Allow SAM CLI to create IAM roles with the required permissions.

1. Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file `samconfig.toml`, you can use `sam deploy` in future to use these defaults.

AWS SAM deploys three Lambda functions with streaming support.
* **HappyPathFunction**: Returns a full stream.
* **MidstreamErrorFunction**: Simulates an error midstream.
* **TimeoutFunction**: Function times out before stream completes.

## Testing

1.	Run the SDK example application, which invokes each Lambda function and outputs the result.

    ```
    npm install @aws-sdk/client-lambda
    node index.mjs
    ```

You can see each function and how the midstream and timeout errors are returned back to the SDK client.

![Streaming midstream error](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2023/03/31/Streaming-midstream-error.png)
![Streaming timeout error](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2023/03/31/Streaming-timeout-error.png)

## Cleanup
 
1. Delete the stack, Enter `Y` to confirm deleting the stack and folder.
    ```
    sam delete
    ```
----
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
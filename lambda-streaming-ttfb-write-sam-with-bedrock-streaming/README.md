# Lambda Response streaming: time-to-first-byte using write() method

This pattern shows how to use Lambda response streaming ability and bedrock LLM streaming inference api to improve time-to-first byte using the write() method and `InvokeModelWithResponseStreamCommand`. For more information on the feature, see the [launch blog post](https://aws.amazon.com/blogs/compute/introducing-aws-lambda-response-streaming/).

Learn more about this pattern at Serverless Land Patterns: [lambda-streaming-ttfb-write-sam](https://github.com/aws-samples/serverless-patterns/tree/main/lambda-streaming-ttfb-write-sam)

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
    cd lambda-streaming-ttfb-write-sam-with-bedrock-streaming
    ```

1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:

    ```
    sam deploy -g --stack-name lambda-streaming-ttfb-write-sam-with-bredrock-streaming
    ```

1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region - AWS CLI default region is recommended if you are planning to run the test (test.sh) script
    * Allow SAM CLI to create IAM roles with the required permissions.

1. Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file `samconfig.toml`, you can use `sam deploy` in future to use these defaults.

AWS SAM deploys a Lambda function with streaming support and a function URL

![AWS SAM deploy --g](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2023/03/31/AWS-SAM-deploy-g.png)

The AWS SAM output returns a Lambda function URL.

![AWS SAM resources](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2023/03/31/AWS-SAM-resources.png)

## Testing

1.	Use curl with your AWS credentials to view the streaming response as the url uses AWS Identity and Access Management (IAM) for authorization. Replace the URL and Region parameters for your deployment.

    ```
    curl --request GET https://<url>.lambda-url.<Region>.on.aws/ --user AKIAIOSFODNN7EXAMPLE:wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY --aws-sigv4 'aws:amz:<Region>:lambda' -d '{"prompt": "hello! how are you?"}'
    ```

You can see the gradual display of the streamed response.

![Using curl to stream response from write() function](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2023/03/31/Using-curl-to-stream-response-from-write-function.png)

## Cleanup
 
1. Delete the stack, Enter `Y` to confirm deleting the stack and folder.
    ```
    sam delete
    ```
----
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
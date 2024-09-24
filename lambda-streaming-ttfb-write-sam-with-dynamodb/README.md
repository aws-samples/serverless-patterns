# AWS Lambda Response streaming: Streaming incremental Amazon DynamoDB Query results.

This pattern shows how to use Lambda response streaming to incrementally retrieve and stream DynamoDB query / scan results using the write() method. Instead of waiting for the entire query / scan operation to complete, the Lambda function streams data in batches by setting a limit on the number of items per query and sending each batch as soon as it's retrieved. This improves the time-to-first-byte (TTFB) by streaming results to the client as they become available.

For more information on the Lambda response streaming feature, see the [launch blog post](https://aws.amazon.com/blogs/compute/introducing-aws-lambda-response-streaming/).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

```
git clone https://github.com/aws-samples/serverless-patterns
```

1. Change directory to the pattern directory:

   ```
   cd lambda-streaming-ttfb-write-sam-with-dynamodb
   ```

1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:

   ```
   sam deploy -g --stack-name lambda-streaming-ttfb-write-sam-with-dynamodb
   ```

1. During the prompts:

   - Enter a stack name
   - Enter the desired AWS Region
   - Allow SAM CLI to create IAM roles with the required permissions.

1. After running `sam deploy --guided` mode once and saving arguments to a configuration file `samconfig.toml`, you can use `sam deploy` in future to use these defaults.

AWS SAM deploys a Lambda function with streaming support and a function URL

![AWS SAM deploy --g](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2023/03/31/AWS-SAM-deploy-g.png)

The AWS SAM output returns a Lambda function URL.

![AWS SAM resources](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2023/03/31/AWS-SAM-resources.png)

## How it works

The service interaction in this pattern uses AWS Lambda's response streaming capability to stream data in batches from Amazon DynamoDB. Instead of retrieving all query / scan results at once, the Lambda function processes the query incrementally, retrieving and sending results as they become available. Here are the details of the interaction:

1. Client Request
   A client sends a request to the Lambda URL, asking for specific data from a DynamoDB table.
2. Lambda Function Initialization :
   When the Lambda function is invoked, it initializes a connection to DynamoDB and prepares to run a query operation. The query includes a limit parameter, which restricts the number of items retrieved in each batch.
3. Querying
   The Lambda function begins querying DynamoDB using the defined limit (e.g., 100 items per batch). DynamoDB will return only a limited set of results instead of the entire result set at once.
4. Response Streaming
   As soon as a batch of results is retrieved, the function uses Lambda's streaming API `write()` method to send the data to the client. This happens immediately, without waiting for the entire query operation to complete.
5. Pagination Handling
   If DynamoDB returns a LastEvaluatedKey (which indicates that more data is available), the Lambda function automatically continues querying the next batch of data. Each batch is streamed to the client as it becomes available.
6. Final Response
   The Lambda function continues this process, retrieving a batch from DynamoDB and streaming it to the client until all data is fetched. Once DynamoDB returns no more data (i.e., no LastEvaluatedKey), the function sends the final batch and closes the stream.

## Testing

1. Run the data dump function to populate the DynamoDB table.

   Use curl with your AWS credentials as the url uses AWS Identity and Access Management (IAM) for authorization. Replace the URL and Region parameters for your deployment.

   ```
   curl --request GET https://<url-of-data-dump-lambda>.lambda-url.<Region>.on.aws/ --user AKIAIOSFODNN7EXAMPLE:wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY --aws-sigv4 'aws:amz:<Region>:lambda'
   ```

2. Run the streaming function to view the streaming response.

   Use curl with your AWS credentials to view the streaming response as the url uses AWS Identity and Access Management (IAM) for authorization. Replace the URL and Region parameters for your deployment.

   ```
   curl --request GET https://<url-of-streaming-lambda>.lambda-url.<Region>.on.aws/ --user AKIAIOSFODNN7EXAMPLE:wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY --aws-sigv4 'aws:amz:<Region>:lambda'
   ```

   You can see the gradual display of the streamed response.

## Cleanup

1. Delete the stack, Enter `Y` to confirm deleting the stack and folder.
   ```
   sam delete
   ```

---

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

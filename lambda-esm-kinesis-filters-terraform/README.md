# AWS Event Source Mapping for Lambda from Amazon Kinesis Data Stream (Terraform)

This pattern demonstrates the ability to filter Amazon Kinesis events so that only a subset of all events is sent to an AWS Lambda function for processing. Demo stack will create a single Amazon Kinesis Data Stream (kinesis_stream_lambda_esm) and two AWS Lambda functions (esm_lambda_with_filter and esm_lambda_with_no_filter), one with specific filter criteria and one without any filtering criterias, that are subscribed to that stream using different filter configurations.

Review [Filter Rule Syntax](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-syntax) for more details on the message filtering configuration.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/lambda-esm-kinesis-filters-terraform).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Clone the project to your local working directory

   ```sh
   git clone https://github.com/aws-samples/serverless-patterns/ 
   ```

2. Change the working directory to this pattern's directory

   ```sh
   cd serverless-patterns/lambda-esm-kinesis-filters-terraform
   ```

3. From the command line, initialize terraform to  to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```

4. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```

5. During the prompts:
   - Enter yes

## How it works

A new Amazon Kinesis Data Stream (kinesis_stream_lambda_esm) is created. Two AWS Lambda functions (esm_lambda_with_filter and esm_lambda_with_no_filter) that are subscribed to that stream with different filter settings. This way we demonstrate how various filtering settings affect which Amazon Kinesis Data Stream events are sent to each AWS Lambda function for processing.

All AWS Lambda functions use the same code for demo purposes.

The following considerations should be taken into account when working with Amazon Kinesis Data Stream events:

- Event payload is base64 encoded and Lambda function is responsible for decoding it before processing
- Event filtering for Amazon Kinesis Data Stream supports a subset of Amazon EventBridge event patterns, for example, Or (multiple fields) and Ends with didn't work
- Filter definition should not contain any whitespace (tabs, space, etc.) in order to work properly!

Note: The default region is `us-east-1`, it can also be changed using the variable `region`.

**Note:** Variables can be supplied in different options, check the [Terraform documentation](https://developer.hashicorp.com/terraform/language/values/variables) for more details.

## Testing

You can execute a test script to submit a number of test messages to the demo Kinesis Data Stream (stream-lambda-esm-filter).

    ```sh
        cd serverless-patterns/lambda-esm-kinesis-filters-terraform/test
        python stock.py
    ```

This script sends a series of test events to kinesis_stream_lambda_esm Kinesis Data Stream. It would generate the following sample events, 

{'event_time': '2023-08-31T11:44:06.359748', 'ticker': 'MSFT', 'price': 87.79} <br>
{'event_time': '2023-08-31T11:44:06.502610', 'ticker': 'TBV', 'price': 14.46} <br>
{'event_time': '2023-08-31T11:44:06.527346', 'ticker': 'AMZN', 'price': 65.42} <br>
{'event_time': '2023-08-31T11:44:06.553462', 'ticker': 'INTC', 'price': 48.72} <br>
{'event_time': '2023-08-31T11:44:06.576400', 'ticker': 'AMZN', 'price': 59.14} <br>

## Viewing Test Results

| Log Group | Pattern(s) | Match messages | Comment |
| --- | --- | --- | --- |
| /aws/lambda/esm_lambda_with_no_filter | | ALL | logs all test messages |
| /aws/lambda/esm_lambda_with_filter | {"data" = {"ticker" : ["AMZN"]}} | AMZN | logs events that matches the 'AMZN' ticker symbol only|         
   
## Cleanup

1. Change directory to the pattern directory:
    ```sh
    cd serverless-patterns/lambda-esm-kinesis-filters-terraform
    ```

2. Delete all created resources
    ```sh
    terraform destroy
    ```

3. During the prompts:
    * Enter yes

4. Confirm all created resources has been deleted
    ```sh
    terraform show
    ```

## Reference

- [AWS Lambda event source mappings](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html)
- [AWS Lambda event filtering](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html)

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
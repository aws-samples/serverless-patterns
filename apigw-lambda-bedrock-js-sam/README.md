# Amazon API Gateway to AWS Lambda to Amazon Bedrock using AWS SDK for JS and SAM

This sample project deploys an Amazon API Gateway REST API with an AWS Lambda integration. The Lambda function is written in TypeScript, calls the Amazon Bedrock API for Anthropic Claude Sonnet 4.5 model and returns a response containing the generated content.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-lambda-bedrock-js-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Prerequisite
Amazon Bedrock users need to request access to models before they are available for use. If you want to add additional models for text, chat, and image generation, you need to request access to models in Amazon Bedrock. Please refer to the link below for instruction:
[Model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```bash
   cd apigw-lambda-bedrock-js-sam
   ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```bash
   sam deploy --guided
   ```
4. During the prompts:

   - Enter a stack name
   - Enter the desired AWS Region
   - Allow SAM CLI to create IAM roles with the required permissions.

   Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

   When asked "`BedrockLambdaFunction` has no authentication. Is this okay? [y/N]", answer explicitly with y for the purposes of this sample application. As a result, anyone will be able to call this example REST API without any form of authentication.

   For production applications, you should [enable authentication for the API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html) using one of several available options and [follow the API Gateway security best practices](https://docs.aws.amazon.com/apigateway/latest/developerguide/security-best-practices.html).

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for next step as well as testing.
6. Run the `create_lambda_layer.sh`. You may have to change the file permission to make it executable.  This will create the lambda layer with the latest AWS SDK for JS for performing Bedrock API calls.
   ```bash
   ./create_lambda_layer.sh
   ```
7. Provide a name for the Lambda layer. Such as: 
   ```bash
   Enter the name of the Layer: awssdk-js-lambda-layer
   ```
   It will show output like below:
   ```bash
   Publishing the layer. Please wait ...
   {
    "Content": {
      .....
      .....
    },
    "LayerArn": "arn:aws:lambda:us-east-1:xxxxxxxxxxxx:layer:awssdk-js-lambda-layer",
    "LayerVersionArn": "arn:aws:lambda:us-east-1:xxxxxxxxxxxx:layer:awssdk-js-lambda-layer:1",
    "Description": "",
    "CreatedDate": "YYYY-MM-DDT10:47:36.983+0000",
    "Version": 1
   }
   ``` 
8. You may have to press `q` to come out of the output. Copy the value of `LayerVersionArn` from the above output and provide it into the next step. Such as:
   ```bash
   Enter the LayerVersionArn from the above command: arn:aws:lambda:us-east-1:xxxxxxxxxxxx:layer:awssdk-js-lambda-layer:1
   ```
9. Please copy the value of `BedrockLambdaFunction` from the `sam deploy --guided` output and provide that as response to next question. Such as:
   ```bash
   Enter the Lambda function name from the SAM deploy output: your-stack-name-BedrockLambdaFunctionXx-xxxxxxxxxxxx
   ```
   The script will now run aws cli command to add the newly created layer to the Lambda function. It will show output as below:
   It will show output like below:
   ```bash
   Adding the new layer to your Lambda function's configuration. Please wait ...
   {
      "FunctionName": "your-stack-name-BedrockLambdaFunctionXx-xxxxxxxxxxxx",
      ......
      ......
      "State": "Active",
      "LastUpdateStatus": "InProgress",
      "LastUpdateStatusReason": "The function is being created.",
      "LastUpdateStatusReasonCode": "Creating",
      "PackageType": "Zip",
      "Architectures": [
         "arm64"
      ],
      "EphemeralStorage": {
         "Size": 512
      }
   }      
   ```    
10. You may have to press `q` to come out of the output. The setup is ready for testing.

## How it works

This SAM project uses Amazon Bedrock API for Anthropic Claude Sonnet 4.5 model to generate content based on given prompt. This is exposed through a serverless REST API. Please refer to the architecture diagram below:
![End to End Architecture](images/architecture.png)

Here's a breakdown of the steps:

1. **Amazon API Gateway**: Receives the HTTP POST request containing the prompt.

2. **AWS Lambda**: Triggered by the API Gateway, this function forwards the prompt to Amazon Bedrock API using boto3 bedrock-runtime API. It uses Anthropic Claude Sonnet 4.5 model and sets other required parameters to fixed values for simplicity.

3. **Amazon Bedrock**: Based on the given prompt, using Anthropic Claude Sonnet 4.5 model generates the content and returns the response to Lambda.

4. **Response**: Lambda processes the Bedrock output and sends it back to the user via the API Gateway.

## Testing

Test the deployed content generation API by providing a prompt. You can use [curl](https://curl.se/) to send a HTTP POST request to the API. Make sure to replace `BedrockRestApi` with the one from your `sam deploy --guided` output:

```bash
curl -d '{"prompt": "Please write 5 lines on Solar Systems"}' -H 'Content-Type: application/json'  <BedrockRestApi>
```

The API returns a response with generated content. Such as (Your output may vary): 

```
{"model":"claude-sonnet-4-5-20250929","id":"msg_bdrk_01S1Rn7gPy3cdRt9aFWf255a","type":"message","role":"assistant","content":[{"type":"text","text":"# Five Facts About Solar Systems\n\n1. **Our Solar System** formed approximately 4.6 billion years ago from a giant rotating cloud of gas and dust called the solar nebula.\n\n2. **The Sun** contains 99.8% of the Solar System's total mass and provides the gravitational force that keeps all planets in orbit.\n\n3. **Eight planets** orbit our Sun in elliptical paths, divided into rocky terrestrial planets (Mercury, Venus, Earth, Mars) and gas/ice giants (Jupiter, Saturn, Uranus, Neptune).\n\n4. **Beyond Neptune** lies the Kuiper Belt, home to dwarf planets like Pluto and countless icy bodies left over from the Solar System's formation.\n\n5. **Scientists estimate** there are billions of other solar systems in our Milky Way galaxy alone, many potentially harboring planets in habitable zones."}],"stop_reason":"end_turn","stop_sequence":null,"usage":{"input_tokens":16,"cache_creation_input_tokens":0,"cache_read_input_tokens":0,"cache_creation":{"ephemeral_5m_input_tokens":0,"ephemeral_1h_input_tokens":0},"output_tokens":192}}
```

## Cleanup

1. To delete the resources deployed to your AWS account via AWS SAM, run the following command:

```bash
sam delete
```
2. Delete the Lambda layer version using the `delete_lambda_layer.sh` script. You may have to give execution permission to the file. You will need to pass the Lambda layer name and the version in the input when requested:
```bash
./delete_lambda_layer.sh
```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

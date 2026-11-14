# API Gateway WebSocket API to stream response from Bedrock

This pattern creates a WebSocket API and Lambda functions that provides a streaming response from the LLMs in Amazon Bedrock.

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
    cd apigw-websocket-api-bedrock/
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

This sample project demonstrates how to use WebSocket API as a front door to Lambda functions that perform inference on Amazon Bedrock LLMs using the [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html) API, where the LLM responses are returned in a stream. With WebSockets API, developers of interactive LLM chatbot interfaces can provide a better user experience by displaying the LLM responses as they are generated (which at times can be long), rather than relying on the synchronous [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) API request.

This template does not implement Authentication in WebSocket API to keep it simple. However, it is recommended to implement Authentication on WebSocket API.

## Testing

### Testing with `wscat` CLI

1. The stack will output the **WebSocketURL**. Use wscat to test the API (see [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-wscat.html) for more details on how to set it up):

    ```bash
    wscat -c < WebSocket URL from the stack >
    ```
1. Send a payload to the API in the correct format of the Model, otherwise you will receive a 'Forbidden' exception. The model in the template expects the request in below format:
    ```
    {"action":"invokeModel", "parameters":{"modelId": "anthropic.claude-v2", "temperature": 0}, "prompt": "\n\nHuman:Under 20 words, explain why the sky is blue?\n\nAssistant:"}
    ```

    > [!NOTE]  
    > For a list of Bedrock model IDs, please refer to [this documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids-arns.html). Specifically for Anthropic models, the prompt needs to follow a specific format, i.e. `\n\nHuman: {{Query Content}}\n\nAssistant:`. See the [prompt engineering guidelines](https://docs.aws.amazon.com/bedrock/latest/userguide/general-guidelines-for-bedrock-users.html) for Amazon Bedrock LLMs.

1. A successful invocation to Amazon Bedrock would return the LLM responses in multiple lines like below. Note that there is a custom message of `<End of LLM response>` to signify the end of the LLM response. This is useful to know when to stop receiving the message from the WebSocket API and close the connection.
    ```
    <  The
    <  sky appears blue due to the way the
    <  atmosphere sc
    < atters light from the
    <  sun.
    < <End of LLM response>
    ```

### Testing with Python websocket client

1. The stack will output the **WebSocketURL**. Note this URL as it is one of the required parameters to the Python script.

1. Run the `websocket-client.py` file with the following parameters:

    * `--websockets-url`: Use the WebSocket URL in the CloudFormation Stack output.
    * `--prompt`: Provide the user query to submit to the LLMs. Specifically for Anthropic models, the prompt needs to follow a specific format, i.e. `\n\nHuman: {{Query Content}}\n\nAssistant:`. See the [prompt engineering guidelines](https://docs.aws.amazon.com/bedrock/latest/userguide/general-guidelines-for-bedrock-users.html) for Amazon Bedrock LLMs.
    * `--model-id`: Amazon Bedrock model ID. For a list of Bedrock model IDs, please refer to [this documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids-arns.html). Defaults to `anthropic.claude-v2:1`.
    * `--temperature`: LLM temperature parameter to be used. Defaults to 0.

    ```python
    python3 websocket-client.py -w 'wss://u6731a4wn6.execute-api.us-east-1.amazonaws.com/prod/' -p '\n\nHuman:Under 100 words, explain why the sky is blue.\n\nAssistant:'
    ```

1. A successful invocation to Amazon Bedrock would return the LLM responses in batches that continue on the same line. 

    ```
    --Start of LLM response--

    Here is a 97-word explanation for why the sky appears blue:

    The sky appears blue because of the way air molecules in Earth's atmosphere interact with sunlight. As sunlight passes through the atmosphere, some of the light at the blue end of the visible spectrum is scattered by the air molecules more than other colors. The scattered blue light is what gives the sky its blue color. The amount of scattering depends on the wavelength of light - shorter wavelengths like blue and violet are scattered more. This effect is called Rayleigh scattering. With more blue light scattered to our eyes from all directions, the sky takes on a blue hue during the daytime.

    --End of LLM response--
    ```

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
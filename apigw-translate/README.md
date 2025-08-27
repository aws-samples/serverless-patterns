# Amazon API Gateway to Amazon Translate Integration

This pattern creates a REST API Gateway that can perform POST API Call to Amazon Translate's TranslateText API

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

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
    cd apigw-translate
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

This pattern deploys an Amazon API Gateway REST API with a /translate endpoint integrated with Amazon Translate’s TranslateText API. The service processes the provided text and language codes in the request body, returning the translated text or an error response if the specified language code is unsupported.

## Testing

Once the application is deployed, either use a curl or call the endpoint from Postman.

Example POST Request to translate text to Spanish:
```
    curl -X POST "https://YOUR_API_ID.execute-api.YOUR_AWS_REGION.amazonaws.com/Prod/translate" -H "Content-Type: application/json" -d '{"text": "Hello, world!", "sourceLanguageCode": "en", "targetLanguageCode": "es"}'
```

Response:
```
  {"SourceLanguageCode":"en","TargetLanguageCode":"es","TranslatedText":"¡Hola, mundo!"}
```

## Cleanup
 
1. In your command line, from the sam application project directory, run the following:
    ```bash
    sam delete

    ```

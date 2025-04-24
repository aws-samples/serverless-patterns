# Amazon API Gateway to Amazon Translate

This pattern creates a REST API Gateway that can perform POST API Call to Amazon Translate's TranslateText API 

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd apigw-translate-python-cdk
    ```
3. Create a virtual environment for Python:
    ```
    python3 -m venv .venv
    ```
4. Activate the virtual environment:
    ```
    source .venv/bin/activate
    ```
    For a Windows platform, activate the virtualenv like this:
    ```
    .venv\Scripts\activate.bat
    ```
5. Install the required Python dependencies:
    ```
    pip install -r requirements.txt
    ```
6. Bootstrap the AWS environment, if you haven't already done so:
    ```
    cdk bootstrap
    ```
7. Review the CloudFormation template AWS CDK generates for the stack:
    ```
    cdk synth
    ```
8. Deploy the AWS resources:
    ```
    cdk deploy
    ```
    
9. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.
The deployment will create a REST API Gateway.

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
 
To clean up the resources created as part of this demonstration, run the command `cdk destroy` in the directory `apigw-translate-python-cdk`. In addition, users are advised to terminate the Cloud9 EC2 instance to avoid any unexpected charges.

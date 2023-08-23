# s3-lambda-textract-comprehend-s3
![image](https://github.com/paulkannan/New-serverless-pattern-s3-lambda-textract-comprehend-s3/assets/46925641/f5dbe7a8-a9ef-423a-bf39-8ca201107b19)

This pattern demonstrates the usage of AWS serverless services to extract data from the uploaded document with Textract and validate the extracted data for Identification of Document by Comprehend confidence scores. If the Comprehend confidence score is >0.7, the submitted document is classified into valid Government issued ID otherwise as invalid ID. 

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>


Important: This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.


Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

To install the AWS Cloud Development Kit (CDK), you can use Python's package manager, pip. The CDK is available as a Python package that you can install globally on your system. Here's how you can install the CDK:

**Install npm (Node.js Package Manager):**
Before you install the CDK, you need to have Node.js and npm installed on your system, as the CDK CLI is built on top of npm. You can download Node.js and npm from the official Node.js website: https://nodejs.org/

**Install the AWS CDK using npm:**
Open a terminal or command prompt and run the following command to install the AWS CDK CLI: **npm install -g aws-cdk**
This command installs the CDK globally on your system, making it available as a command-line tool.

**Verify Installation:**
After the installation is complete, you can verify that the CDK CLI is installed by running the following command: **cdk --version**
This should display the version number of the CDK CLI, indicating that the installation was successful.

**Deployment Instructions**
Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
git clone https://github.com/aws-samples/serverless-patterns

Change directory to the pattern directory: **cd _patterns-model**

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3` (or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,you can create the virtualenv manually.

**To manually create a virtualenv on MacOS and Linux:**

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```
When you deploy a CDK application for the first time in an AWS region, you need to perform a one-time bootstrap process to create the necessary infrastructure for managing the deployment of CDK stacks.

```
$ cdk bootstrap
```
Finally to deploy an application:
```
$ cdk deploy
```
To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

**How it works**
When a file (pdf,jpeg, png) is uploaded to S3, the event will trigger a Lambda function (S3Event). The Lambda will pass the file to textract to extract the data. Textract will extract the contents and the output will be passed to Comprehend to identify the type of Document with entity & PII detection and confidence score. Based on the entity & PII detection, the documents are identified as valid Government ID (Driving License,Aadhaar, NREGA, PAN, Passport) or the uploaded file contains these information, identified documents are stored in S3 valid docs bucket and unidentified documents are stored in invalid docs folder.

**Testing**
Provide steps to trigger the integration and show what should be observed if successful.

**Cleanup**
Delete the stack
cdk destroy
Confirm the stack has been deleted
aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

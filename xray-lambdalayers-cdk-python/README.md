# How to set AWS XRay on Lambda using Layers with the CDK

# Overview

This CDK example sets up AWS X-Ray for a Lambda function that uses Lambda Layers. The example demonstrates the use of the folder structure for a Lambda layer written in Python, and using constructs for deploying and using the layer and X-Ray. 

Important: This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/)  for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

# Requirements

 * [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html)  if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
 * [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)  installed and configured
 * [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
 * [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK >= 2.1.0) installed

# Python Setup

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
.venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
pip install -r requirements.txt
```
To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command. 

# How to Run X-Ray on the Lambda function using layers

# Deployment Instructutions
1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

```
git clone https://github.com/aws-samples/serverless-patterns
```

2. Change directory to the pattern directory:

```
cd serverless-patterns/xray-lambdalayers-cdk-python
```

3. Create a [lambda layer](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda/README.html#layers) for AWS X-Ray.
To do this we'll install the python dependencies inside this folder: `lambda_layer_x_ray_stack/layers/`:

```
pip install aws-xray-sdk -t lambda_layer_x_ray_stack/layers/xray/python
```

```
pip install boto3 -t lambda_layer_x_ray_stack/layers/boto3/python
```

4. Each bucket name has to be globally unique so update the source and resized bucket names by replacing < your-name > with your name and any random digits in the lambda_layer_x_ray_stack_stack.py file. 

5. Update the pillow arn in the lambda_layer_x_ray_stack_stack.py file to the latest version in your region. See [Klayers](https://github.com/keithrozario/Klayers/tree/master/deployments/python3.8/arns) and select your region and the latest pillow package version arn.

```
layerpillow = lambda_.LayerVersion.from_layer_version_arn(self, 'pillowlayerversion', 'Your_Region_Pillow_ARN')
```

6. Deploy application via `cdk`:

At this point you can now synthesize the CloudFormation template for this code.

```
cdk synth
```

A Lambda layer is a .zip file archive that can contain additional code or data. When deployed, CDK creates a layer .zip asset to be stored in a staging bucket managed by CDK. To enable this the AWS account being used needs to be bootstrapped.

With default Profile,

```
cdk bootstrap
```

With specific profile,

```
cdk bootstrap --profile test
```

Now we can deploy our stack.
```
cdk deploy
```

# Testing

On the AWS Mangement Console, navigate to the source S3 bucket and upload a few images. Go to the AWS X-Ray service and check that a Service Map has been created and is displaying traces. 


## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

# Documentation 

1. AWS Documentation for using [AWS CDK in Python](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html)
2. AWS Documentation for using [AWS Lambda with AWS X-Ray](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html)
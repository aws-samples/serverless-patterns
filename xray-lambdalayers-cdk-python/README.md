# How to set AWS XRay on Lambda using Layers with the CDK

# Overview

This CDK example sets up AWS X-Ray for a Lambda function that uses Lambda Layers. The example demonstrates the use of the folder structure for a Lambda layer written in Python, and using constructs for deploying and using the layer and X-Ray.


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
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

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
To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command. 

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```
#CDK deploy

A Lambda layer is a .zip file archive that can contain additional code or data. When deployed, CDK creates a layer .zip asset to be stored in a staging bucket managed by CDK. To enable this the AWS account being used needs to be bootstrapped.

With default Profile,

```
$ cdk bootstrap
```

With specific profile,

```
$ cdk bootstrap --profile test
```
# How to Run X-Ray on the Lambda function using layers

# Deployment Instructutions
1. Create a [lambda layer](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda/README.html#layers) for AWS X-Ray.
To do this we'll install the python dependencies inside this folder: `lambda_layer_x_ray_stack/layers/`:

```
pip install aws-xray-sdk -t lambda_layer_x_ray_stack/layers/xray/python/lib/python3.8/site-packages
```

```
pip install boto3 -t lambda_layer_x_ray_stack/layers/boto3/python
```

```
Create a lambda layer from the console and select specify an ARN. Go to [Library ARNS](https://github.com/keithrozario/Klayers/tree/master/deployments/python3.8/arns) and select your region and the latest pillow package version arn. Paste this into the console and click add. 
```

2. Deploy application via `cdk`:

```
cdk synth
cdk deploy
```


# Testing

On the AWS Mangement Console, navigate to the lambda function and invoke it a few times. Go to the AWS X-Ray service and check that a Service Map has been created and is displaying traces. 


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

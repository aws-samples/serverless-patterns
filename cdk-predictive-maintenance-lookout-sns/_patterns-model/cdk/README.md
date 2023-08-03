# Predictive Maintenance using Amazon Lookout for Equipment

The solution deploys a python CDK for a predictive maintenance inferencing pipeline for Amazon Lookout for Equipment by using AWS IoT Core, Amazon S3, Amazon SNS, Amazon Kinesis Firehose and AWS Lambda

## Prerequisites

- Python
- AWS CLI
- AWS CDK
- (Optional) [Architecture and Demo Video](https://www.youtube.com/watch?v=N_eCUxrsPr0&feature=youtu.be)

## Steps to setup python environment in CDK

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project. The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory. To create the virtualenv it assumes that there is a `python3`
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

Then bootstrap your cloud environment

```
$ cdk bootstrap aws://ACCOUNT-NUMBER/REGION
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Deployment instructions

- There is a parameter to add a user's email to receive the SNS notification so ensure you add the user's email before deploying by entering `cdk deploy PredictiveMaintenanceAppStack --parameters EmailParameter=<email>`
- Ensure your IoT devices or simulator can effectively communicate with IoT Core by using MQTT test client to subscribe to the IoT topic.
- In the IoT Core Rule, ensure that you edit the SQL statement to the appropriate SQL for your IoT devices and add a `,` seperator or whatever seperator used in your data to the Kinesis Firehose Stream Action.
- Create a model and schedule inferencing on Amazon Lookout for Equipment on the console and connect it to the input and output buckets created from the stack. To learn how to to do this watch this [video](https://www.youtube.com/watch?v=N_eCUxrsPr0&feature=youtu.be)
- Add a prefix/sub-directory `output/` to the S3 output bucket.

Enjoy!

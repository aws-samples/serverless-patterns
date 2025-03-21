
# Auto-tag creator's username to AWS Secrets Manager entries

Implements automatic tagging of AWS Secrets Manager entries with the creator's username. When users authenticated via AWS IAM Identity Center create secrets, their username is automatically added as a tag. This enables easier ownership tracking and management of secrets across the organization.

Eventbridge rule is configured to look for CreateSecret events to invoke a Lambda function to tag the secret with the creator's username.

# Deployment Instructions

Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

``` 
git clone https://github.com/aws-samples/serverless-patterns
```

Change directory to the pattern directory:

```
cd automate-secrets-manager-tags
```
    
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

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

## Deploy
At this point you can deploy the stack. 

Using the default profile

```
$ cdk deploy
```

With specific profile

```
$ cdk deploy --profile test
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

## Testing

To test the automated tagging of secrets in AWS Secrets Manager, we will need to use the AWS console. 

1. Login to AWS Console using AWS IAM Identity Center.
2. Navigate to AWS Secrets Manager and create a secret.
3. Open the "Tags" tab of the newly created secret to see the automated tag key=LoginUserName and value=<Username>.

## Cleanup

Run below script in the `automate-secrets-manager-tags` directory to delete AWS resources created by this sample stack.

```
cdk destroy
```
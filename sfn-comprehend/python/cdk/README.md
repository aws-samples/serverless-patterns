
# Create an AWS Step Functions workflow to integrate with Amazon Comprehend using SDK integration.

This CDK application deploys a Step Functions workflow, that takes in a payload and sends it to the sentiment analysis API of the Amazon Comprehend service. The output of the Sentiment Analysis API returns the overall sentiment ((Positive, Negative, Neutral, or Mixed) of the text we have provided. This pattern exactly shows how we can use AWS Step Functions SDK integrations to call any of the over two hundred AWS services directly from your state machine. The application contains the minimum IAM resources required to run the workflow.

<br>
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


Deploy your code

```
$ cdk deploy
```


## How it works

* Start the Step Function execution with the sample event payload 
* As part of the execution, part of the payload (the `text` attribute of the payload) gets pushed to the Amazon Comprehend service to do sentiment analysis

## Testing

Run the following AWS CLI command to send a 'start-execution` command to start the Step Functions workflow. Note, you must edit the {StateMachineArn } placeholder with the ARN of the deployed Step Functions workflow. This is provided in the stack outputs.

```bash
aws stepfunctions start-execution  --name "test" --state-machine-arn "{StateMachineArn}" --input "{\"text\": \"I hope you have a good day\" }"
```

### output:

```bash
{
    "executionArn": "arn:aws:states:us-east-1:123456789012:execution:MyStateMachine-LIXV3ls6HtnY:test",
    "startDate": 1620244153.977
}
```

Note the `executionArn` from the above output and run the below  cli command to get the status of the execution

```bash
aws stepfunctions describe-execution --execution-arn  "{executionArn}"
```

### Get execution status output:

```bash
{
    "executionArn": "arn:aws:states:us-east-1:123456789012:execution:MyStateMachine-LIXV3ls6HtnY:test",
    "stateMachineArn": "arn:aws:states:us-east-1:123456789012:stateMachine:MyStateMachine-LIXV3lsV8tnY",
    "name": "60805db6-ca0a-44ee-b280-c6a44c5578a1",
    "status": "SUCCEEDED",
    "startDate": 1620244175.722,
    "stopDate": 1620244175.849,
    "input": "{\"text\": \"I hope you have a good day\" }",
    "inputDetails": {
        "included": true
    },
    "output": "{\n  \"Sentiment\": \"NEUTRAL\",\n  \"SentimentScore\": {\n    \"Mixed\": 0.20609446,\n    \"Negative\": 0.16206247,\n    \"Neutral\": 0.617416,\n    \"Positive\": 0.014427028\n  }\n}",
    "outputDetails": {
        "included": true
    }
}
```

Below is the output of the sentiment analysis for the text provided

```bash
{
  "Sentiment": "NEUTRAL",
  "SentimentScore": {
    "Mixed": 0.20609446,
    "Negative": 0.16206247,
    "Neutral": 0.617416,
    "Positive": 0.014427028
  }
}
```

## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```
   
## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

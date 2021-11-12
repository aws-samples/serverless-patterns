
# Create an AWS Step Functions workflow to integrate with Amazon SQS using CDK.



This CDK application deploys a Step Functions workflow, that takes in a payload and sends part of it to an Amazon SQS. In this pattern, the state machine does not wait for a callback from the queue. The application contains the minimum IAM resources required to run the workflow.
You can find the SAM template for the same pattern [here](https://serverlessland.com/patterns/sfn-sqs)

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
* As part of the execution, part of the payload (the `message` attribute of the payload) gets pushed to the queue
* Run the cli command to pull messages from the queue to verify if the message got delivered.

## Testing

Run the following AWS CLI command to send a 'start-execution` command to start the Step Functions workflow. Note, you must edit the {StateMachineExpressSynctoLambda} placeholder with the ARN of the deployed Step Functions workflow. This is provided in the stack outputs.

```bash
aws stepfunctions start-execution  --name "test" --state-machine-arn "{StateMachineArn}" --input "{\"message\": {\"hello\" : \"world\" } }"
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
    "input": "{\"message\": {\"hello\" : \"world\" } }",
    "inputDetails": {
        "included": true
    },
    "output": "{\"MD5OfMessageBody\":\"fbc24bcc7a1794758fc1327fcfebdaf6\",\"MessageId\":\"faec3da7-cb2c-4b72-9cc8-98fdc4e72773\",\"SdkHttpMetadata\":{\"AllHttpHeaders\":{\"x-amzn-RequestId\":[\"522cc894-5c35-493d-a1ce-f95e71162dfd\"],\"Content-Length\":[\"378\"],\"Date\":[\"Wed, 05 May 2021 19:49:35 GMT\"],\"Content-Type\":[\"text/xml\"]},\"HttpHeaders\":{\"Content-Length\":\"378\",\"Content-Type\":\"text/xml\",\"Date\":\"Wed, 05 May 2021 19:49:35 GMT\",\"x-amzn-RequestId\":\"522cc894-5c35-493d-a1ce-f95e71162dfd\"},\"HttpStatusCode\":200},\"SdkResponseMetadata\":{\"RequestId\":\"522cc894-5c35-493d-a1ce-f95e71162dfd\"}}",
    "outputDetails": {
        "included": true
    }
}
```
Once the `status` is `SUCCEEDED`, we can verify if the message got delivered to the SQS or not by running the below command

```bash
aws sqs receive-message --queue-url  "{QueueUrl}"
```

### Queue Message output:

```bash
{
    "Messages": [
        {
            "MessageId": "3f7fb159-df5f-4acd-a127-f535064a73fd",
            "ReceiptHandle": "AQEBi9nc1QjBPdjVNfoIBz0F7momTMA0EdMCv4UkQAQEBi9nc1QjBPdjVNfoIBz0F7momTMA0EdMCv4UkQ",
            "MD5OfBody": "fbc24bcc7a1794758fc1327fcfebdaf6",
            "Body": "{\"hello\":\"world\"}"
        }
    ]
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

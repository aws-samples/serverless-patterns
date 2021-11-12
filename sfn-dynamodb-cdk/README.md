
# Create an AWS Step Functions workflow to integrate with Amazon DynamoDB

The CDK application deploys a Step Functions workflow, that takes in a payload and puts the item in DynamoBb. Additionally, this workflow also shows how to read an item directly from the DynamoDB table. The CDK application contains the minimum IAM resources required to run the application.
You can find the SAM template for the same pattern [here](https://serverlessland.com/patterns/sfn-dynamodb) 

Learn more about this pattern at: https://serverlessland.com/patterns/sfn-dynamodb-cdk.

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

You can deploy the application using the below command.

```
$ cdk deploy
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## How it works

* Start the Step Function execution with the sample event payload 
* As part of the execution, the payload written to the dynamodb table we created as part of the stack
* Check the dynamodb table to see if the item got written to the table

## Testing

Run the following AWS CLI command to send a 'start-execution` command to start the Step Functions workflow. Note, you must edit the {StateMachineArn} placeholder with the ARN of the deployed Step Functions workflow. This is provided in the stack outputs.
```bash
aws stepfunctions start-execution  --name "test" --state-machine-arn "{StateMachineArn}" --input "{\"id\":  \"12345\" }"
```

### output:

```bash
{
    "executionArn": "arn:aws:states:us-east-1:123456789012:execution:MyStateMachine-LIXV3ls6HtnY:test",
    "startDate": 1620244153.977
}
```

Note the `executionArn` from the above output and run the below cli command to get the status of the execution

```bash
aws stepfunctions describe-execution --execution-arn  "{executionArn}"
```

### Get execution status output:

```bash
{
    "executionArn": "arn:aws:states:us-east-1:826849495443:execution:StateMachinetoDDB-AiwwYeLJk2AL:test",
    "stateMachineArn": "arn:aws:states:us-east-1:826849495443:stateMachine:StateMachinetoDDB-AiwwYeLJk2AL",
    "name": "test",
    "status": "SUCCEEDED",
    "startDate": 1620674586.347,
    "stopDate": 1620674586.553,
    "input": "{\"id\":  \"123456\" }",
    "inputDetails": {
        "included": true
    },
    "output": "{\"description\":{\"S\":\"Hello, my id is 123456.\"},\"id\":{\"S\":\"123456\"}}",
    "outputDetails": {
        "included": true
    }
}
```
Once the `status` is `SUCCEEDED`, you can verify what was stored in DynamoDB table by looking at the "output" attribute.
Additionally, you can also verify if the item is stored in DynamoDB by running the below get item cli command on the table.

```bash
 aws dynamodb get-item --table-name my-table --key "{\"id\": {\"S\": \"12345\"} }"
```

### DynamoDB Get Item Output:

```bash
{
    "Item": {
        "id": {
            "S": "12345"
        },
        "description": {
            "S": "Hello, my id is 12345"
        }
    }
}
```

## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```

----


## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation


-----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

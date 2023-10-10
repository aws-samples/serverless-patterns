# CDK Stack iot-dynamodbv2-ttl-cdk

This project is generated using `cdk` toolkit version `2.37` in Typescript. 
The `cdk.json` file tells the CDK Toolkit how to execute your app.

To deploy the stack:

```sh
cdk deploy
```

To destroy the stack:

```sh
cdk destroy
```

If this is the first time you are using CDK with your AWS account/region, you would have to run the following:

```sh
cdk bootstrap
```

## Notes

1. `iot-ddbv2-stack.ts` has the resources for creating the IAM Role required for the IoT Rule and the AWS IoT rule action to publish data to Amazon DynamoDB. This stack invokes the nested stack (see below) to create the DynamoDB Table.
2. `dynamodb.ts` is a nested stack invoked by the stack above to create a DynamoDB table. 
3. Names of the table in `config.json` file. 
4. Time to live configuration is in `config.json` file.
5. Resources have their removal policy set to destroy inlcuding for the DynamoDB table. This is to make it easier for deleting resources when experimenting with the pattern. Remove for production.



## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk synth`       emits the synthesized CloudFormation template

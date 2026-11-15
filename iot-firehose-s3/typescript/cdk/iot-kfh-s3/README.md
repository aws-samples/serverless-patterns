# CDK Stack iot-kfh-s3

This project is generated using `cdk` toolkit version `2.33` in Typescript. 
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

1. `iot-kfh-s3` has the resources for Amazon Kinesis Data Firehose and AWS IoT Core.
2. `s3buckets.ts` is a nested stack invoked by the stack above to create an Amazon S3 bucket that will be used as a destination for the Kinesis Data Firehose. This stack can be changed to lookup an existing bucket and returning instead of creating a new one.
3. All resources have their removal policy set to destroy even for the Amazon S3 bucket. This is to make it easier for deleting resources.



## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk synth`       emits the synthesized CloudFormation template

# CDK Stack iot-timestream

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

1. `iot-timestream-stack.ts` has the resources for creating the IAM Role required for the IoT Rule and the AWS IoT rule action to publish data to Amazon Timestream. This stack invokes the nested stack (see below) to create the Amazon Timestream Database and Table.
2. `timestream.ts` is a nested stack invoked by the stack above to create a Amazon Timestream database and table. 
3. Names of the database and table are setup in `config.json` file. 
4. The SQL statement and version are specified in `config.json` file.
5. Please pay special attention to this seciton in [Amazon Timestream and AWS IoT Core](https://docs.aws.amazon.com/timestream/latest/developerguide/IOT-Core.html):

    > The Timestream action in IoT Rules is used to insert data from incoming messages directly into Timestream. The action parses the results of the IoT Core SQL statement and stores data in Timestream. The names of the fields from returned SQL result set are used as the measure::name and the value of the field is the measure::value.

6. On the use of an older version of SQL, read the following [Timestream Action](https://docs.aws.amazon.com/iot/latest/developerguide/timestream-rule-action.html):

    > Note  
    With SQL V2 (2016-03-23), numeric values that are whole numbers, such as 10.0, are converted their Integer representation (10). Explicitly casting them to a Decimal value, such as by using the cast() function, does not prevent this behavior—the result is still an Integer value. This can cause type mismatch errors that prevent data from being recorded in the Timestream database. To reliably process whole number numeric values as Decimal values, use SQL V1 (2015-10-08) for the rule query statement.

7. Timestream resources have their removal policy set to destroy. This is to make it easier for deleting resources when experimenting with the pattern. Remove for production.



## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk synth`       emits the synthesized CloudFormation template

const { Construct } = require('constructs');
const { Stack, Duration, StackProps, CfnOutput } = require('aws-cdk-lib');              // core constructs
const cloudwatch = require('aws-cdk-lib/aws-cloudwatch');
const iam = require('aws-cdk-lib/aws-iam');
const lambda = require('aws-cdk-lib/aws-lambda');
const lambdajs = require('aws-cdk-lib/aws-lambda-nodejs');
const path = require('path');

class LambdaCloudWatchCdkStack extends Stack {
  /**
   *
   * @param {Construct} scope
   * @param {string} id
   * @param {StackProps=} props
   */
  constructor(scope, id, props) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const policyStatement = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: ['cloudwatch:PutMetricData'],
      resources: ['*']
    });

    const metric = new cloudwatch.Metric({
      namespace: 'MyNamespace',
      metricName: 'MyMetric'
    });


    const lambdaCloudWatch = new lambdajs.NodejsFunction(
      this,
      'lambdaCloudWatch',
      {
        runtime: lambda.Runtime.NODEJS_14_X,
        memorySize: 1024,
        timeout: Duration.seconds(3),
        entry: path.join(__dirname, '../src/app.js'),
        handler: 'main',
        environment: {
          Metric: metric.metricName
        },
        initialPolicy: [policyStatement]
      }
    );

    new CfnOutput(this, 'LambdFunctionArn', { value: lambdaCloudWatch.functionArn });
  }
}

module.exports = { LambdaCloudWatchCdkStack }

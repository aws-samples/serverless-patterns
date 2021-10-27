const cdk = require('@aws-cdk/core');
const { Metric } = require('@aws-cdk/aws-cloudwatch');
const { NodejsFunction, NODEJS_14_X } = require('@aws-cdk/aws-lambda-nodejs');
const { PolicyDocument, PolicyStatement, Effect } = require('@aws-cdk/aws-iam');
const path = require('path');

class LambdaCloudWatchCdkStack extends cdk.Stack {
  /**
   *
   * @param {cdk.Construct} scope
   * @param {string} id
   * @param {cdk.StackProps=} props
   */
  constructor(scope, id, props) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const policyStatement = new PolicyStatement({
      effect: Effect.ALLOW,
      actions: ['cloudwatch:PutMetricData'],
      resources: ['*']
    });

    const metric = new Metric({
      namespace: 'MyNamespace',
      metricName: 'MyMetric'
    });


    const lambdaCloudWatch = new NodejsFunction(
      this,
      'lambdaCloudWatch',
      {
        runtime: NODEJS_14_X,
        memorySize: 1024,
        timeout: cdk.Duration.seconds(3),
        entry: path.join(__dirname, '../src/app.js'),
        handler: 'main',
        environment: {
          Metric: metric.metricName
        },
        initialPolicy: [policyStatement]
      }
    );

    new cdk.CfnOutput(this, 'LambdFunctionArn', { value: lambdaCloudWatch.functionArn });
  }
}

module.exports = { LambdaCloudWatchCdkStack }

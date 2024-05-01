const { Stack, Duration, CfnOutput } = require('aws-cdk-lib');
const { Function, Runtime, Code, FunctionUrlAuthType } = require('aws-cdk-lib/aws-lambda');
const path = require('path');

class LambdaWithCompressionStack extends Stack {
  constructor(scope, id, props) {
    super(scope, id, props);

    const fn = new Function(this, 'MyFunction', {
      runtime: Runtime.NODEJS_20_X,
      handler: 'index.handler',
      memorySize: 1024,
      timeout: Duration.seconds(10),
      code: Code.fromAsset(path.join(__dirname, '../lambda'))
    });

    const furl = fn.addFunctionUrl({
      authType: FunctionUrlAuthType.AWS_IAM
    });

    new CfnOutput(this, 'FunctionUrl', {
      value: furl.url
    });
  }
}

module.exports = { LambdaWithCompressionStack }

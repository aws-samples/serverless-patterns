const cdk = require('aws-cdk-lib');

const { CloudfrontOacLambdaUrlNodejsCdkConstruct } = require('./cloudfront-oac-lambda-url-nodejs-cdk-construct');

class CloudfrontOacLambdaUrlNodejsCdkStack extends cdk.Stack {
  /**
   * @param {cdk.App} scope
   * @param {string} id
   * @param {cdk.StackProps=} props
   */
  constructor(scope, id, props) {
    super(scope, id, props);

    const construct = new CloudfrontOacLambdaUrlNodejsCdkConstruct(this, 'CloudfrontAocLambdaUrlNodejsCdkConstruct');

  }
}

module.exports = { CloudfrontOacLambdaUrlNodejsCdkStack: CloudfrontOacLambdaUrlNodejsCdkStack }

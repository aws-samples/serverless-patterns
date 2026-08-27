import * as cdk from 'aws-cdk-lib';
import { Template } from 'aws-cdk-lib/assertions';
import { ApigwSqsMsgFilteringCdkStack } from '../lib/apigw-sqs-msg-filtering-stack';


test('SQS Queue Created', () => {
    const app = new cdk.App();
    const stack = new ApigwSqsMsgFilteringCdkStack(app, 'MyTestStack');

    Template.fromStack(stack).hasResource("AWS::ApiGateway::Method", {});
    Template.fromStack(stack).hasResource("AWS::SQS::Queue", {});
});



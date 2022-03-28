import { Template } from 'aws-cdk-lib/assertions';
import * as cdk from 'aws-cdk-lib';
import * as DynamodbKinesisCdk from '../lib/dynamodb-kinesis-cdk-stack';

test('Empty Stack', () => {
    const app = new cdk.App();
    // WHEN
    const stack = new DynamodbKinesisCdk.DynamodbKinesisCdkStack(app, 'MyTestStack');
    // THEN
    Template.fromStack(stack).hasResource("AWS::DynamoDB::Table", {});
});

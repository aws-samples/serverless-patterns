import * as cdk from 'aws-cdk-lib/core';
import { Template, Match } from 'aws-cdk-lib/assertions';
import { CdkBedrockAsyncInvokeStack } from '../lib/cdk-bedrock-async-invoke-stack';

describe('CdkBedrockAsyncInvokeStack', () => {
    const app = new cdk.App();
    const stack = new CdkBedrockAsyncInvokeStack(app, 'TestStack');
    const template = Template.fromStack(stack);

    test('creates an S3 bucket for video output', () => {
        template.hasResource('AWS::S3::Bucket', {
            DeletionPolicy: 'Delete',
        });
    });

    test('creates a durable Lambda function', () => {
        template.hasResourceProperties('AWS::Lambda::Function', {
            FunctionName: 'video-generator-durable',
            Runtime: 'nodejs22.x',
        });
    });

    test('grants scoped Bedrock permissions', () => {
        template.hasResourceProperties('AWS::IAM::Policy', {
            PolicyDocument: {
                Statement: Match.arrayWith([
                    Match.objectLike({
                        Action: Match.arrayWith([
                            'bedrock:InvokeModel',
                            'bedrock:StartAsyncInvoke',
                        ]),
                        Resource: 'arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-reel-v1:*',
                    }),
                    Match.objectLike({
                        Action: 'bedrock:GetAsyncInvoke',
                    }),
                ]),
            },
        });
    });

    test('creates CloudWatch log group with DESTROY removal', () => {
        template.hasResource('AWS::Logs::LogGroup', {
            DeletionPolicy: 'Delete',
            Properties: {
                LogGroupName: '/aws/lambda/video-generator-durable',
            },
        });
    });
});
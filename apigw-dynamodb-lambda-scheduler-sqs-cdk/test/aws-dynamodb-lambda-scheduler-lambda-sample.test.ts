import * as cdk from 'aws-cdk-lib';
import { App } from 'aws-cdk-lib';
import { Match, Template } from 'aws-cdk-lib/assertions';
import * as AwsDynamodbLambdaSchedulerLambdaSample from '../lib/aws-dynamodb-lambda-scheduler-lambda-sample-stack';

// example resource in lib/aws-dynamodb-lambda-scheduler-lambda-sample-stack.ts

const modelName = 'TempTable';

describe('SQS Test Functions', () => {

    test('SQS Queue Created', () => {
        const app = new cdk.App();
        // WHEN
        const stack = new AwsDynamodbLambdaSchedulerLambdaSample.AwsDynamodbLambdaSchedulerLambdaSampleStack(app, 'MyTestStack');
        // THEN
        const template = Template.fromStack(stack);

        template.hasResourceProperties('AWS::SQS::Queue', {
            VisibilityTimeout: 300
        });
    });

    test('Lambda Functions Created', () => {
        const app = new cdk.App();
        // WHEN
        const stack = new AwsDynamodbLambdaSchedulerLambdaSample.AwsDynamodbLambdaSchedulerLambdaSampleStack(app, 'MyTestStack');
        // THEN
        const template = Template.fromStack(stack);

        template.hasResourceProperties('AWS::Lambda::Function', {
            Handler: 'dynamo_stream_handler.handler',
            Runtime: 'nodejs18.x',
            Code: {
                S3Bucket: {
                    'Fn::Sub': Match.anyValue()
                },
                S3Key: Match.anyValue()
            },
            Role: {
                'Fn::GetAtt': Match.arrayWith(['Arn'])
            },
            Environment: {
                Variables: {
                 LAMBDA_TARGET_ARN: {
                    'Fn::GetAtt': Match.anyValue()
                 },
                 LAMBDA_TARGET_ROLE_ARN: {
                    'Fn::GetAtt': Match.anyValue()
                 },
                 QUEUE_TARGET_ARN: {
                    'Fn::GetAtt': Match.anyValue()
                 },
                 QUEUE_TARGET_ROLE_ARN: {
                    'Fn::GetAtt': Match.anyValue()
                 }
                }
            }
        });

        template.hasResourceProperties('AWS::Lambda::Function', {
            Handler: 'event_schedule_handler.handler',
            Runtime: 'nodejs18.x',
            Code: {
                S3Bucket: {
                    'Fn::Sub': Match.anyValue()
                },
                S3Key: Match.anyValue()
            },
            Role: {
                'Fn::GetAtt': Match.arrayWith(['Arn'])
            }
        });
    });

    test('Create table', () => {
        const app = new App();

        const stack = new AwsDynamodbLambdaSchedulerLambdaSample.AwsDynamodbLambdaSchedulerLambdaSampleStack(app, 'MyTestStack');

        const template = Template.fromStack(stack);

        template.resourceCountIs('AWS::DynamoDB::Table', 1);
        template.hasResource('AWS::DynamoDB::Table', {
            Properties: Match.objectLike({
                KeySchema: [
                    {
                        AttributeName: `id`,
                        KeyType: 'HASH',
                    },
                    {
                        AttributeName: "scheduleTime",
                        KeyType: "RANGE"
                    }
                ],
                        AttributeDefinitions: [
                    {
                        AttributeName: "id",
                        AttributeType: "S"
                    },
                    {
                        AttributeName: "scheduleTime",
                        AttributeType: "S"
                    }
                ],
                StreamSpecification: {
                    StreamViewType: "NEW_IMAGE"
                }
            }),
            UpdateReplacePolicy: Match.exact('Delete'),
            DeletionPolicy: Match.exact('Delete')
        });
    });

    test('IAM Roles and Policies Created', () => {
        const app = new cdk.App();
        // WHEN
        const stack = new AwsDynamodbLambdaSchedulerLambdaSample.AwsDynamodbLambdaSchedulerLambdaSampleStack(app, 'MyTestStack');
        // THEN
        const template = Template.fromStack(stack);

        template.resourceCountIs('AWS::IAM::Role', 6);

        template.resourceCountIs('AWS::IAM::Policy', 3);
    });

    test('Event Bridge Schedule Groups Created', () => {
        const app = new cdk.App();
        // WHEN
        const stack = new AwsDynamodbLambdaSchedulerLambdaSample.AwsDynamodbLambdaSchedulerLambdaSampleStack(app, 'MyTestStack');
        // THEN
        const template = Template.fromStack(stack);

        template.resourceCountIs('AWS::Scheduler::ScheduleGroup', 2);

        template.hasResourceProperties('AWS::Scheduler::ScheduleGroup', {
             Name: Match.exact("Lambda")
        });
        template.hasResourceProperties('AWS::Scheduler::ScheduleGroup', {
            Name: Match.exact("Queue")
       });
    });

    test('API Gateway Created', () => {
        const app = new cdk.App();
        // WHEN
        const stack = new AwsDynamodbLambdaSchedulerLambdaSample.AwsDynamodbLambdaSchedulerLambdaSampleStack(app, 'MyTestStack');
        // THEN
        const template = Template.fromStack(stack);

        template.resourceCountIs('AWS::ApiGateway::RestApi', 1);

        template.resourceCountIs('AWS::ApiGateway::Stage', 1);

        template.resourceCountIs('AWS::ApiGateway::Method', 4);
    });
});
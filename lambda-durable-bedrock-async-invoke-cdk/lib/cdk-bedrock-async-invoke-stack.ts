import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as nodejs from 'aws-cdk-lib/aws-lambda-nodejs';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as cdk from 'aws-cdk-lib/core';
import { Construct } from 'constructs';
import * as path from 'path';

export class CdkBedrockAsyncInvokeStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        // S3 bucket where Bedrock writes the generated video output
        const outputBucket = new s3.Bucket(this, 'VideoOutputBucket', {
            removalPolicy: cdk.RemovalPolicy.DESTROY,
            autoDeleteObjects: true,
            lifecycleRules: [
                {
                    expiration: cdk.Duration.days(7),
                    id: 'ExpireVideosAfter7Days',
                },
            ],
        });

        // Explicit log group with cleanup on stack destroy
        const logGroup = new logs.LogGroup(this, 'VideoGeneratorLogGroup', {
            logGroupName: '/aws/lambda/video-generator-durable',
            retention: logs.RetentionDays.ONE_WEEK,
            removalPolicy: cdk.RemovalPolicy.DESTROY,
        });

        // Durable Lambda function for the video generation workflow
        const videoGeneratorFunction = new nodejs.NodejsFunction(this, 'VideoGeneratorFunction', {
            functionName: 'video-generator-durable',
            description:
                'Durable function demonstrating Bedrock async invoke for AI video generation',
            runtime: lambda.Runtime.NODEJS_22_X,
            handler: 'handler',
            entry: path.join(__dirname, 'lambda', 'video-generator.ts'),
            timeout: cdk.Duration.minutes(1),
            memorySize: 256,
            durableConfig: {
                executionTimeout: cdk.Duration.minutes(30),
                retentionPeriod: cdk.Duration.days(1),
            },
            bundling: {
                minify: true,
                sourceMap: true,
                externalModules: [],
            },
            environment: {
                NODE_OPTIONS: '--enable-source-maps',
                OUTPUT_BUCKET_NAME: outputBucket.bucketName,
                BEDROCK_MODEL_ID: 'amazon.nova-reel-v1:1',
                BEDROCK_REGION: 'us-east-1',
            },
            logGroup: logGroup,
        });

        // Grant the function permission to write to the output bucket.
        // Bedrock writes the video output directly, but the function also
        // needs s3:PutObject so that Bedrock can use the function's role
        // when writing to the bucket via the async invocation.
        outputBucket.grantReadWrite(videoGeneratorFunction);

        // Grant Bedrock invocation permissions
        videoGeneratorFunction.addToRolePolicy(
            new iam.PolicyStatement({
                actions: [
                    'bedrock:InvokeModel',
                    'bedrock:GetAsyncInvoke',
                    'bedrock:StartAsyncInvoke',
                ],
                resources: ['*'],
            }),
        );

        // Add durable execution managed policy (required when using explicit log groups)
        videoGeneratorFunction.role?.addManagedPolicy(
            iam.ManagedPolicy.fromAwsManagedPolicyName(
                'service-role/AWSLambdaBasicDurableExecutionRolePolicy',
            ),
        );

        // Stack outputs
        new cdk.CfnOutput(this, 'VideoGeneratorFunctionArn', {
            value: videoGeneratorFunction.functionArn,
            description: 'ARN of the Video Generator Durable Function',
        });

        new cdk.CfnOutput(this, 'VideoGeneratorFunctionName', {
            value: videoGeneratorFunction.functionName,
            description: 'Name of the Video Generator Durable Function',
        });

        new cdk.CfnOutput(this, 'VideoOutputBucketName', {
            value: outputBucket.bucketName,
            description: 'S3 bucket where generated videos are stored',
        });
    }
}
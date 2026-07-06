import { aws_lambda, aws_logs, aws_sns, aws_apigateway, aws_iam, aws_dynamodb } from 'aws-cdk-lib';
import { EmailSubscription } from 'aws-cdk-lib/aws-sns-subscriptions';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import * as cdk from 'aws-cdk-lib/core';
import { Duration, RemovalPolicy } from 'aws-cdk-lib/core';
import { Construct } from 'constructs';

export class HitlLambdaDurableFunctionCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const email = this.node.tryGetContext('Email') as string;
    if (!email) {
      throw new Error('Email address is required. Please provide it using the --context flag.');
    }

    // Amazon DynamoDB table for storing callback tokens
    const callbackTable = new aws_dynamodb.Table(this, 'CallbackTable', {
      tableName: 'hitl-callback-tokens',
      partitionKey: {
        name: 'approvalId',
        type: aws_dynamodb.AttributeType.STRING,
      },
      billingMode: aws_dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: RemovalPolicy.DESTROY,
      timeToLiveAttribute: 'ttl', // Auto-expire old tokens
    });

    // Amazon SNS topic for email notifications
    const approvalTopic = new aws_sns.Topic(this, 'ApprovalTopic', {
      displayName: 'Human Approval Notifications',
      topicName: 'hitl-approval-notifications',
    });

    // Subscribe email to Amazon SNS topic
    approvalTopic.addSubscription(new EmailSubscription(email));

    // Amazon API Gateway for callback handling
    const api = new aws_apigateway.RestApi(this, 'HitlCallbackApi', {
      restApiName: 'HITL-Callback-API',
      description: 'Handles human-in-the-loop callbacks for the HITL durable function pattern',
      deployOptions: {
        stageName: 'prod',
      },
    });

    const verifyResource = api.root.addResource('verify');

    // HITL orchestrator — AWS Lambda durable function
    const hitlDurableFunctionLogGroup = new aws_logs.LogGroup(this, 'HitlDurableFunctionLogGroup', {
      logGroupName: '/aws/lambda/hitl-durable-function',
      retention: aws_logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    const hitlDurableFunction = new NodejsFunction(this, 'HitlDurableFunction', {
      runtime: aws_lambda.Runtime.NODEJS_22_X,
      tracing: aws_lambda.Tracing.ACTIVE,
      functionName: 'hitl-durable-function',
      description: 'Orchestrates the human-in-the-loop workflow using AWS Lambda durable functions',
      loggingFormat: aws_lambda.LoggingFormat.JSON,
      handler: 'index.lambdaHandler',
      logGroup: hitlDurableFunctionLogGroup,
      durableConfig: {
        executionTimeout: Duration.hours(1),
        retentionPeriod: Duration.days(30),
      },
      code: aws_lambda.Code.fromAsset('lambdas/hitl-durable-function'),
      environment: {
        SNS_TOPIC_ARN: approvalTopic.topicArn,
        API_URL: api.url,
        CALLBACK_TABLE_NAME: callbackTable.tableName,
      },
    });

    // Grant permissions
    approvalTopic.grantPublish(hitlDurableFunction);
    callbackTable.grantWriteData(hitlDurableFunction);

    // Callback handler Lambda function
    const callbackHandlerLogGroup = new aws_logs.LogGroup(this, 'CallbackHandlerLogGroup', {
      logGroupName: '/aws/lambda/hitl-callback-handler',
      retention: aws_logs.RetentionDays.ONE_WEEK,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    const callbackHandler = new aws_lambda.Function(this, 'CallbackHandler', {
      runtime: aws_lambda.Runtime.NODEJS_22_X,
      tracing: aws_lambda.Tracing.ACTIVE,
      functionName: 'hitl-callback-handler',
      timeout: Duration.minutes(1),
      description: 'Processes human approval/rejection decisions from Amazon API Gateway callback links',
      loggingFormat: aws_lambda.LoggingFormat.JSON,
      handler: 'index.handler',
      logGroup: callbackHandlerLogGroup,
      code: aws_lambda.Code.fromAsset('lambdas/callback-handler'),
      environment: {
        CALLBACK_TABLE_NAME: callbackTable.tableName,
      },
    });

    // Grant callback handler permission to send durable execution callbacks
    callbackHandler.addToRolePolicy(new aws_iam.PolicyStatement({
      actions: [
        'lambda:SendDurableExecutionCallbackSuccess',
        'lambda:SendDurableExecutionCallbackFailure',
      ],
      resources: ['*'], // Callback operations don't target specific function ARNs
    }));

    // Grant callback handler read and write access to Amazon DynamoDB
    // Write access is needed to mark tokens as consumed (single-use enforcement)
    callbackTable.grantReadWriteData(callbackHandler);

    const integration = new aws_apigateway.LambdaIntegration(callbackHandler);

    // GET /verify — renders a confirmation page (never executes the decision).
    // This prevents email prefetchers (Outlook Safe Links, Slack unfurl) from
    // silently triggering approvals when they pre-fetch links in emails.
    verifyResource.addMethod('GET', integration);

    // POST /verify — executes the actual approval or rejection decision.
    verifyResource.addMethod('POST', integration);

    // Throttle the callback API as defense-in-depth against brute-force token guessing
    const plan = api.addUsagePlan('HitlUsagePlan', {
      name: 'hitl-callback-throttle',
      throttle: { rateLimit: 5, burstLimit: 10 },
    });
    plan.addApiStage({ stage: api.deploymentStage });

    // Outputs
    new cdk.CfnOutput(this, 'Hitl-ApiUrl', {
      value: api.url,
      description: 'Amazon API Gateway URL for callbacks',
    });

    new cdk.CfnOutput(this, 'Hitl-Sns-TopicArn', {
      value: approvalTopic.topicArn,
      description: 'Amazon SNS topic ARN for approval notifications',
    });

    new cdk.CfnOutput(this, 'Hitl-Durable-Function-Name', {
      value: hitlDurableFunction.functionName,
      description: 'AWS Lambda durable function name for the HITL orchestrator',
    });

    new cdk.CfnOutput(this, 'Hitl-Callback-Table-Name', {
      value: callbackTable.tableName,
      description: 'Amazon DynamoDB table name for callback tokens',
    });
  }
}

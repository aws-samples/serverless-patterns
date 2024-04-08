import { ApiGatewayToDynamoDB } from '@aws-solutions-constructs/aws-apigateway-dynamodb';
import * as cdk from 'aws-cdk-lib';
import * as apigw from "aws-cdk-lib/aws-apigateway";
import { JsonSchemaType } from 'aws-cdk-lib/aws-apigateway';
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from "aws-cdk-lib/aws-lambda";
import { DynamoEventSource } from 'aws-cdk-lib/aws-lambda-event-sources';
import { CfnScheduleGroup } from 'aws-cdk-lib/aws-scheduler';
import * as sqs from "aws-cdk-lib/aws-sqs";
import { Construct } from 'constructs';

export class AwsDynamodbLambdaSchedulerLambdaSampleStack extends cdk.Stack {
  public readonly apiGatewayToDynamoDB: ApiGatewayToDynamoDB;

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    const projectName = 'EBSchedulerDemo'
    /**
     * DynamoDB Creation
     * Enabled Streaming to send the whole new object down the pipe
     */
    const table = new dynamodb.Table(this, 'SchedulerDDB', {
      partitionKey: { name: 'id', type: dynamodb.AttributeType.STRING },
      sortKey: { name: 'scheduleTime', type: dynamodb.AttributeType.STRING },
      stream: dynamodb.StreamViewType.NEW_IMAGE,
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY
    });

    /**
     * Lambda Dynamo Stream Subscriber Creation
     */
    const eventBridgeProducerLambda = new lambda.Function(this, 'ProducerLambdaHandler', {
      runtime: lambda.Runtime.NODEJS_18_X,      // execution environment
      code: lambda.Code.fromAsset('lambdas'),  // code loaded from the "lambdas" directory
      handler: 'dynamo_stream_handler.handler',                // file is "dynamo_stream_handler", function is "handler"
      environment: {
      },
    });

    // subscribe producer lambda to the stream
    eventBridgeProducerLambda.addEventSource(new DynamoEventSource(table, { startingPosition: lambda.StartingPosition.LATEST }));


    /**
     *  Lambda function to handle dynamo db stream
     *  This function will create schedule at a given time
     */
    const eventBridgeConsumerLambda = new lambda.Function(this, 'ConsumerLambdaHandler', {
      runtime: lambda.Runtime.NODEJS_18_X,      // execution environment
      code: lambda.Code.fromAsset('lambdas'),  // code loaded from the "lambdas" directory
      handler: 'event_schedule_handler.handler',                // file is "event_schedule_handler", function is "handler"
      environment: {
      },
    });


    /**
     *  Create queue and deadletter queue to handle messages
     */
    const queue = new sqs.Queue(this, 'SchedulerQueue', {
      visibilityTimeout: cdk.Duration.seconds(300)
    });

    const lambdaScheduleGroup = new CfnScheduleGroup(this, 'LambdaScheduleGroup', {
      name: 'Lambda'
    });

    const queueScheduleGroup = new CfnScheduleGroup(this, 'QueueScheduleGroup', {
      name: 'Queue'
    });

    /**
     *  Create Custom Permission Policy for event bridge schedular
     */
    const lambdaEBSchedulerPolicy = new iam.PolicyDocument({
      statements: [
        new iam.PolicyStatement({
          effect: iam.Effect.ALLOW,
          resources: [eventBridgeConsumerLambda.functionArn + ":*",
          eventBridgeConsumerLambda.functionArn],
          actions: ['lambda:InvokeFunction'
          ],
        })
      ],
    });

    const queueEBSchedulerPolicy = new iam.PolicyDocument({
      statements: [
        new iam.PolicyStatement({
          effect: iam.Effect.ALLOW,
          resources: [queue.queueArn],
          actions: [
            "sqs:GetQueueUrl",
            "sqs:SendMessage",
            "sqs:GetQueueAttributes"
          ],
        }),
      ],
    });

    // Create Role for event bridge schedular
    const lambdaEBSchedulerRole = new iam.Role(this, 'LambdaSchedulerIamRole', {
      assumedBy: new iam.ServicePrincipal('scheduler.amazonaws.com'),
      description: 'An IAM role for EB scheduler to send message to trigger Lambda',
      inlinePolicies: {
        EventBridgeSchedulerPolicy: lambdaEBSchedulerPolicy,
      }
    });

    const queueEBSchedulerRole = new iam.Role(this, 'QueueSchedulerIamRole', {
      assumedBy: new iam.ServicePrincipal('scheduler.amazonaws.com'),
      description: 'An IAM role for EB scheduler to send message to queue',
      inlinePolicies: {
        EventBridgeSchedulerPolicy: queueEBSchedulerPolicy,
      }
    });

    // Add Target environment variable for producer lambda
    eventBridgeProducerLambda.addEnvironment("LAMBDA_TARGET_ARN", eventBridgeConsumerLambda.functionArn);
    eventBridgeProducerLambda.addEnvironment("LAMBDA_TARGET_ROLE_ARN", lambdaEBSchedulerRole.roleArn);

    eventBridgeProducerLambda.addEnvironment("QUEUE_TARGET_ARN", queue.queueArn);
    eventBridgeProducerLambda.addEnvironment("QUEUE_TARGET_ROLE_ARN", queueEBSchedulerRole.roleArn);


    /**
     *  Create Custom Permission Statement for event bridge schedular
     */
    const createSchedulerCustomStatement = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      resources: [lambdaScheduleGroup.attrArn,
      queueScheduleGroup.attrArn,
      'arn:aws:scheduler:'+process.env.CDK_DEFAULT_REGION+':'+process.env.CDK_DEFAULT_ACCOUNT+':schedule/Lambda/*',
      'arn:aws:scheduler:'+process.env.CDK_DEFAULT_REGION+':'+process.env.CDK_DEFAULT_ACCOUNT+':schedule/Queue/*'
    ],
      actions: [
        "scheduler:GetSchedule",
        "scheduler:CreateSchedule",
        "scheduler:GetScheduleGroup"
      ],
    });

    const deleteSchedulerCustomStatement = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      resources: [lambdaScheduleGroup.attrArn,
      queueScheduleGroup.attrArn,
      'arn:aws:scheduler:'+process.env.CDK_DEFAULT_REGION+':'+process.env.CDK_DEFAULT_ACCOUNT+':schedule/Lambda/*',
      'arn:aws:scheduler:'+process.env.CDK_DEFAULT_REGION+':'+process.env.CDK_DEFAULT_ACCOUNT+':schedule/Queue/*'
            ],
        actions: [
        "scheduler:GetSchedule",
        "scheduler:GetScheduleGroup",
        "scheduler:DeleteSchedule"
      ],
    });

    const passRoleCustomStatement = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        "iam:PassRole"
      ],
      resources: ["arn:aws:iam::*:role/*"],
      conditions: {
        "StringLike": {
          "iam:PassedToService": "scheduler.amazonaws.com"
        }
      }
    });

    eventBridgeConsumerLambda.addToRolePolicy(deleteSchedulerCustomStatement);
    eventBridgeConsumerLambda.addToRolePolicy(passRoleCustomStatement);
    
    eventBridgeProducerLambda.addToRolePolicy(createSchedulerCustomStatement);
    eventBridgeProducerLambda.addToRolePolicy(passRoleCustomStatement);


    /**
     * API Gateway Creation
     */
    this.apiGatewayToDynamoDB = new ApiGatewayToDynamoDB(this, projectName, {
      existingTableObj: table,
      allowCreateOperation: true,
      apiGatewayProps: {
        defaultCorsPreflightOptions: {
          allowOrigins: apigw.Cors.ALL_ORIGINS
        },
        restApiName: `${projectName} Service`
      },
      createRequestTemplate: `{
        "Item": {
          "id": {
            "S": "$context.requestId"
          },
          "eventName":{
            "S": "$input.path('$.eventName')"
          },
          "eventType":{
            "S": "$input.path('$.eventType')"
          },
          "scheduleTime":{
            "S": "$input.path('$.scheduleTime')"
          }
        },
        "TableName": "${table.tableName}"
      }`
    })

    const inputEventRequestModel = new apigw.Model(this, "model-validator", {
      restApi: this.apiGatewayToDynamoDB.apiGateway,
      contentType: "application/json",
      description: "To validate the request body",
      modelName: "inputEventRequestModel",
      schema: {
        type: JsonSchemaType.OBJECT,
        required: ["eventName","eventType", "scheduleTime"],
        properties: {
          eventName: { type: apigw.JsonSchemaType.STRING, maxLength: 16 },
          eventType: { type: apigw.JsonSchemaType.STRING, minLength: 16 },
          scheduleTime: { type: apigw.JsonSchemaType.STRING, maxLength: 16, enum : ["Lambda", "Queue"] },
        },
      },
    });
  }
}

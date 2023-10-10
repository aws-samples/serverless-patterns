import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as events from 'aws-cdk-lib/aws-events';
import * as pipes from 'aws-cdk-lib/aws-pipes';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class NormalizerStack extends cdk.Stack {
  
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Step 1: Create source, enrichment and target
    const deadLetterQueue = new sqs.Queue(this, 'NormalizerSourceDeadLetterQueue', {
      enforceSSL: true,
    })

    const sourceQueue = new sqs.Queue(this, 'NormalizerSourceQueue', {
      enforceSSL: true,
      deadLetterQueue: {
        maxReceiveCount: 1,
        queue: deadLetterQueue,
      }
    });

    const enrichmentWorkflow = new sfn.StateMachine(this, 'NormalizerEnrichmentWorkflow', {
      stateMachineType: sfn.StateMachineType.EXPRESS, 
      tracingEnabled: true,
      logs: {
        destination: new logs.LogGroup(this, 'UnifyNameWorkflowLogGroup', {
          logGroupName: '/aws/vendedlogs/UnifyNameWorkflowLogGroup',
          removalPolicy: cdk.RemovalPolicy.DESTROY,
        }),
        includeExecutionData: true,
        level: sfn.LogLevel.ALL
      },
      definition: new sfn.Pass(this, 'Parse JSON', {
        parameters: {
          "body.$": "States.StringToJson($.[0].body)"
        },
      }).next(
        new sfn.Choice(this, 'Source')
          .when(sfn.Condition.stringEquals('$.body.source', 'systemA'), new sfn.Pass(this, 'UnifyA', {
            parameters: {
              first_name: sfn.JsonPath.stringAt("$.body.customer.first_name"),
              name: sfn.JsonPath.stringAt("$.body.customer.last_name"),
              data: sfn.JsonPath.stringAt("$.body.data")
            },
          })) 
          .when(sfn.Condition.stringEquals('$.body.source', 'systemB'), new sfn.Pass(this, 'UnifyB', {
            parameters: {
              first_name: sfn.JsonPath.stringAt("$.body.first_name"),
              name: sfn.JsonPath.stringAt("$.body.name"),
              data: sfn.JsonPath.stringAt("$.body.data")
            },
          })) 
          .when(sfn.Condition.stringEquals('$.body.source', 'systemC'), new sfn.Pass(this, 'Add splitter', {
            parameters: {
              splitter: " ",
              data: sfn.JsonPath.stringAt("$.body.data"),
              full_name: sfn.JsonPath.stringAt("$.body.sender")
            },
          }).next(new sfn.Pass(this, 'Split name', {
            parameters: {
              data: sfn.JsonPath.stringAt("$.data"),
              full_name: sfn.JsonPath.stringSplit(sfn.JsonPath.stringAt("$.full_name"), sfn.JsonPath.stringAt("$.splitter")),
              indexFirst: 0,
              indexLast: 1
            }
          })).next(new sfn.Pass(this, 'UnifyC', {
            parameters: {
              first_name: sfn.JsonPath.arrayGetItem(sfn.JsonPath.stringAt("$.full_name"), sfn.JsonPath.numberAt("$.indexFirst")),
              name: sfn.JsonPath.arrayGetItem(sfn.JsonPath.stringAt("$.full_name"), sfn.JsonPath.numberAt("$.indexLast")),
              data: sfn.JsonPath.stringAt("$.data"),
            },
          })))
          .otherwise(new sfn.Fail(this, 'Invalid Source'))
      )
    });
    const normalizerTargetBus = new events.EventBus(this, 'NormalizerTargetBus', {
      eventBusName: 'normalizerTargetBus'
    });

    // create an Amazon EventBridge rule to send all events to Amazon CloudWatch Logs:
    const normalizerTargetLogRule = new events.Rule(this, 'NormalizerTargetLog', {
      ruleName: 'normalizerTargetLog',
      eventBus: normalizerTargetBus,
      eventPattern: {
        source: events.Match.prefix(''),
      },
      targets: [new targets.CloudWatchLogGroup(new logs.LogGroup(this, 'NormalizerLogGroup', {
        logGroupName: '/aws/events/normalizerTargetLog',
        removalPolicy: cdk.RemovalPolicy.DESTROY,
      }))],
    });

    const allowEventBridgePolicy = new iam.PolicyDocument({
      statements: [
        new iam.PolicyStatement({
          resources: [
            `arn:aws:logs:${process.env.CDK_DEFAULT_REGION}:${process.env.CDK_DEFAULT_ACCOUNT}:log-group:/aws/events/*:*"`,
          ],
          actions: ["logs:CreateLogStream", "logs:PutLogEvents"],
          principals: [new iam.ServicePrincipal("events.amazonaws.com"), new iam.ServicePrincipal("delivery.logs.amazonaws.com")],
        }),
      ],
    });

    // Step 2: Create the pipes' execution role 
    const pipeRole = new iam.Role(this, 'NormalizerRole', {
      assumedBy: new iam.ServicePrincipal('pipes.amazonaws.com'),
    });

    sourceQueue.grantConsumeMessages(pipeRole);
    enrichmentWorkflow.grantStartSyncExecution(pipeRole);
    normalizerTargetBus.grantPutEventsTo(pipeRole);

    const normalizerPipe = new pipes.CfnPipe(this, 'NormalizerPipe', {
      roleArn: pipeRole.roleArn,
      source: sourceQueue.queueArn,
      target: normalizerTargetBus.eventBusArn,
      enrichment: enrichmentWorkflow.stateMachineArn,
      sourceParameters: {
        sqsQueueParameters: {
          batchSize: 1,
        },
      },
    });

    // Create AWS Lambda function that writes three sample messages to the queue to easily test the pipe
    const sourceLambda = new lambda.Function(this, 'NormalizerSampleDataCreatorLambda', {
      runtime: lambda.Runtime.NODEJS_18_X,
      code: lambda.Code.fromAsset('lib/lambda'),
      handler: 'normalizerSampleDataCreator.handler',
      environment: {
        QUEUE_URL: sourceQueue.queueUrl,
      }
    });
    sourceQueue.grantSendMessages(sourceLambda);

    // Relevant outputs so that the user can trigger this pattern and watch it in action.
    new cdk.CfnOutput(this, "NormalizerSampleDataCreatorLambdaArn", {
      value: sourceLambda.functionArn,
      exportName: "NormalizerSampleDataCreatorLambdaArn",
    });
  }
}
import * as cdk from 'aws-cdk-lib/core';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as nodejs from 'aws-cdk-lib/aws-lambda-nodejs';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as s3deploy from 'aws-cdk-lib/aws-s3-deployment';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as tasks from 'aws-cdk-lib/aws-stepfunctions-tasks';
import { Construct } from 'constructs';
import * as path from 'path';

export class CdkSfnDmapDfStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // ===== S3 Bucket for input data =====
    const dataBucket = new s3.Bucket(this, 'CatalogDataBucket', {
      bucketName: `sfn-dmap-df-catalog-${cdk.Aws.ACCOUNT_ID}-${cdk.Aws.REGION}`,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });

    // Deploy items.json to the bucket
    new s3deploy.BucketDeployment(this, 'DeployCatalogData', {
      sources: [s3deploy.Source.asset(path.join(__dirname, '..', 'data'))],
      destinationBucket: dataBucket,
    });

    // ===== Durable Lambda Function =====

    const functionLogGroup = new logs.LogGroup(this, 'ItemProcessorLogGroup', {
      logGroupName: '/aws/lambda/catalog-item-processor',
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const itemProcessor = new nodejs.NodejsFunction(this, 'ItemProcessorFunction', {
      functionName: 'catalog-item-processor',
      description: 'Durable function that validates and updates a single product catalog item',
      runtime: lambda.Runtime.NODEJS_22_X,
      handler: 'handler',
      entry: path.join(__dirname, 'lambda', 'item-processor.ts'),
      timeout: cdk.Duration.minutes(1),
      memorySize: 256,
      logGroup: functionLogGroup,
      durableConfig: {
        executionTimeout: cdk.Duration.minutes(15),
        retentionPeriod: cdk.Duration.days(1),
      },
      bundling: {
        minify: true,
        sourceMap: true,
        externalModules: [],
      },
      environment: {
        NODE_OPTIONS: '--enable-source-maps',
      },
    });

    // ===== Step Functions State Machine =====

    // Use the AWS SDK service integration (CallAwsService) to invoke the
    // durable function. The optimized Lambda integration does not expose the
    // DurableExecutionName parameter, so we drop down to the raw
    // lambda:invoke API call which gives us full control over all parameters.
    const invokeDurableFunction = new tasks.CallAwsService(this, 'InvokeDurableFunction', {
      service: 'lambda',
      action: 'invoke',
      iamAction: 'lambda:InvokeFunction',
      parameters: {
        // Qualified name required for durable invocations
        'FunctionName': `${itemProcessor.functionArn}:$LATEST`,
        'InvocationType': 'RequestResponse',
        // Derive a stable execution name from the item ID for idempotency
        'DurableExecutionName.$': "States.Format('dmap-item-{}', $.itemId)",
        'Payload.$': '$',
      },
      iamResources: [
        `${itemProcessor.functionArn}:$LATEST`,
        itemProcessor.functionArn,
      ],
      // Extract just the parsed response payload
      resultSelector: {
        'result.$': 'States.StringToJson($.Payload)',
      },
      resultPath: '$.processingResult',
    });

    // Distributed Map reads items from S3 and fans out to the invoke task
    const distributedMap = new sfn.DistributedMap(this, 'ProcessCatalogItems', {
      comment: 'Fan out across 50 product items from S3, invoking a durable function per item',
      maxConcurrency: 10,
      itemReader: new sfn.S3JsonItemReader({
        bucket: dataBucket,
        key: 'items.json',
      }),
      resultWriterV2: new sfn.ResultWriterV2({
        bucket: dataBucket,
        prefix: 'results',
      }),
    });

    distributedMap.itemProcessor(invokeDurableFunction, {
      mode: sfn.ProcessorMode.DISTRIBUTED,
      executionType: sfn.ProcessorType.STANDARD,
    });

    // State machine log group
    const stateMachineLogGroup = new logs.LogGroup(this, 'StateMachineLogGroup', {
      logGroupName: '/aws/vendedlogs/states/catalog-update-sm',
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const stateMachine = new sfn.StateMachine(this, 'CatalogUpdateStateMachine', {
      stateMachineName: 'catalog-update-distributed-map',
      definitionBody: sfn.DefinitionBody.fromChainable(distributedMap),
      timeout: cdk.Duration.hours(1),
      logs: {
        destination: stateMachineLogGroup,
        level: sfn.LogLevel.ALL,
        includeExecutionData: true,
      },
    });

    // Grant the state machine permission to read from and write to the S3 bucket
    dataBucket.grantRead(stateMachine);
    dataBucket.grantWrite(stateMachine);

    // Grant the state machine permission to start distributed map child executions
    stateMachine.addToRolePolicy(new iam.PolicyStatement({
      actions: ['states:StartExecution'],
      resources: [`arn:aws:states:${cdk.Aws.REGION}:${cdk.Aws.ACCOUNT_ID}:stateMachine:catalog-update-distributed-map`],
    }));

    // Grant the state machine the ability to describe and stop child executions
    stateMachine.addToRolePolicy(new iam.PolicyStatement({
      actions: ['states:DescribeExecution', 'states:StopExecution'],
      resources: [`arn:aws:states:${cdk.Aws.REGION}:${cdk.Aws.ACCOUNT_ID}:execution:catalog-update-distributed-map/*`],
    }));

    // ===== Stack Outputs =====

    new cdk.CfnOutput(this, 'StateMachineArn', {
      value: stateMachine.stateMachineArn,
      description: 'ARN of the catalog update state machine',
    });

    new cdk.CfnOutput(this, 'ItemProcessorFunctionArn', {
      value: itemProcessor.functionArn,
      description: 'ARN of the durable item processor function',
    });

    new cdk.CfnOutput(this, 'DataBucketName', {
      value: dataBucket.bucketName,
      description: 'S3 bucket containing the product catalog data',
    });
  }
}

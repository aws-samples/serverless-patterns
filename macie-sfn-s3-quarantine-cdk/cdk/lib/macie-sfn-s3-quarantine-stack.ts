// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0
// 2026

import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as sns from 'aws-cdk-lib/aws-sns';
import * as sns_subscriptions from 'aws-cdk-lib/aws-sns-subscriptions';
import * as events from 'aws-cdk-lib/aws-events';
import * as events_targets from 'aws-cdk-lib/aws-events-targets';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as tasks from 'aws-cdk-lib/aws-stepfunctions-tasks';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as path from 'path';

export class MacieSfnS3QuarantineStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Email parameter for SNS notifications
    const notificationEmail = new cdk.CfnParameter(this, 'NotificationEmail', {
      type: 'String',
      description: 'Email address to receive sensitive data finding notifications',
      default: 'security-team@example.com',
    });

    // Source bucket (monitored by Amazon Macie)
    const sourceBucket = new s3.Bucket(this, 'MonitoredBucket', {
      bucketName: `macie-monitored-${cdk.Aws.ACCOUNT_ID}-${cdk.Aws.REGION}`,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
      versioned: true,
    });

    // Quarantine bucket (where sensitive objects are moved)
    const quarantineBucket = new s3.Bucket(this, 'QuarantineBucket', {
      bucketName: `macie-quarantine-${cdk.Aws.ACCOUNT_ID}-${cdk.Aws.REGION}`,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
      versioned: true,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
    });

    // SNS topic for notifications
    const notificationTopic = new sns.Topic(this, 'FindingNotificationTopic', {
      topicName: 'MacieSensitiveDataFindings',
      displayName: 'Amazon Macie Sensitive Data Findings',
    });

    notificationTopic.addSubscription(
      new sns_subscriptions.EmailSubscription(notificationEmail.valueAsString)
    );

    // Lambda function to quarantine S3 objects
    const quarantineFunction = new lambda.Function(this, 'QuarantineFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'index.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '../src/quarantine-handler')),
      timeout: cdk.Duration.seconds(60),
      environment: {
        QUARANTINE_BUCKET: quarantineBucket.bucketName,
      },
    });

    // Grant the Lambda function read from source and write to quarantine
    sourceBucket.grantRead(quarantineFunction);
    sourceBucket.grantDelete(quarantineFunction);
    quarantineBucket.grantWrite(quarantineFunction);

    // Also allow tagging the source object
    quarantineFunction.addToRolePolicy(new iam.PolicyStatement({
      actions: ['s3:PutObjectTagging'],
      resources: [sourceBucket.arnForObjects('*')],
    }));

    // Step Functions state machine
    // Step 1: Classify severity
    const classifySeverity = new sfn.Choice(this, 'ClassifySeverity')
      .when(
        sfn.Condition.numberGreaterThanEquals('$.detail.severity.score', 7),
        new sfn.Pass(this, 'HighSeverity', {
          result: sfn.Result.fromObject({ action: 'quarantine', severity: 'HIGH' }),
          resultPath: '$.classification',
        })
      )
      .when(
        sfn.Condition.numberGreaterThanEquals('$.detail.severity.score', 4),
        new sfn.Pass(this, 'MediumSeverity', {
          result: sfn.Result.fromObject({ action: 'tag_and_notify', severity: 'MEDIUM' }),
          resultPath: '$.classification',
        })
      )
      .otherwise(
        new sfn.Pass(this, 'LowSeverity', {
          result: sfn.Result.fromObject({ action: 'notify_only', severity: 'LOW' }),
          resultPath: '$.classification',
        })
      );

    // Step 2: Quarantine the object (move to quarantine bucket)
    const quarantineObject = new tasks.LambdaInvoke(this, 'QuarantineObject', {
      lambdaFunction: quarantineFunction,
      payload: sfn.TaskInput.fromObject({
        'bucketName.$': '$.detail.resourcesAffected.s3Bucket.name',
        'objectKey.$': '$.detail.resourcesAffected.s3Object.key',
        'findingId.$': '$.detail.id',
        'severity.$': '$.detail.severity.description',
      }),
      resultPath: '$.quarantineResult',
    });

    // Step 3: Send SNS notification
    const sendNotification = new tasks.SnsPublish(this, 'SendNotification', {
      topic: notificationTopic,
      subject: sfn.JsonPath.format(
        'Macie Finding: Sensitive data detected [{}]',
        sfn.JsonPath.stringAt('$.detail.severity.description')
      ),
      message: sfn.TaskInput.fromObject({
        'findingId.$': '$.detail.id',
        'findingType.$': '$.detail.type',
        'severity.$': '$.detail.severity.description',
        'bucket.$': '$.detail.resourcesAffected.s3Bucket.name',
        'objectKey.$': '$.detail.resourcesAffected.s3Object.key',
        'detectedDataTypes.$': '$.detail.classificationDetails.result.sensitiveData[*].category',
        'action.$': '$.classification.action',
      }),
      resultPath: '$.notificationResult',
    });

    // Step 4: Tag source object (for medium severity - don't quarantine but mark it)
    const tagObject = new tasks.LambdaInvoke(this, 'TagObject', {
      lambdaFunction: quarantineFunction,
      payload: sfn.TaskInput.fromObject({
        'bucketName.$': '$.detail.resourcesAffected.s3Bucket.name',
        'objectKey.$': '$.detail.resourcesAffected.s3Object.key',
        'findingId.$': '$.detail.id',
        'severity.$': '$.detail.severity.description',
        'tagOnly': true,
      }),
      resultPath: '$.tagResult',
    });

    // Wire the state machine
    const highSeverityChain = quarantineObject.next(sendNotification);
    const mediumSeverityChain = tagObject.next(sendNotification);
    const lowSeverityChain = sendNotification;

    // After classification, route to appropriate action
    const routeAction = new sfn.Choice(this, 'RouteAction')
      .when(
        sfn.Condition.stringEquals('$.classification.action', 'quarantine'),
        highSeverityChain
      )
      .when(
        sfn.Condition.stringEquals('$.classification.action', 'tag_and_notify'),
        mediumSeverityChain
      )
      .otherwise(lowSeverityChain);

    // Build the full definition
    const definition = classifySeverity.afterwards().next(routeAction);

    const stateMachine = new sfn.StateMachine(this, 'MacieResponseStateMachine', {
      stateMachineName: 'MacieSensitiveDataResponse',
      definitionBody: sfn.DefinitionBody.fromChainable(definition),
      timeout: cdk.Duration.minutes(5),
    });

    // EventBridge rule: Macie finding published
    const macieRule = new events.Rule(this, 'MacieFindingRule', {
      ruleName: 'MacieSensitiveDataFinding',
      description: 'Routes Amazon Macie sensitive data findings to Step Functions for automated response',
      eventPattern: {
        source: ['aws.macie'],
        detailType: ['Macie Finding'],
        detail: {
          type: [{ prefix: 'SensitiveData' }],
        },
      },
    });

    macieRule.addTarget(new events_targets.SfnStateMachine(stateMachine));

    // Enable Macie (creates a session if not already enabled)
    const macieSession = new cdk.CfnResource(this, 'MacieSession', {
      type: 'AWS::Macie::Session',
      properties: {
        FindingPublishingFrequency: 'FIFTEEN_MINUTES',
        Status: 'ENABLED',
      },
    });

    // Outputs
    new cdk.CfnOutput(this, 'MonitoredBucketName', {
      value: sourceBucket.bucketName,
      description: 'Upload files here to be scanned by Amazon Macie',
    });

    new cdk.CfnOutput(this, 'QuarantineBucketName', {
      value: quarantineBucket.bucketName,
      description: 'High-severity sensitive data objects are moved here',
    });

    new cdk.CfnOutput(this, 'StateMachineArn', {
      value: stateMachine.stateMachineArn,
      description: 'Step Functions state machine ARN for Macie response automation',
    });

    new cdk.CfnOutput(this, 'NotificationTopicArn', {
      value: notificationTopic.topicArn,
      description: 'SNS topic for finding notifications',
    });
  }
}

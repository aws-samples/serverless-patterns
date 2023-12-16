import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import path = require('path');
import * as iam from 'aws-cdk-lib/aws-iam';
import * as sns from 'aws-cdk-lib/aws-sns';
import * as event_source from 'aws-cdk-lib/aws-lambda-event-sources';


export class CdkCodepipelineManualApprovalLambdaSchedulerSesStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    const accountId = cdk.Stack.of(this).account;
    const region = cdk.Stack.of(this).region;

    const snsTopicARN = new cdk.CfnParameter(this, 'SNSTopicARN', {
      type: 'String',
      description: 'ARN of the SNS topic associated with the Manual Approval Stage',
    });
    
    const senderEmail = new cdk.CfnParameter(this, 'SenderEmail', {
      type: 'String',
      description: 'Email ID of the sender who would send reminder emails using SES',
    });
    
    const receiverEmail = new cdk.CfnParameter(this, 'ReceiverEmail', {
      type: 'String',
      description: 'Email ID of the receiver who would receive reminder emails. ',
    });
    
    const triggerFnRole = new iam.Role(this, 'TriggerFunctionRole', {
      assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com')
    });
    
    triggerFnRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonSESFullAccess'));
    triggerFnRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('AWSCodePipeline_FullAccess'));
    triggerFnRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('CloudWatchLogsFullAccess'));
    
    const schedulerRole = new iam.Role(this, 'SchedulerRole', {
      assumedBy: new iam.ServicePrincipal('scheduler.amazonaws.com')
    });

    const triggerfn = new lambda.Function(this, 'ReminderFunction', {
      runtime: lambda.Runtime.PYTHON_3_11,
      handler: 'trigger_function.lambda_handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '../trigger_function')),
      environment: {
        'SES_SOURCE_EMAIL': senderEmail.valueAsString
      },
      role:triggerFnRole
    },
    );
    
    const schedulerPolicy = new iam.Policy(this, 'SchedulerPolicy', {
      statements: [
        new iam.PolicyStatement({
          actions: ['lambda:InvokeFunction'],
          resources: [
            `arn:aws:lambda:${region}:${accountId}:function:${triggerfn.functionName}:*`,
            `arn:aws:lambda:${region}:${accountId}:function:${triggerfn.functionName}`
            ]
        })
        ]
    });
    schedulerPolicy.attachToRole(schedulerRole);
    
    const role = new iam.Role(this, 'LambdaFunctionRole', {
      
      assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com')
    });
    role.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('AWSCodePipeline_FullAccess'));
    role.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonEventBridgeSchedulerFullAccess'));
    role.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('CloudWatchLogsFullAccess'));
    
    
    const fn = new lambda.Function(this, 'SchedulerFunction', {
      runtime: lambda.Runtime.PYTHON_3_11,
      handler: 'eventbridge_scheduler.lambda_handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '../scheduler_function'), {
        bundling: { 
          image: lambda.Runtime.PYTHON_3_11.bundlingImage,
          command: [
            'bash', '-c',
            'pip install -r requirements.txt -t /asset-output && cp -au . /asset-output'
            ],
      },
      }),
      environment: {
        'SES_DESTINATION_EMAIL': receiverEmail.valueAsString,
        'TRIGGER_LAMBDA_ARN': triggerfn.functionArn,
        'SCHEDULER_ROLE_ARN': schedulerRole.roleArn
      },
      role: role
    });
    
    const snsTopic = sns.Topic.fromTopicArn(this, 'mySNSTopic', snsTopicARN.valueAsString);
    
    fn.addEventSource(new event_source.SnsEventSource(snsTopic));
    
  }
}

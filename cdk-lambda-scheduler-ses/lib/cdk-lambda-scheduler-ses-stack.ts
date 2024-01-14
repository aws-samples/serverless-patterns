import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import path = require('path');
import * as iam from 'aws-cdk-lib/aws-iam';

export class CdkLambdaSchedulerSesStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    
    const senderEmail = new cdk.CfnParameter(this, 'SenderEmail', {
      type: 'String',
      description: 'Email ID of the sender who would send reminder emails using SES',
    });

    const schedulerRole = new iam.Role(this, 'SchedulerRole', {
      assumedBy: new iam.ServicePrincipal('scheduler.amazonaws.com')
    });

    const schedulerPolicy = new iam.Policy(this, 'SchedulerPolicy', {
      statements: [
        new iam.PolicyStatement({
          actions: ['ses:SendEmail'],
          resources: ['*']
        })
        ]
    });
    schedulerPolicy.attachToRole(schedulerRole);
    const role = new iam.Role(this, 'LambdaFunctionRole', {
      
      assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com')
    });
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
        'SCHEDULER_ROLE_ARN': schedulerRole.roleArn,
        'SES_SENDER_IDENTITY': senderEmail.valueAsString
      },
      role: role
    });

  }
}










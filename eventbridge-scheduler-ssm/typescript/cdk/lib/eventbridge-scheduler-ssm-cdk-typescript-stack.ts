import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnSchedule } from 'aws-cdk-lib/aws-scheduler';
import { PolicyStatement, Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { aws_ssm as ssm } from 'aws-cdk-lib';

export class EventbridgeSchedulerSsmCdkTypescriptStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // create an association to update SSM agent on all instances
    const cfnAssociation = new ssm.CfnAssociation(this, 'SSMAssociation', {
      name: 'AWS-UpdateSSMAgent',
      associationName: 'UpdateSSMAgent',
      targets: [{
        key: 'instanceids',
        values: ['*'],
      }],
      waitForSuccessTimeoutSeconds: 120,
    });

    // create a role and a policy to allow running associations
    const schedulerRole = new Role(this, 'scheduler-role', {
      assumedBy: new ServicePrincipal('scheduler.amazonaws.com'),
    });

    schedulerRole.addToPolicy(new PolicyStatement({
      actions: ['ssm:StartAssociationsOnce'],
      resources: ['*']
    }));

    const flexibleTimeWindowProperty: CfnSchedule.FlexibleTimeWindowProperty = {
      mode: 'OFF',    
    };
    
    // schedule to run every Sunday at 2:00am
    const scheduler = new CfnSchedule(this, 'run-command', {
      scheduleExpression: 'cron(0 2 ? * SUN *)',
      description: "Schedule to run an SSM accociation every Sunday",
      flexibleTimeWindow: flexibleTimeWindowProperty,
      target: {
        input: JSON.stringify({"AssociationIds": [cfnAssociation.attrAssociationId]}),
        arn: 'arn:aws:scheduler:::aws-sdk:ssm:startAssociationsOnce',
        roleArn: schedulerRole.roleArn
      }
    })

  }
}

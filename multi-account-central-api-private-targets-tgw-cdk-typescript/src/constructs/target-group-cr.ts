import { Construct } from 'constructs';
import {
  AwsCustomResource,
  PhysicalResourceId,
} from 'aws-cdk-lib/custom-resources';
import { LoggingFormat, Runtime, Tracing } from 'aws-cdk-lib/aws-lambda';
import { Duration } from 'aws-cdk-lib';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { Protocol, TargetType } from 'aws-cdk-lib/aws-elasticloadbalancingv2';

export interface MyTargetGroupProps {
  readonly tgName: string;
  readonly listenerPort: number;
  readonly targetPort: number;
  readonly protocol: Protocol;
  readonly targetType: TargetType;
  readonly vpcId: string;
  readonly ssmARN: string;
  readonly nlbARN: string;
  readonly accountNumber: string;
  readonly tags?: { [key: string]: string };
}

export class MyTargetGroup extends Construct {
  constructor(scope: Construct, id: string, props: MyTargetGroupProps) {
    super(scope, id);

    // Lambda Function props
    const nodejsFunctionProps = {
      runtime: Runtime.NODEJS_22_X,
      memorySize: 128,
      timeout: Duration.seconds(100),
      tracing: Tracing.ACTIVE,
      loggingFormat: LoggingFormat.JSON,
    };

    // Create Lambda Function to be used for the custom resource
    const onUpdateEventLambda = new NodejsFunction(
      this,
      'CreateListenerTargetGroup',
      {
        handler: 'handler',
        entry: `${__dirname}/../lambda/create-nlb-targetgrp.ts`,
        ...nodejsFunctionProps,
      }
    );

    // Delete Lambda Function to be used for the custom resource
    const onDeleteEventLambda = new NodejsFunction(this, 'DeleteTargetGroups', {
      handler: 'handler',
      entry: `${__dirname}/../lambda/delete-nlb-targetgrp.ts`,
      ...nodejsFunctionProps,
    });

    // Add permissions to Lambda to create listener and target group
    onUpdateEventLambda.addToRolePolicy(
      new PolicyStatement({
        actions: [
          'elasticloadbalancing:CreateListener',
          'elasticloadbalancing:CreateTargetGroup',
          'elasticloadbalancing:RegisterTargets',
          'elasticloadbalancing:AddTags',
        ],
        resources: [
          props.nlbARN,
          `arn:aws:elasticloadbalancing:*:${props.accountNumber}:listener/net/*/*/*`,
          `arn:aws:elasticloadbalancing:*:${props.accountNumber}:listener-rule/net/*/*/*/*`,
          `arn:aws:elasticloadbalancing:*:${props.accountNumber}:targetgroup/*/*`,
        ],
      })
    );

    // Add permissions to Lambda to read from parameter store
    onUpdateEventLambda.addToRolePolicy(
      new PolicyStatement({
        actions: ['ssm:GetParameter'],
        resources: [props.ssmARN],
      })
    );

    // Add permissions to Lambda to tag resoruces
    onUpdateEventLambda.addToRolePolicy(
      new PolicyStatement({
        actions: ['tag:TagResources'],
        resources: ['*'],
      })
    );

    // Add permissions to Lambda to delete target group
    onDeleteEventLambda.addToRolePolicy(
      new PolicyStatement({
        actions: [
          'elasticloadbalancing:DeleteTargetGroup',
          'elasticloadbalancing:DeleteListener',
        ],
        resources: [
          `arn:aws:elasticloadbalancing:*:${props.accountNumber}:targetgroup/*/*`,
          `arn:aws:elasticloadbalancing:*:${props.accountNumber}:listener/net/*/*/*`,
        ],
      })
    );

    onDeleteEventLambda.addToRolePolicy(
      new PolicyStatement({
        actions: [
          'elasticloadbalancing:DescribeTargetGroups',
          'elasticloadbalancing:DescribeListeners',
        ],
        resources: ['*'],
      })
    );

    // Create custom resource
    const nlbTargetGroupCR = new AwsCustomResource(this, 'ELB-ENIS', {
      onUpdate: {
        service: 'Lambda',
        action: 'invoke',
        parameters: {
          FunctionName: onUpdateEventLambda.functionName,
          InvocationType: 'RequestResponse',
          Payload: JSON.stringify({
            tgName: props.tgName,
            listenerPort: props.listenerPort,
            targetPort: props.targetPort,
            protocol: props.protocol,
            targetType: props.targetType,
            vpcId: props.vpcId,
            ssmARN: props.ssmARN,
            nlbARN: props.nlbARN,
            tags: props.tags,
          }),
        },
        physicalResourceId: PhysicalResourceId.of(Date.now().toString()), // Update physical id to always fetch the latest version
      },
      onDelete: {
        service: 'Lambda',
        action: 'invoke',
        parameters: {
          FunctionName: onDeleteEventLambda.functionName,
          InvocationType: 'Event',
          Payload: JSON.stringify({
            nlbARN: props.nlbARN,
          }),
        },
      },
      policy: {
        statements: [
          new PolicyStatement({
            actions: ['lambda:InvokeFunction'],
            resources: [
              onUpdateEventLambda.functionArn,
              onDeleteEventLambda.functionArn,
            ],
          }),
        ],
      },
    });

    // Adding dependencies to the custom resource
    nlbTargetGroupCR.node.addDependency(onUpdateEventLambda);
    nlbTargetGroupCR.node.addDependency(onDeleteEventLambda);

    // Saving the ELB ENI information from the Lambda Function
    //this.elbPoints = elbAttributes.getResponseField('Payload');
  }
}

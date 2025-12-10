import { Stack, StackProps, Duration, CfnOutput } from 'aws-cdk-lib/core';
import { NodejsFunction, OutputFormat } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Architecture, CapacityProvider, Runtime } from 'aws-cdk-lib/aws-lambda';
import { Construct } from 'constructs';
import { SecurityGroup, Vpc } from 'aws-cdk-lib/aws-ec2';

export class DemoStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const durableFunction = new NodejsFunction(this, 'StepWaitStepFunction', {
      entry: 'lambda/step-wait-step.mts',
      handler: 'handler',
      runtime: Runtime.NODEJS_24_X,
      architecture: Architecture.ARM_64,
      functionName: 'step-wait-step-durable-function',
      description: 'Lambda durable function demonstrating step-wait-step pattern',
      bundling: {
        format: OutputFormat.ESM,
        mainFields: ['module', 'main'],
      },
      durableConfig: {
        executionTimeout: Duration.hours(1), retentionPeriod: Duration.days(30),
      },
    });

    const vpc = new Vpc(this, 'LambdaManagedInstancesVPC');
    const securityGroup = new SecurityGroup(this, 'SecurityGroup', { vpc });

    const capacityProvider = new CapacityProvider(this, 'LambdaCapacityProvider', {
      capacityProviderName: 'lambda-capacity-provider',
      subnets: vpc.privateSubnets,
      securityGroups: [securityGroup],
      architectures: [Architecture.ARM_64],
    });

    capacityProvider.addFunction(durableFunction);

    new CfnOutput(this, 'FunctionName', {
      value: durableFunction.functionName,
      description: 'Lambda function name for CLI invocation',
    });
  }
}

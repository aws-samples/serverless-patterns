import { Stack, StackProps, CfnOutput, RemovalPolicy } from 'aws-cdk-lib/core';
import { NodejsFunction, OutputFormat } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Architecture, CapacityProvider, Runtime, LoggingFormat } from 'aws-cdk-lib/aws-lambda';
import { Construct } from 'constructs';
import { SecurityGroup, Vpc } from 'aws-cdk-lib/aws-ec2';
import { LogGroup, RetentionDays } from 'aws-cdk-lib/aws-logs';

export class DemoStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const functionName = 'hello-world-managed-instances-cdk';

    const logGroup = new LogGroup(this, 'DemoLogGroup', {
      logGroupName: `/demo/lambda/${functionName}`,
      retention: RetentionDays.TWO_WEEKS,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    const helloWorldFunction = new NodejsFunction(this, 'HelloWorldFunction', {
      entry: 'lambda/hello-world.mts',
      handler: 'handler',
      runtime: Runtime.NODEJS_24_X,
      architecture: Architecture.ARM_64,
      functionName,
      description: 'Simple Hello World Lambda function on Managed Instances',
      loggingFormat: LoggingFormat.JSON,
      logGroup,
      bundling: {
        format: OutputFormat.ESM,
        mainFields: ['module', 'main'],
      },
    });

    const vpc = new Vpc(this, 'LambdaManagedInstancesVPC');
    const securityGroup = new SecurityGroup(this, 'SecurityGroup', { vpc });

    const capacityProvider = new CapacityProvider(this, 'LambdaCapacityProvider', {
      capacityProviderName: 'lambda-capacity-provider-cdk',
      subnets: vpc.privateSubnets,
      securityGroups: [securityGroup],
      architectures: [Architecture.ARM_64],
    });

    capacityProvider.addFunction(helloWorldFunction);

    new CfnOutput(this, 'FunctionName', {
      value: helloWorldFunction.functionName,
      description: 'Lambda function name for CLI invocation',
    });

    new CfnOutput(this, 'FunctionArn', {
      value: helloWorldFunction.functionArn,
      description: 'Lambda function ARN',
    });

    new CfnOutput(this, 'LogGroupName', {
      value: logGroup.logGroupName,
      description: 'CloudWatch Log Group name',
    });
  }
}
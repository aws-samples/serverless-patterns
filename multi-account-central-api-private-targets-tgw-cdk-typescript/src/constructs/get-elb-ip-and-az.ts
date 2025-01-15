import { Construct } from 'constructs';
import {
  AwsCustomResource,
  PhysicalResourceId,
} from 'aws-cdk-lib/custom-resources';
import {
  LoggingFormat,
  Runtime,
  Tracing,
} from 'aws-cdk-lib/aws-lambda';
import { Duration } from 'aws-cdk-lib';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { PolicyStatement } from 'aws-cdk-lib/aws-iam';

export interface MyELBIPAttributesProps {
  readonly elbArn: string;
}

export class MyELBIPAttributes extends Construct {
  readonly elbPoints: string;

  constructor(scope: Construct, id: string, props: MyELBIPAttributesProps) {
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
    const onEventLambda = new NodejsFunction(this, 'GetELBIpAz', {
      handler: 'handler',
      entry: `${__dirname}/../lambda/get-elb-ip-az.ts`,
      ...nodejsFunctionProps,
    });

    // Add permissions to Lambda to call EC2 calls
    onEventLambda.addToRolePolicy(
      new PolicyStatement({
        actions: ['ec2:DescribeNetworkInterfaces'],
        resources: ['*'],
      })
    );

    // Create custom resource
    const elbAttributes = new AwsCustomResource(this, 'ELB-ENIS', {
      onUpdate: {
        service: 'Lambda',
        action: 'invoke',
        parameters: {
          FunctionName: onEventLambda.functionName,
          InvocationType: 'RequestResponse',
          Payload: JSON.stringify({
            elbArn: props.elbArn,
          }),
        },
        physicalResourceId: PhysicalResourceId.of(Date.now().toString()), // Update physical id to always fetch the latest version
      },
      policy: {
        statements: [
          new PolicyStatement({
            actions: ['lambda:InvokeFunction'],
            resources: [onEventLambda.functionArn],
          }),
        ],
      },
    });

    // Adding dependencies to the custom resource
    elbAttributes.node.addDependency(onEventLambda);

    // Saving the ELB ENI information from the Lambda Function
    this.elbPoints = elbAttributes.getResponseField('Payload');
  }
}

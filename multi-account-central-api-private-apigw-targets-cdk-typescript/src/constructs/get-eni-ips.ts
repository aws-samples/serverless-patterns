import { Construct } from 'constructs';
import {
  AwsCustomResource,
  PhysicalResourceId,
} from 'aws-cdk-lib/custom-resources';
import { Token } from 'aws-cdk-lib';
import { PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { Vpc } from 'aws-cdk-lib/aws-ec2';
import { IpTarget } from 'aws-cdk-lib/aws-elasticloadbalancingv2-targets';

export interface MyENIAttributesProps {
  readonly interfaceEPId: string;
  readonly vpc: Vpc;
}

export class MyENIIPAttributes extends Construct {
  readonly ipList: IpTarget[] = [];

  constructor(scope: Construct, id: string, props: MyENIAttributesProps) {
    super(scope, id);

    // Create an array of output paths to return from the custom source
    const outputPaths = props.vpc.privateSubnets.map(
      (_, index) => `NetworkInterfaces.${index}.PrivateIpAddress`
    );
    const getEndpointIp = new AwsCustomResource(this, `GetEndpointIp`, {
      onUpdate: {
        service: 'EC2',
        action: 'describeNetworkInterfaces',
        outputPaths: outputPaths,
        parameters: {
          Filters: [
            {
              Name: 'description',
              Values: [`VPC Endpoint Interface ${props.interfaceEPId}`],
            },
          ],
        },
        physicalResourceId: PhysicalResourceId.of(props.interfaceEPId),
      },
      policy: {
        statements: [
          new PolicyStatement({
            actions: ['ec2:DescribeNetworkInterfaces'],
            resources: ['*'],
          }),
        ],
      },
    });

    outputPaths.map((outputPath) => {
      this.ipList.push(
        new IpTarget(Token.asString(getEndpointIp.getResponseField(outputPath)))
      );
    });
  }
}

import { StackProps, Stack, CfnOutput } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnTransitGateway } from 'aws-cdk-lib/aws-ec2';
import { CfnResourceShare } from 'aws-cdk-lib/aws-ram';
import { ParameterTier, StringParameter } from 'aws-cdk-lib/aws-ssm';

export interface TgwStackProps extends StackProps {
  accountsToShare: string[];
  tgwParamId: string;
  tgwParamName: string;
}

export class TgwStack extends Stack {
  public readonly transitGateway: CfnTransitGateway;

  constructor(scope: Construct, id: string, props: TgwStackProps) {
    super(scope, id, props);

    // Create Transit Gateway
    this.transitGateway = new CfnTransitGateway(this, 'MyTGW', {
      description: 'Central API Transit Gateway',
      autoAcceptSharedAttachments: 'enable',
      defaultRouteTableAssociation: 'enable',
      defaultRouteTablePropagation: 'enable',
      tags: [
        {
          key: 'Name',
          value: 'Central API Transit Gateway',
        },
      ],
    });

    // Share Transit Gateway
    new CfnResourceShare(this, 'CentralApiTgwShare', {
      name: 'CentralApiTgwShare',
      allowExternalPrincipals: true,
      principals: props.accountsToShare,
      resourceArns: [this.transitGateway.attrTransitGatewayArn],
    });

    // Store the TGW ID in SSM Parameter Store
    const tgwParam = new StringParameter(this, props.tgwParamId, {
      parameterName: props.tgwParamName,
      tier: ParameterTier.ADVANCED,
      stringValue: this.transitGateway.ref,
    });

    // Share SSM Parameter
    new CfnResourceShare(this, 'TGWShare', {
      name: 'TGWShare',
      allowExternalPrincipals: true,
      principals: props.accountsToShare,
      resourceArns: [tgwParam.parameterArn],
    });

    new CfnOutput(this, 'TGWID', {
      value: this.transitGateway.ref,
      description: 'Trasnit Gateway ID',
    });
  }
}

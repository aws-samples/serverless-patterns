import { StackProps, Stack } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { MyVPC } from '../constructs/vpc-with-ssm';
import { MyFargateService } from '../constructs/fargate-service';
import { MyELBIPAttributes } from '../constructs/get-elb-ip-and-az';
import { ParameterTier, StringParameter } from 'aws-cdk-lib/aws-ssm';
import { CfnResourceShare } from 'aws-cdk-lib/aws-ram';

export interface ServiceBStackProps extends StackProps {
  accountsForNLBShare: string[];
  svcACidr: string;
  svcBCidr: string;
  centralApiCidr: string;
  tgwParamId: string;
  tgwParamName: string;
  tgwAccount: string;
  svcBNLBParamId: string;
  svcBNLBParamName: string;
}

export class ServiceBStack extends Stack {
  constructor(scope: Construct, id: string, props: ServiceBStackProps) {
    super(scope, id, props);

    // Create VPC for the workload
    const myVPC = new MyVPC(this, 'MyVPC', {
      cidr: props.svcBCidr,
      tgwParamId: props.tgwParamId,
      tgwParamName: props.tgwParamName,
      tgwAccount: props.tgwAccount,
      associatedVPCCidrs: [props.svcACidr, props.centralApiCidr],
    });

    // Create Fargate for ECS
    const myFargateService = new MyFargateService(this, 'ServiceB', {
      vpc: myVPC.vpc,
      loadbalancerType: 'NLB',
    });

    // Getting the NLB IP and AZs, store them in Parameter Store and share with the Central API account
    const nlbENIs = new MyELBIPAttributes(this, 'MyELBIPAttributes', {
      elbArn: myFargateService.fargateService.loadBalancer.loadBalancerArn,
    });

    // Store the NLB ENI information SSM Parameter Store
    const nlbParam = new StringParameter(this, props.svcBNLBParamId, {
      parameterName: props.svcBNLBParamName,
      tier: ParameterTier.ADVANCED,
      stringValue: nlbENIs.elbPoints,
    });

    // Share SSM Parameter
    new CfnResourceShare(this, 'SvcB-NLB-Share', {
      name: 'SvcB-NLB-Share',
      allowExternalPrincipals: true,
      principals: props.accountsForNLBShare,
      resourceArns: [nlbParam.parameterArn],
    });
  }
}

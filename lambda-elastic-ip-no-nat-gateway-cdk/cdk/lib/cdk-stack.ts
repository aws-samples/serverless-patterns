import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';

export interface LambdaElasticIpStackProps extends cdk.StackProps {
    vpcId?: string;
    subnetId?: string;
    securityGroupId?: string;
}

interface AssociateLambdaToElasticIpCRProps {
    elasticIP: cdk.aws_ec2.CfnEIP;
    vpc: cdk.aws_ec2.IVpc;
    publicSubnet: cdk.aws_ec2.ISubnet;
    securityGroup: cdk.aws_ec2.ISecurityGroup;
    functionName: string;
}
export class LambdaElasticIpStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props: LambdaElasticIpStackProps) {
        super(scope, id, props);

        const vpc = cdk.aws_ec2.Vpc.fromLookup(this, 'Default-VPC', { isDefault: !props.vpcId, vpcId: props.vpcId });
        const securityGroup = !!props.securityGroupId
            ? cdk.aws_ec2.SecurityGroup.fromLookupById(this, 'Elastic-IP-Lambda-Security-Group', props.securityGroupId)
            : new cdk.aws_ec2.SecurityGroup(this, 'Elastic-IP-Lambda-Security-Group', {
                  vpc,
                  allowAllOutbound: true,
                  description:
                      'This is a security group for a vpc attached lambda that uses elastic ip to have outbound communication without the need for a NAT solution',
              });

        const publicSubnet = !!props.subnetId
            ? cdk.aws_ec2.Subnet.fromSubnetId(this, 'Elastic-IP-Lambda-Subnet', props.subnetId)
            : vpc.publicSubnets[0];

        const publicFunction = new cdk.aws_lambda_nodejs.NodejsFunction(this, 'Lambda-With-Elastic-IP', {
            memorySize: 128,
            handler: 'handler',
            functionName: 'vin-api-lambda',
            timeout: cdk.Duration.seconds(10),
            bundling: {
                minify: true,
                sourceMap: true,
                sourceMapMode: cdk.aws_lambda_nodejs.SourceMapMode.DEFAULT, // defaults to SourceMapMode.DEFAULT
            },
            vpc,
            securityGroups: [securityGroup],
            allowPublicSubnet: true,
            vpcSubnets: { subnets: [publicSubnet] },
            runtime: cdk.aws_lambda.Runtime.NODEJS_18_X,
            entry: 'src/lambdas/vin-api-lambda.ts',
        });

        const elasticIP = new cdk.aws_ec2.CfnEIP(this, 'Lambda-Elastic-Ip', {});

        this.associateLambdaToElasticIpCR({
            elasticIP,
            vpc,
            publicSubnet,
            securityGroup,
            functionName: publicFunction.functionName,
        });
    }

    private associateLambdaToElasticIpCR({ elasticIP, publicSubnet, securityGroup, vpc, functionName }: AssociateLambdaToElasticIpCRProps) {
        const associateElasticIpFunctionCR = new cdk.aws_lambda_nodejs.NodejsFunction(this, 'Associate-Elastic-IP-CR', {
            memorySize: 128,
            handler: 'handler',
            timeout: cdk.Duration.seconds(10),
            bundling: {
                minify: true,
                sourceMap: true,
                sourceMapMode: cdk.aws_lambda_nodejs.SourceMapMode.DEFAULT, // defaults to SourceMapMode.DEFAULT
            },
            environment: {
                ELASTIC_IP_ALLOCATION_ID: elasticIP.attrAllocationId,
            },
            runtime: cdk.aws_lambda.Runtime.NODEJS_18_X,
            entry: 'src/lambdas/associate-lambda-elastic-ip-cr.ts',
        });

        associateElasticIpFunctionCR.addToRolePolicy(
            new cdk.aws_iam.PolicyStatement({
                effect: cdk.aws_iam.Effect.ALLOW,
                actions: ['ec2:AssociateAddress', 'ec2:DescribeNetworkInterfaces'],
                resources: ['*'],
            }),
        );

        const awsSDKCall: cdk.custom_resources.AwsSdkCall = {
            service: 'Lambda',
            action: 'invoke',
            parameters: {
                FunctionName: associateElasticIpFunctionCR.functionName,
                Payload: JSON.stringify({
                    vpcId: vpc.vpcId,
                    subnetId: publicSubnet.subnetId,
                    securityGroupId: securityGroup.securityGroupId,
                    availabilityZone: publicSubnet.availabilityZone,
                    allocationId: elasticIP.attrAllocationId,
                    staticIp: elasticIP.ref,
                    functionName,
                    date: new Date(),
                }),
            },
            physicalResourceId: cdk.custom_resources.PhysicalResourceId.of(`Associate-Elastic-IP-CR`),
        };
        const customResource = new cdk.custom_resources.AwsCustomResource(this, 'Invoke-Associate-Elastic-IP-Lambda', {
            onCreate: awsSDKCall,
            onUpdate: awsSDKCall,
            policy: cdk.custom_resources.AwsCustomResourcePolicy.fromSdkCalls({
                resources: cdk.custom_resources.AwsCustomResourcePolicy.ANY_RESOURCE,
            }),
        });

        associateElasticIpFunctionCR.grantInvoke(customResource);
    }
}

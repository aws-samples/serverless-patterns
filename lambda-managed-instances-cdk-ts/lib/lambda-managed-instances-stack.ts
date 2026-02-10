import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as path from 'path';

export class LambdaManagedInstancesStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Step 1: Create the required IAM roles (following instructions exactly)
    
    // Lambda execution role
    const lambdaExecutionRole = new iam.Role(this, 'LambdaExecutionRole', {
      roleName: 'MyLambdaExecutionRole',
      assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaBasicExecutionRole')
      ]
    });

    // Capacity provider operator role
    const capacityProviderOperatorRole = new iam.Role(this, 'CapacityProviderOperatorRole', {
      roleName: 'MyCapacityProviderOperatorRole',
      assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('AWSLambdaManagedEC2ResourceOperator')
      ]
    });

    // Step 2: Set up VPC resources (following instructions exactly)
    
    // Create VPC with CIDR 10.0.0.0/16
    const vpc = new ec2.Vpc(this, 'LambdaManagedInstancesVpc', {
      ipAddresses: ec2.IpAddresses.cidr('10.0.0.0/16'),
      maxAzs: 1, // Instructions show single subnet
      subnetConfiguration: [
        {
          cidrMask: 24,
          name: 'lambda-subnet',
          subnetType: ec2.SubnetType.PUBLIC, // Instructions create in public for simplicity
        }
      ],
      natGateways: 0 // No NAT needed for public subnet
    });

    // Create security group (following instructions exactly)
    const securityGroup = new ec2.SecurityGroup(this, 'LambdaManagedInstancesSecurityGroup', {
      vpc: vpc,
      description: 'Security group for Lambda Managed Instances',
      securityGroupName: 'my-capacity-provider-sg'
    });

    // Step 3: Create capacity provider (using native CDK L1 construct)
    const capacityProvider = new lambda.CfnCapacityProvider(this, 'CapacityProvider', {
      capacityProviderName: 'my-capacity-provider',
      vpcConfig: {
        subnetIds: [vpc.publicSubnets[0].subnetId],
        securityGroupIds: [securityGroup.securityGroupId]
      },
      permissionsConfig: {
        capacityProviderOperatorRoleArn: capacityProviderOperatorRole.roleArn
      },
      instanceRequirements: {
        architectures: ['x86_64']
      },
      capacityProviderScalingConfig: {
        maxVCpuCount: 30
      }
    });

    // Step 4: Create Lambda function with managed instances
    const managedInstanceFunction = new lambda.CfnFunction(this, 'ManagedInstanceFunction', {
      functionName: 'my-managed-instance-function',
      runtime: 'nodejs24.x', // Using nodejs24.x as requested
      handler: 'index.handler',
      code: {
        zipFile: `
exports.handler = async (event, context) => {
  console.log('Event:', JSON.stringify(event, null, 2));
  
  return {
    statusCode: 200,
    body: JSON.stringify({
      message: 'Hello from Lambda Managed Instances!',
      event: event
    })
  };
};`
      },
      role: lambdaExecutionRole.roleArn,
      architectures: ['x86_64'],
      memorySize: 2048,
      ephemeralStorage: {
        size: 512
      },
      capacityProviderConfig: {
        lambdaManagedInstancesCapacityProviderConfig: {
          capacityProviderArn: capacityProvider.capacityProviderRef.capacityProviderArn
        }
      }
    });

    // Step 5: Publish function version (following instructions exactly)
    const functionVersion = new lambda.CfnVersion(this, 'ManagedInstanceFunctionVersion', {
      functionName: managedInstanceFunction.ref,
      description: 'Version 1 of Lambda Managed Instance function'
    });

    // Outputs (matching the instructions)
    new cdk.CfnOutput(this, 'VpcId', {
      value: vpc.vpcId,
      description: 'VPC ID for Lambda Managed Instances'
    });

    new cdk.CfnOutput(this, 'SubnetId', {
      value: vpc.publicSubnets[0].subnetId,
      description: 'Subnet ID for Lambda Managed Instances'
    });

    new cdk.CfnOutput(this, 'SecurityGroupId', {
      value: securityGroup.securityGroupId,
      description: 'Security Group ID for Lambda Managed Instances'
    });

    new cdk.CfnOutput(this, 'LambdaFunctionName', {
      value: managedInstanceFunction.ref,
      description: 'Lambda function name'
    });

    new cdk.CfnOutput(this, 'LambdaFunctionArn', {
      value: managedInstanceFunction.attrArn,
      description: 'Lambda function ARN'
    });

    new cdk.CfnOutput(this, 'CapacityProviderOperatorRoleArn', {
      value: capacityProviderOperatorRole.roleArn,
      description: 'Capacity Provider Operator Role ARN'
    });
  }
}
import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { aws_ec2 as ec2 } from 'aws-cdk-lib';
import { PythonFunction } from "@aws-cdk/aws-lambda-python-alpha";
import { Runtime } from 'aws-cdk-lib/aws-lambda';
import { Effect, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { Stack, StackProps, Duration } from 'aws-cdk-lib';
import * as secretsmanager from 'aws-cdk-lib/aws-secretsmanager';
export class AwsLambdaPrivSubnetStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const privateLambdaVPC = new ec2.Vpc(this, "PrivateLambdaVPC", {
      vpcName: "PrivateLambdaVPC",
      subnetConfiguration: [
        {
          name: 'Isolated',
          subnetType: ec2.SubnetType.PRIVATE_ISOLATED,
        }
      ]
    });

    const lambdaSecurityGroup = new ec2.SecurityGroup(this, 'PrivateLambdaSG', {
      securityGroupName: 'PrivateLambdaSG',
      vpc: privateLambdaVPC
    });

    lambdaSecurityGroup.connections.allowFrom(lambdaSecurityGroup, ec2.Port.allTraffic());

    const lambdaFunctionPrivate = new PythonFunction(this, `LambdaFunctionPrivate`, {
      entry: `lambda/LambdaFunctionPrivate`,
      index: 'handler.py',
      handler: 'lambda_handler',
      functionName: 'LambdaFunctionPrivate',
      runtime: Runtime.PYTHON_3_9,
      memorySize: 128,
      securityGroups: [lambdaSecurityGroup],
      vpc: privateLambdaVPC,
      timeout: Duration.seconds(60)
    });

    lambdaFunctionPrivate.addToRolePolicy(new PolicyStatement({
      "effect": Effect.ALLOW,
      "actions": [
        "secretsmanager:ListSecrets",
        "ec2:CreateNetworkInterface",
        "ec2:DeleteNetworkInterface",
        "ec2:DescribeNetworkInterfaces"
      ],
      "resources": ["*"]
    }));

    const secretsManagerInterfaceEndpoint = privateLambdaVPC.addInterfaceEndpoint('SecretsManagerEndpoint', {
      service: ec2.InterfaceVpcEndpointAwsService.SECRETS_MANAGER,
      privateDnsEnabled: true,
      subnets: { subnetType: ec2.SubnetType.PRIVATE_ISOLATED },
      securityGroups: [lambdaSecurityGroup]
    });

    const secret = new secretsmanager.Secret(this, 'CDKExampleSecret');


  }
}

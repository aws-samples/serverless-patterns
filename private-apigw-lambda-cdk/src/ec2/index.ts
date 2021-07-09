
import * as cdk from '@aws-cdk/core';
import * as  ec2  from '@aws-cdk/aws-ec2';
import { Role, ServicePrincipal, ManagedPolicy, CfnInstanceProfile } from '@aws-cdk/aws-iam'
import config from "../api/config.json";

export class Ec2Stack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, vpc: ec2.Vpc) {
    super(scope, id);

    const privateSubnetOne = vpc.privateSubnets[0];

    // define the IAM role that will allow the EC2 instance to communicate with SSM 
    const role = new Role(this, 'apigatewayEC2Role', {
      assumedBy: new ServicePrincipal('ec2.amazonaws.com')
    });

    role.addManagedPolicy(ManagedPolicy.fromAwsManagedPolicyName('AmazonSSMManagedInstanceCore'));
    
    // user data script
    const ssmaUserData = ec2.UserData.forLinux();
    
    // make sure the latest SSM Agent is installed.
    // will use ssm from aws console to access this ec2 instance so no private key is needed 
    const SSM_AGENT_RPM='https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm';
    ssmaUserData.addCommands(`sudo yum install -y ${SSM_AGENT_RPM}`, 'restart amazon-ssm-agent');
  
    //EC2 instance in the private subnet
    const profile = new CfnInstanceProfile(this, `${id}Profile`, {
      roles: [ role.roleName ]
    });
    // create the instance
    const instance = new ec2.CfnInstance(this, 'apiGatewayEC2Instance', {
      imageId: new ec2.AmazonLinuxImage().getImage(this).imageId,
      instanceType: ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO).toString(),
      networkInterfaces: [
        {
          deviceIndex: "0",
          subnetId: privateSubnetOne?.subnetId
        }
      ]
      ,userData: cdk.Fn.base64(ssmaUserData.render())
      ,iamInstanceProfile: profile.ref
    });

    // tag the instance
    const tags = config.tags
    tags.forEach(tag => {
      cdk.Tags.of(instance).add(tag.key, tag.value)
    }) 
  }
}
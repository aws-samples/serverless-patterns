const {Construct} = require("constructs");
const ec2 = require("aws-cdk-lib/aws-ec2");
const iam = require("aws-cdk-lib/aws-iam");
const cdk = require("aws-cdk-lib");

/**
 * Creates a testing EC2 instance and required endpoints to establish SSM connection.
 */
class TestingConstruct extends Construct {
    constructor(scope, id, props) {
        super(scope, id, props);

        const vpc = props.vpc;

        const securityGroup = new ec2.SecurityGroup(this, 'ClientSecurityGroup', {
            vpc: vpc,
            securityGroupName: 'clientSecurityGroup'
        });

        vpc.addInterfaceEndpoint('BackendSsmEndpoint', {
            service: ec2.InterfaceVpcEndpointAwsService.SSM,
            securityGroups: [securityGroup]
        });

        vpc.addInterfaceEndpoint('BackendSsmMessagesEndpoint', {
            service: ec2.InterfaceVpcEndpointAwsService.SSM_MESSAGES,
            securityGroups: [securityGroup]
        });

        vpc.addInterfaceEndpoint('Ec2MessagesEndpoint', {
            service: ec2.InterfaceVpcEndpointAwsService.EC2_MESSAGES,
            securityGroups: [securityGroup]
        });

        const ami = new ec2.AmazonLinuxImage({
            generation: ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            cpuType: ec2.AmazonLinuxCpuType.ARM_64
        });

        const role = new iam.Role(this, 'Ec2Role', {
            assumedBy: new iam.ServicePrincipal('ec2.amazonaws.com')
        })
        role.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonSSMManagedInstanceCore'))

        const clientInstance = new ec2.Instance(this, 'TestingEC2Instance', {
            instanceName: 'client',
            vpc: vpc,
            instanceType: ec2.InstanceType.of(ec2.InstanceClass.T4G, ec2.InstanceSize.SMALL),
            machineImage: ami,
            securityGroup: securityGroup,
            role: role
        });

        new cdk.CfnOutput(this, 'ClientInstanceId', {value: clientInstance.instanceId});
    }
}

module.exports = {TestingConstruct}
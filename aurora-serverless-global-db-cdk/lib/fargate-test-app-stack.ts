import { Construct } from 'constructs';
import { Stack, aws_iam as iam } from 'aws-cdk-lib'
import { SubnetType, Port, SecurityGroup, Peer } from 'aws-cdk-lib/aws-ec2';
import { Cluster, ContainerImage, AssetImageProps } from 'aws-cdk-lib/aws-ecs';
import { ApplicationLoadBalancedFargateService} from 'aws-cdk-lib/aws-ecs-patterns';
import { DBClusterProps } from './aurora-regional-cluster-stack';

export class FargateTestAppStack extends Stack {
  constructor(scope: Construct, id: string, props: DBClusterProps) {
    super(scope, id, props);

    const dbSecurityGroup = SecurityGroup.fromSecurityGroupId(this, "db-security-group", props.dbSecurityGroupId);

    const appSecurityGroup: SecurityGroup = new SecurityGroup(this, 'app-security-group', {
      securityGroupName: 'app-security-group',
      description: 'app-security-group',
      allowAllOutbound: true,
      vpc: props.vpc,
    });

    dbSecurityGroup.addIngressRule(
      appSecurityGroup, Port.tcp(3306), 'allow port 3306 from the appSecurityGroup'
    );

    appSecurityGroup.addIngressRule(
      Peer.ipv4('0.0.0.0/0'), Port.tcp(80), 'allow port 80'
    );
    // ECS Fargate Cluster
    const cluster = new Cluster(this, 'MyCluster', {
      vpc: props.vpc
    });

    var roleName;
    var policyName;

    if (props.isPrimary) {
      roleName = 'primary-test-app-task-role';
      policyName = 'primary-test-app-task-policy';
    } else {
      roleName = 'secondary-test-app-task-role';
      policyName = 'secondary-test-app-task-policy';
    }

    const taskRole = new iam.Role(this, roleName, {
      assumedBy: new iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
      roleName: roleName,
      description: "Role that the api task definitions use to run the api code",
    });

    taskRole.attachInlinePolicy(
      new iam.Policy(this, policyName, {
        statements: [
          new iam.PolicyStatement({
            effect: iam.Effect.ALLOW,
            actions: ["secretsmanager:GetSecretValue"],
            resources: ["*"],
          }),
        ],
      })
    );

    // To enable image build for both primary and secondary regions
    const assetImageprops: AssetImageProps = {
      extraHash: Stack.of(this).region,
      invalidation: {
        extraHash: true,
      },
    }

    // Fargate based test app
    const fargate = new ApplicationLoadBalancedFargateService(this, 'Fargate', {
      cluster: cluster,
      cpu: 512,
      desiredCount: 1,
      taskImageOptions: {
        image: ContainerImage.fromAsset('fargate', assetImageprops),
        environment: {
          DB_HOST: props.endpoint,
          DB_PORT: props.port,
          REGION: props.region
        },
        taskRole: taskRole
      },
      taskSubnets: { subnetType: SubnetType.PUBLIC },
      assignPublicIp: true,
      memoryLimitMiB: 2048,
      securityGroups: [appSecurityGroup],
    });
  }
}


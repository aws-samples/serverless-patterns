using Amazon.CDK;
using Amazon.CDK.AWS.EC2;
using Amazon.CDK.AWS.ECS;
using Amazon.CDK.AWS.ElasticLoadBalancingV2;
using Amazon.CDK.AWS.IAM;
using Constructs;
using System.Collections.Generic;

namespace WindowsECS
{
    public class WindowsECSClusterStack : Stack
    {
        private Vpc vpc = VPCStack.vpc;
        private SecurityGroup alb_sg = SecurityGroupStack.alb_sg;
        private List<ApplicationTargetGroup> applicationWindowsTargetGroupsList = ALBStack.applicationWindowsTargetGroupsList;

        internal WindowsECSClusterStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // The code that defines your stack goes here
            // Create ECS Execution Role
            Role ecsExecutionRole = CreateExecutionRole();

            // Create ECS task role to be consumed by tasks to call aws resources.
            Role ecsTaskRole = CreateTaskRole();

            // Create Windows cluster
            Cluster ecsWindowsCluster = CreateCluster(vpc);

            // Create ECS Task Definition
            Ec2TaskDefinition taskDefinition = CreateTaskDefinition(ecsExecutionRole, ecsTaskRole);

            // Create new service
            CreateService(alb_sg, applicationWindowsTargetGroupsList, ecsWindowsCluster, taskDefinition);
        }

        private void CreateService(SecurityGroup alb_sg, List<ApplicationTargetGroup> applicationWindowsTargetGroupsList, Cluster ecsWindowsCluster, Ec2TaskDefinition taskDefinition)
        {
            var ec2WindowsService = new Ec2Service(this, "Ec2WindowsService", new Ec2ServiceProps
            {
                TaskDefinition = taskDefinition,
                Cluster = ecsWindowsCluster,
                DesiredCount = 1,
                DeploymentController = new DeploymentController
                {
                    Type = DeploymentControllerType.ECS
                }
            });

            ec2WindowsService.AttachToApplicationTargetGroup(applicationWindowsTargetGroupsList[0]);
            var securityGroupWindowsIs = ecsWindowsCluster.Connections.SecurityGroups[0];
            securityGroupWindowsIs.AddIngressRule(
                alb_sg, Port.TcpRange(32767, 65535), "Allows HTTPS access from ALB to ECS for windows ECS");
        }

        private Ec2TaskDefinition CreateTaskDefinition(Role ecsExecutionRole, Role ecsTaskRole)
        {
            var taskDefinition = new Ec2TaskDefinition(this, "Ec2TaskDefinition", new Ec2TaskDefinitionProps
            {
                ExecutionRole = ecsExecutionRole,
                TaskRole = ecsTaskRole,
                NetworkMode = NetworkMode.NAT
            });

            var ecsWindowsContainer = taskDefinition.AddContainer("EcsWindowsContainer", new ContainerDefinitionProps
            {
                Cpu = 512,
                MemoryLimitMiB = 1024,
                Image = ContainerImage.FromRegistry("mcr.microsoft.com/windows/servercore/iis"),
                Logging = LogDriver.AwsLogs(new AwsLogDriverProps
                {
                    StreamPrefix = "windows-ecs-cluster-logs"
                })
            });

            var portMappings = new PortMapping
            {
                ContainerPort = 80
            };
            ecsWindowsContainer.AddPortMappings(portMappings);
            return taskDefinition;
        }

        private Cluster CreateCluster(Vpc vpc)
        {
            var ecsWindowsCluster = new Cluster(this, "Windowscluster", new ClusterProps
            {
                Vpc = vpc,
                Capacity = new AddCapacityOptions
                {
                    InstanceType = new InstanceType("t2.xlarge"),
                    MachineImage = EcsOptimizedImage.Windows(WindowsOptimizedVersion.SERVER_2019),
                    MinCapacity = 1,
                    MaxCapacity = 3
                },
            });

            var userData = UserData.ForWindows();
            userData.AddCommands(
                "Import-Module ECSTools",
                "Initialize-ECSAgent -Cluster " + ecsWindowsCluster.ClusterName + " -EnableTaskIAMRole -LoggingDrivers '[json-file, awslogs]' -EnableTaskENI -AwsvpcBlockIMDS");
            Amazon.CDK.Tags.Of(ecsWindowsCluster).Add("Name", "ecs-windows-cluster");
            return ecsWindowsCluster;
        }

        private Role CreateTaskRole()
        {
            return new Role(this, "EcsTaskRoleForWindows", new RoleProps
            {
                AssumedBy = new ServicePrincipal("ecs-tasks.amazonaws.com")
            });
        }

        private Role CreateExecutionRole()
        {
            var ecsExecutionRole = new Role(this, "EcsExecutionRoleForWindows", new RoleProps
            {
                AssumedBy = new ServicePrincipal("ecs-tasks.amazonaws.com")
            });

            ecsExecutionRole.AddManagedPolicy(ManagedPolicy.FromManagedPolicyArn(this, "ManagedPolicyArnForWindows", "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"));
            return ecsExecutionRole;
        }
    }
}
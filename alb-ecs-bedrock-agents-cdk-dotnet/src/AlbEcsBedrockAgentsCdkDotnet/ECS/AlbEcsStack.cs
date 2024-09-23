using Amazon.CDK;
using Amazon.CDK.AWS.EC2;
using Amazon.CDK.AWS.ECS;
using Amazon.CDK.AWS.ECS.Patterns;
using Amazon.CDK.AWS.ElasticLoadBalancingV2;
using Amazon.CDK.AWS.IAM;
using Constructs;

namespace AlbEcsBedrockAgentsCdkDotnet.ECS
{
    public class AlbEcsStack : NestedStack
    {
        internal AlbEcsStack(Construct scope, string id, INestedStackProps props = null) 
            : base(scope, id, props)
        {
            // VPC
            var vpc = new Vpc(this, " ChatBotVpc", new VpcProps
            {
                MaxAzs = 2
            });

            // ECS Cluster
            var cluster = new Cluster(this, "ChatBotCluster", new ClusterProps
            {
                Vpc = vpc
            });

            // ALB
            var alb = new ApplicationLoadBalancer(
                this, 
                "ChatBotALB", 
                new Amazon.CDK.AWS.ElasticLoadBalancingV2.ApplicationLoadBalancerProps
                {
                    Vpc = vpc,
                    InternetFacing = true
                });
            
            // ECS Task Definition
            var taskDefinition = new FargateTaskDefinition(this, "ChatBotTask", new FargateTaskDefinitionProps
            {
                MemoryLimitMiB = 512,
                Cpu = 256
            });

            // Add container to the task
            taskDefinition.AddContainer("ChatBotContainer", new ContainerDefinitionOptions
            {
                Image = ContainerImage.FromAsset("./src/ChatBotService"),
                PortMappings = new[] { new PortMapping { ContainerPort = 80 } }
            });

            // Grant permissions to the task to access Bedrock
            taskDefinition.TaskRole.AddManagedPolicy(ManagedPolicy.FromAwsManagedPolicyName("AmazonBedrockFullAccess"));

            // ECS Service
            var ecsService = new ApplicationLoadBalancedFargateService(
                this, 
                "GlobalTrekAdventuresCHatBotService", 
                new ApplicationLoadBalancedFargateServiceProps
                {
                    Cluster = cluster,
                    TaskDefinition = taskDefinition,
                    PublicLoadBalancer = true,
                    DesiredCount = 2,
                    ListenerPort = 80
                });
        }
    }
}

using System.Collections.Generic;
using System.Runtime.InteropServices;
using AlbEcsBedrockAgentsCdkDotnet.Common;
using Amazon.CDK;
using Amazon.CDK.AWS.ApplicationAutoScaling;
using Amazon.CDK.AWS.EC2;
using Amazon.CDK.AWS.Ecr.Assets;
using Amazon.CDK.AWS.ECS;
using Amazon.CDK.AWS.ElasticLoadBalancingV2;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Logs;
using Amazon.JSII.Runtime.Deputy;
using Constructs;
using HealthCheck = Amazon.CDK.AWS.ElasticLoadBalancingV2.HealthCheck;

namespace AlbEcsBedrockAgentsCdkDotnet.ECS
{
    public class AlbEcsStack : NestedStack
    {
        private static readonly string CloudWatchLogGroupName = "/aws/ecs/chatbot-ecs-cluster-logs";

        /// <summary>
        /// Initializes a new instance of <see cref="AlbEcsStack"/>
        /// </summary>
        /// <param name="scope"><see cref="Construct"/></param>
        /// <param name="id">Stack Name</param>
        /// <param name="props">Stack properties</param>
        internal AlbEcsStack(Construct scope, string id, INestedStackProps props = null)
            : base(scope, id, props)
        {
            // AgentId Parameter
            AgentId = new CfnParameter(this, "AgentId", new CfnParameterProps
            {
                Type = "String",
                Description = "Bedrock Agent ID"
            });

            // AgentAliasId Parameter
            AgentAliasId = new CfnParameter(this, "AgentAliasId", new CfnParameterProps
            {
                Type = "String",
                Description = "Bedrock Agent Alias ID"
            });

            // Create VPC
            Vpc = CreateVpc();

            // Create VPC Flow logs
            VpcFlowLog = CreateVpcFlowlogs(Vpc);

            // Create security group for ALB
            AlbSecurityGroup = CreateSecurityGroupForALB(Vpc);

            // Create security group for ECS
            EcsSecurityGroup = CreateSecurityGroupForECS(Vpc, AlbSecurityGroup);

            // Create application load balancer
            ApplicationLoadBalancer = CreateApplicationLoadBalancer(Vpc, AlbSecurityGroup);

            // Create target groups for ALB
            AlbListener = CreateAlbListener(ApplicationLoadBalancer);

            // Create ECS Cluster
            EcsCluster = CreateEcsCluster(Vpc);

            // Create execution role for ECS
            EcsExecutionRole = CreateEcsExecutionRole();

            // Create task role for ECS
            EcsTaskRole = CreateTaskRole(AgentId.ValueAsString, AgentAliasId.ValueAsString);

            // ECS Task Definition
            TaskDefinition = CreateTaskDefinition(EcsExecutionRole, EcsTaskRole);

            // Add container to the task
            ContainerDefinitions = CreateTaskContainers(TaskDefinition, AgentId.ValueAsString, AgentAliasId.ValueAsString);

            // Create ECS Service
            EcsService = CreateFargateService(EcsCluster, EcsSecurityGroup, TaskDefinition, AlbListener);

            // Add dependency to remove Capacity Provider Association before Cluster
            Aspects.Of(this).Add(new CapacityProviderDependencyAspect());
        }

        /// <summary>
        /// Gets/Sets the AgentId parameter
        /// </summary>
        /// <value><see cref="CfnParameter"/></value>
        internal CfnParameter AgentId { get; set; }

        /// <summary>
        /// Gets/Sets the AgentAliasId parameter
        /// </summary>
        /// <value><see cref="CfnParameter"/></value>
        internal CfnParameter AgentAliasId { get; set; }

        /// <summary>
        /// Gets the VPC
        /// </summary>
        /// <value><see cref="Vpc"/></value>
        internal Vpc Vpc { get; }

        /// <summary>
        /// Gets the VPC Flow logs
        /// </summary>
        /// <value><see cref="FlowLog"/></value>
        internal FlowLog VpcFlowLog { get; }

        /// <summary>
        /// Gets the security group for ALB
        /// </summary>
        /// <value><see cref="SecurityGroup"/></value>
        internal SecurityGroup AlbSecurityGroup { get; }

        /// <summary>
        /// Gets the security group for ECS Cluster/Service
        /// </summary>
        /// <value><see cref="SecurityGroup"/></value>
        internal SecurityGroup EcsSecurityGroup { get; }

        /// <summary>
        /// Gets the Application Load Balancer
        /// </summary>
        /// <value><see cref="ApplicationLoadBalancer"/></value>
        internal ApplicationLoadBalancer ApplicationLoadBalancer { get; }

        /// <summary>
        /// Gets the ALB Listener
        /// </summary>
        /// <value><see cref="ApplicationListener"/></value>
        internal ApplicationListener AlbListener { get; }

        /// <summary>
        /// Gets the execution role for ECS
        /// </summary>
        /// <value><see cref="Role"/></value>
        internal Role EcsExecutionRole { get; }

        /// <summary>
        /// Gets the task role for ECS
        /// </summary>
        /// <value><see cref="Role"/></value>
        internal Role EcsTaskRole { get; }

        /// <summary>
        /// Gets the ECS cluster
        /// </summary>
        /// <value><see cref="Cluster"/></value>
        internal Cluster EcsCluster { get; }

        /// <summary>
        /// Gets the Fargate Task Definition
        /// </summary>
        /// <value></value>
        internal FargateTaskDefinition TaskDefinition { get; }

        /// <summary>
        /// Gets the Container Definitions
        /// </summary>
        /// <value></value>
        internal ContainerDefinition[] ContainerDefinitions { get; }

        /// <summary>
        /// Gets the Fargate-based ECS Service
        /// </summary>
        /// <value></value>
        internal FargateService EcsService { get; }

        /// <summary>
        /// Create a VPC with public and private subnets
        /// </summary>
        /// <returns><see cref="Vpc"/></returns>
        private Vpc CreateVpc()
        {
            // VPC
            return new Vpc(
                this,
                "ChatBotVpc",
                new VpcProps
                {
                    MaxAzs = 2,
                    SubnetConfiguration =
                    [
                        new SubnetConfiguration
                        {
                            Name = "Public",
                            SubnetType = SubnetType.PUBLIC,
                        },
                        new SubnetConfiguration
                        {
                            Name = "Private",
                            SubnetType = SubnetType.PRIVATE_WITH_EGRESS
                        }
                    ],
                    VpcName = $"{Constants.ResourceNamePrefix}-vpc-{Utils.GenerateRandomStringFromStackId(StackId)}",
                });
        }

        /// <summary>
        /// Creates a VPC Flowlogs for VPC
        /// </summary>
        /// <param name="vpc"></param>
        /// <returns><see cref="Flowlog"/></returns>
        private FlowLog CreateVpcFlowlogs(Vpc vpc)
        {
            return new FlowLog(
                this,
                "ChatBotVpcFlowLog",
                new FlowLogProps
                {
                    FlowLogName = $"{Constants.ResourceNamePrefix}-vpc-flowlog-{Utils.GenerateRandomStringFromStackId(StackId)}",
                    ResourceType = FlowLogResourceType.FromVpc(vpc),
                    Destination = FlowLogDestination.ToCloudWatchLogs(
                        new LogGroup(
                            this,
                            "ChatBotVpcFlowLogGroup",
                            new LogGroupProps
                            {
                                LogGroupName = $"ChatBotVpcFlowLogGroup-{Utils.GenerateRandomStringFromStackId(StackId)}",
                                Retention = RetentionDays.ONE_MONTH,
                                RemovalPolicy = RemovalPolicy.DESTROY
                            })),
                    TrafficType = FlowLogTrafficType.ALL
                });
        }

        /// <summary>
        /// Create a security group for the ALB
        /// </summary>
        /// <param name="vpc"><see cref="Vpc"/></param>
        /// <returns><see cref="SecurityGroup"/></returns>
        private SecurityGroup CreateSecurityGroupForALB(Vpc vpc)
        {
            var securityGroup = new SecurityGroup(
                this,
                "ChatBotAlbSecurityGroup",
                new SecurityGroupProps
                {
                    Vpc = vpc,
                    SecurityGroupName = $"{Constants.ResourceNamePrefix}-alb-sg-{Utils.GenerateRandomStringFromStackId(StackId)}",
                    AllowAllOutbound = true,
                    AllowAllIpv6Outbound = null,
                    Description = "Security group for ChatBot ALB"
                });

            // Adding Inbound rule for ALB
            securityGroup.AddIngressRule(Peer.AnyIpv4(), Port.Tcp(80), "Allows HTTP access from Internet to ALB");

            Amazon.CDK.Tags.Of(securityGroup).Add("Name", "chatbot-alb-security-group");
            return securityGroup;
        }

        /// <summary>
        /// Create a security group for the ECS Cluster/Service
        /// </summary>
        /// <param name="vpc"><see cref="Vpc"/></param>
        /// <returns><see cref="SecurityGroup"/></returns>
        private SecurityGroup CreateSecurityGroupForECS(Vpc vpc, SecurityGroup albSecurityGroup)
        {
            var securityGroup = new SecurityGroup(
                this,
                "ChatBotEcsSecurityGroup",
                new SecurityGroupProps
                {
                    Vpc = vpc,
                    SecurityGroupName = $"{Constants.ResourceNamePrefix}-ecs-sg-{Utils.GenerateRandomStringFromStackId(StackId)}",
                    Description = "Security group for ChatBot ECS Cluster/Service",
                });

            // Adding Inbound rule from ALB
            securityGroup.AddIngressRule(Peer.SecurityGroupId(
                albSecurityGroup.SecurityGroupId), Port.Tcp(8080), "Allows HTTP access from ALB to ECS");

            Amazon.CDK.Tags.Of(securityGroup).Add("Name", "chatbot-alb-security-group");
            return securityGroup;
        }

        /// <summary>
        /// Creates an Application Load Balancer
        /// </summary>
        /// <param name="albSecurityGroup">ALB <see cref="SecurityGroup"/></param>
        /// <returns><see cref="ApplicationLoadBalancer"/></returns>
        private ApplicationLoadBalancer CreateApplicationLoadBalancer(Vpc vpc, SecurityGroup albSecurityGroup)
        {
            return new ApplicationLoadBalancer(
                this,
                "ChatBotAlb",
                new ApplicationLoadBalancerProps
                {
                    Vpc = vpc,
                    InternetFacing = true,
                    LoadBalancerName = $"chatbot-alb-{Utils.GenerateRandomStringFromStackId(StackId)}",
                    SecurityGroup = albSecurityGroup,
                    VpcSubnets = new SubnetSelection
                    {
                        SubnetType = SubnetType.PUBLIC,
                        OnePerAz = true,
                    },
                    IpAddressType = IpAddressType.IPV4,
                    CrossZoneEnabled = true,
                    DropInvalidHeaderFields = true
                });
        }

        /// <summary>
        /// Creates the listener for the ALB
        /// </summary>
        /// <param name="applicationLoadBalancer"><see cref="ApplicationLoadBalancer"/></param>
        /// <returns><see cref="ApplicationListener"/></returns>
        private static ApplicationListener CreateAlbListener(ApplicationLoadBalancer applicationLoadBalancer)
        {
            return applicationLoadBalancer.AddListener(
                $"{Constants.ResourceNamePrefix}-alb-listener",
                new BaseApplicationListenerProps
                {
                    Certificates = null,
                    DefaultAction = null,
                    DefaultTargetGroups = null,
                    MutualAuthentication = null,
                    Open = true,
                    Port = 80,
                    Protocol = ApplicationProtocol.HTTP,
                    SslPolicy = null
                }
            );
        }

        /// <summary>
        /// Creates an ECS cluster
        /// </summary>
        /// <param name="vpc"><see cref="Vpc"/></param>
        /// <returns><see cref="Cluster"/></returns>
        private Cluster CreateEcsCluster(Vpc vpc)
        {
            var ecsCluster = new Cluster(
                this,
                "ChatBotCluster",
                new ClusterProps
                {
                    ClusterName = $"{Constants.ResourceNamePrefix}-ecs-cluster-{Utils.GenerateRandomStringFromStackId(StackId)}",
                    Vpc = vpc,
                    EnableFargateCapacityProviders = true,
                    ContainerInsights = false,
                    ExecuteCommandConfiguration = null
                });

            Amazon.CDK.Tags.Of(ecsCluster).Add("Name", "ecs-chatbot-cluster");
            return ecsCluster;
        }

        /// <summary>
        /// Create an execution role for ECS
        /// </summary>
        /// <returns><see cref="Role"/></returns>
        private Role CreateEcsExecutionRole()
        {
            var ecsExecutionRole =
                new Role(
                    this,
                    "ChatBotEcsExecutionRole",
                    new RoleProps
                    {
                        AssumedBy = new ServicePrincipal("ecs-tasks.amazonaws.com"),
                        RoleName = $"ChatBotEcsExecutionRole_{Utils.GenerateRandomStringFromStackId(StackId)}",
                        ManagedPolicies =
                        [
                            ManagedPolicy.FromManagedPolicyArn(
                                this,
                                "AmazonECSTaskExecutionRolePolicy",
                                "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy")
                        ],
                        InlinePolicies = new Dictionary<string, PolicyDocument>
                        {
                            [$"EcsExecutionPolicyForCloudWatchCreateLogGroup_{Utils.GenerateRandomStringFromStackId(StackId)}"] =
                                new PolicyDocument(
                                    new PolicyDocumentProps
                                    {
                                        Statements =
                                        [
                                            new PolicyStatement(
                                                new PolicyStatementProps
                                                {
                                                    Sid = "CloudWatchCreateLogGroup",
                                                    Effect = Effect.ALLOW,
                                                    Actions = ["logs:CreateLogGroup"],
                                                    Resources = ["*"]
                                                })
                                        ]
                                    })
                        }
                    });

            return ecsExecutionRole;
        }

        /// <summary>
        /// Create a task role for ECS
        /// </summary>
        /// <returns><see cref="Role"/></returns>
        private Role CreateTaskRole(string agentId, string agentAliasId)
        {
            return new Role(
                this,
                "ChatBotEcsTaskRole",
                new RoleProps
                {
                    Description = "Task role for ChatBot ECS Task",
                    RoleName = $"ChatBotEcsTaskRoleFor_{Utils.GenerateRandomStringFromStackId(StackId)}",
                    Path = "/service-role/",
                    MaxSessionDuration = Duration.Minutes(60),
                    AssumedBy = new ServicePrincipal("ecs-tasks.amazonaws.com"),
                    InlinePolicies = new Dictionary<string, PolicyDocument>
                    {
                        [$"EcsTaskPolicyForBedrockAgents_{Utils.GenerateRandomStringFromStackId(StackId)}"] =
                            new PolicyDocument(new PolicyDocumentProps
                            {
                                Statements =
                                [
                                    new PolicyStatement(
                                        new PolicyStatementProps
                                        {
                                            Sid = "EcsTaskBedrockAgentInvoke",
                                            Effect = Effect.ALLOW,
                                            Actions = ["bedrock:InvokeAgent"],
                                            Resources = [$"arn:aws:bedrock:{Region}:{Account}:agent-alias/{agentId}/{agentAliasId}"]
                                        })
                                ]
                            }),
                        [$"EcsTaskPolicyForCloudWatchDescribeLogGroups_{Utils.GenerateRandomStringFromStackId(StackId)}"] =
                            new PolicyDocument(new PolicyDocumentProps
                            {
                                Statements =
                                [
                                    new PolicyStatement(
                                        new PolicyStatementProps
                                        {
                                            Sid = "CloudWatchDescribeLogGroups",
                                            Effect = Effect.ALLOW,
                                            Actions = ["logs:DescribeLogGroups"],
                                            Resources = ["*"]
                                        })
                                ]
                            }),
                        [$"EcsTaskPolicyForCloudWatch_{Utils.GenerateRandomStringFromStackId(StackId)}"] =
                            new PolicyDocument(new PolicyDocumentProps
                            {
                                Statements =
                                [
                                    new PolicyStatement(
                                        new PolicyStatementProps
                                        {
                                            Sid = "CloudWatchLogs",
                                            Effect = Effect.ALLOW,
                                            Actions =
                                            [
                                                "logs:CreateLogStream",
                                                "logs:PutLogEvents",
                                                "logs:DescribeLogStreams"
                                            ],
                                            Resources = [$"arn:aws:logs:{Region}:{Account}:log-group:{CloudWatchLogGroupName}-{Utils.GenerateRandomStringFromStackId(StackId)}:*"]
                                        })
                                ]
                            })
                    }
                });
        }

        /// <summary>
        /// Creates 
        /// </summary>
        /// <param name="ecsExecutionRole"></param>
        /// <param name="ecsTaskRole"></param>
        /// <returns></returns>
        private FargateTaskDefinition CreateTaskDefinition(Role ecsExecutionRole, Role ecsTaskRole)
        {
            // ECS Task Definition
            return new FargateTaskDefinition(
                this,
                "ChatBotTaskDefinition",
                new FargateTaskDefinitionProps
                {
                    Cpu = 512,
                    MemoryLimitMiB = 1024,
                    ExecutionRole = ecsExecutionRole,
                    TaskRole = ecsTaskRole,
                    Family = $"{Constants.ResourceNamePrefix}-ecs-task-definition-{Utils.GenerateRandomStringFromStackId(StackId)}",
                    RuntimePlatform = new RuntimePlatform()
                    {
                        OperatingSystemFamily = OperatingSystemFamily.LINUX,
                        CpuArchitecture = RuntimeInformation.ProcessArchitecture == Architecture.X64
                        ? CpuArchitecture.X86_64
                        : CpuArchitecture.ARM64,
                    },
                    PidMode = PidMode.TASK,
                    EphemeralStorageGiB = 21,
                    Volumes = []
                });
        }

        /// <summary>
        /// Create container definitions for <paramref name="taskDefinition"/>
        /// </summary>
        /// <param name="taskDefinition">Fargate task definition</param>
        /// <returns>Array of <see cref="ContainerDefinition"/></returns>
        private ContainerDefinition[] CreateTaskContainers(
            FargateTaskDefinition taskDefinition,
            string agentId,
            string agentAliasId)
        {
            var containerDefinitions = new List<ContainerDefinition>
            {
                // Bedrock Agent's API Proxy Container
                taskDefinition.AddContainer(
                "EcsChatBotContainer",
                new ContainerDefinitionProps
                {
                    ContainerName = "ChatBotContainer",
                    Hostname = null,
                    Cpu = 512,
                    MemoryLimitMiB = 1024,
                    Image = ContainerImage.FromAsset(
                        "./src/ECSTasks/BedrockAgentsApiProxy",
                        new AssetImageProps
                        {
                            File = "Dockerfile",
                            BuildArgs = new Dictionary<string, string>
                            {
                                ["ASPNETCORE_ENVIRONMENT"] = "Production"
                            },
                            AssetName = "chatbot-bedrock-agents-api-proxy-docker-image",
                            NetworkMode = Amazon.CDK.AWS.Ecr.Assets.NetworkMode.DEFAULT,
                            Platform = RuntimeInformation.ProcessArchitecture == Architecture.X64
                                ? Platform_.LINUX_AMD64
                                : Platform_.LINUX_ARM64
                        }),
                    Logging = LogDriver.AwsLogs(
                        new AwsLogDriverProps
                        {
                            LogGroup = new LogGroup(
                                this,
                                "ChatBotLogGroup",
                                new LogGroupProps
                                {
                                    LogGroupName = $"{CloudWatchLogGroupName}-{Utils.GenerateRandomStringFromStackId(StackId)}",
                                    RemovalPolicy = RemovalPolicy.DESTROY,
                                    Retention = RetentionDays.TWO_WEEKS
                                }),
                            StreamPrefix = $"ecs-logs-{Utils.GenerateRandomStringFromStackId(StackId)}",
                            Mode = AwsLogDriverMode.NON_BLOCKING,
                            MaxBufferSize = Size.Bytes(1 * 1024 * 1024 * 1024)
                        }),
                    Essential = true,
                    DisableNetworking = false,
                    Environment = new Dictionary<string, string>
                    {
                        ["AGENT_ID"] = agentId,
                        ["AGENT_ALIAS_ID"] = agentAliasId,
                    },
                    HealthCheck = new Amazon.CDK.AWS.ECS.HealthCheck
                    {
                        Command = ["CMD-SHELL", "curl -f http://localhost:8080/health || exit 1"],
                        Interval = Duration.Seconds(30),
                        Retries = 3,
                        Timeout = Duration.Seconds(5),
                    },
                    Interactive = false,
                    LinuxParameters = new LinuxParameters(
                        this,
                        "LinuxParameters",
                        new LinuxParametersProps
                        {
                            InitProcessEnabled = true
                        }),
                    PortMappings =
                    [
                        new PortMapping
                        {
                            ContainerPort = 8080,
                            AppProtocol = AppProtocol.Http,
                            Name = "http",
                            Protocol = Amazon.CDK.AWS.ECS.Protocol.TCP
                        }
                    ],
                    Privileged = false,
                    PseudoTerminal = false,
                    ReadonlyRootFilesystem = false,
                    StartTimeout = Duration.Seconds(60),
                    StopTimeout = Duration.Seconds(30),
                    TaskDefinition = taskDefinition,
                    User = "appuser"
                })
            };

            return [.. containerDefinitions];
        }


        /// <summary>
        /// Creates a new Fargate based ECS Service
        /// </summary>
        /// <returns><see cref="FargateService"/></returns>
        private FargateService CreateFargateService(
            Cluster ecsCluster,
            SecurityGroup ecsSecurityGroup,
            FargateTaskDefinition taskDefinition,
            ApplicationListener albListener)
        {
            var fargateService = new FargateService(
                this,
                "ChatBotFargateService",
                new FargateServiceProps
                {
                    AssignPublicIp = false,
                    CapacityProviderStrategies =
                    [
                        new CapacityProviderStrategy
                        {
                            CapacityProvider = "FARGATE",
                            Base = 0,
                            Weight = 100
                        },
                        new CapacityProviderStrategy
                        {
                            CapacityProvider = "FARGATE_SPOT",
                            Base = null,
                            Weight = null
                        }
                    ],
                    CircuitBreaker = new DeploymentCircuitBreaker
                    {
                        Rollback = true,
                        Enable = true,
                    },
                    CloudMapOptions = null,
                    Cluster = ecsCluster,
                    DeploymentAlarms = null,
                    DeploymentController = new DeploymentController
                    {
                        Type = DeploymentControllerType.ECS
                    },
                    DesiredCount = 2,
                    EnableECSManagedTags = true,
                    EnableExecuteCommand = true,
                    HealthCheckGracePeriod = Duration.Seconds(60),
                    MaxHealthyPercent = 200,
                    MinHealthyPercent = 100,
                    PlatformVersion = FargatePlatformVersion.LATEST,
                    PropagateTags = null,
                    SecurityGroups = [ecsSecurityGroup],
                    ServiceConnectConfiguration = null,
                    ServiceName = $"chatbot-fargate-service-{Utils.GenerateRandomStringFromStackId(StackId)}",
                    TaskDefinition = taskDefinition,
                    TaskDefinitionRevision = TaskDefinitionRevision.LATEST,
                    VolumeConfigurations = null,
                    VpcSubnets = new SubnetSelection { OnePerAz = true, SubnetType = SubnetType.PRIVATE_WITH_EGRESS }
                }
            );

            // Removal policy
            fargateService.ApplyRemovalPolicy(RemovalPolicy.DESTROY);

            // Register ALB Listener
            fargateService.RegisterLoadBalancerTargets(
                new EcsTarget
                {
                    ContainerName = "ChatBotContainer",
                    ContainerPort = 8080,
                    Listener = ListenerConfig.ApplicationListener(
                        albListener,
                        new AddApplicationTargetsProps
                        {
                            Conditions = null,
                            DeregistrationDelay = null,
                            EnableAnomalyMitigation = null,
                            HealthCheck = new HealthCheck
                            {
                                Enabled = true,
                                HealthyHttpCodes = "200",
                                HealthyThresholdCount = 5,
                                Interval = Duration.Seconds(10),
                                Path = "/health",
                                Port = "8080",
                                Protocol = Amazon.CDK.AWS.ElasticLoadBalancingV2.Protocol.HTTP,
                                Timeout = Duration.Seconds(6),
                                UnhealthyThresholdCount = 2
                            },
                            LoadBalancingAlgorithmType = TargetGroupLoadBalancingAlgorithmType.ROUND_ROBIN,
                            Port = 80,
                            Priority = null,
                            Protocol = ApplicationProtocol.HTTP,
                            ProtocolVersion = ApplicationProtocolVersion.HTTP1,
                            SlowStart = Duration.Seconds(60),
                            StickinessCookieDuration = null,
                            StickinessCookieName = null,
                            TargetGroupName = $"fargate-tg-{Utils.GenerateRandomStringFromStackId(StackId)}",
                            Targets = null,
                        }
                    ),
                    NewTargetGroupId = $"{Constants.ResourceNamePrefix}-fargate-tg",
                    Protocol = Amazon.CDK.AWS.ECS.Protocol.TCP
                }
            );

            // Auto-scaling
            var scalableTaskCount = fargateService.AutoScaleTaskCount(
                new EnableScalingProps
                {
                    MaxCapacity = 2,
                    MinCapacity = 1,
                });

            scalableTaskCount.ScaleOnCpuUtilization(
                "scaleOnCpu",
                new CpuUtilizationScalingProps
                {
                    DisableScaleIn = false,
                    PolicyName = "scaleOnCpu",
                    ScaleInCooldown = Duration.Seconds(60),
                    ScaleOutCooldown = Duration.Seconds(60),
                    TargetUtilizationPercent = 70
                });

            // Return
            return fargateService;
        }
    }

    /// <summary>
    /// Class to add dependencies between constructs to remove Capacity Provider Association before Cluster
    /// </summary>
    internal class CapacityProviderDependencyAspect : DeputyBase, IAspect
    {
        public void Visit(IConstruct node)
        {
            if (node is FargateService fargateServiceNode)
            {
                var children = fargateServiceNode.Cluster.Node.FindAll();
                foreach (var child in children)
                {
                    if (child is CfnClusterCapacityProviderAssociations cfnClusterCapacityProviderAssociations)
                    {
                        cfnClusterCapacityProviderAssociations.Node.AddDependency(fargateServiceNode.Cluster);
                        fargateServiceNode.Node.AddDependency(cfnClusterCapacityProviderAssociations);
                    }
                }
            }
        }
    }
}

using Amazon.CDK;
using Amazon.CDK.AWS.CertificateManager;
using Amazon.CDK.AWS.EC2;
using Amazon.CDK.AWS.Ecr.Assets;
using Amazon.CDK.AWS.ECS;
using Amazon.CDK.AWS.ECS.Patterns;
using Amazon.CDK.AWS.Route53;
using Amazon.CDK.AWS.Route53.Targets;
using Constructs;
using Microsoft.Extensions.Options;
using System.Collections.Generic;

namespace Route53AlbFargateCdkDotnet
{
    public class Route53AlbFargateCdkDotnetStack : Stack
    {
        internal Route53AlbFargateCdkDotnetStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // Replace the value with your domain name
            string apiDomainName = "api.YOUR-DOMAIN.com";

            // 1. Hosted zone
            var hostedZone = new HostedZone(this, "hosted-zone", new HostedZoneProps
            {
                ZoneName = apiDomainName
            });
            hostedZone.ApplyRemovalPolicy(RemovalPolicy.RETAIN);


            // 2. SSL certificate via ACM
            var certificate = new Certificate(this, "certificate", new CertificateProps
            {
                DomainName = apiDomainName,
                Validation = CertificateValidation.FromDns(hostedZone),
            });


            // 3. VPC with public and private subnets
            var vpc = new Vpc(this, "vpc", new VpcProps
            {
                Cidr = "10.0.0.0/16",
                MaxAzs = 3,
                SubnetConfiguration = new[]
                {
                    new SubnetConfiguration
                    {
                        Name="private",
                        SubnetType= SubnetType.PRIVATE_ISOLATED,
                        CidrMask= 24
                    },
                    new SubnetConfiguration
                    {
                        Name="public",
                        SubnetType= SubnetType.PUBLIC,
                        CidrMask= 24
                    }
                }
            });

            // Create required VPC endpoints to privately retrieve docker images from the ECR repository
            // Reference link - https://docs.aws.amazon.com/AmazonECR/latest/userguide/vpc-endpoints.html

            // 4.1. VPC endpoint 1
            var ecrDockerVpcEndpoint = new InterfaceVpcEndpoint(this, "ecr-dkr-vpc-endpoint", new InterfaceVpcEndpointProps
            {
                Vpc = vpc,
                Service = InterfaceVpcEndpointAwsService.ECR_DOCKER,
                PrivateDnsEnabled = true
            });

            // 4.2. VPC endpoint 2
            var ecrVpcEndpoint = new InterfaceVpcEndpoint(this, "ecr-vpc-endpoint", new InterfaceVpcEndpointProps
            {
                Vpc = vpc,
                Service = InterfaceVpcEndpointAwsService.ECR,
                PrivateDnsEnabled = true
            });

            // 4.3. VPC endpoint 3
            var cwVpcEndpoint = new InterfaceVpcEndpoint(this, "cloudwatch-vpc-endpoint", new InterfaceVpcEndpointProps
            {
                Vpc = vpc,
                Service = InterfaceVpcEndpointAwsService.CLOUDWATCH,
                PrivateDnsEnabled = true
            });

            // 4.4. VPC endpoint 4
            var cwLogsVpcEndpoint = new InterfaceVpcEndpoint(this, "cloudwatch-logs-vpc-endpoint", new InterfaceVpcEndpointProps
            {
                Vpc = vpc,
                Service = InterfaceVpcEndpointAwsService.CLOUDWATCH_LOGS,
                PrivateDnsEnabled = true
            });

            // 4.5. VPC endpoint 5
            var s3VpcEndpoint = new GatewayVpcEndpoint(this, "s3-vpc-endpoint", new GatewayVpcEndpointProps
            {
                Vpc = vpc,
                Service = GatewayVpcEndpointAwsService.S3
            });


            // 5. ECS cluster
            var ecsCluster = new Cluster(this, "ecs-cluster", new ClusterProps
            {
                Vpc = vpc
            });


            // 6. ECS fargate service frontend by ALB
            var albFargateService = new ApplicationLoadBalancedFargateService(this, "sample-api-service", new ApplicationLoadBalancedFargateServiceProps
            {
                // ----: Networking (Task Subnets) :-----
                // By default, public subnets are used if assignPublicIp is set, otherwise the first available one of Private, Isolated, Public, in that order.

                Cluster = ecsCluster,
                DesiredCount = 1,
                Cpu = 1024,  // 1024 unit represents 1 vCPU (per task)
                MemoryLimitMiB = 2048,
                TaskImageOptions = new ApplicationLoadBalancedTaskImageOptions
                {
                    ContainerPort = 80, // container port, automatically assigned to host port via dynamic port mapping
                    Image = ContainerImage.FromAsset("./src/SampleApplication.API")
                },
                Certificate = certificate,
                DomainName = apiDomainName,
                DomainZone = hostedZone,
                AssignPublicIp = false
            });

            albFargateService.TargetGroup.ConfigureHealthCheck(new Amazon.CDK.AWS.ElasticLoadBalancingV2.HealthCheck
            {
                Path = "/WeatherForecast"
            });
        }
    }
}


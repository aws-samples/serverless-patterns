using Amazon.CDK;
using Amazon.CDK.AWS.AppRunner.Alpha;
using Amazon.CDK.AWS.Ecr.Assets;
using Amazon.CDK.AWS.IAM;
using Constructs;

namespace ApprunnerCdkDotnet
{
    public class ApprunnerCdkDotnetStack : Stack
    {
        public ApprunnerCdkDotnetStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // Define Docker image asset for the AppRunner service
            var appRunnerContainerImage = new DockerImageAsset(this, "ApplicationImageAsset", new DockerImageAssetProps
            {
                Directory = "./src/DemoApplication.API"
            });

            // Create a role for the AppRunner service
            var appRunnerServiceRole = new Role(this, "AppRunnerServiceRole", new RoleProps()
            {
                AssumedBy = new ServicePrincipal("build.apprunner.amazonaws.com")
            });

            // Create a role for AppRunner instances
            var appRunnerInstanceRole = new Role(this, "AppRunnerInstanceRole", new RoleProps()
            {
                AssumedBy = new ServicePrincipal("tasks.apprunner.amazonaws.com")
            });

            // Define the AppRunner service
            var appRunnerService = new Service(this, "AppRunnerService", new ServiceProps
            {
                ServiceName = "dotnet-webapi-apprunner-service",
                Source = Source.FromAsset(new AssetProps
                {
                    ImageConfiguration = new ImageConfiguration { Port = 80 },
                    Asset = appRunnerContainerImage
                }),
                
                Cpu = Cpu.ONE_VCPU,
                Memory = Memory.TWO_GB,
                AccessRole = appRunnerServiceRole,
                InstanceRole = appRunnerInstanceRole,
                AutoDeploymentsEnabled = true
            });

            // Output the AppRunner service URL
            new CfnOutput(this, "AppRunnerServiceURL", new CfnOutputProps
            {
                Value = $"https://{appRunnerService.ServiceUrl}"
            });
        }
    }
}
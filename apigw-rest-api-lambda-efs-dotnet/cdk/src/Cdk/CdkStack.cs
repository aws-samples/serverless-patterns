using Amazon.CDK;
using Amazon.CDK.AWS.APIGateway;
using Amazon.CDK.AWS.EC2;
using Amazon.CDK.AWS.EFS;
using Amazon.CDK.AWS.Lambda;
using Constructs;

namespace Cdk
{
    public class CdkStack : Stack
    {
        private string vpcName = "VpcDemo";
        private string fileSystemName = "FileSystemDemo";
        private string path = "/export/lambda";
        private string mountPath = "/mnt/lambdaefs";
        private string accessPointName = "AccessPointDemo";
        private string functionName = "DemoFunction";
        private string endpointName = "EndpointDemo";
        private string handler = "dotnet.webapi::dotnet.webapi.LambdaEntryPoint::FunctionHandlerAsync";
        private string codePath = "code/src/dotnet.webapi";

        internal CdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            var buildOption = new BundlingOptions()
            {
                Image = Runtime.DOTNET_6.BundlingImage,
                User = "root",
                OutputType = BundlingOutput.ARCHIVED,
                Command = new string[]{
               "/bin/sh",
                "-c",
                " dotnet tool install -g Amazon.Lambda.Tools"+
                " && dotnet build"+
                " && dotnet lambda package --output-package /asset-output/function.zip"
                }
            };

            // Create a new VPC
            var vpc = new Vpc(this, vpcName, new VpcProps
            {
                MaxAzs = 2
            });

            // Create an Amazon EFS file system
            var fileSystem = new Amazon.CDK.AWS.EFS.FileSystem(this, fileSystemName, new FileSystemProps
            {
                Vpc = vpc,
                FileSystemName = fileSystemName,
                PerformanceMode = PerformanceMode.GENERAL_PURPOSE,
                Encrypted = true,
                LifecyclePolicy = LifecyclePolicy.AFTER_30_DAYS,
                RemovalPolicy = RemovalPolicy.DESTROY
            });

            // Add the accesspoint
            var accessPoint = fileSystem.AddAccessPoint(accessPointName, new AccessPointOptions
            {
                CreateAcl = new Acl
                {
                    OwnerGid = "1001",
                    OwnerUid = "1001",
                    Permissions = "750"
                },
                Path = path,
                PosixUser = new PosixUser
                {
                    Gid = "1001",
                    Uid = "1001"
                }
            });

            // Create a Lambda function to access Amazon EFS            
            var function = new Function(this, functionName, new FunctionProps
            {
                FunctionName = functionName,
                Runtime = Runtime.DOTNET_6,
                Code = Code.FromAsset(codePath, new Amazon.CDK.AWS.S3.Assets.AssetOptions()
                {
                    Bundling = buildOption
                }),
                Handler = handler,
                Timeout = Duration.Seconds(120),
                Vpc = vpc,
                Filesystem = Amazon.CDK.AWS.Lambda.FileSystem.FromEfsAccessPoint(accessPoint, mountPath),
            });

            // Defines an API Gateway REST API resource backed by our lambda function.
            new LambdaRestApi(this, endpointName, new LambdaRestApiProps
            {
                Handler = function
            });
        }
    }
}
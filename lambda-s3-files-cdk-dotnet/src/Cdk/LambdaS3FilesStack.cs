using Amazon.CDK;
using Amazon.CDK.AWS.EC2;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.S3;
using Constructs;
using S3Files = Amazon.CDK.AWS.S3Files;
using FileSystem = Amazon.CDK.AWS.Lambda.FileSystem;

namespace Cdk;

public class LambdaS3FilesStack : Stack
{
    internal LambdaS3FilesStack(Construct scope, string id, IStackProps? props = null)
        : base(scope, id, props)
    {
        var mountPath = "/mnt/s3data";

        // S3 bucket for the file system (versioning required by S3 Files)
        var bucket = new Bucket(this, "DataBucket", new BucketProps
        {
            RemovalPolicy = RemovalPolicy.DESTROY,
            AutoDeleteObjects = true,
            Versioned = true
        });

        // VPC for Lambda and S3 Files mount targets (no NAT — uses VPC endpoints instead)
        var vpc = new Vpc(this, "Vpc", new VpcProps
        {
            MaxAzs = 2,
            NatGateways = 0,
            SubnetConfiguration = new[]
            {
                new SubnetConfiguration
                {
                    Name = "Private",
                    SubnetType = SubnetType.PRIVATE_ISOLATED,
                    CidrMask = 24
                }
            }
        });

        // S3 Gateway endpoint for direct S3 API access from private subnets
        vpc.AddGatewayEndpoint("S3Endpoint", new GatewayVpcEndpointOptions
        {
            Service = GatewayVpcEndpointAwsService.S3
        });

        // Security group allowing NFS traffic (port 2049)
        var s3FilesSg = new SecurityGroup(this, "S3FilesSg", new SecurityGroupProps
        {
            Vpc = vpc,
            Description = "Allow NFS traffic for S3 Files mount targets"
        });
        s3FilesSg.AddIngressRule(s3FilesSg, Port.Tcp(2049), "NFS from Lambda");

        // IAM role for S3 Files to access the bucket (uses EFS service principal)
        var s3FilesRole = new Role(this, "S3FilesRole", new RoleProps
        {
            AssumedBy = new ServicePrincipal("elasticfilesystem.amazonaws.com")
        });
        bucket.GrantReadWrite(s3FilesRole);

        // S3 Files FileSystem
        var fileSystem = new S3Files.CfnFileSystem(this, "S3FileSystem", new S3Files.CfnFileSystemProps
        {
            Bucket = bucket.BucketArn,
            RoleArn = s3FilesRole.RoleArn
        });

        // Mount targets in each isolated subnet
        var isolatedSubnets = vpc.IsolatedSubnets;
        var mountTargets = new List<S3Files.CfnMountTarget>();
        for (var i = 0; i < isolatedSubnets.Length; i++)
        {
            var mt = new S3Files.CfnMountTarget(this, $"MountTarget{i}", new S3Files.CfnMountTargetProps
            {
                FileSystemId = fileSystem.AttrFileSystemId,
                SubnetId = isolatedSubnets[i].SubnetId,
                SecurityGroups = new[] { s3FilesSg.SecurityGroupId }
            });
            mt.AddDependency(fileSystem);
            mountTargets.Add(mt);
        }

        // Access point for Lambda (UID/GID 1000, root /lambda)
        var accessPoint = new S3Files.CfnAccessPoint(this, "S3FilesAccessPoint", new S3Files.CfnAccessPointProps
        {
            FileSystemId = fileSystem.AttrFileSystemId,
            PosixUser = new S3Files.CfnAccessPoint.PosixUserProperty
            {
                Uid = "1000",
                Gid = "1000"
            },
            RootDirectory = new S3Files.CfnAccessPoint.RootDirectoryProperty
            {
                Path = "/lambda",
                CreationPermissions = new S3Files.CfnAccessPoint.CreationPermissionsProperty
                {
                    OwnerUid = "1000",
                    OwnerGid = "1000",
                    Permissions = "755"
                }
            }
        });
        accessPoint.AddDependency(fileSystem);

        // Lambda function with S3 Files mount
        var fn = new Function(this, "S3FilesFn", new FunctionProps
        {
            Runtime = Runtime.DOTNET_10,
            Handler = "S3FilesLambda::S3FilesLambda.Function::FunctionHandler",
            Code = Code.FromAsset("src/S3FilesLambda/publish"),
            Timeout = Duration.Minutes(1),
            MemorySize = 512,
            Vpc = vpc,
            VpcSubnets = new SubnetSelection { SubnetType = SubnetType.PRIVATE_ISOLATED },
            SecurityGroups = new[] { s3FilesSg },
            Filesystem = FileSystem.FromS3FilesAccessPoint(accessPoint, mountPath),
            Environment = new Dictionary<string, string>
            {
                ["MOUNT_PATH"] = mountPath
            },
            Description = "Lambda function with S3 Files mount (.NET)"
        });

        // Ensure mount targets are ready before Lambda
        var cfnFn = (CfnFunction)fn.Node.DefaultChild!;
        foreach (var mt in mountTargets)
        {
            cfnFn.AddDependency(mt);
        }

        // Lambda permissions for S3 Files and direct S3 reads
        fn.AddToRolePolicy(new PolicyStatement(new PolicyStatementProps
        {
            Actions = new[] { "s3files:ClientMount", "s3files:ClientWrite" },
            Resources = new[] { accessPoint.AttrAccessPointArn }
        }));
        bucket.GrantRead(fn);

        // Outputs
        _ = new CfnOutput(this, "FunctionName", new CfnOutputProps
        {
            Value = fn.FunctionName
        });
        _ = new CfnOutput(this, "BucketName", new CfnOutputProps
        {
            Value = bucket.BucketName
        });
        _ = new CfnOutput(this, "FileSystemId", new CfnOutputProps
        {
            Value = fileSystem.AttrFileSystemId
        });
    }
}

import * as cdk from "aws-cdk-lib";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as s3 from "aws-cdk-lib/aws-s3";
import * as s3files from "aws-cdk-lib/aws-s3files";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as iam from "aws-cdk-lib/aws-iam";
import { Construct } from "constructs";

export class LambdaS3FilesStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const mountPath = "/mnt/s3data";

    // S3 bucket for the file system (versioning required by S3 Files)
    const bucket = new s3.Bucket(this, "DataBucket", {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
      versioned: true,
    });

    // VPC for Lambda and S3 Files mount targets
    const vpc = new ec2.Vpc(this, "Vpc", {
      maxAzs: 2,
      natGateways: 1,
    });

    // Security group allowing NFS traffic (port 2049)
    const s3FilesSg = new ec2.SecurityGroup(this, "S3FilesSg", {
      vpc,
      description: "Allow NFS traffic for S3 Files mount targets",
    });
    s3FilesSg.addIngressRule(s3FilesSg, ec2.Port.tcp(2049), "NFS from Lambda");

    // IAM role for S3 Files to access the bucket (uses EFS service principal)
    const s3FilesRole = new iam.Role(this, "S3FilesRole", {
      assumedBy: new iam.ServicePrincipal("elasticfilesystem.amazonaws.com"),
    });
    bucket.grantReadWrite(s3FilesRole);

    // S3 Files FileSystem
    const fileSystem = new s3files.CfnFileSystem(this, "S3FileSystem", {
      bucket: bucket.bucketArn,
      roleArn: s3FilesRole.roleArn,
    });

    // Mount targets in each private subnet
    const privateSubnets = vpc.privateSubnets;
    const mountTargets = privateSubnets.map((subnet, i) => {
      const mt = new s3files.CfnMountTarget(this, `MountTarget${i}`, {
        fileSystemId: fileSystem.attrFileSystemId,
        subnetId: subnet.subnetId,
        securityGroups: [s3FilesSg.securityGroupId],
      });
      mt.addDependency(fileSystem);
      return mt;
    });

    // Access point for Lambda (UID/GID 1000, root /lambda)
    const accessPoint = new s3files.CfnAccessPoint(this, "S3FilesAccessPoint", {
      fileSystemId: fileSystem.attrFileSystemId,
      posixUser: { uid: "1000", gid: "1000" },
      rootDirectory: {
        path: "/lambda",
        creationPermissions: {
          ownerUid: "1000",
          ownerGid: "1000",
          permissions: "755",
        },
      },
    });
    accessPoint.addDependency(fileSystem);

    // Lambda function with S3 Files mount
    const fn = new lambda.Function(this, "S3FilesFn", {
      runtime: lambda.Runtime.NODEJS_24_X,
      handler: "index.handler",
      code: lambda.Code.fromAsset("src"),
      timeout: cdk.Duration.minutes(1),
      memorySize: 512,
      vpc,
      vpcSubnets: { subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS },
      securityGroups: [s3FilesSg],
      filesystem: lambda.FileSystem.fromS3FilesAccessPoint(accessPoint, mountPath),
      environment: { MOUNT_PATH: mountPath },
      description: "Lambda function with S3 Files mount",
    });

    // Ensure mount targets are ready before Lambda
    const cfnFn = fn.node.defaultChild as lambda.CfnFunction;
    mountTargets.forEach((mt) => cfnFn.addDependency(mt));

    // Lambda permissions for S3 Files and direct S3 reads
    fn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["s3files:ClientMount", "s3files:ClientWrite"],
        resources: [accessPoint.attrAccessPointArn],
      })
    );
    bucket.grantRead(fn);

    new cdk.CfnOutput(this, "FunctionName", { value: fn.functionName });
    new cdk.CfnOutput(this, "BucketName", { value: bucket.bucketName });
    new cdk.CfnOutput(this, "FileSystemId", {
      value: fileSystem.attrFileSystemId,
    });
  }
}

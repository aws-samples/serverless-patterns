import * as cdk from "aws-cdk-lib";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as s3 from "aws-cdk-lib/aws-s3";
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

    // S3 Files FileSystem (L1 construct — no L2 yet)
    const fileSystem = new cdk.CfnResource(this, "S3FileSystem", {
      type: "AWS::S3Files::FileSystem",
      properties: {
        Bucket: bucket.bucketArn,
        RoleArn: s3FilesRole.roleArn,
        AcceptBucketWarning: true,
      },
    });

    // Mount targets in each private subnet
    const privateSubnets = vpc.privateSubnets;
    const mountTargets = privateSubnets.map((subnet, i) => {
      const mt = new cdk.CfnResource(this, `MountTarget${i}`, {
        type: "AWS::S3Files::MountTarget",
        properties: {
          FileSystemId: fileSystem.getAtt("FileSystemId"),
          SubnetId: subnet.subnetId,
          SecurityGroups: [s3FilesSg.securityGroupId],
        },
      });
      mt.addDependency(fileSystem);
      return mt;
    });

    // Access point for Lambda (UID/GID 1000, root /lambda)
    const accessPoint = new cdk.CfnResource(this, "S3FilesAccessPoint", {
      type: "AWS::S3Files::AccessPoint",
      properties: {
        FileSystemId: fileSystem.getAtt("FileSystemId"),
        PosixUser: { Uid: "1000", Gid: "1000" },
        RootDirectory: {
          Path: "/lambda",
          CreationPermissions: {
            OwnerUid: "1000",
            OwnerGid: "1000",
            Permissions: "755",
          },
        },
      },
    });
    accessPoint.addDependency(fileSystem);

    // Lambda function with S3 Files mount
    const fn = new lambda.Function(this, "S3FilesFn", {
      runtime: lambda.Runtime.NODEJS_22_X, // overridden to nodejs24.x below
      handler: "index.handler",
      code: lambda.Code.fromAsset("src"),
      timeout: cdk.Duration.minutes(1),
      memorySize: 512,
      vpc,
      vpcSubnets: { subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS },
      securityGroups: [s3FilesSg],
      environment: { MOUNT_PATH: mountPath },
      description: "Lambda function with S3 Files mount",
    });

    // Attach S3 Files filesystem config via escape hatch
    const cfnFn = fn.node.defaultChild as lambda.CfnFunction;
    cfnFn.addOverride("Properties.Runtime", "nodejs24.x");
    cfnFn.fileSystemConfigs = [
      {
        arn: accessPoint.getAtt("AccessPointArn").toString(),
        localMountPath: mountPath,
      },
    ];

    // Ensure mount targets are ready before Lambda
    mountTargets.forEach((mt) => cfnFn.addDependency(mt));
    cfnFn.addDependency(accessPoint);

    // Lambda permissions for S3 Files and direct S3 reads
    fn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["s3files:ClientMount", "s3files:ClientWrite"],
        resources: [accessPoint.getAtt("AccessPointArn").toString()],
      })
    );
    bucket.grantRead(fn);

    new cdk.CfnOutput(this, "FunctionName", { value: fn.functionName });
    new cdk.CfnOutput(this, "BucketName", { value: bucket.bucketName });
    new cdk.CfnOutput(this, "FileSystemId", {
      value: fileSystem.getAtt("FileSystemId").toString(),
    });
  }
}

import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as kinesis from "aws-cdk-lib/aws-kinesis";
import * as firehose from "aws-cdk-lib/aws-kinesisfirehose";
import * as kms from "aws-cdk-lib/aws-kms";
import * as s3 from "aws-cdk-lib/aws-s3";
import * as iam from "aws-cdk-lib/aws-iam";
import * as kinesisanalyticsv2 from "aws-cdk-lib/aws-kinesisanalyticsv2";
import * as s3Asset from "aws-cdk-lib/aws-s3-assets";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as logs from "aws-cdk-lib/aws-logs";
import * as path from "path";

export class CdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, "FlinkCdcVpc", {
      ipAddresses: ec2.IpAddresses.cidr("10.0.0.0/16"),
    });

    const streamKey = new kms.Key(this, "StreamKey");
    const s3Key = new kms.Key(this, "S3Key");

    const firehoseDestBucket = new s3.Bucket(this, "FirehoseDestinationBucket", {
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      encryption: s3.BucketEncryption.KMS,
      encryptionKey: s3Key,
    });

    const kinesisStream = new kinesis.Stream(this, "KinesisSource", {
      encryption: kinesis.StreamEncryption.KMS,
      encryptionKey: streamKey,
    });

    const firehoseS3Policy = new iam.PolicyDocument({
      statements: [
        new iam.PolicyStatement({
          actions: [
            "s3:AbortMultipartUpload",
            "s3:GetBucketLocation",
            "s3:GetObject",
            "s3:ListBucket",
            "s3:ListBucketMultipartUploads",
            "s3:PutObject",
          ],
          resources: [firehoseDestBucket.bucketArn, firehoseDestBucket.bucketArn + "/*"],
        }),
        new iam.PolicyStatement({
          actions: ["kms:Decrypt", "kms:GenerateDataKey"],
          resources: [s3Key.keyArn],
        }),
      ],
    });

    const firehoseDestRole = new iam.Role(this, "FirehoseDestRole", {
      assumedBy: new iam.ServicePrincipal("firehose.amazonaws.com"),
      inlinePolicies: {
        s3Policy: firehoseS3Policy,
      },
    });

    const kinesisFirehose = new firehose.CfnDeliveryStream(this, "FirehoseSink", {
      deliveryStreamEncryptionConfigurationInput: {
        keyType: "AWS_OWNED_CMK",
      },
      deliveryStreamType: "DirectPut",
      s3DestinationConfiguration: {
        bucketArn: firehoseDestBucket.bucketArn,
        roleArn: firehoseDestRole.roleArn,
        encryptionConfiguration: {
          kmsEncryptionConfig: {
            awskmsKeyArn: s3Key.keyArn,
          },
        },
      },
    });

    const flinkVpcPolicy = new iam.PolicyDocument({
      statements: [
        new iam.PolicyStatement({
          actions: ["ec2:DescribeVpcs", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups", "ec2:DescribeDhcpOptions"],
          resources: ["*"],
        }),
        new iam.PolicyStatement({
          actions: [
            "ec2:CreateNetworkInterface",
            "ec2:CreateNetworkInterfacePermission",
            "ec2:DescribeNetworkInterfaces",
            "ec2:DeleteNetworkInterface",
          ],
          resources: ["*"],
        }),
      ],
    });
    const flinkKinesisPolicy = new iam.PolicyDocument({
      statements: [
        new iam.PolicyStatement({
          actions: ["kinesis:DescribeStream", "kinesis:GetShardIterator", "kinesis:GetRecords", "kinesis:ListShards"],
          resources: [kinesisStream.streamArn],
        }),
        new iam.PolicyStatement({
          actions: ["firehose:DescribeDeliveryStream", "firehose:PutRecord", "firehose:PutRecordBatch"],
          resources: [kinesisFirehose.attrArn],
        }),
      ],
    });

    const flinkRole = new iam.Role(this, "KinesisAnalyticsRole", {
      assumedBy: new iam.ServicePrincipal("kinesisanalytics.amazonaws.com"),
      inlinePolicies: {
        vpcPolicy: flinkVpcPolicy,
        kinesisPolicy: flinkKinesisPolicy,
      },
    });
    flinkRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName("CloudWatchFullAccess"));

    const flinkAsset = new s3Asset.Asset(this, "flinkAppAsset2", {
      path: path.join(__dirname, "../flink-application/kinesis-flink-firehose-app/target/kinesis-flink-firehose-app-0.1.jar"),
    });

    const flinkSg = new ec2.SecurityGroup(this, "FlinkSg", {
      vpc,
    });
    const analyticsAppName = "exampleFlinkAnalyticsApp";
    const analyticsApp = new kinesisanalyticsv2.CfnApplication(this, "FlinkAnalyticsApp2", {
      runtimeEnvironment: "FLINK-1_15",
      serviceExecutionRole: flinkRole.roleArn,
      applicationName: analyticsAppName,
      applicationConfiguration: {
        flinkApplicationConfiguration: {
          monitoringConfiguration: {
            configurationType: "CUSTOM",
            logLevel: "INFO",
            metricsLevel: "APPLICATION",
          },
        },
        applicationCodeConfiguration: {
          codeContent: {
            s3ContentLocation: {
              bucketArn: flinkAsset.bucket.bucketArn,
              fileKey: flinkAsset.s3ObjectKey,
            },
          },
          codeContentType: "ZIPFILE",
        },
        environmentProperties: {
          propertyGroups: [
            {
              propertyGroupId: "ConsumerStreamName",
              propertyMap: {
                ConsumerStreamName: kinesisStream.streamName,
              },
            },
            {
              propertyGroupId: "DeliveryFirehoseName",
              propertyMap: {
                DeliveryFirehoseName: kinesisFirehose.ref || "invalidFirehose",
              },
            },
            {
              propertyGroupId: "ConsumerStreamProperties",
              propertyMap: {
                STREAM_INITIAL_POSITION: "LATEST",
                "aws.region": process.env.CDK_DEFAULT_REGION || "us-west-2",
              },
            },
            {
              propertyGroupId: "DeliveryFirehoseProperties",
              propertyMap: {
                "aws.region": process.env.CDK_DEFAULT_REGION || "us-west-2",
              },
            },
          ],
        },
        vpcConfigurations: [
          {
            securityGroupIds: [flinkSg.securityGroupId],
            subnetIds: vpc.selectSubnets({
              subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
            }).subnetIds,
          },
        ],
      },
      applicationDescription: "Flink application showcasing a kinesis data stream source and a firehose sink",
      runConfiguration: {
        flinkRunConfiguration: {
          allowNonRestoredState: false,
        },
      },
    });

    analyticsApp.node.addDependency(flinkAsset);
    analyticsApp.node.addDependency(kinesisStream);
    analyticsApp.addDependency(kinesisFirehose);
    analyticsApp.node.addDependency(flinkRole);

    const logGroup = new logs.LogGroup(this, "AnalyticsAppLogGroup");
    const logStream = new logs.LogStream(this, "MyLogStream", {
      logGroup: logGroup,
    });
    logStream.node.addDependency(logGroup);

    var logStreamArn =
      "arn:aws:logs:" +
      process.env.CDK_DEFAULT_REGION +
      ":" +
      this.account +
      ":log-group:" +
      logGroup.logGroupName +
      ":log-stream:" +
      logStream.logStreamName;

    const analyticsAppCwLogs = new kinesisanalyticsv2.CfnApplicationCloudWatchLoggingOption(this, "AnalyticsAppCwLogs", {
      applicationName: analyticsAppName,
      cloudWatchLoggingOption: {
        logStreamArn: logStreamArn,
      },
    });
    analyticsAppCwLogs.addDependency(analyticsApp);
    analyticsAppCwLogs.node.addDependency(logStream);
    analyticsApp.node.addDependency(vpc);

    flinkAsset.grantRead(flinkRole);

    streamKey.grantDecrypt(flinkRole);
  }
}

import * as cdk from "aws-cdk-lib";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as iam from "aws-cdk-lib/aws-iam";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as rds from "aws-cdk-lib/aws-rds";
import { Construct } from "constructs";

export class AuroraServerlessV2LambdaBedrockStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Use default VPC
    const vpc = ec2.Vpc.fromLookup(this, "DefaultVpc", { isDefault: true });

    // Aurora Serverless v2 cluster (PostgreSQL, scales to zero)
    const cluster = new rds.DatabaseCluster(this, "AuroraCluster", {
      engine: rds.DatabaseClusterEngine.auroraPostgres({
        version: rds.AuroraPostgresEngineVersion.VER_16_4,
      }),
      serverlessV2MinCapacity: 0,
      serverlessV2MaxCapacity: 4,
      writer: rds.ClusterInstance.serverlessV2("writer"),
      vpc,
      vpcSubnets: { subnetType: ec2.SubnetType.PUBLIC },
      defaultDatabaseName: "appdb",
      enableDataApi: true,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // Data API policy for Lambdas
    const dataApiPolicy = new iam.PolicyStatement({
      actions: [
        "rds-data:ExecuteStatement",
        "rds-data:BatchExecuteStatement",
      ],
      resources: [cluster.clusterArn],
    });

    const envVars = {
      CLUSTER_ARN: cluster.clusterArn,
      SECRET_ARN: cluster.secret!.secretArn,
      DB_NAME: "appdb",
    };

    // Setup Lambda — initializes the knowledge table
    const setupFn = new lambda.Function(this, "SetupFn", {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: "index.handler",
      code: lambda.Code.fromAsset("src/setup"),
      timeout: cdk.Duration.seconds(60),
      memorySize: 256,
      environment: envVars,
      description: "Seeds Aurora knowledge table via Data API",
    });
    cluster.secret!.grantRead(setupFn);
    setupFn.addToRolePolicy(dataApiPolicy);

    // Query Lambda — queries Aurora, sends context to Bedrock
    const queryFn = new lambda.Function(this, "QueryFn", {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: "index.handler",
      code: lambda.Code.fromAsset("src/query-fn"),
      timeout: cdk.Duration.minutes(2),
      memorySize: 512,
      environment: {
        ...envVars,
        MODEL_ID: "us.anthropic.claude-sonnet-4-20250514-v1:0",
      },
      description: "Queries Aurora knowledge base and sends to Bedrock",
    });
    cluster.secret!.grantRead(queryFn);
    queryFn.addToRolePolicy(dataApiPolicy);
    queryFn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["bedrock:InvokeModel"],
        resources: ["*"],
      })
    );

    new cdk.CfnOutput(this, "SetupFunctionName", {
      value: setupFn.functionName,
    });
    new cdk.CfnOutput(this, "QueryFunctionName", {
      value: queryFn.functionName,
    });
    new cdk.CfnOutput(this, "ClusterEndpoint", {
      value: cluster.clusterEndpoint.hostname,
    });
  }
}

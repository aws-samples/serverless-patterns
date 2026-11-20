import * as path from "path";
import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as dynamodb from "aws-cdk-lib/aws-dynamodb";
import * as iam from "aws-cdk-lib/aws-iam";
import * as lambda from "aws-cdk-lib/aws-lambda";
import { NodejsFunction, OutputFormat } from "aws-cdk-lib/aws-lambda-nodejs";
import * as logs from "aws-cdk-lib/aws-logs";
import * as s3assets from "aws-cdk-lib/aws-s3-assets";
import * as cloudfront from "aws-cdk-lib/aws-cloudfront";
import * as origins from "aws-cdk-lib/aws-cloudfront-origins";

// Deploy to us-east-1: Lambda@Edge functions can only be created there (see bin/app.ts).
export class MicrovmEdgeSessionsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // --- Session store -----------------------------------------------------
    // sessionId -> { microvmId, endpoint, token, tokenExpiresAt, launchedAt }. TTL on
    // `expiresAt` cleans up abandoned sessions.
    const table = new dynamodb.Table(this, "Sessions", {
      partitionKey: { name: "sessionId", type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      timeToLiveAttribute: "expiresAt",
    });

    // --- MicroVM image -----------------------------------------------------
    // The in-VM app dir, zipped and uploaded under a content-hashed key: any app change
    // yields a new CodeArtifact URI, which is what makes the image rebuild.
    const appAsset = new s3assets.Asset(this, "MicrovmAppAsset", {
      path: path.join(__dirname, "..", "src", "microvm-app"),
    });

    // The MicroVM service assumes the build and execution roles with sts:TagSession.
    const microvmRole = (id: string) => {
      const role = new iam.Role(this, id, { assumedBy: new iam.ServicePrincipal("lambda.amazonaws.com") });
      role.assumeRolePolicy?.addStatements(
        new iam.PolicyStatement({
          actions: ["sts:TagSession"],
          principals: [new iam.ServicePrincipal("lambda.amazonaws.com")],
        }),
      );
      return role;
    };

    // Build role: read the code artifact and write build logs. The service picks the
    // build log group name, so logs can't be scoped to a known ARN here.
    const buildRole = microvmRole("MicrovmBuildRole");
    appAsset.grantRead(buildRole);
    buildRole.addToPolicy(
      new iam.PolicyStatement({
        actions: ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
        resources: ["*"],
      }),
    );

    // Execution role: write the per-session VM's runtime logs to this stack's log group.
    const runtimeLogs = new logs.LogGroup(this, "MicrovmRuntimeLogs", {
      logGroupName: `/aws/lambda-microvms/${this.stackName}`,
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
    const executionRole = microvmRole("MicrovmExecutionRole");
    runtimeLogs.grantWrite(executionRole);

    // No L2 for AWS::Lambda::MicrovmImage yet, so use the L1.
    const image = new lambda.CfnMicrovmImage(this, "MicrovmImage", {
      name: `${this.stackName}-image`,
      baseImageArn: `arn:${cdk.Aws.PARTITION}:lambda:${cdk.Aws.REGION}:aws:microvm-image:al2023-1`,
      // Pinned base version. Versions are deprecated, then expire (see README "Gotchas");
      // list current ones with `aws lambda-microvms list-managed-microvm-image-versions`.
      baseImageVersion: "2",
      buildRoleArn: buildRole.roleArn,
      codeArtifact: { uri: appAsset.s3ObjectUrl },
      cpuConfigurations: [{ architecture: "ARM_64" }],
      // Required by CloudFormation; "ALL" (elevated OS capabilities) is its only allowed value,
      // and what the sibling MicroVM patterns use. The hello-world app doesn't need them.
      additionalOsCapabilities: ["ALL"],
      description: "Hello-world per-session MicroVM (Node 22 on AL2023)",
      egressNetworkConnectors: [],
      environmentVariables: [],
      hooks: {
        port: 9000, // the service's ready poller can't reach 8081, next to the app port
        microvmImageHooks: { ready: "ENABLED", readyTimeoutInSeconds: 60 },
        // Only /run matters here (it carries the session id); the app just returns 200 to
        // the others. TODO: try enabling only `run` once a deploy confirms that's accepted.
        microvmHooks: {
          run: "ENABLED",
          runTimeoutInSeconds: 30,
          resume: "ENABLED",
          resumeTimeoutInSeconds: 30,
          suspend: "ENABLED",
          suspendTimeoutInSeconds: 30,
          terminate: "ENABLED",
          terminateTimeoutInSeconds: 30,
        },
      },
      logging: { cloudWatch: { logGroup: runtimeLogs.logGroupName } },
      resources: [{ minimumMemoryInMiB: 512 }],
    });
    image.node.addDependency(buildRole);

    // --- Edge router (Lambda@Edge, origin-request) -------------------------
    const edgeFn = new NodejsFunction(this, "EdgeRouter", {
      runtime: lambda.Runtime.NODEJS_24_X,
      entry: path.join(__dirname, "..", "src", "edge", "lambda.ts"),
      timeout: cdk.Duration.seconds(5),
      memorySize: 128,
      bundling: { format: OutputFormat.CJS },
    });
    // Lambda@Edge roles must also trust edgelambda.amazonaws.com; CDK adds that trust when
    // the function is attached to the distribution below.
    table.grant(edgeFn, "dynamodb:GetItem");

    // --- Control plane (regional Lambda + IAM-auth Function URL) -----------
    const controlFn = new NodejsFunction(this, "Control", {
      runtime: lambda.Runtime.NODEJS_24_X,
      entry: path.join(__dirname, "..", "src", "control", "lambda.ts"),
      timeout: cdk.Duration.seconds(60),
      memorySize: 256,
      environment: {
        SESSION_TABLE: table.tableName,
        IMAGE_ARN: image.attrImageArn,
        EXECUTION_ROLE_ARN: executionRole.roleArn,
        RUNTIME_LOG_GROUP: runtimeLogs.logGroupName,
      },
      // The MicroVMs client isn't guaranteed to be in the runtime's SDK, so bundle it.
      bundling: { format: OutputFormat.CJS, externalModules: [] },
    });
    table.grant(controlFn, "dynamodb:GetItem", "dynamodb:PutItem", "dynamodb:DeleteItem");

    // MicroVM actions use the `lambda:` IAM prefix (not `lambda-microvms:`) and are
    // authorized on the image: there is no per-MicroVM ARN, so this is the tightest grant.
    controlFn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["lambda:RunMicrovm", "lambda:GetMicrovm", "lambda:CreateMicrovmAuthToken", "lambda:TerminateMicrovm"],
        resources: [image.attrImageArn],
      }),
    );
    // RunMicrovm also requires lambda:PassNetworkConnector for the AWS-managed network
    // connectors it attaches. The resource form follows the managed connector ARNs.
    controlFn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["lambda:PassNetworkConnector"],
        resources: [`arn:${cdk.Aws.PARTITION}:lambda:${cdk.Aws.REGION}:aws:network-connector:aws-network-connector:*`],
      }),
    );
    controlFn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["iam:PassRole"],
        resources: [executionRole.roleArn],
        conditions: { StringEquals: { "iam:PassedToService": "lambda.amazonaws.com" } },
      }),
    );

    // IAM-auth Function URL, reachable only through CloudFront's SigV4-signing OAC.
    const fnUrl = controlFn.addFunctionUrl({ authType: lambda.FunctionUrlAuthType.AWS_IAM });

    // --- CloudFront --------------------------------------------------------
    // The default behavior's origin is a placeholder: the edge function either points
    // the request at a MicroVM or answers it itself, so example.com is never contacted.
    // Its custom headers carry the edge function's config (Lambda@Edge has no env vars).
    const routerOrigin = new origins.HttpOrigin("example.com", {
      protocolPolicy: cloudfront.OriginProtocolPolicy.HTTPS_ONLY,
      customHeaders: { "x-sessions-table": table.tableName, "x-sessions-region": this.region },
    });

    const distribution = new cloudfront.Distribution(this, "Cdn", {
      comment: "Session routing to per-session Lambda MicroVMs",
      defaultBehavior: {
        origin: routerOrigin,
        viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
        allowedMethods: cloudfront.AllowedMethods.ALLOW_ALL,
        cachePolicy: cloudfront.CachePolicy.CACHING_DISABLED,
        // The edge function overwrites Host with the MicroVM endpoint.
        originRequestPolicy: cloudfront.OriginRequestPolicy.ALL_VIEWER,
        edgeLambdas: [{ functionVersion: edgeFn.currentVersion, eventType: cloudfront.LambdaEdgeEventType.ORIGIN_REQUEST }],
      },
      additionalBehaviors: {
        "/_control*": {
          // OAC signs requests with SigV4. This helper also grants cloudfront.amazonaws.com
          // both lambda:InvokeFunctionUrl and lambda:InvokeFunction, scoped to this distribution.
          origin: origins.FunctionUrlOrigin.withOriginAccessControl(fnUrl),
          viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
          allowedMethods: cloudfront.AllowedMethods.ALLOW_ALL,
          cachePolicy: cloudfront.CachePolicy.CACHING_DISABLED,
          // Not the viewer Host: the OAC signature must be for the Function URL host.
          originRequestPolicy: cloudfront.OriginRequestPolicy.ALL_VIEWER_EXCEPT_HOST_HEADER,
        },
      },
    });

    new cdk.CfnOutput(this, "DistributionUrl", {
      value: `https://${distribution.distributionDomainName}`,
      description: "Open https://<this>/s/<sessionId>/ to reach that session's MicroVM.",
    });
  }
}

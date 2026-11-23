import * as path from 'path';
import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as appconfig from 'aws-cdk-lib/aws-appconfig';
import * as cloudwatch from 'aws-cdk-lib/aws-cloudwatch';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as logs from 'aws-cdk-lib/aws-logs';

// Amazon Bedrock models the function may call. AWS AppConfig stores only the model id, so this IAM list is the
// allowlist: a configuration that names any other model fails with AccessDeniedException and fires the alarm.
const ALLOWED_MODELS = ['amazon.nova-2-lite-v1:0', 'amazon.nova-micro-v1:0'];
const INITIAL_MODEL = ALLOWED_MODELS[0];

// Destination Regions of the us. and eu. geo inference profiles of both models (Nova 2 Lite and Nova Micro model cards).
const GEO_DESTINATIONS: Record<string, string[]> = {
  us: ['us-east-1', 'us-east-2', 'us-west-2'],
  eu: ['eu-central-1', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-3'],
};

// Supported Regions: geo prefix plus the AWS-published arm64 layer of the AWS AppConfig Agent Lambda extension
// (owner account and layer version for extension 2.0.27899, from the "available versions" page of the AppConfig guide).
const REGIONS: Record<string, { geo: string; layer: string }> = {
  'us-east-1': { geo: 'us', layer: '027255383542:289' },
  'us-east-2': { geo: 'us', layer: '728743619870:262' },
  'us-west-2': { geo: 'us', layer: '359756378197:307' },
  'eu-central-1': { geo: 'eu', layer: '066940009817:264' },
  'eu-north-1': { geo: 'eu', layer: '646970417810:253' },
  'eu-west-1': { geo: 'eu', layer: '434848589818:269' },
  'eu-west-3': { geo: 'eu', layer: '493207061005:225' },
};

export class AppconfigAiModelLambdaBedrockStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    if (cdk.Token.isUnresolved(this.region) || !REGIONS[this.region]) {
      throw new Error(`Deploy to one of: ${Object.keys(REGIONS).join(', ')} (set AWS_REGION or a default Region). See the README.`);
    }
    const { geo, layer } = REGIONS[this.region];
    const [layerOwner, layerVersion] = layer.split(':');

    // AWS AppConfig names are scoped to this stack, so two stacks can deploy side by side.
    const application = new appconfig.Application(this, 'Application', { applicationName: this.stackName });
    const environmentName = `${this.stackName}-live`;
    const profileName = `${this.stackName}-model`;

    // The function reads its configuration through the agent by name. Names (not ids) keep the function
    // independent of the environment, which depends on the alarm, which depends on the function.
    const logGroup = new logs.LogGroup(this, 'AssistantLogGroup', {
      retention: logs.RetentionDays.TWO_WEEKS,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
    const fn = new lambda.Function(this, 'AssistantFunction', {
      runtime: lambda.Runtime.NODEJS_24_X,
      architecture: lambda.Architecture.ARM_64,
      handler: 'index.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', 'lambda')),
      timeout: cdk.Duration.seconds(30),
      memorySize: 256,
      logGroup,
      loggingFormat: lambda.LoggingFormat.JSON,
      layers: [lambda.LayerVersion.fromLayerVersionArn(this, 'AppConfigAgentLayer',
        `arn:${this.partition}:lambda:${this.region}:${layerOwner}:layer:AWS-AppConfig-Extension-Arm64:${layerVersion}`)],
      environment: {
        CONFIG_PATH: `/applications/${this.stackName}/environments/${environmentName}/configurations/${profileName}`,
        AWS_APPCONFIG_EXTENSION_POLL_INTERVAL_SECONDS: '15', // default 45; shorter so a test sees changes quickly
      },
    });

    // Converse needs bedrock:InvokeModel on the geo inference profile and on the model in every destination Region.
    fn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: ALLOWED_MODELS.flatMap((model) => [
        `arn:${this.partition}:bedrock:${this.region}:${this.account}:inference-profile/${geo}.${model}`,
        ...GEO_DESTINATIONS[geo].map((r) => `arn:${this.partition}:bedrock:${r}::foundation-model/${model}`),
      ]),
    }));

    // Any function error during a deployment or its bake time makes AWS AppConfig roll the configuration back.
    const errorsAlarm = fn.metricErrors({ period: cdk.Duration.minutes(1), statistic: 'Sum' }).createAlarm(this, 'ErrorsAlarm', {
      threshold: 1,
      evaluationPeriods: 1,
      comparisonOperator: cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
      treatMissingData: cloudwatch.TreatMissingData.NOT_BREACHING,
      alarmDescription: 'AWS AppConfig rolls back a model configuration deployment when this alarm fires',
    });

    // Role AWS AppConfig assumes to read the alarm, trusted only for calls from this account (confused deputy).
    // DescribeAlarms needs Resource "*" (AWS AppConfig user guide, "Configure permissions for automatic rollback").
    // An inline policy, so the role can read the alarm as soon as the environment that references it exists.
    const monitorRole = new iam.Role(this, 'MonitorRole', {
      assumedBy: new iam.ServicePrincipal('appconfig.amazonaws.com', {
        conditions: { StringEquals: { 'aws:SourceAccount': this.account } },
      }),
      inlinePolicies: {
        ReadAlarm: new iam.PolicyDocument({
          statements: [new iam.PolicyStatement({ actions: ['cloudwatch:DescribeAlarms'], resources: ['*'] })],
        }),
      },
    });
    const environment = new appconfig.Environment(this, 'Environment', {
      application,
      environmentName,
      monitors: [appconfig.Monitor.fromCloudWatchAlarm(errorsAlarm, monitorRole)],
      deletionProtectionCheck: appconfig.DeletionProtectionCheck.BYPASS, // demo: cdk destroy works right after a test
    });

    // L1 resource: the L2 ConfigurationType enum in aws-cdk-lib has no value for AI model invocation profiles yet.
    const profile = new appconfig.CfnConfigurationProfile(this, 'ModelProfile', {
      applicationId: application.applicationId,
      name: profileName,
      locationUri: 'hosted',
      type: 'AWS.AppConfig.AIModelInvocation',
      deletionProtectionCheck: 'BYPASS',
    });
    const profileId = profile.attrConfigurationProfileId;

    // Version 1. AWS AppConfig validates it against the AI model invocation schema. CloudFormation rejects plain
    // application/json for this profile type and asks for the typed content type below.
    const version1 = new appconfig.CfnHostedConfigurationVersion(this, 'ModelConfigV1', {
      applicationId: application.applicationId,
      configurationProfileId: profileId,
      contentType: 'application/json; type=AWS.AppConfig.AIModelInvocation',
      content: JSON.stringify({
        schemaVersion: '1',
        model: `${geo}.${INITIAL_MODEL}`,
        inferenceParameters: { temperature: 0.2, maxTokens: 300 },
        messages: [{ role: 'system', content: 'You are a concise assistant. Answer in at most two sentences.' }],
      }),
    });

    // Stack creation deploys version 1 at once; later changes use the gradual strategy below.
    const initialStrategy = new appconfig.DeploymentStrategy(this, 'InitialStrategy', {
      rolloutStrategy: appconfig.RolloutStrategy.linear({
        growthFactor: 100, deploymentDuration: cdk.Duration.minutes(0), finalBakeTime: cdk.Duration.minutes(0),
      }),
    });
    // 50 percent of the agents, then 100 percent, over 4 minutes, then 5 minutes of bake time with the alarm watched.
    const rolloutStrategy = new appconfig.DeploymentStrategy(this, 'RolloutStrategy', {
      rolloutStrategy: appconfig.RolloutStrategy.linear({
        growthFactor: 50, deploymentDuration: cdk.Duration.minutes(4), finalBakeTime: cdk.Duration.minutes(5),
      }),
    });
    new appconfig.CfnDeployment(this, 'InitialDeployment', {
      applicationId: application.applicationId,
      environmentId: environment.environmentId,
      configurationProfileId: profileId,
      configurationVersion: version1.attrVersionNumber,
      deploymentStrategyId: initialStrategy.deploymentStrategyId,
    });

    // A separate policy (not the role's default policy) keeps the function out of the environment's dependency chain.
    new iam.Policy(this, 'ReadModelConfig', {
      roles: [fn.role as iam.IRole],
      statements: [new iam.PolicyStatement({
        actions: ['appconfig:StartConfigurationSession', 'appconfig:GetLatestConfiguration'],
        resources: [`${environment.environmentArn}/configuration/${profileId}`],
      })],
    });

    new cdk.CfnOutput(this, 'FunctionName', { value: fn.functionName });
    new cdk.CfnOutput(this, 'LogGroupName', { value: logGroup.logGroupName });
    new cdk.CfnOutput(this, 'ApplicationId', { value: application.applicationId });
    new cdk.CfnOutput(this, 'EnvironmentId', { value: environment.environmentId });
    new cdk.CfnOutput(this, 'ConfigurationProfileId', { value: profileId });
    new cdk.CfnOutput(this, 'RolloutStrategyId', { value: rolloutStrategy.deploymentStrategyId });
    new cdk.CfnOutput(this, 'AlarmName', { value: errorsAlarm.alarmName });
    new cdk.CfnOutput(this, 'GeoPrefix', { value: geo });
  }
}

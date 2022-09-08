import { Stack, StackProps, aws_appconfig as appconfig, aws_lambda_nodejs as nodejs_lambda, aws_lambda as lambda, Duration, CfnParameter, aws_iam as iam } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as path from 'path';

export class AppConfigFeatureFlagCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const appConfigExtensionArn = new CfnParameter(this, 'appConfigExtensionArn', { type: 'String' });

    // ##########################################################################
    // # APPCONFIG RESOURCES
    // ##########################################################################
    const myAppconfigApplication = new appconfig.CfnApplication(this, 'MyAppconfigApplication', {
      name: 'MyAppconfigApplication',
    });

    const myAppconfigConfigurationProfile = new appconfig.CfnConfigurationProfile(this, 'myAppconfigConfigurationProfile', {
      applicationId: myAppconfigApplication.ref,
      locationUri: 'hosted',
      name: 'DiscountCodeConfigurationProfile',
      type: 'AWS.AppConfig.FeatureFlags',
    });

    const myHostedConfigurationVersion = new appconfig.CfnHostedConfigurationVersion(this, 'MyHostedConfigurationVersion', {
      applicationId: myAppconfigApplication.ref,
      configurationProfileId: myAppconfigConfigurationProfile.ref,
      contentType: 'application/json',
      content: JSON.stringify({
        "version": "1",
        "flags": {
          myFeatureFlag: {
            "name": "myFeatureFlag",
          }
        },
        "values": {
          myFeatureFlag: {
            "enabled": true,
          }
        }
      }),
    });

    const myAppconfigEnv = new appconfig.CfnEnvironment(this, 'myAppconfigEnv', {
      applicationId: myAppconfigApplication.ref,
      name: 'dev',
    });

    const myDeploymentStrategy = new appconfig.CfnDeploymentStrategy(this, 'myDeploymentStrategy', {
      deploymentDurationInMinutes: 0,
      growthFactor: 100,
      name: 'myDeploymentStrategy',
      replicateTo: 'SSM_DOCUMENT',
      finalBakeTimeInMinutes: 0,
    });

    const deployment = new appconfig.CfnDeployment(this, 'InitialDeployment', {
      applicationId: myAppconfigApplication.ref,
      configurationProfileId: myAppconfigConfigurationProfile.ref,
      configurationVersion: myHostedConfigurationVersion.ref,
      environmentId: myAppconfigEnv.ref,
      deploymentStrategyId: myDeploymentStrategy.ref,
    });

    // ##########################################################################
    // # LAMBDA FUNCTION
    // ##########################################################################

    const APPCONFIG_EXTENSION_ARN = appConfigExtensionArn.valueAsString;

    const checkFeatureFlagStatusLambda = new nodejs_lambda.NodejsFunction(this, "CheckFeatureFlagStatusLambda", {
      runtime: lambda.Runtime.NODEJS_14_X,
      entry: path.join(__dirname, `/../lambda/index.ts`),
      handler: "handler",
      retryAttempts: 0,
      timeout: Duration.seconds(15),
      environment: {
        APPCONFIG_APPLICATION_ID: myAppconfigApplication.ref,
        APPCONFIG_ENVIRONMENT: myAppconfigEnv.name,
        APPCONFIG_CONFIGURATION_ID: myAppconfigConfigurationProfile.ref,
        FEATURE_FLAG_NAME: "myFeatureFlag",
      }
    });

    checkFeatureFlagStatusLambda.addLayers(
      lambda.LayerVersion.fromLayerVersionArn(this, 'AppConfigExtension', APPCONFIG_EXTENSION_ARN)
    );

    // Setting permissions for AppConfig
    checkFeatureFlagStatusLambda.role?.attachInlinePolicy(
      new iam.Policy(this, 'additionalPermissionsForAppConfig', {
        statements: [
          new iam.PolicyStatement({
            actions: ['appconfig:StartConfigurationSession', 'appconfig:GetLatestConfiguration'],
            resources: ['*'],
          }),
        ],
      }),
    )
  }
}

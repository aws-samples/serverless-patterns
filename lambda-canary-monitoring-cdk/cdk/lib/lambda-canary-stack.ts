import { Duration, RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as path from 'path';
import * as codedeploy from 'aws-cdk-lib/aws-codedeploy';
import * as cloudwatch from 'aws-cdk-lib/aws-cloudwatch';
import { IMonitoring } from './monitoring-stack';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { PolicyStatement } from 'aws-cdk-lib/aws-iam';


interface LambdaCanaryMonitoringStackProps extends StackProps {
  readonly VERSION_NUMBER: string;
  readonly monitoring: IMonitoring;
}


export class LambdaCanaryMonitoringStack extends Stack {
  constructor(
    scope: Construct,
    id: string,
    props: LambdaCanaryMonitoringStackProps
  ) {
    super(scope, id, props);

    const dashboardLambda = this.createDashboardLambda(props.monitoring.dashboard);
    const businessLambda = this.createBusinessLambda(props.VERSION_NUMBER);
    const deploymentGroup = this.deployBusinessLambda(businessLambda, dashboardLambda);
    this.assignIAMPolicyToDashboardLambda(dashboardLambda, props.monitoring.dashboard, deploymentGroup);
  }

  private createBusinessLambda(versionNumber:string): lambda.Function{
    return new NodejsFunction(this, 'Business-Lambda', {
      currentVersionOptions: {
        removalPolicy: RemovalPolicy.RETAIN,
      },
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'handler',
      entry: path.join(__dirname, '../lambda-code/app.ts'),
      timeout: Duration.seconds(25),
      environment: {
        SLEEP_SEC: '2',
        VERSION: versionNumber,
      },
    });
  }

  private deployBusinessLambda(handler: lambda.Function, dashboardLambda: lambda.Function):codedeploy.LambdaDeploymentGroup {
    const application = new codedeploy.LambdaApplication(
      this,
      'CodeDeployApplication',
      {
        applicationName: 'LambdaCanaryMonitoringApplication',
      }
    );
    
    const aliasBusinessLambda = new lambda.Alias(this, 'alias', {
      aliasName: 'prod',
      version: handler.currentVersion,
      // provisionedConcurrentExecutions: 100, //commented this line to reduce accidental costs. Comment in, to test provisioned concurrency traffic shift
    });
    

    const deploymentGroup = new codedeploy.LambdaDeploymentGroup(this,
      'LambdaCanaryMonitoringDeploymentGroup',
      {
        application: application,
        alias: aliasBusinessLambda,
        deploymentConfig: codedeploy.LambdaDeploymentConfig.ALL_AT_ONCE,
        preHook: dashboardLambda,
      }
    );

    // Can be used to run a load test during traffic shift
    aliasBusinessLambda.addFunctionUrl({
      authType: lambda.FunctionUrlAuthType.NONE,
    });
    return deploymentGroup;
  }

  /**
   * Creates the Lambda Function that will be called in the CodeDeploy preHook and changes the given CloudWatch Dashboard
   * @param dashboard Name of the dashboard where the metrics should be added
   */
  private createDashboardLambda(dashboard: cloudwatch.Dashboard): lambda.Function {
    return new NodejsFunction(this, 'Dashboard-Lambda', {
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'handler',
      entry: path.join(__dirname, '../lambda-code/dashboard-lambda.ts'),
      environment: { DASHBOARD_NAME: dashboard.dashboardName },
      timeout: Duration.seconds(10),
      bundling: {
        externalModules: ['aws-sdk'],
        sourceMap: true,
      },
    });
  }

  private assignIAMPolicyToDashboardLambda(dashboardLambda: lambda.Function, dashboard: cloudwatch.Dashboard, deploymentGroup: codedeploy.LambdaDeploymentGroup){
    /**
     * IAM Policies for the Lambda to read from CodeDeploy and create the CloudWatch Dashboard
     */
    const policyCodeDeployApplication = new PolicyStatement();
    policyCodeDeployApplication.addResources(deploymentGroup.application.applicationArn);
    policyCodeDeployApplication.addActions('codedeploy:GetApplicationRevision');
    
    const policyCodeDeployDeploymentGroup = new PolicyStatement();
    policyCodeDeployDeploymentGroup.addResources(deploymentGroup.deploymentGroupArn);
    policyCodeDeployDeploymentGroup.addActions('codedeploy:GetDeployment');
        
    const policyCloudwatch = new PolicyStatement();
    policyCloudwatch.addResources(dashboard.dashboardArn+dashboard.dashboardName);
    policyCloudwatch.addActions('cloudwatch:PutDashboard');
    
    dashboardLambda.addToRolePolicy(policyCodeDeployApplication);
    dashboardLambda.addToRolePolicy(policyCodeDeployDeploymentGroup);
    dashboardLambda.addToRolePolicy(policyCloudwatch);
  }
}

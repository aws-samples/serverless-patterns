'use strict';
import {
  CodeDeploy,
  GetDeploymentOutput,
  GetApplicationRevisionOutput,
  RevisionLocation,
  PutLifecycleEventHookExecutionStatusInput,
} from '@aws-sdk/client-codedeploy';
import { CloudWatch } from '@aws-sdk/client-cloudwatch';
import { Handler } from 'aws-lambda';
const codedeploy = new CodeDeploy({ apiVersion: '2014-10-06' });
const cloudwatch = new CloudWatch();
const DASHBOARD_NAME = process.env.DASHBOARD_NAME || '';
const METRIC_REGION = process.env.AWS_REGION || '';

/**
 * This Lambda Function can be configured as a BeforeAllowTestTraffic Hook in a CodeDeploy Deployment of a Lambda Function
 * The function will read the information about the Deployed Lambda Version and will create metrics on a pre-created CloudWatch Dashboard.
 * It will create metrics for the currently running Version of the Lambda Function and for the to-be-deployed function.
 * This allows you to monitor traffic shift to your new version.
 * Currently the metrics focus on monitoring Provisioned Concurrency related metrics, however this can be adjusted.
 */
export const handler: Handler = async (event: any, _context: any) => {
  const validationTestResult = performTrafficValidationTests();

  const revisionDetails: RevisionLocation = await getRevisionDetails(
    event.DeploymentId
  );

  const { lambdaName, currentVersion, targetVersion, lambdaAlias } =
    getLambdaDetailsFromRevision(revisionDetails);

  await createMetricGraphs(
    currentVersion,
    targetVersion,
    lambdaName,
    lambdaAlias,
    METRIC_REGION
  );

  const params: PutLifecycleEventHookExecutionStatusInput = {
    deploymentId: event.DeploymentId,
    lifecycleEventHookExecutionId: event.LifecycleEventHookExecutionId,
    status: validationTestResult, // status can be 'Succeeded' or 'Failed'
  };
  // Sends Status to CodeDeploy, so the Deployment can continue or rollback
  await codedeploy.putLifecycleEventHookExecutionStatus(params);
};

function performTrafficValidationTests() {
  console.log('This is where AfterAllowTestTraffic validation tests happen.');
  if (true) {
    return 'Succeeded';
  }
  return 'Failed';
}

async function getRevisionDetails(
  deploymentId: string
): Promise<RevisionLocation> {
  // Read the DeploymentId and LifecycleEventHookExecutionId from the event payload

  const deploymentData: GetDeploymentOutput = await codedeploy
    .getDeployment({ deploymentId: deploymentId });

  const appName = deploymentData.deploymentInfo?.applicationName || '';

  const revision: GetApplicationRevisionOutput = await codedeploy
    .getApplicationRevision({
      applicationName: appName,
      revision: deploymentData.deploymentInfo?.revision || {},
    });

  return revision.revision || {};
}

function getLambdaDetailsFromRevision(revisionLocation: RevisionLocation): {
  lambdaName: string;
  currentVersion: string;
  targetVersion: string;
  lambdaAlias: string;
} {
  //   const sampleRevisionDetails = {
  //   version: '0.0',
  //   Resources: [
  //     {
  //       '<NameOfDeployedLambda>': {
  //         Type: 'AWS::Lambda::Function',
  //         Properties: {
  //           Name: '<NameOfDeployedLambda>',
  //           Alias: 'prod',
  //           CurrentVersion: '18',
  //           TargetVersion: '19',
  //         },
  //       },
  //     },
  //   ],
  //   Hooks: [
  //     {
  //       BeforeAllowTraffic:
  //         '<NameOfHookLambda>',
  //     },
  //   ],
  // };

  const revisionDetails = JSON.parse(revisionLocation.string?.content || '');
  const lambdaName = Object.keys(revisionDetails.Resources[0])[0];
  const lambdaData = revisionDetails.Resources[0][lambdaName].Properties;

  const currentVersion = lambdaData.CurrentVersion;
  const targetVersion = lambdaData.TargetVersion;
  const lambdaAlias = lambdaData.Alias;

  return { lambdaName, currentVersion, targetVersion, lambdaAlias };
}

async function createMetricGraphs(
  currentVersion: string,
  targetVersion: string,
  lambdaName: string,
  lambdaAlias: string,
  metricRegion: string
) {
  const metricData = generateWidgetsForFunctions(
    lambdaName,
    [currentVersion, targetVersion],
    lambdaAlias,
    metricRegion
  );
  const dashboardBody = { widgets: metricData };
  await cloudwatch
    .putDashboard({
      DashboardName: DASHBOARD_NAME,
      DashboardBody: JSON.stringify(dashboardBody),
    });
}

/**
 * Generates JSON that can be pushed to the Dashboard. One row of metrics per function.
 * @param functionName
 * @param versions
 * @param lambdaAlias
 * @returns
 */
function generateWidgetsForFunctions(
  functionName: string,
  versions: string[],
  lambdaAlias: string,
  metricRegion: string
) {
  
  const metrics = [
    {
      metricName: 'ProvisionedConcurrentExecutions',
      stat: 'Maximum',
      period: 60,
    },
    {
      metricName: 'ProvisionedConcurrencySpilloverInvocations',
      stat: 'Sum',
      period: 60,
    },
    {
      metricName: 'ProvisionedConcurrencyInvocations',
      stat: 'Sum',
      period: 60,
    },
    {
      metricName: 'Throttles',
      stat: 'Sum',
      period: 60,
    },
    {
      metricName: 'Invocations',
      stat: 'Sum',
      period: 60,
    },
  ];
  // Max width of Dashboard is 24
  const metricWidth = Math.floor(24/metrics.length);
  const metricHeight = 6;
  //Alternates between these two colors for the metric graphs
  const colorOrange = '#f89256';
  const colorBlue = '#08aad2';
  const output = [];
  let yPosition = 0;
  let counter = 0;
  for (let version of versions) {
    let xPosition = 0;
    for (let metric of metrics) {
      let singleMetricElement = {
        type: 'metric',
        x: xPosition,
        y: yPosition,
        width: metricWidth,
        height: metricHeight,
        properties: {
          metrics: [
            [
              'AWS/Lambda',
              metric.metricName,
              'FunctionName',
              functionName,
              'ExecutedVersion',
              `${version}`,
              'Resource',
              `${functionName}:${lambdaAlias}`,
            ],
          ],
          view: 'timeSeries',
          stacked: false,
          region: metricRegion,
          color: counter % 2 ? colorBlue : colorOrange,
          label: `v${version}`,
          stat: metric.stat,
          period: metric.period,
          title: `v${version}-${metric.metricName}`,
        },
      };
      output.push(singleMetricElement);
      xPosition += metricWidth;
    }
    yPosition += metricHeight;
    counter++;
  }
  return output;
}

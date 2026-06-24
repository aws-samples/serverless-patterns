import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as agentcore from 'aws-cdk-lib/aws-bedrockagentcore';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class AgentcoreBrowserStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Amazon Bedrock AgentCore Browser for AI agent web browsing
    const browser = new agentcore.BrowserCustom(this, 'AgentBrowser', {
      browserCustomName: 'agent_browser',
      description: 'Amazon Bedrock AgentCore Browser for AI agent web interaction',
      networkConfiguration: agentcore.BrowserNetworkConfiguration.usingPublicNetwork(),
    });

    // AWS Lambda function to demonstrate browser operations
    const fn = new lambda.Function(this, 'BrowserFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src/handler'),
      timeout: cdk.Duration.seconds(60),
      environment: {
        BROWSER_ID: browser.browserId,
      },
    });

    // Grant the AWS Lambda function permissions to use Amazon Bedrock AgentCore Browser
    browser.grantUse(fn);
    fn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock-agentcore:ListBrowserSessions'],
      resources: [browser.browserArn],
    }));

    // Outputs
    new cdk.CfnOutput(this, 'BrowserId', { value: browser.browserId });
    new cdk.CfnOutput(this, 'FunctionName', { value: fn.functionName });
  }
}

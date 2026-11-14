// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0 (2026)

import * as cdk from 'aws-cdk-lib';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as wafv2 from 'aws-cdk-lib/aws-wafv2';
import * as logs from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';
import * as path from 'path';

export class WafAgentcoreGatewayBedrockStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const region = cdk.Stack.of(this).region;
    const account = cdk.Stack.of(this).account;

    // --- Lambda Tool: Bedrock Inference ---
    const toolRole = new iam.Role(this, 'ToolLambdaRole', {
      assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaBasicExecutionRole'),
      ],
      inlinePolicies: {
        BedrockInvoke: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({
              actions: ['bedrock:InvokeModel'],
              resources: [
                `arn:aws:bedrock:*::foundation-model/anthropic.claude-sonnet-4-6*`,
                `arn:aws:bedrock:${region}:${account}:inference-profile/us.anthropic.claude-sonnet-4-6`,
              ],
            }),
          ],
        }),
      },
    });

    const toolFunction = new lambda.Function(this, 'BedrockToolFunction', {
      runtime: lambda.Runtime.NODEJS_22_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', 'lambda')),
      role: toolRole,
      timeout: cdk.Duration.seconds(30),
      memorySize: 256,
      environment: {
        MODEL_ID: 'us.anthropic.claude-sonnet-4-6',
        REGION: region,
      },
    });

    // --- AgentCore Gateway ---
    const gatewayRole = new iam.Role(this, 'GatewayRole', {
      assumedBy: new iam.ServicePrincipal('bedrock-agentcore.amazonaws.com'),
      inlinePolicies: {
        InvokeLambda: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({
              actions: ['lambda:InvokeFunction'],
              resources: [toolFunction.functionArn],
            }),
          ],
        }),
      },
    });

    const gateway = new cdk.CfnResource(this, 'AgentCoreGateway', {
      type: 'AWS::BedrockAgentCore::Gateway',
      properties: {
        Name: 'waf-protected-gateway',
        Description: 'AgentCore Gateway protected by AWS WAF',
        AuthorizerType: 'NONE',
        RoleArn: gatewayRole.roleArn,
        ProtocolConfiguration: {
          Mcp: {
            SupportedVersions: ['2025-11-25'],
            Instructions: 'WAF-protected gateway routing tool invocations to Lambda functions with Amazon Bedrock inference',
          },
        },
      },
    });

    const gatewayTarget = new cdk.CfnResource(this, 'BedrockToolTarget', {
      type: 'AWS::BedrockAgentCore::GatewayTarget',
      properties: {
        GatewayIdentifier: gateway.ref,
        Name: 'bedrock-inference',
        Description: 'Lambda tool that invokes Amazon Bedrock for AI inference',
        CredentialProviderConfigurations: [
          {
            CredentialProviderType: 'GATEWAY_IAM_ROLE',
          },
        ],
        TargetConfiguration: {
          Mcp: {
            Lambda: {
              LambdaArn: toolFunction.functionArn,
              ToolSchema: {
                InlinePayload: [
                  {
                    Name: 'invoke_bedrock',
                    Description: 'Invoke Amazon Bedrock Claude model with a user prompt and return the AI-generated response',
                    InputSchema: {
                      Type: 'object',
                      Properties: {
                        prompt: {
                          Type: 'string',
                          Description: 'The user prompt to send to Amazon Bedrock',
                        },
                      },
                      Required: ['prompt'],
                    },
                  },
                ],
              },
            },
          },
        },
      },
    });

    // --- WAF WebACL ---
    const wafLogGroup = new logs.LogGroup(this, 'WafLogGroup', {
      logGroupName: `aws-waf-logs-agentcore-gateway`,
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const ipAllowSet = new wafv2.CfnIPSet(this, 'TrustedAgentIPs', {
      name: 'TrustedAgentIPSet',
      scope: 'REGIONAL',
      ipAddressVersion: 'IPV4',
      addresses: [
        // Add trusted agent/client CIDR blocks here
        '10.0.0.0/8',
      ],
      description: 'IP addresses of trusted AI agents and internal services',
    });

    const webAcl = new wafv2.CfnWebACL(this, 'GatewayWebACL', {
      name: 'agentcore-gateway-protection',
      scope: 'REGIONAL',
      defaultAction: { allow: {} },
      visibilityConfig: {
        cloudWatchMetricsEnabled: true,
        metricName: 'AgentCoreGatewayWAF',
        sampledRequestsEnabled: true,
      },
      rules: [
        // Rule 1: Rate-based rule — throttle abusive traffic
        {
          name: 'RateLimitPerIP',
          priority: 1,
          action: {
            block: {
              customResponse: {
                responseCode: 429,
                customResponseBodyKey: 'rate-limited',
              },
            },
          },
          statement: {
            rateBasedStatement: {
              limit: 100,
              aggregateKeyType: 'IP',
            },
          },
          visibilityConfig: {
            cloudWatchMetricsEnabled: true,
            metricName: 'RateLimitPerIP',
            sampledRequestsEnabled: true,
          },
        },
        // Rule 2: AWS Managed Rules — Common Rule Set
        {
          name: 'AWSManagedRulesCommonRuleSet',
          priority: 2,
          overrideAction: { none: {} },
          statement: {
            managedRuleGroupStatement: {
              vendorName: 'AWS',
              name: 'AWSManagedRulesCommonRuleSet',
            },
          },
          visibilityConfig: {
            cloudWatchMetricsEnabled: true,
            metricName: 'CommonRuleSet',
            sampledRequestsEnabled: true,
          },
        },
        // Rule 3: AWS Managed Rules — Known Bad Inputs
        {
          name: 'AWSManagedRulesKnownBadInputsRuleSet',
          priority: 3,
          overrideAction: { none: {} },
          statement: {
            managedRuleGroupStatement: {
              vendorName: 'AWS',
              name: 'AWSManagedRulesKnownBadInputsRuleSet',
            },
          },
          visibilityConfig: {
            cloudWatchMetricsEnabled: true,
            metricName: 'KnownBadInputs',
            sampledRequestsEnabled: true,
          },
        },
        // Rule 4: AWS Bot Control — detect and manage bot traffic
        {
          name: 'AWSManagedRulesBotControlRuleSet',
          priority: 4,
          overrideAction: { count: {} },
          statement: {
            managedRuleGroupStatement: {
              vendorName: 'AWS',
              name: 'AWSManagedRulesBotControlRuleSet',
              managedRuleGroupConfigs: [
                {
                  awsManagedRulesBotControlRuleSet: {
                    inspectionLevel: 'COMMON',
                  },
                },
              ],
            },
          },
          visibilityConfig: {
            cloudWatchMetricsEnabled: true,
            metricName: 'BotControl',
            sampledRequestsEnabled: true,
          },
        },
        // Rule 5: Allow trusted agent IPs (higher priority override)
        {
          name: 'AllowTrustedAgentIPs',
          priority: 0,
          action: { allow: {} },
          statement: {
            ipSetReferenceStatement: {
              arn: ipAllowSet.attrArn,
            },
          },
          visibilityConfig: {
            cloudWatchMetricsEnabled: true,
            metricName: 'TrustedAgentIPs',
            sampledRequestsEnabled: true,
          },
        },
      ],
      customResponseBodies: {
        'rate-limited': {
          contentType: 'APPLICATION_JSON',
          content: JSON.stringify({
            error: 'TooManyRequests',
            message: 'Rate limit exceeded. Please retry after a brief delay.',
            retryAfterSeconds: 60,
          }),
        },
      },
    });

    // --- WAF Association with AgentCore Gateway ---
    const webAclAssociation = new wafv2.CfnWebACLAssociation(this, 'WafGatewayAssociation', {
      resourceArn: gateway.getAtt('GatewayArn').toString(),
      webAclArn: webAcl.attrArn,
    });

    // --- WAF Logging Configuration ---
    const loggingConfig = new wafv2.CfnLoggingConfiguration(this, 'WafLogging', {
      resourceArn: webAcl.attrArn,
      logDestinationConfigs: [
        `arn:aws:logs:${region}:${account}:log-group:aws-waf-logs-agentcore-gateway`,
      ],
    });

    loggingConfig.addDependency(wafLogGroup.node.defaultChild as cdk.CfnResource);

    // --- Outputs ---
    new cdk.CfnOutput(this, 'GatewayId', {
      value: gateway.ref,
      description: 'AgentCore Gateway ID',
    });

    new cdk.CfnOutput(this, 'GatewayArn', {
      value: gateway.getAtt('GatewayArn').toString(),
      description: 'AgentCore Gateway ARN',
    });

    new cdk.CfnOutput(this, 'WebACLArn', {
      value: webAcl.attrArn,
      description: 'AWS WAF WebACL ARN protecting the gateway',
    });

    new cdk.CfnOutput(this, 'ToolFunctionArn', {
      value: toolFunction.functionArn,
      description: 'Lambda tool function ARN',
    });

    new cdk.CfnOutput(this, 'WafLogGroupName', {
      value: wafLogGroup.logGroupName,
      description: 'CloudWatch Log Group for AWS WAF logs',
    });
  }
}

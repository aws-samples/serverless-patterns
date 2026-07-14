import * as cdk from "aws-cdk-lib";
import * as apigateway from "aws-cdk-lib/aws-apigateway";
import { Construct } from "constructs";

export class ApigwUsagePlanApiKeyStack extends cdk.Stack {
  public readonly usagePlan: apigateway.UsagePlan;
  public readonly apiKey: apigateway.IApiKey;

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create a Usage Plan (API stage association will be added by the API stack)
    this.usagePlan = new apigateway.UsagePlan(this, "TenantUsagePlan", {
      name: "TenantUsagePlan",
      description: "Usage plan for tenant-based API key throttling",
      throttle: {
        burstLimit: 50,
        rateLimit: 100,
      },
    });

    // Create an API Key
    this.apiKey = new apigateway.ApiKey(this, "TenantApiKey", {
      apiKeyName: "SampleTenantKey",
      description: "Sample API key for tenant usage plan",
      enabled: true,
      value: "tenant-usage-api-key-123",
    });

    // Associate the API Key with the Usage Plan
    this.usagePlan.addApiKey(this.apiKey);

    new cdk.CfnOutput(this, "UsagePlanId", {
      value: this.usagePlan.usagePlanId,
      description: "Usage Plan ID",
    });

    new cdk.CfnOutput(this, "ApiKeyId", {
      value: this.apiKey.keyId,
      description: "API Key ID",
    });
  }
}

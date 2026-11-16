package com.example;

import software.amazon.awscdk.App;
import software.amazon.awscdk.Duration;
import software.amazon.awscdk.RemovalPolicy;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.apigateway.LambdaIntegration;
import software.amazon.awscdk.services.apigateway.RestApi;
import software.amazon.awscdk.services.iam.PolicyStatement;
import software.amazon.awscdk.services.iam.PolicyStatementProps;
import software.amazon.awscdk.services.lambda.Code;
import software.amazon.awscdk.services.lambda.Function;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awscdk.services.logs.LogGroup;
import software.amazon.awscdk.services.logs.RetentionDays;
import software.constructs.Construct;

import java.util.List;
import java.util.Map;

public class InfrastructureStack extends Stack {
    public InfrastructureStack(final App parent, final String id) {
        this(parent, id, null);
    }

    public InfrastructureStack(final Construct parent, final String id, final StackProps props) {
        super(parent, id, props);

        // Claude Haiku 5.5 through the global cross-Region inference profile.
        // Bedrock serves this model on demand only through an inference profile.
        String modelName = "anthropic.claude-haiku-5-5";
        String inferenceProfileArn = "arn:aws:bedrock:" + getRegion() + ":" + getAccount()
                + ":inference-profile/global." + modelName;

        // Allow Lambda to call the inference profile...
        PolicyStatement invokeProfilePolicy = new PolicyStatement(PolicyStatementProps.builder()
                .actions(List.of("bedrock:InvokeModel"))
                .resources(List.of(inferenceProfileArn))
                .build());

        // ...and the model it routes to, only through that profile
        PolicyStatement invokeModelPolicy = new PolicyStatement(PolicyStatementProps.builder()
                .actions(List.of("bedrock:InvokeModel"))
                .resources(List.of(
                        "arn:aws:bedrock:" + getRegion() + "::foundation-model/" + modelName,
                        "arn:aws:bedrock:::foundation-model/" + modelName))
                .conditions(Map.of("StringEquals", Map.of("bedrock:InferenceProfileArn", inferenceProfileArn)))
                .build());

        // Create CloudWatch log group for storing Lambda logs
        LogGroup functionLogGroup = LogGroup.Builder.create(this, "server-log-group")
                .retention(RetentionDays.THREE_DAYS)
                .logGroupName("/aws/lambda/LambdaBedrockFunction")
                .removalPolicy(RemovalPolicy.DESTROY)
                .build();

        // Create a Lambda function
        Function lambdaFunction = Function.Builder.create(this, "LambdaBedrockFunction")
                .runtime(Runtime.JAVA_21)
                .handler("com.example.BedrockClient::handleRequest")
                .code(Code.fromAsset("../software/target/BedrockClient-1.0.jar"))
                .timeout(Duration.seconds(60))
                .environment(Map.of("MODEL_ID", "global." + modelName))
                .initialPolicy(List.of(invokeProfilePolicy, invokeModelPolicy))
                .logGroup(functionLogGroup)
                .build();

        // Create an API Gateway
        RestApi api = RestApi.Builder.create(this, "LambdaBedrockAPI")
                .restApiName("LambdaBedrockAPI")
                .description("The serverless pattern for calling Bedrock using Java SDK")
                .build();

        // Create a Lambda integration and connect it to the root resource
        LambdaIntegration lambdaIntegration = LambdaIntegration.Builder.create(lambdaFunction)
                .build();

        api.getRoot().addMethod("POST", lambdaIntegration);
    }
}

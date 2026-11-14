package com.myorg;

import software.amazon.awscdk.Fn;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.apigateway.CfnDeployment;
import software.amazon.awscdk.services.lambda.Function;
import software.amazon.awscdk.services.lambda.IFunction;
import software.constructs.Construct;

import java.util.Map;

public class CanaryDeploymentStack extends Stack {
    public CanaryDeploymentStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public CanaryDeploymentStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);


        String LAMBDA_ARN=Fn.importValue("MyLambdaFunction");
        String API_ID = Fn.importValue("MyAPIGWID");

        IFunction lambdaFn = Function.fromFunctionArn(this,"lambda_fn",LAMBDA_ARN);
        Object o =CfnDeployment.Builder.create(this,"CanaryDeployment").restApiId(API_ID)
              .deploymentCanarySettings(CfnDeployment.DeploymentCanarySettingsProperty.builder()
                      .percentTraffic(50)
                      .stageVariableOverrides(Map.of("lambdaAlias","Dev")).build()).stageName("prod").build();


    }
}

package com.unicorn;

import software.amazon.awscdk.CfnOutput;
import software.amazon.awscdk.CfnOutputProps;
import software.amazon.awscdk.Duration;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.apigateway.LambdaRestApi;
import software.amazon.awscdk.services.apigateway.RestApi;
import software.amazon.awscdk.services.lambda.Alias;
import software.amazon.awscdk.services.lambda.CfnFunction;
import software.amazon.awscdk.services.lambda.Code;
import software.amazon.awscdk.services.lambda.Function;
import software.amazon.awscdk.services.lambda.IFunction;
import software.amazon.awscdk.services.lambda.Runtime;
import software.constructs.Construct;

import java.util.List;
import java.util.Map;

public class UnicornStoreStack extends Stack {

    private final InfrastructureStack infrastructureStack;

    public UnicornStoreStack(final Construct scope, final String id, final StackProps props,
                             final InfrastructureStack infrastructureStack) {
        super(scope, id, props);

        //Get previously created infrastructure stack
        this.infrastructureStack = infrastructureStack;

        //Create Micronaut Lambda function with SnapStart enabled
        var unicornStoreLambda = createUnicornLambdaFunction();

        //Only Lambda function versions will benefit from SnapStart
        var version = unicornStoreLambda.getCurrentVersion();
        var alias = Alias.Builder.create(this, "UnicornStoreProdAlias")
                .aliasName("Prod")
                .version(version)
                .build();

        //Setup a API Gateway to access the specific version of the Spring Lambda function using an alias
        var restApi = setupRestApi(alias);

        //Create output values for later reference
        new CfnOutput(this, "unicorn-store-function-arn", CfnOutputProps.builder()
                .value(unicornStoreLambda.getFunctionArn())
                .build());

        new CfnOutput(this, "ApiEndpoint", CfnOutputProps.builder()
                .value(restApi.getUrl())
                .build());
    }

    private RestApi setupRestApi(IFunction unicornStoreLambda) {
        return LambdaRestApi.Builder.create(this, "UnicornStoreApi")
                .restApiName("UnicornStoreApi")
                .handler(unicornStoreLambda)
                .build();
    }

    private Function createUnicornLambdaFunction() {
        Function function = Function.Builder.create(this, "UnicornStoreFunction")
                .runtime(Runtime.JAVA_11)
                .functionName("unicorn-store")
                .memorySize(2048)
                .timeout(Duration.seconds(29))
                .code(Code.fromAsset("../../software/unicorn-store/target/store-micronaut-1.0.0.jar"))
                .handler("io.micronaut.function.aws.proxy.MicronautLambdaHandler")
                .vpc(infrastructureStack.getVpc())
                .securityGroups(List.of(infrastructureStack.getApplicationSecurityGroup()))
                .environment(Map.of(
                        "DATASOURCES_DEFAULT_USERNAME", "postgres",
                        "DATASOURCES_DEFAULT_PASSWORD", infrastructureStack.getDatabaseSecretString(),
                        "DATASOURCES_DEFAULT_URL", infrastructureStack.getDatabaseJDBCConnectionString(),
                        "AWS_SERVERLESS_JAVA_CONTAINER_INIT_GRACE_TIME", "500",
                        "JAVA_TOOL_OPTIONS", "-XX:+TieredCompilation -XX:TieredStopAtLevel=1"
                ))
                .build();

        CfnFunction cfnFunction = (CfnFunction) function.getNode().getDefaultChild();
        cfnFunction.setSnapStart(CfnFunction.SnapStartProperty.builder()
                .applyOn("PublishedVersions")
                .build());

        return function;
    }
}

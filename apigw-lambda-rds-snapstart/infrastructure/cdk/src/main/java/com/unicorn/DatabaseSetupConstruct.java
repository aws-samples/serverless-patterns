package com.unicorn;

import software.amazon.awscdk.CfnOutput;
import software.amazon.awscdk.CfnOutputProps;
import software.amazon.awscdk.Duration;
import software.amazon.awscdk.services.lambda.Code;
import software.amazon.awscdk.services.lambda.Function;
import software.amazon.awscdk.services.lambda.Runtime;
import software.constructs.Construct;

import java.util.HashMap;
import java.util.List;

public class DatabaseSetupConstruct extends Construct {

    private final InfrastructureStack infrastructureStack;

    public DatabaseSetupConstruct(final Construct scope, final String id) {
        super(scope, id);

        this.infrastructureStack = (InfrastructureStack) scope;

        var dbSetupLambdaFunction = createDbSetupLambdaFunction();

        new CfnOutput(scope, "DbSetupArn", CfnOutputProps.builder()
                .value(dbSetupLambdaFunction.getFunctionArn())
                .build());
    }

    private Function createDbSetupLambdaFunction() {
        return Function.Builder.create(this, "DBSetupLambdaFunction")
                .runtime(Runtime.JAVA_11)
                .memorySize(512)
                .timeout(Duration.seconds(29))
                .code(Code.fromAsset("../db-setup/target/db-setup.jar"))
                .handler("com.amazon.aws.DBSetupHandler")
                .vpc(infrastructureStack.getVpc())
                .securityGroups(List.of(infrastructureStack.getApplicationSecurityGroup()))
                .environment(new HashMap<>() {{
                    put("DB_PASSWORD", infrastructureStack.getDatabaseSecretString());
                    put("DB_CONNECTION_URL", infrastructureStack.getDatabaseJDBCConnectionString());
                    put("DB_USER", "postgres");
                }})
                .build();
    }

}

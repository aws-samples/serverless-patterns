package com.myorg;

import software.amazon.awscdk.*;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.lambda.eventsources.KinesisEventSource;
import software.amazon.awscdk.services.kinesis.Stream;
import software.amazon.awscdk.services.s3.assets.AssetOptions;
import software.constructs.Construct;

import java.util.Arrays;
import java.util.List;

import static java.util.Collections.singletonList;
import static software.amazon.awscdk.BundlingOutput.ARCHIVED;

public class MyServerlessApplicationStack extends Stack {
    public MyServerlessApplicationStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public MyServerlessApplicationStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        List<String> functionOnePackagingInstructions = Arrays.asList(
                "/bin/sh",
                "-c",
                "cd LambdaFunction " +
                  "&& mvn clean install " +
                  "&& cp /asset-input/LambdaFunction/target/myfunction.jar /asset-output/"
        );


        BundlingOptions.Builder builderOptions = BundlingOptions.builder()
                .command(functionOnePackagingInstructions)
                .image(Runtime.JAVA_11.getBundlingImage())
                .volumes(singletonList(
                        // Mount local .m2 repo to avoid download all the dependencies again inside the container
                        DockerVolume.builder()
                                .hostPath(System.getProperty("user.home") + "/.m2/")
                                .containerPath("/root/.m2/")
                                .build()
                ))
                .user("root")
                .outputType(ARCHIVED);

        Function lambdaFn = Function.Builder.create(this,"KinesisLambda-Function")
                .currentVersionOptions(VersionOptions.builder().removalPolicy(RemovalPolicy.RETAIN).build())
                .runtime(Runtime.JAVA_11)
                .handler("com.example.MyFunction")
                .timeout(Duration.seconds(300))
                .code(Code.fromAsset("software/", AssetOptions.builder()
                        .bundling(builderOptions
                                .command(functionOnePackagingInstructions)
                                .build())

                        .build()))
                .build();
        
        Stream stream = new Stream(this, "KinesisLambda-Stream");

        lambdaFn.addEventSource(KinesisEventSource.Builder.create(stream)
               .batchSize(100) // default
               .startingPosition(StartingPosition.TRIM_HORIZON)
               .build());

        new CfnOutput(this,"LambdaFunction", CfnOutputProps.builder().exportName("MyLambdaFunction").value(lambdaFn.getFunctionArn()).build());
        new CfnOutput(this,"KinesisLambda-KinesisStream", CfnOutputProps.builder().exportName("MyKinesisStream").value(lambdaFn.getFunctionArn()).build());
    }
}

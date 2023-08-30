package com.myorg;

import java.util.Arrays;
import java.util.List;

import software.amazon.awscdk.App;
import software.amazon.awscdk.BundlingOptions;
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awscdk.services.lambda.eventsources.KinesisEventSourceProps;
import software.amazon.awsconstructs.services.kinesisstreamslambda.KinesisStreamsToLambda;
import software.amazon.awsconstructs.services.kinesisstreamslambda.KinesisStreamsToLambdaProps;
import software.constructs.Construct;
import software.amazon.awscdk.DockerVolume;
import software.amazon.awscdk.Duration;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.s3.assets.AssetOptions;

import static java.util.Collections.singletonList;
import static software.amazon.awscdk.BundlingOutput.ARCHIVED;

public class InfrastructureStack extends Stack {
    public InfrastructureStack(final App parent, final String id) {
        this(parent, id, null);
    }

    public InfrastructureStack(final Construct parent, final String id, final StackProps props) {
        super(parent, id, props);

        List<String> kinesisLambdaClientPackagingInstructions = Arrays.asList(
                "/bin/sh",
                "-c",
                "cd KinesisLambdaClient " +
                "&& mvn clean install " +
                "&& cp /asset-input/KinesisLambdaClient/target/KinesisLambdaClient.jar /asset-output/"
        );

        BundlingOptions.Builder builderOptions = BundlingOptions.builder()
                .command(kinesisLambdaClientPackagingInstructions)
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

        new KinesisStreamsToLambda(this, "KinesisToLambdaPattern", new KinesisStreamsToLambdaProps.Builder()
                .kinesisEventSourceProps(new KinesisEventSourceProps.Builder()
                        .startingPosition(StartingPosition.TRIM_HORIZON)
                        .batchSize(3)
                        .maxBatchingWindow(Duration.seconds(20))
                        .maxRecordAge(Duration.seconds(3600))
                        .bisectBatchOnError(true)
                        .retryAttempts(1)
                        .reportBatchItemFailures(true)
                        .build())
                .lambdaFunctionProps(new FunctionProps.Builder()
                        .runtime(Runtime.JAVA_11)
                        .code(Code.fromAsset("../software/", AssetOptions.builder()
                                .bundling(builderOptions
                                        .command(kinesisLambdaClientPackagingInstructions)
                                        .build())
                                .build()))
                        .handler("com.myorg.kinesis.client.App")
                        .memorySize(1024)
                        .functionName("KinesisLambdaClient")
                        .reservedConcurrentExecutions(1)
                        .timeout(Duration.seconds(10))
                        .build())
                .build());
    }
}

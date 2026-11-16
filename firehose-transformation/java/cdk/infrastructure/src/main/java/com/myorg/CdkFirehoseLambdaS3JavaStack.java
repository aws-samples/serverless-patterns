package com.myorg;

import software.amazon.awscdk.*;
import software.amazon.awscdk.services.kinesisfirehose.alpha.DeliveryStream;
import software.amazon.awscdk.services.kinesisfirehose.alpha.LambdaFunctionProcessor;
import software.amazon.awscdk.services.kinesisfirehose.destinations.alpha.S3Bucket;
import software.amazon.awscdk.services.lambda.Code;
import software.amazon.awscdk.services.lambda.Function;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awscdk.services.lambda.RuntimeFamily;
import software.amazon.awscdk.services.s3.Bucket;
import software.amazon.awscdk.services.s3.BucketProps;
import software.amazon.awscdk.services.s3.assets.AssetOptions;
import software.constructs.Construct;

import java.util.Arrays;
import java.util.List;

import static java.util.Collections.singletonList;
import static software.amazon.awscdk.BundlingOutput.ARCHIVED;

public class CdkFirehoseLambdaS3JavaStack extends Stack {

    public CdkFirehoseLambdaS3JavaStack(final App parent, final String id) {
        this(parent, id, null);
    }

    public CdkFirehoseLambdaS3JavaStack(final Construct parent, final String id, final StackProps props) {
        super(parent, id, props);
        // Declared by name because the aws-cdk-lib version that the Firehose alpha modules pull in may predate Runtime.JAVA_25.
        Runtime java25 = new Runtime("java25", RuntimeFamily.JAVA);
        List<String> kinesisLambdaClientPackagingInstructions = Arrays.asList(
                "/bin/sh",
                "-c",
                "cd FirehoseTransformationLambda " +
                        "&& mvn clean install " +
                        "&& cp /asset-input/FirehoseTransformationLambda/target/KinesisLambdaClient.jar /asset-output/"
        );

        BundlingOptions.Builder builderOptions = BundlingOptions.builder()
                .command(kinesisLambdaClientPackagingInstructions)
                .image(java25.getBundlingImage())
                .volumes(singletonList(
                        // Mount local .m2 repo to avoid download all the dependencies again inside the container
                        DockerVolume.builder()
                                .hostPath(System.getProperty("user.home") + "/.m2/")
                                .containerPath("/root/.m2/")
                                .build()
                ))
                .user("root")
                .outputType(ARCHIVED);


        Bucket bucket = new Bucket(this, "firehose-lambda-processor", new BucketProps.Builder()
                .versioned(false)
                .build());

        Function lambdaFunction = Function.Builder.create(this, "fh-lambda-transformer")
                .runtime(java25)
                .code(Code.fromAsset("../software/", AssetOptions.builder()
                        .bundling(builderOptions
                                .command(kinesisLambdaClientPackagingInstructions)
                                .build())
                        .build()))
                .handler("com.myorg.kinesis.client.App")
                .memorySize(1024)
                .functionName("KinesisFHLambdaProcessor")
                .reservedConcurrentExecutions(1)
                .timeout(Duration.seconds(10))
                .build();

        LambdaFunctionProcessor lambdaProcessor = LambdaFunctionProcessor.Builder.create(lambdaFunction)
                .bufferInterval(Duration.minutes(5))
                .bufferSize(Size.mebibytes(3))
                .retries(5)
                .build();

        S3Bucket s3Destination = S3Bucket.Builder.create(bucket)
                .processor(lambdaProcessor)
                .build();
        DeliveryStream.Builder.create(this, "Delivery Stream")
                .destinations(List.of(s3Destination))
                .build();
    }
}

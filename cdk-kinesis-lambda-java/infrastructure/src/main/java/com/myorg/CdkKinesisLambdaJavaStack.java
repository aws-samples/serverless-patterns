package com.myorg;

import software.amazon.awscdk.Duration;
import software.amazon.awscdk.services.lambda.Code;
import software.amazon.awscdk.services.lambda.FunctionProps;
import software.amazon.awscdk.services.lambda.StartingPosition;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awscdk.services.lambda.eventsources.KinesisEventSourceProps;
import software.constructs.Construct;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awsconstructs.services.kinesisstreamslambda.*;

public class CdkKinesisLambdaJavaStack extends Stack {
    public CdkKinesisLambdaJavaStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public CdkKinesisLambdaJavaStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        new KinesisStreamsToLambda(this, "KinesisToLambdaPattern", new KinesisStreamsToLambdaProps.Builder()
                .kinesisEventSourceProps(new KinesisEventSourceProps.Builder()
                        .startingPosition(StartingPosition.TRIM_HORIZON)
                        .batchSize(5)
                        .maxRecordAge(Duration.seconds(60))
                        .bisectBatchOnError(true)
                        .reportBatchItemFailures(true)
                        .build())
                .lambdaFunctionProps(new FunctionProps.Builder()
                        .runtime(Runtime.JAVA_11)
                        .code(Code.fromAsset("../asset"))
                        .handler("com.myorg.lambda.client.KinesisLambdaClient")
                        .build())
                .build());
    }
}

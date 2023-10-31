package org.myorg.example

import software.amazon.awscdk.Duration
import software.amazon.awscdk.RemovalPolicy
import software.amazon.awscdk.Stack
import software.amazon.awscdk.services.dynamodb.Attribute
import software.amazon.awscdk.services.dynamodb.AttributeType
import software.amazon.awscdk.services.dynamodb.StreamViewType
import software.amazon.awscdk.services.dynamodb.Table
import software.amazon.awscdk.services.lambda.Code
import software.amazon.awscdk.services.lambda.Function
import software.amazon.awscdk.services.lambda.Runtime
import software.amazon.awscdk.services.lambda.StartingPosition
import software.amazon.awscdk.services.lambda.eventsources.DynamoEventSource
import software.constructs.Construct

class MyStack(scope: Construct, id: String) : Stack(scope, id) {
    private val myTable: Table = newDynamoDbTable()
    private  val myLambda: Function = newLambda()

    private fun deviceIdKey() =
        Attribute.builder().name("id").type(AttributeType.STRING).build()

    init {
        addDynamoDBStreamToLambda(myLambda, myTable)
    }

    private fun newDynamoDbTable(): Table = Table.Builder
        .create(this, "my-table")
        .tableName("my-table")
        .partitionKey(deviceIdKey())
        .removalPolicy(RemovalPolicy.DESTROY)
        .stream(StreamViewType.NEW_IMAGE)
        .build()

    private fun newLambda(): Function =
        Function.Builder.create(this, "my-lambda")
            .functionName("my-lambda")
            .code(Code.fromAsset("../serverless/build/libs/serverless.jar"))
            .handler("org.myorg.example.MyLambda::handleRequest")
            .timeout(Duration.seconds(50))
            .memorySize(1024)
            .runtime(Runtime.JAVA_8)
            .build()

    private fun addDynamoDBStreamToLambda(function: Function, table: Table) {
        function.addEventSource(
            DynamoEventSource.Builder.create(table)
                .startingPosition(StartingPosition.TRIM_HORIZON)
                .batchSize(5)
                .bisectBatchOnError(true)
                .build()
        )
    }
}

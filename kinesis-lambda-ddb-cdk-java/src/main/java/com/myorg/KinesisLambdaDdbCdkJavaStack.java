package com.myorg;

import software.constructs.Construct;
import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.*;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awscdk.services.lambda.*;
import software.amazon.awscdk.services.lambda.eventsources.KinesisEventSource;
import software.amazon.awscdk.services.kinesis.Stream;
import software.amazon.awscdk.services.iam.*;
import software.amazon.awscdk.services.dynamodb.Table;
import software.amazon.awscdk.services.dynamodb.TableProps;
import software.amazon.awscdk.services.dynamodb.Attribute;
import software.amazon.awscdk.services.dynamodb.AttributeType;
import software.amazon.awscdk.services.lambda.Code;
import software.amazon.awscdk.services.lambda.Function;
import software.amazon.awscdk.services.lambda.Runtime;
import software.amazon.awscdk.services.s3.assets.AssetOptions;
import software.constructs.Construct;

import java.util.Arrays;
import java.util.List;
import java.util.Map;

import static java.util.Collections.singletonList;
import static software.amazon.awscdk.BundlingOutput.ARCHIVED;

public class KinesisLambdaDdbCdkJavaStack extends Stack {
    public KinesisLambdaDdbCdkJavaStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public KinesisLambdaDdbCdkJavaStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        Role lambdaRole = Role.Builder.create(this, "LambdaRole")
        .assumedBy(new ServicePrincipal("lambda.amazonaws.com"))
        .build();

        // Attach a policy to the role to grant DynamoDB access
        lambdaRole.addManagedPolicy(
        ManagedPolicy.fromAwsManagedPolicyName("service-role/AWSLambdaBasicExecutionRole")
        );

        lambdaRole.addManagedPolicy(
        ManagedPolicy.fromAwsManagedPolicyName("AmazonDynamoDBFullAccess")
        );
        
        Function lambdaFn = Function.Builder.create(this, "MyLambda")
        .code(Code.fromAsset("lambda-code"))
        .handler("index.lambda_handler")
        .timeout(Duration.minutes(0.5))
        .runtime(Runtime.PYTHON_3_11)
        .role(lambdaRole)
        .build();

        
        Stream stream = new Stream(this, "KinesisStream");
        
        lambdaFn.addEventSource(KinesisEventSource.Builder.create(stream)
               .batchSize(100) 
               .startingPosition(StartingPosition.TRIM_HORIZON)
               .build());
        
        Table dynamoDBTable = Table.Builder.create(this, "MyDynamoDBTable")
            .tableName("table-name") // Replace with any table name
            .partitionKey(Attribute.builder()
                .name("id")
                .type(AttributeType.STRING)
                .build())
        .build();


        new CfnOutput(this, "DynamoDBTableName", CfnOutputProps.builder().exportName("MyDynamoDBTableName").value(dynamoDBTable.getTableName()).build());
        new CfnOutput(this,"LambdaFunction", CfnOutputProps.builder().exportName("MyLambdaFunction").value(lambdaFn.getFunctionArn()).build());
        new CfnOutput(this,"KinesisLambda-KinesisStream", CfnOutputProps.builder().exportName("MyKinesisStream").value(lambdaFn.getFunctionArn()).build());
        
    }
}

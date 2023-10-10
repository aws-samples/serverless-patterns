package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.example.model.Sensor;
import software.amazon.awssdk.core.SdkSystemSetting;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbEnhancedClient;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbTable;
import software.amazon.awssdk.enhanced.dynamodb.TableSchema;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;

import java.util.UUID;

public class DataProducer implements RequestHandler<Sensor, String> {

    private final DynamoDbClient ddb = DynamoDbClient.builder()
            .region(Region.of(System.getenv(SdkSystemSetting.AWS_REGION.environmentVariable())))
            .build();

    private final DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.builder()
            .dynamoDbClient(ddb)
            .build();
    private final String DDB_TABLE = System.getenv("DDB_TABLE");

    @Override
    public String handleRequest(Sensor sensor, Context context) {
        String sensorId = UUID.randomUUID().toString();
        sensor.setSensorId(sensorId);

        ddbPersist(sensor);

        return sensorId;
    }

    private void ddbPersist(Sensor sensor) {
        DynamoDbTable<Sensor> mappedTable = enhancedClient
                .table(DDB_TABLE, TableSchema.fromBean(Sensor.class));
        mappedTable.putItem(sensor);
    }
}

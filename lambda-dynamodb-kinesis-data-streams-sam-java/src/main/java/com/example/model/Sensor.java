package com.example.model;

import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbBean;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbPartitionKey;

@DynamoDbBean
public class Sensor {
    private String sensorId;
    private String temperature;

    public Sensor() {
    }

    public Sensor(String sensorId, String temperature) {
        this.sensorId = sensorId;
        this.temperature = temperature;
    }

    @DynamoDbPartitionKey
    public String getSensorId() {
        return sensorId;
    }

    public void setSensorId(String sensorId) {
        this.sensorId = sensorId;
    }

    public String getTemperature() {
        return temperature;
    }

    public void setTemperature(String temperature) {
        this.temperature = temperature;
    }
}

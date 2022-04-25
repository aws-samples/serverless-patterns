package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.core.SdkSystemSetting;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.firehose.FirehoseClient;
import software.amazon.awssdk.services.firehose.model.PutRecordRequest;
import software.amazon.awssdk.services.firehose.model.PutRecordResponse;
import software.amazon.awssdk.services.firehose.model.Record;

public class DataProcessor implements RequestHandler {

    private final FirehoseClient firehoseClient = FirehoseClient.builder()
            .region(Region.of(System.getenv(SdkSystemSetting.AWS_REGION.environmentVariable())))
            .build();
    private final String FIREHOSE_NAME = System.getenv("FIREHOSE_NAME");

    @Override
    public Object handleRequest(Object o, Context context) {
        String recordId = sendDataToFirehose();
        return "[record ID] " + recordId;
    }

    private String sendDataToFirehose() {

        String textValue = " Sample Data";
        SdkBytes sdkBytes = SdkBytes.fromByteArray(textValue.getBytes());

        Record record = Record.builder()
                .data(sdkBytes)
                .build();

        PutRecordRequest recordRequest = PutRecordRequest.builder()
                .deliveryStreamName(FIREHOSE_NAME)
                .record(record)
                .build();

        PutRecordResponse recordResponse = firehoseClient.putRecord(recordRequest) ;
        return recordResponse.recordId();
    }
}

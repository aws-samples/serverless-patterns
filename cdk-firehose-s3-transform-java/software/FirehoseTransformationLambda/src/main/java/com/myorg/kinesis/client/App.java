package com.myorg.kinesis.client;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.KinesisFirehoseEvent;
import com.myorg.kinesis.client.model.ResponseRecord;
import com.myorg.kinesis.client.model.TransofrmedRecords;
import org.json.JSONObject;

import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<KinesisFirehoseEvent, TransofrmedRecords> {

    private List<ResponseRecord> responseRecord;
    private TransofrmedRecords transofrmedRecords;

    @Override
    public TransofrmedRecords handleRequest(KinesisFirehoseEvent input, Context context) {
        System.out.println("Firehose Triggered Lambda");
        System.out.println("Firehose Event: " + input);

        transofrmedRecords = new TransofrmedRecords();
        responseRecord = new ArrayList<ResponseRecord>();
        input.getRecords().stream().forEach(
                event -> {
                    String eventData = null;
                    eventData = new String(event.getData().array(), StandardCharsets.UTF_8);
                    System.out.println("Firehose Event Data: " + eventData);
                    JSONObject jsonObject = new JSONObject(eventData);

                    String TICKER_SYMBOL = jsonObject.get("TICKER_SYMBOL").toString();
                    String SECTOR = jsonObject.get("SECTOR").toString();
                    String CHANGE = jsonObject.get("CHANGE").toString();
                    String PRICE = jsonObject.get("PRICE").toString();

                    String prompt = "The Organization with Ticket Symbol " + TICKER_SYMBOL + " in this " + SECTOR + " industry has seen a change of " + CHANGE + " in price to " + PRICE;
                    System.out.println("Event Summary: " + prompt);
                    jsonObject.put("SUMMARY", prompt);

                    System.out.println("Firehose Transformed Data: " + jsonObject);

                    responseRecord.add(new ResponseRecord(event.getRecordId(), "Ok", encode(jsonObject.toString())));

                }
        );

        transofrmedRecords.setRecords(responseRecord);

        return transofrmedRecords;
    }

    private ByteBuffer encode(String content) {
        return ByteBuffer.wrap(content.getBytes());
    }

}
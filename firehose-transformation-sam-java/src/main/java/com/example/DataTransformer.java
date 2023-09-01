package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.KinesisFirehoseEvent;
import com.amazonaws.services.lambda.runtime.events.KinesisFirehoseEvent.Record;

import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.List;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
public class DataTransformer implements RequestHandler<KinesisFirehoseEvent, TransformedRecords> {

    Logger logger = LoggerFactory.getLogger(DataTransformer.class);

    @Override
    public TransformedRecords handleRequest(KinesisFirehoseEvent event, Context context) {
        List<TransformedRecord> transformedRecords = new ArrayList<>();
        TransformedRecords records = new TransformedRecords();
        for(Record rec : event.getRecords()) {
            ByteBuffer data = rec.getData(); // Transform the data as needed
            TransformedRecord transformedRecord = new TransformedRecord(rec.getRecordId(),"Ok", data);
            transformedRecords.add(transformedRecord);
        }
        logger.info("[Records transformed] " + transformedRecords.size());
        records.setRecords(transformedRecords);
        return records;
    }
}


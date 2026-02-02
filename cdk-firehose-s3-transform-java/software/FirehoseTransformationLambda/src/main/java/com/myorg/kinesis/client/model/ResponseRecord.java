package com.myorg.kinesis.client.model;

import java.nio.ByteBuffer;

public class ResponseRecord {
    public ResponseRecord(String recordId, String result, ByteBuffer data) {
        this.setData(data);
        this.setRecordId(recordId);
        this.setResult(result);
    }

    enum Status {
        Ok,
        Dropped,
        ProcessingFailed
    }

    String recordId = "";

    ByteBuffer data;

    String result = "Ok";

    public String getRecordId() {
        return recordId;
    }

    public void setRecordId(String recordId) {
        this.recordId = recordId;
    }

    public ByteBuffer getData() {
        return data;
    }

    public void setData(ByteBuffer data) {
        this.data = data;
    }

    public String getResult() {
        return result;
    }

    public void setResult(String result) {
        this.result = result;
    }

}

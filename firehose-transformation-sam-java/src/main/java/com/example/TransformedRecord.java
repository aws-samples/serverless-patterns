package com.example;

import java.nio.ByteBuffer;

public class TransformedRecord {

    private String recordId;
    private String result;
    private ByteBuffer data;

    public TransformedRecord(String recordId, String result, ByteBuffer data) {
        this.recordId = recordId;
        this.result = result;
        this.data = data;
    }

    public String getRecordId() {
        return recordId;
    }

    public void setRecordId(String recordId) {
        this.recordId = recordId;
    }

    public String getResult() {
        return result;
    }

    public void setResult(String result) {
        this.result = result;
    }

    public ByteBuffer getData() {
        return data;
    }

    public void setData(ByteBuffer data) {
        this.data = data;
    }
}

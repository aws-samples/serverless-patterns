package com.myorg.kinesis.client.model;

import java.util.List;

public class TransofrmedRecords {

    public List<ResponseRecord> getRecords() {
        return records;
    }

    public void setRecords(List<ResponseRecord> records) {
        this.records = records;
    }

    private List<ResponseRecord> records;
}

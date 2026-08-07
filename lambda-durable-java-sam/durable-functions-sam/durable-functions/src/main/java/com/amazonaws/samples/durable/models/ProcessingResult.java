package com.amazonaws.samples.durable.models;

import java.util.Map;

public class ProcessingResult {
    private String executionId;
    private String pattern;
    private String status;
    private Map<String, Object> data;
    private String timestamp;

    public ProcessingResult() {}

    public ProcessingResult(String executionId, String pattern, String status, Map<String, Object> data) {
        this.executionId = executionId;
        this.pattern = pattern;
        this.status = status;
        this.data = data;
        this.timestamp = java.time.Instant.now().toString();
    }

    public String getExecutionId() { return executionId; }
    public void setExecutionId(String executionId) { this.executionId = executionId; }
    public String getPattern() { return pattern; }
    public void setPattern(String pattern) { this.pattern = pattern; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public Map<String, Object> getData() { return data; }
    public void setData(Map<String, Object> data) { this.data = data; }
    public String getTimestamp() { return timestamp; }
    public void setTimestamp(String timestamp) { this.timestamp = timestamp; }
}

package com.example.model;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serializable;

public class Message implements Serializable {

    private static final long serialVersionUID = 1L;

    @JsonProperty("messageId")
    private String messageId = null;
    @JsonProperty("receiptHandle")
    private String receiptHandle = null;
    @JsonProperty("body")
    private String body = null;

    public Message() {
    }

    public Message(String messageId, String receiptHandle, String body) {
        this.messageId = messageId;
        this.receiptHandle = receiptHandle;
        this.body = body;
    }

    public String getMessageId() {
        return messageId;
    }

    public void setMessageId(String messageId) {
        this.messageId = messageId;
    }

    public String getReceiptHandle() {
        return receiptHandle;
    }

    public void setReceiptHandle(String receiptHandle) {
        this.receiptHandle = receiptHandle;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    @Override
    public String toString() {
        return "Message{" +
                "messageId='" + messageId + '\'' +
                ", receiptHandle='" + receiptHandle + '\'' +
                ", body='" + body + '\'' +
                '}';
    }
}

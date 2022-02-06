package com.example.consumer;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serializable;

public class OrderSQSMessage implements Serializable {
    private static final long serialVersionUID = 1L;

    @JsonProperty("Message")
    private String message = null;

    public OrderSQSMessage() {
    }

    public OrderSQSMessage(String message) {
        this.message = message;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}

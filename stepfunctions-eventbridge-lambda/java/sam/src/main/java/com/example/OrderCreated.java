package com.example;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serializable;

public class OrderCreated implements Serializable {

    private static final long serialVersionUID = 1L;

    @JsonProperty("data")
    private String data = null;

    public OrderCreated() {
    }

    public OrderCreated(String data) {
        this.data = data;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
}

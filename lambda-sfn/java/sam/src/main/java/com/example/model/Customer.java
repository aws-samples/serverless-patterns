package com.example.model;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serializable;

public class Customer implements Serializable {
    private static final long serialVersionUID = 1L;

    @JsonProperty("customerId")
    private String customerId = null;

    @JsonProperty("creditCard")
    private String creditCard = null;

    public Customer() {
    }

    public Customer(String customerId, String creditCard) {
        this.customerId = customerId;
        this.creditCard = creditCard;
    }

    public String getCustomerId() {
        return customerId;
    }

    public void setCustomerId(String customerId) {
        this.customerId = customerId;
    }

    public String getCreditCard() {
        return creditCard;
    }

    public void setCreditCard(String creditCard) {
        this.creditCard = creditCard;
    }
}

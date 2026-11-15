package com.example.model;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serializable;

public class OrderCreated implements Serializable {

    private static final long serialVersionUID = 1L;

    @JsonProperty("customer")
    private Customer customer = null;

    public OrderCreated() {
    }

    public OrderCreated(Customer customer) {
        this.customer = customer;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
}

package com.example.publisher.model;

public class PaymentCreated {
    private String customerId;
    private String productId;
    private String amount;

    public PaymentCreated() {
    }

    public PaymentCreated(String customerId, String productId, String amount) {
        this.customerId = customerId;
        this.productId = productId;
        this.amount = amount;
    }

    public String getCustomerId() {
        return customerId;
    }

    public void setCustomerId(String customerId) {
        this.customerId = customerId;
    }

    public String getProductId() {
        return productId;
    }

    public void setProductId(String productId) {
        this.productId = productId;
    }

    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
}

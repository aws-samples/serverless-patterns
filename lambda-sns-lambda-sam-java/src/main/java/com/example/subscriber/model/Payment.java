package com.example.subscriber.model;

public class Payment {
    private String paymentId;
    private String customerId;
    private String productId;
    private String amount;

    public Payment() {
    }

    public Payment(String paymentId, String customerId, String productId, String amount) {
        this.paymentId = paymentId;
        this.customerId = customerId;
        this.productId = productId;
        this.amount = amount;
    }

    public String getPaymentId() {
        return paymentId;
    }

    public void setPaymentId(String paymentId) {
        this.paymentId = paymentId;
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

    @Override
    public String toString() {
        return "Payment{" +
                "paymentId='" + paymentId + '\'' +
                ", customerId='" + customerId + '\'' +
                ", productId='" + productId + '\'' +
                ", amount='" + amount + '\'' +
                '}';
    }
}

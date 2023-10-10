package com.example.request.model;

public class Payload {
    private String message;

    public Payload() {
    }

    public Payload(String message) {
        this.message = message;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    @Override
    public String toString() {
        return "Payload{" +
                "message='" + message + '\'' +
                '}';
    }
}

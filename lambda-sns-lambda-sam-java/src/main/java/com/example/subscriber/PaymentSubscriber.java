package com.example.subscriber;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.SNSEvent;
import com.example.subscriber.model.Payment;
import com.google.gson.Gson;

import java.util.UUID;

public class PaymentSubscriber implements RequestHandler<SNSEvent, String> {

    private final Gson GSON = new Gson();

    @Override
    public String handleRequest(SNSEvent snsEvent, Context context) {

        snsEvent.getRecords()
                        .forEach(record -> {
                            Payment payment = GSON.fromJson(record.getSNS().getMessage(), Payment.class);
                            payment.setPaymentId(UUID.randomUUID().toString());
                            System.out.println(GSON.toJson(payment));
                        });
        return "Done";
    }
}

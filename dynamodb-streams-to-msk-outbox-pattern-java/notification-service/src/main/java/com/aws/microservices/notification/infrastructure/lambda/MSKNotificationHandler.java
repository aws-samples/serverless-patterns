package com.aws.microservices.notification.infrastructure.lambda;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.KafkaEvent;
import lombok.extern.slf4j.Slf4j;
@Slf4j
public class MSKNotificationHandler implements RequestHandler<KafkaEvent, String> {

	@Override
	public String handleRequest(KafkaEvent kafkaEvent, Context context) {
		String response = "200 OK";
		System.out.println("Lambda function is invoked:" +kafkaEvent.getRecords().values().toString());

		//Read Notification event based on order status success or failure process the message.

		return response;
	}
}

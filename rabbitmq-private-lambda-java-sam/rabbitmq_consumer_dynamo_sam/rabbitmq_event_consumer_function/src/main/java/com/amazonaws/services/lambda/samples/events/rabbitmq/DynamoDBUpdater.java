package com.amazonaws.services.lambda.samples.events.rabbitmq;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.Map;

import com.amazonaws.client.builder.AwsClientBuilder.EndpointConfiguration;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.PutItemOutcome;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.events.RabbitMQEvent;
import com.amazonaws.services.lambda.runtime.events.RabbitMQEvent.BasicProperties;

public class DynamoDBUpdater {

	String dynamoDBTableName;
	AmazonDynamoDB client;
	DynamoDB dynamoDB;
	Table dynamoTable;	

	public DynamoDBUpdater(String dynamoDBTableName) {
		super();
		if (null == dynamoDBTableName) {
			this.dynamoDBTableName = "ACTIVEMQ_LAMBDA_DYNAMO_TABLE";
		} else {
			this.dynamoDBTableName = dynamoDBTableName;
		}
		String AWS_SAM_LOCAL = System.getenv("AWS_SAM_LOCAL");
		if (null == AWS_SAM_LOCAL) {
			this.client = AmazonDynamoDBClientBuilder.standard().build();
		} else {
			this.client = AmazonDynamoDBClientBuilder.standard().withEndpointConfiguration(new EndpointConfiguration("http://127.0.0.1:8000", "")).build();
			this.dynamoDBTableName = "ACTIVEMQ_LAMBDA_DYNAMO_TABLE";
		}
		this.dynamoDB = new DynamoDB(client);
		this.dynamoTable = dynamoDB.getTable(this.dynamoDBTableName);
	}
	
	public PutItemOutcome insertIntoDynamoDB(RabbitMQEvent.RabbitMessage thisMessage, Person thisPerson, LambdaLogger logger, long receiveTime, String queueName, String eventSource, String eventSourceARN) {
		BasicProperties thisMessageProperties = thisMessage.getBasicProperties();
		logger.log("Now inserting a row in DynamoDB for messageID = " + thisMessageProperties.getMessageId());
		Item item = new Item();
		item.withPrimaryKey("MessageID", thisMessageProperties.getMessageId());
		item.withString("EventSource", eventSource);
		item.withString("EventSourceARN", eventSourceARN);
		item.withString("Queue", queueName);
		item.withString("Firstname", thisPerson.getFirstname());
		item.withString("Lastname", thisPerson.getLastname());
		item.withString("Company", thisPerson.getCompany());
		item.withString("Street", thisPerson.getStreet());
		item.withString("City", thisPerson.getCity());
		item.withString("County", thisPerson.getCounty());
		item.withString("State", thisPerson.getState());
		item.withString("Zip", thisPerson.getZip());
		item.withString("Cellphone", thisPerson.getCellPhone());
		item.withString("Homephone", thisPerson.getHomePhone());
		item.withString("Email", thisPerson.getEmail());
		item.withString("Website", thisPerson.getWebsite());
		item.withString("CorrelationID", thisMessageProperties.getCorrelationId());
		item.withString("MessageType", thisMessageProperties.getMessageId());
		if (null == thisMessageProperties.getReplyTo()) {
			item.withNull("ReplyTo");
		} else {
			item.withString("ReplyTo", thisMessageProperties.getReplyTo());
		}
		if (null == thisMessageProperties.getType()) {
			item.withNull("Type");
		} else {
			item.withString("Type", thisMessageProperties.getType());
		}
		item.withBoolean("WhetherRedelivered", thisMessage.getRedelivered());
		item.withString("AppID", thisMessageProperties.getAppId());
		item.withInt("BodySize", thisMessageProperties.getBodySize());
		item.withString("ClusterId", thisMessageProperties.getClusterId());
		item.withString("ContentEncoding", thisMessageProperties.getContentEncoding());
		item.withString("ContentType", thisMessageProperties.getContentType());
		item.withInt("DeliveryMode", thisMessageProperties.getDeliveryMode());
		item.withInt("Expiration", thisMessageProperties.getExpiration());
		item.withInt("Priority", thisMessageProperties.getPriority());
		if (null != thisMessageProperties.getReplyTo()) {
			item.withString("ReplyTo", thisMessageProperties.getReplyTo());
		} else {
			item.withNull("ReplyTo");
		}
		item.withString("Timestamp", thisMessageProperties.getTimestamp());
		item.withString("Type", thisMessageProperties.getType());
		item.withString("UserId", thisMessageProperties.getUserId());
		Map<String, Object> thisMessageHeaders = thisMessageProperties.getHeaders();
		thisMessageHeaders.forEach((headerName, headerValue) -> {
			if (headerValue.getClass().getName().equalsIgnoreCase("java.util.LinkedHashMap")) {
				LinkedHashMap<String, Object> headerValueLinkedHashMap = (LinkedHashMap<String, Object>)headerValue;
				ArrayList<Integer> headerValueArrayList = (ArrayList<Integer>)headerValueLinkedHashMap.get("bytes");
				byte[] headerValueByteArray = new byte[headerValueArrayList.size()];
				int i=0;
				for (Integer thisInteger: headerValueArrayList) {
					headerValueByteArray[i] = thisInteger.byteValue();
					i++;
				}
				String headerValueString = new String(headerValueByteArray);
				item.withString(headerName, headerValueString);
			} else {
				item.with(headerName, headerValue);
			}
		});
	    logger.log("Now done inserting a row in DynamoDB for messageID = " + thisMessageProperties.getMessageId());
		return dynamoTable.putItem(item);
	}
}

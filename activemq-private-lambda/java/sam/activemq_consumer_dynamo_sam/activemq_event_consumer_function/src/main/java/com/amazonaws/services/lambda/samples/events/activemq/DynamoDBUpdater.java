package com.amazonaws.services.lambda.samples.events.activemq;

import com.amazonaws.client.builder.AwsClientBuilder.EndpointConfiguration;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.PutItemOutcome;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.events.ActiveMQEvent;

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
		//this.client = AmazonDynamoDBClientBuilder.standard().build();
		this.dynamoDB = new DynamoDB(client);
		this.dynamoTable = dynamoDB.getTable(this.dynamoDBTableName);
	}
	
	public PutItemOutcome insertIntoDynamoDB(ActiveMQEvent.ActiveMQMessage msg, Person thisPerson, LambdaLogger logger, long receiveTime, String eventSource, String eventSourceARN) {
		logger.log("Now inserting a row in DynamoDB for messageID = " + msg.getMessageID());
		Item item = new Item();
		item.withPrimaryKey("MessageID", msg.getMessageID());
		item.withString("EventSource", eventSource);
		item.withString("EventSourceARN", eventSourceARN);
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
		item.withString("CorrelationID", msg.getCorrelationID());
		item.withString("MessageType", msg.getMessageType());
		if (null == msg.getReplyTo()) {
			item.withNull("ReplyTo");
		} else {
			item.withString("ReplyTo", msg.getReplyTo());
		}
		if (null == msg.getType()) {
			item.withNull("Type");
		} else {
			item.withString("Type", msg.getType());
		}
		item.withLong("BrokerInTime", msg.getBrokerInTime());
		item.withLong("BrokerOutTime", msg.getBrokerOutTime());
		item.withInt("DeliveryMode", msg.getDeliveryMode());
		item.withLong("Expiration", msg.getExpiration());
		item.withInt("Priority", msg.getPriority());
		item.withLong("TimeStamp", msg.getTimestamp());
		item.withString("Queue", msg.getDestination().getPhysicalName());
		item.withBoolean("WhetherRedelivered", msg.getRedelivered());
		item.withLong("ReceiveTime", receiveTime);
	    logger.log("Now done inserting a row in DynamoDB for messageID = " + msg.getMessageID());
		return dynamoTable.putItem(item);
	}
	
}

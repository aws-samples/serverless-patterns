package com.amazonaws.services.lambda.samples.events.documentdbstreams;

import com.amazonaws.client.builder.AwsClientBuilder.EndpointConfiguration;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.PutItemOutcome;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.samples.events.documentdbstreams.models.EventEvent;

public class DynamoDBUpdater {

	String dynamoDBTableName;
	AmazonDynamoDB client;
	DynamoDB dynamoDB;
	Table dynamoTable;
	

	public DynamoDBUpdater(String dynamoDBTableName) {
		super();
		if (null == dynamoDBTableName) {
			this.dynamoDBTableName = "SQS_LAMBDA_DYNAMO_TABLE";
		} else {
			this.dynamoDBTableName = dynamoDBTableName;
		}
		String AWS_SAM_LOCAL = System.getenv("AWS_SAM_LOCAL");
		if (null == AWS_SAM_LOCAL) {
			this.client = AmazonDynamoDBClientBuilder.standard().build();
		} else {
			this.client = AmazonDynamoDBClientBuilder.standard().withEndpointConfiguration(new EndpointConfiguration("http://127.0.0.1:8000", "")).build();
			this.dynamoDBTableName = "SQS_LAMBDA_DYNAMO_TABLE";
		}		
		this.dynamoDB = new DynamoDB(client);
		this.dynamoTable = dynamoDB.getTable(this.dynamoDBTableName);
	}
	
	public PutItemOutcome insertIntoDynamoDB(EventEvent eventEvent, String EventSource, String EventSourceARN, LambdaLogger logger) {
		logger.log("Now inserting a row in DynamoDB for messageID = " + eventEvent.getFullDocument().get_id());
		Item item = new Item();
		item.withPrimaryKey("MessageID", eventEvent.getFullDocument().get_id());
		item.withString("EventSource", EventSource);
		item.withString("EventSourceARN", EventSourceARN);
		item.withString("EventIDData", eventEvent.get_id().get_data());
		item.withString("OperationType", eventEvent.getOperationType());
		item.withString("DocumentDBDatabase", eventEvent.getNs().getDb());
		item.withString("DocumentDBCollection", eventEvent.getNs().getColl());
		item.withString("DocumentKeyID", eventEvent.getDocumentKey().get_id());
		item.withLong("ClusterTimeTimeStampT = ", eventEvent.getClusterTime().get$timestamp().getT());
		item.withLong("ClusterTimeTimeStampI = ", eventEvent.getClusterTime().get$timestamp().getI());
		item.withString("CustomerID = ", eventEvent.getFullDocument().get_id());
		item.withString("CustomerFirstname = ", eventEvent.getFullDocument().getFirstname());
		item.withString("CustomerLastname = ", eventEvent.getFullDocument().getLastname());
		item.withString("CustomerStreet = ", eventEvent.getFullDocument().getStreet());
		item.withString("CustomerCity = ", eventEvent.getFullDocument().getCity());
		item.withString("CustomerCounty = ", eventEvent.getFullDocument().getCounty());
		item.withString("CustomerState = ", eventEvent.getFullDocument().getState());
		item.withString("CustomerZip = ", eventEvent.getFullDocument().getZip());
		item.withString("CustomerHomePhone = ", eventEvent.getFullDocument().getHomePhone());
		item.withString("CustomerCellPhone = ", eventEvent.getFullDocument().getCellPhone());
		item.withString("CustomerEmail = ", eventEvent.getFullDocument().getEmail());
		item.withString("CustomerCompany = ", eventEvent.getFullDocument().getCompany());
		item.withString("CustomerWebsite = ", eventEvent.getFullDocument().getWebsite());
	    logger.log("Now done inserting a row in DynamoDB for messageID = " + eventEvent.getFullDocument().get_id());
		return dynamoTable.putItem(item);
	}
}
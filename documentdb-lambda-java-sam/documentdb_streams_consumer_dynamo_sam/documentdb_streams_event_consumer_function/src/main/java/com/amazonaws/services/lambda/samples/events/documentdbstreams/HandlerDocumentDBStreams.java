//Lambda Runtime delivers a batch of messages to the lambda function
//Each batch of messages has two fields EventSource and EventSourceARN
//Each batch of messages also has a field called Records
//The Records is a map with multiple keys and values
//Each key is a combination of the Topic Name and the Partition Number
//One batch of messages can contain messages from multiple partitions

/*
To simplify representing a batch of Kafka messages as a list of messages
We have created a Java class called KafkaMessage under the models package
Here we are mapping the structure of an incoming Kafka event to a list of
objects of the KafkaMessage class
 */

package com.amazonaws.services.lambda.samples.events.documentdbstreams;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestStreamHandler;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.amazonaws.services.lambda.samples.events.documentdbstreams.models.*;


public class HandlerDocumentDBStreams implements RequestStreamHandler{
	Gson gson = new GsonBuilder().setPrettyPrinting().create();
	String dynamoDBTableName = System.getenv("DYNAMO_DB_TABLE");
	DynamoDBUpdater ddbUpdater = new DynamoDBUpdater(dynamoDBTableName);
	boolean addToDynamoDB;
	//ObjectMapper objectMapper = new ObjectMapper();
	@Override
	public void handleRequest(InputStream inputStream, OutputStream outputStream, Context context) throws IOException
	{
		LambdaLogger logger = context.getLogger();
		addToDynamoDB = true;
		logger.log("Begin Event *************");
		try {
			BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
			DocumentDBStreamMessage message = gson.fromJson(reader, DocumentDBStreamMessage.class);
			logger.log("Message = " + message);
			logger.log("EventSource = " + message.getEventSource());
		    logger.log("EventSourceARN = " + message.getEventSourceArn());
		    for (int i=0;i<message.getEvents().length;i++) {
		    	logger.log("Starting a new message **************");
		    	EventElement eventElement = message.getEvents()[i];
		    	EventEvent eventEvent = eventElement.getEvent();
		    	logger.log("EventIDData = " + eventEvent.get_id().get_data());
		    	logger.log("OperationType = " + eventEvent.getOperationType());
		    	logger.log("Database = " + eventEvent.getNs().getDb());
		    	logger.log("Collection = " + eventEvent.getNs().getColl());
		    	logger.log("DocumentKeyID = " + eventEvent.getDocumentKey().get_id());
		    	logger.log("ClusterTimeTimeStampT = " + eventEvent.getClusterTime().get$timestamp().getT());
		    	logger.log("ClusterTimeTimeStampI = " + eventEvent.getClusterTime().get$timestamp().getI());
		    	logger.log("CustomerID = " + eventEvent.getFullDocument().get_id());
		    	logger.log("CustomerFirstname = " + eventEvent.getFullDocument().getFirstname());
		    	logger.log("CustomerLastname = " + eventEvent.getFullDocument().getLastname());
		    	logger.log("CustomerStreet = " + eventEvent.getFullDocument().getStreet());
		    	logger.log("CustomerCity = " + eventEvent.getFullDocument().getCity());
		    	logger.log("CustomerCounty = " + eventEvent.getFullDocument().getCounty());
		    	logger.log("CustomerState = " + eventEvent.getFullDocument().getState());
		    	logger.log("CustomerZip = " + eventEvent.getFullDocument().getZip());
		    	logger.log("CustomerHomePhone = " + eventEvent.getFullDocument().getHomePhone());
		    	logger.log("CustomerCellPhone = " + eventEvent.getFullDocument().getCellPhone());
		    	logger.log("CustomerEmail = " + eventEvent.getFullDocument().getEmail());
		    	logger.log("CustomerCompany = " + eventEvent.getFullDocument().getCompany());
		    	logger.log("CustomerWebsite = " + eventEvent.getFullDocument().getWebsite());
		    	logger.log("Finishing a new message **************");
		    	String AWS_SAM_LOCAL = System.getenv("AWS_SAM_LOCAL");
				if ((null == AWS_SAM_LOCAL) && (addToDynamoDB)) {
					ddbUpdater.insertIntoDynamoDB(eventEvent, message.getEventSource(), message.getEventSourceArn(), logger);
				}
		    }
		} catch (Exception e1) {
			logger.log(e1.getMessage());
		}
		logger.log("End Event ***************");
		
	}
	
	public void throwit(String message) throws Exception{
		throw new Exception(message);
	}

}

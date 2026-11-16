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

package com.amazonaws.services.lambda.samples.events.activemq;

import java.util.Base64;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.ActiveMQEvent;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

// Handler value: example.HandlerSQS
public class HandlerActiveMQ implements RequestHandler<ActiveMQEvent, String>{
	String dynamoDBTableName = System.getenv("DYNAMO_DB_TABLE");
	DynamoDBUpdater ddbUpdater = new DynamoDBUpdater(dynamoDBTableName);
	boolean addToDynamoDB;
	ObjectMapper objectMapper = new ObjectMapper();
	@Override
	public String handleRequest(ActiveMQEvent event, Context context)
	{
		LambdaLogger logger = context.getLogger();
		logger.log("Begin Event *************");
		try {
			logger.log(objectMapper.writeValueAsString(event));
		} catch (JsonProcessingException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		logger.log("End Event ***************");
		for(ActiveMQEvent.ActiveMQMessage msg : event.getMessages()){
			try {
				addToDynamoDB = true;
				long currentTime = System.currentTimeMillis();
				logger.log("Begin Message *************");
				logger.log(objectMapper.writeValueAsString(msg));
				logger.log("End Message ***************");
				logger.log("Begin Message Body *************");
				String base64EncodedData = msg.getData();
				String decodedData = "";
				if (null != base64EncodedData) {
					byte[] decodedDataBytes = Base64.getDecoder().decode(base64EncodedData);
					decodedData = new String(decodedDataBytes);
				} 
				logger.log(decodedData);
				logger.log("End Message Body ***************");
				logger.log("EventSource = " + event.getEventSource());
				logger.log("EventSourceARN = " + event.getEventSourceArn());
				logger.log("CorrelationID = " + msg.getCorrelationID());
				logger.log("MessageID = " + msg.getMessageID());
				logger.log("MessageType = " + msg.getMessageType());
				logger.log("ReplyTo = " + msg.getReplyTo());
				logger.log("Type = " + msg.getType());
				logger.log("BrokerInTime = " + msg.getBrokerInTime());
				logger.log("BrokerOutTime = " + msg.getBrokerOutTime());
				logger.log("DeliveryMode = " + msg.getDeliveryMode());
				logger.log("Expiration = " + msg.getExpiration());
				logger.log("Priority = " + msg.getPriority());
				logger.log("TimeStamp = " + msg.getTimestamp());
				logger.log("Queue = " + msg.getDestination().getPhysicalName());
				logger.log("WhetherRedelivered = " + msg.getRedelivered());
				Person thisPerson = objectMapper.readValue(decodedData, Person.class);
				//Person thisPerson = gson.fromJson(decodedData, Person.class);
				logger.log("This person = " + thisPerson.toJson());
				String AWS_SAM_LOCAL = System.getenv("AWS_SAM_LOCAL");
				if ((null == AWS_SAM_LOCAL) && (addToDynamoDB)) {
					ddbUpdater.insertIntoDynamoDB(msg, thisPerson, logger, currentTime, event.getEventSource(), event.getEventSourceArn());
				}
			} catch (Exception e) {
				logger.log("An exception happened - " + e.getMessage());
				return "500";
			}
		}
		return "200";
	}
}

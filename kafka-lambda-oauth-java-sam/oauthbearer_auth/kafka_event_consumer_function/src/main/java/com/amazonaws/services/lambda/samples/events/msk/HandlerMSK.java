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

package com.amazonaws.services.lambda.samples.events.msk;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.KafkaEvent;
import com.amazonaws.services.lambda.runtime.events.KafkaEvent.KafkaEventRecord;

import java.net.URI;
import java.util.ArrayList;
import java.util.Base64;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;

import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import software.amazon.awssdk.services.dynamodb.model.PutItemRequest;

public class HandlerMSK implements RequestHandler<KafkaEvent, String>{
	//We initialize an empty list of the KafkaMessage class
	List<KafkaMessage> listOfMessages = new ArrayList<KafkaMessage>();
	Gson gson = new GsonBuilder().setPrettyPrinting().create();
	// The DynamoDB table to persist messages to is supplied via an environment
	// variable. When it is not set (e.g. local unit tests) DynamoDB is skipped.
	private static final String TABLE_NAME = System.getenv("DYNAMODB_TABLE_NAME");
	private static DynamoDbClient ddbClient;
	// `sam local invoke` sets AWS_SAM_LOCAL=true. Local runs write to DynamoDB Local
	// (started by scripts/local_dynamodb.sh) so they never touch the real table.
	private static final String LOCAL_DYNAMODB_ENDPOINT = "http://dynamodb-local:8000";

	private static synchronized DynamoDbClient ddb() {
		if (ddbClient == null) {
			if ("true".equals(System.getenv("AWS_SAM_LOCAL"))) {
				ddbClient = DynamoDbClient.builder().endpointOverride(URI.create(LOCAL_DYNAMODB_ENDPOINT)).build();
			} else {
				ddbClient = DynamoDbClient.create();
			}
		}
		return ddbClient;
	}
	@Override
	public String handleRequest(KafkaEvent event, Context context) {
		LambdaLogger logger = context.getLogger();
		String response = new String("200 OK");
		this.listOfMessages = new ArrayList<KafkaMessage>();
		//Incoming KafkaEvent object has a property called records that is a map
		//Each key in the map is a combination of a topic and a partition
		Map<String, List<KafkaEventRecord>> record=event.getRecords();
		Set<String> keySet = record.keySet();  
		Iterator<String> iterator = keySet.iterator();
		//We iterate through each of the keys in the map
		while (iterator.hasNext()) {
			String thisKey=(String)iterator.next();
			//Using the key we retrieve the value of the map which is a list of KafkaEventRecord
	    	//One object of KafkaEventRecord represents an individual Kafka message
			List<KafkaEventRecord>  thisListOfRecords = record.get(thisKey);
			//We now iterate through the list of KafkaEventRecords
			for(KafkaEventRecord thisRecord : thisListOfRecords) {
				/*
	    		We initialize a new object of the KafkaMessage class which is a simplified representation in our models package
	    		We then get the fields from each kafka message in the object of KafkaEventRecord class and set them to the fields
	    		of the KafkaRecord class
	    		*/
				KafkaMessage thisMessage = new KafkaMessage();
				thisMessage.setTopic(thisRecord.getTopic());
				thisMessage.setPartition(thisRecord.getPartition());
				thisMessage.setOffset(thisRecord.getOffset());
				thisMessage.setTimestamp(thisRecord.getTimestamp());
				thisMessage.setTimestampType(thisRecord.getTimestampType());
				String key = thisRecord.getKey();
				String value = thisRecord.getValue();
				String decodedKey = "null";
				String decodedValue = "null";
				//the key and value inside a kafka message are base64 encrypted and will need to be decrypted
				if (null != key) {
					byte[] decodedKeyBytes = Base64.getDecoder().decode(key);
					decodedKey = new String(decodedKeyBytes);
				} 
				if (null != value) {
					byte[] decodedValueBytes = Base64.getDecoder().decode(value);
					decodedValue = new String(decodedValueBytes);
				} 
				thisMessage.setKey(key);
	    		thisMessage.setValue(value);
	    		thisMessage.setDecodedKey(decodedKey);
	    		thisMessage.setDecodedValue(decodedValue);
	    		//A kafka message can optionally have a list of headers
	    		//the below code is to get the headers, iterate through each header and get its key and value
				List<KafkaHeader> headersInThisMessage = new ArrayList<KafkaHeader>();
				List<Map<String, byte[]>> headers = thisRecord.getHeaders();
				for (Map<String, byte[]> thisHeader : headers) {
					Set<String> thisHeaderKeys = thisHeader.keySet();
					Iterator<String> thisHeaderKeysIterator = thisHeaderKeys.iterator();
					while (thisHeaderKeysIterator.hasNext()) {
						String thisHeaderKey = thisHeaderKeysIterator.next();
						byte[] thisHeaderValue = (byte[])thisHeader.get(thisHeaderKey);
						String thisHeaderValueString = new String(thisHeaderValue);
						KafkaHeader thisMessageHeader = new KafkaHeader();
						thisMessageHeader.setKey(thisHeaderKey);
						thisMessageHeader.setValue(thisHeaderValueString);
						headersInThisMessage.add(thisMessageHeader);
					}
				}
				thisMessage.setHeaders(headersInThisMessage);
				listOfMessages.add(thisMessage);
				// Below we are logging the particular kafka message in string format using the toString method
	            // as well as in Json format using gson.toJson function
				logger.log("Received this message from Kafka - " + thisMessage.toString());
				logger.log("Message in JSON format : " + gson.toJson(thisMessage));
				// Persist the Kafka metadata and the parsed JSON payload fields to DynamoDB
				writeToDynamoDb(thisMessage, logger);
			}
		}
		logger.log("All Messages in this batch = " + gson.toJson(listOfMessages));
		return response;
	}

	/*
	 * Writes one Kafka message to DynamoDB: the Kafka metadata (topic, partition,
	 * offset, timestamp, timestampType, key) plus every top-level field of the
	 * decoded JSON payload (firstName, lastName, email, ...). The item is keyed by
	 * topicPartition (partition key) + offset (sort key). Skipped when the
	 * DYNAMODB_TABLE_NAME environment variable is not set.
	 */
	private void writeToDynamoDb(KafkaMessage message, LambdaLogger logger) {
		if (null == TABLE_NAME || TABLE_NAME.isEmpty()) {
			return;
		}
		try {
			Map<String, AttributeValue> item = new HashMap<String, AttributeValue>();
			// Kafka metadata
			item.put("topicPartition", AttributeValue.fromS(message.getTopic() + "-" + message.getPartition()));
			item.put("offset", AttributeValue.fromN(Long.toString(message.getOffset())));
			item.put("topic", AttributeValue.fromS(message.getTopic()));
			item.put("partition", AttributeValue.fromN(Integer.toString(message.getPartition())));
			item.put("timestamp", AttributeValue.fromN(Long.toString(message.getTimestamp())));
			if (null != message.getTimestampType()) {
				item.put("timestampType", AttributeValue.fromS(message.getTimestampType()));
			}
			if (null != message.getDecodedKey()) {
				item.put("key", AttributeValue.fromS(message.getDecodedKey()));
			}
			if (null != message.getDecodedValue()) {
				item.put("value", AttributeValue.fromS(message.getDecodedValue()));
			}
			// Parse the decoded value as JSON and store each top-level field as its own attribute
			try {
				JsonElement parsed = JsonParser.parseString(message.getDecodedValue());
				if (parsed.isJsonObject()) {
					for (Map.Entry<String, JsonElement> field : parsed.getAsJsonObject().entrySet()) {
						if (field.getValue().isJsonPrimitive()) {
							item.put(field.getKey(), AttributeValue.fromS(field.getValue().getAsString()));
						}
					}
				}
			} catch (RuntimeException jsonEx) {
				// Not a JSON payload - the raw value is already stored under "value"
			}
			ddb().putItem(PutItemRequest.builder().tableName(TABLE_NAME).item(item).build());
			logger.log("Wrote message to DynamoDB table " + TABLE_NAME
					+ " (topicPartition=" + message.getTopic() + "-" + message.getPartition()
					+ ", offset=" + message.getOffset() + ")");
		} catch (Exception e) {
			logger.log("ERROR writing to DynamoDB table " + TABLE_NAME + ": " + e.getMessage());
			throw e;
		}
	}
}

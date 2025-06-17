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

import java.util.ArrayList;
import java.util.Base64;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class HandlerMSK implements RequestHandler<KafkaEvent, String>{
	//We initialize an empty list of the KafkaMessage class
	List<KafkaMessage> listOfMessages = new ArrayList<KafkaMessage>();
	Gson gson = new GsonBuilder().setPrettyPrinting().create();
	@Override
	public String handleRequest(KafkaEvent event, Context context) {
		LambdaLogger logger = context.getLogger();
		logger.log("========== LAMBDA FUNCTION STARTED ==========");
		logger.log("Event received: " + gson.toJson(event));
		
		String response = new String("200 OK");
		this.listOfMessages = new ArrayList<KafkaMessage>();
		//Incoming KafkaEvent object has a property called records that is a map
		//Each key in the map is a combination of a topic and a partition
		Map<String, List<KafkaEventRecord>> record=event.getRecords();
		
		if (record == null) {
		    logger.log("WARNING: Event records map is null");
		    return response;
		}
		
		logger.log("Records map size: " + record.size());
		
		Set<String> keySet = record.keySet();
		logger.log("Key set size: " + keySet.size());
		logger.log("Keys: " + keySet);
		  
		Iterator<String> iterator = keySet.iterator();
		//We iterate through each of the keys in the map
		while (iterator.hasNext()) {
			String thisKey=(String)iterator.next();
			logger.log("Processing key: " + thisKey);
			
			//Using the key we retrieve the value of the map which is a list of KafkaEventRecord
	    	//One object of KafkaEventRecord represents an individual Kafka message
			List<KafkaEventRecord>  thisListOfRecords = record.get(thisKey);
			
			if (thisListOfRecords == null) {
			    logger.log("WARNING: Record list for key " + thisKey + " is null");
			    continue;
			}
			
			logger.log("Record list size for key " + thisKey + ": " + thisListOfRecords.size());
			
			//We now iterate through the list of KafkaEventRecords
			for(KafkaEventRecord thisRecord : thisListOfRecords) {
				logger.log("Processing record...");
				
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
				
				logger.log("Record metadata - Topic: " + thisRecord.getTopic() + 
				           ", Partition: " + thisRecord.getPartition() + 
				           ", Offset: " + thisRecord.getOffset());
				
				String key = thisRecord.getKey();
				String value = thisRecord.getValue();
				
				logger.log("Key (base64): " + key);
				logger.log("Value (base64): " + value);
				
				String decodedKey = "null";
				String decodedValue = "null";
				//the key and value inside a kafka message are base64 encrypted and will need to be decrypted
				if (null != key) {
					logger.log("Decoding key...");
					try {
					    byte[] decodedKeyBytes = Base64.getDecoder().decode(key);
					    decodedKey = new String(decodedKeyBytes);
					    logger.log("Decoded key: " + decodedKey);
					} catch (Exception e) {
					    logger.log("ERROR decoding key: " + e.getMessage());
					}
				} else {
				    logger.log("Key is null");
				}
				
				if (null != value) {
					logger.log("Decoding value...");
					try {
					    byte[] decodedValueBytes = Base64.getDecoder().decode(value);
					    logger.log("Value decoded, length: " + decodedValueBytes.length + " bytes");
					    
					    // Print the complete message in hex format
					    logger.log("Complete message in hex format:");
					    logger.log(bytesToHexString(decodedValueBytes, 0));
					    
					    try {
					        decodedValue = new String(decodedValueBytes);
					        logger.log("Decoded value as string: " + (decodedValue.length() > 100 ? decodedValue.substring(0, 100) + "..." : decodedValue));
					    } catch (Exception e) {
					        logger.log("ERROR converting bytes to string: " + e.getMessage());
					        decodedValue = "Error decoding: " + e.getMessage();
					    }
					} catch (Exception e) {
					    logger.log("ERROR decoding value: " + e.getMessage());
					    e.printStackTrace();
					}
				} else {
				    logger.log("Value is null");
				}
				
				thisMessage.setKey(key);
	    		thisMessage.setValue(value);
	    		thisMessage.setDecodedKey(decodedKey);
	    		thisMessage.setDecodedValue(decodedValue);
	    		
	    		//A kafka message can optionally have a list of headers
	    		//the below code is to get the headers, iterate through each header and get its key and value
				List<KafkaHeader> headersInThisMessage = new ArrayList<KafkaHeader>();
				List<Map<String, byte[]>> headers = thisRecord.getHeaders();
				
				if (headers != null) {
				    logger.log("Headers count: " + headers.size());
				    
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
						    logger.log("Header - Key: " + thisHeaderKey + ", Value: " + thisHeaderValueString);
					    }
				    }
				} else {
				    logger.log("No headers in message");
				}
				
				thisMessage.setHeaders(headersInThisMessage);
				listOfMessages.add(thisMessage);
				
				// Below we are logging the particular kafka message in string format using the toString method
	            // as well as in Json format using gson.toJson function
				logger.log("Received this message from Kafka - " + thisMessage.toString());
				logger.log("Message in JSON format : " + gson.toJson(thisMessage));
			}
		}
		logger.log("All Messages in this batch = " + gson.toJson(listOfMessages));
		logger.log("========== LAMBDA FUNCTION COMPLETED ==========");
		return response;
	}
	
	/**
     * Convert byte array to hexadecimal string representation
     * 
     * @param bytes Byte array to convert
     * @param maxLength Maximum number of bytes to convert (0 for all)
     * @return Hexadecimal string representation
     */
    private String bytesToHexString(byte[] bytes, int maxLength) {
        StringBuilder sb = new StringBuilder();
        int length = maxLength > 0 && maxLength < bytes.length ? maxLength : bytes.length;
        
        for (int i = 0; i < length; i++) {
            sb.append(String.format("%02X", bytes[i]));
            if (i % 16 == 15) {
                sb.append("\n");
            } else if (i % 4 == 3) {
                sb.append(" ");
            }
        }
        
        if (maxLength > 0 && length < bytes.length) {
            sb.append("... (").append(bytes.length - length).append(" more bytes)");
        }
        
        return sb.toString();
    }
}

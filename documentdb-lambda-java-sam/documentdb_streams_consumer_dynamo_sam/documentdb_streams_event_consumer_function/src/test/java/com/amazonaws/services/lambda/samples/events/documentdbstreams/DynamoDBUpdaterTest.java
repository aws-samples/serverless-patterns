package com.amazonaws.services.lambda.samples.events.documentdbstreams;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;
import java.io.InputStream;
import org.junit.jupiter.api.Test;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.PutItemOutcome;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.samples.events.documentdbstreams.models.DocumentDBStreamMessage;
import com.amazonaws.services.lambda.samples.events.documentdbstreams.models.EventElement;
import com.amazonaws.services.lambda.samples.events.documentdbstreams.models.EventEvent;
import com.google.gson.Gson;
import org.mockito.ArgumentMatchers;

class DynamoDBUpdaterTest {

	@Test
	void testDynamoDBUpdater() {
		DynamoDBUpdater ddbUpdater = new DynamoDBUpdater("DBTable");
		assertNotNull(ddbUpdater);
		assertEquals(ddbUpdater.dynamoDBTableName, "DBTable");
		assertNotNull(ddbUpdater.client);
		assertNotNull(ddbUpdater.dynamoDB);
		assertNotNull(ddbUpdater.dynamoTable);
	}

	@Test
	void testInsertIntoDynamoDB() {
		try {
			InputStream fis = DynamoDBUpdaterTest.class.getClassLoader().getResourceAsStream("event.json");
			byte[] byteArray = fis.readAllBytes();
			fis.close();
			String eventJson = new String(byteArray);
			Gson gson = new Gson();
			DocumentDBStreamMessage message = gson.fromJson(eventJson, DocumentDBStreamMessage.class);
			String eventSource = message.getEventSource();
			String eventSourceARN = message.getEventSourceArn();
			for (int i=0;i<message.getEvents().length;i++) {
		    	EventElement eventElement = message.getEvents()[i];
		    	EventEvent eventEvent = eventElement.getEvent();
		    	Table dynamoDbTable = mock(Table.class);
			    AmazonDynamoDB client = mock(AmazonDynamoDB.class);
				DynamoDB dynamoDB = mock(DynamoDB.class);
			    PutItemOutcome putoutcome = mock(PutItemOutcome.class);
			    LambdaLogger logger = mock(LambdaLogger.class);
			    DynamoDBUpdater ddbUpdater = new DynamoDBUpdater("DBTable");
			    ddbUpdater.client = client;
			    ddbUpdater.dynamoDB = dynamoDB;
			    ddbUpdater.dynamoTable = dynamoDbTable;
			    when(ddbUpdater.dynamoTable.putItem(ArgumentMatchers.any(Item.class))).thenReturn(putoutcome);
				PutItemOutcome putOutcome = ddbUpdater.insertIntoDynamoDB(eventEvent, eventSource, eventSourceARN, logger);
				assertNotNull(putOutcome);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	    
	}
}

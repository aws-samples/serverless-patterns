package com.amazonaws.services.lambda.samples.events.activemq;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import java.util.Base64;

import org.junit.jupiter.api.Test;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.PutItemOutcome;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.events.ActiveMQEvent;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.mockito.ArgumentMatchers;

class DynamoDBUpdaterTest {
	
	private static final String mqEventJson = "{\n"
			+ "    \"eventSource\": \"aws:mq\",\n"
			+ "    \"eventSourceArn\": \"arn:aws:mq:us-west-2:664251831272:broker:ib-activemq-broker:b-aeb08c0d-6e46-412a-ad45-1507816242b0\",\n"
			+ "    \"messages\": [\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:51\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148495,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-51\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": true,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJMb3JyaWUiLCJsYXN0bmFtZSI6Ik5lc3RsZSIsImNvbXBhbnkiOiJCYWxsYXJkIFNwYWhyIEFuZHJld3MiLCJzdHJlZXQiOiIzOSBTIDd0aCBTdCIsImNpdHkiOiJUdWxsYWhvbWEiLCJjb3VudHkiOiJDb2ZmZWUiLCJzdGF0ZSI6IlROIiwiemlwIjoiMzczODgiLCJob21lUGhvbmUiOiI5MzEtODc1LTY2NDQiLCJjZWxsUGhvbmUiOiI5MzEtMzAzLTYwNDEiLCJlbWFpbCI6ImxuZXN0bGVAaG90bWFpbC5jb20iLCJ3ZWJzaXRlIjoiaHR0cDovL3d3dy5iYWxsYXJkc3BhaHJhbmRyZXdzLmNvbSJ9\",\n"
			+ "            \"brokerInTime\": 1687328148496,\n"
			+ "            \"brokerOutTime\": 1687328529311\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:85\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148547,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-85\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": true,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJNeXJhIiwibGFzdG5hbWUiOiJNdW5ucyIsImNvbXBhbnkiOiJBbmtlciBMYXcgT2ZmaWNlIiwic3RyZWV0IjoiNDYxIFByb3NwZWN0IFBsICMzMTYiLCJjaXR5IjoiRXVsZXNzIiwiY291bnR5IjoiVGFycmFudCIsInN0YXRlIjoiVFgiLCJ6aXAiOiI3NjA0MCIsImhvbWVQaG9uZSI6IjgxNy05MTQtNzUxOCIsImNlbGxQaG9uZSI6IjgxNy00NTEtMzUxOCIsImVtYWlsIjoibW11bm5zQGNveC5uZXQiLCJ3ZWJzaXRlIjoiaHR0cDovL3d3dy5hbmtlcmxhd29mZmljZS5jb20ifQ==\",\n"
			+ "            \"brokerInTime\": 1687328148547,\n"
			+ "            \"brokerOutTime\": 1687328529546\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:87\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148552,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-87\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": true,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJMYWkiLCJsYXN0bmFtZSI6IkdhdG8iLCJjb21wYW55IjoiXCJGbGlnZywgS2VubmV0aCBJIEpyXCIiLCJzdHJlZXQiOiIzNyBBbGFiYW1hIEF2ZSIsImNpdHkiOiJFdmFuc3RvbiIsImNvdW50eSI6IkNvb2siLCJzdGF0ZSI6IklMIiwiemlwIjoiNjAyMDEiLCJob21lUGhvbmUiOiI4NDctNzI4LTcyODYiLCJjZWxsUGhvbmUiOiI4NDctOTU3LTQ2MTQiLCJlbWFpbCI6ImxhaS5nYXRvQGdhdG8ub3JnIiwid2Vic2l0ZSI6Imh0dHA6Ly93d3cuZmxpZ2drZW5uZXRoaWpyLmNvbSJ9\",\n"
			+ "            \"brokerInTime\": 1687328148552,\n"
			+ "            \"brokerOutTime\": 1687328529548\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:3\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148391,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-3\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": true,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJMZW5uYSIsImxhc3RuYW1lIjoiUGFwcm9ja2kiLCJjb21wYW55IjoiRmVsdHogUHJpbnRpbmcgU2VydmljZSIsInN0cmVldCI6IjYzOSBNYWluIFN0IiwiY2l0eSI6IkFuY2hvcmFnZSIsImNvdW50eSI6IkFuY2hvcmFnZSIsInN0YXRlIjoiQUsiLCJ6aXAiOiI5OTUwMSIsImhvbWVQaG9uZSI6IjkwNy0zODUtNDQxMiIsImNlbGxQaG9uZSI6IjkwNy05MjEtMjAxMCIsImVtYWlsIjoibHBhcHJvY2tpQGhvdG1haWwuY29tIiwid2Vic2l0ZSI6Imh0dHA6Ly93d3cuZmVsdHpwcmludGluZ3NlcnZpY2UuY29tIn0=\",\n"
			+ "            \"brokerInTime\": 1687328148392,\n"
			+ "            \"brokerOutTime\": 1687328529551\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:19\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148434,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-19\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": true,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJGbGV0Y2hlciIsImxhc3RuYW1lIjoiRmxvc2kiLCJjb21wYW55IjoiUG9zdCBCb3ggU2VydmljZXMgUGx1cyIsInN0cmVldCI6IjM5NCBNYW5jaGVzdGVyIEJsdmQiLCJjaXR5IjoiUm9ja2ZvcmQiLCJjb3VudHkiOiJXaW5uZWJhZ28iLCJzdGF0ZSI6IklMIiwiemlwIjoiNjExMDkiLCJob21lUGhvbmUiOiI4MTUtODI4LTIxNDciLCJjZWxsUGhvbmUiOiI4MTUtNDI2LTU2NTciLCJlbWFpbCI6ImZsZXRjaGVyLmZsb3NpQHlhaG9vLmNvbSIsIndlYnNpdGUiOiJodHRwOi8vd3d3LnBvc3Rib3hzZXJ2aWNlc3BsdXMuY29tIn0=\",\n"
			+ "            \"brokerInTime\": 1687328148435,\n"
			+ "            \"brokerOutTime\": 1687328529565\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:54\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148504,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-54\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": true,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJLYXJsIiwibGFzdG5hbWUiOiJLbG9ub3dza2kiLCJjb21wYW55IjoiXCJSb3NzaSwgTWljaGFlbCBNXCIiLCJzdHJlZXQiOiI3NiBCcm9va3MgU3QgIzkiLCJjaXR5IjoiRmxlbWluZ3RvbiIsImNvdW50eSI6Ikh1bnRlcmRvbiIsInN0YXRlIjoiTkoiLCJ6aXAiOiI4ODIyIiwiaG9tZVBob25lIjoiOTA4LTg3Ny02MTM1IiwiY2VsbFBob25lIjoiOTA4LTQ3MC00NjYxIiwiZW1haWwiOiJrYXJsX2tsb25vd3NraUB5YWhvby5jb20iLCJ3ZWJzaXRlIjoiaHR0cDovL3d3dy5yb3NzaW1pY2hhZWxtLmNvbSJ9\",\n"
			+ "            \"brokerInTime\": 1687328148505,\n"
			+ "            \"brokerOutTime\": 1687328529568\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:49\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148492,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-49\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": true,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJCbGFpciIsImxhc3RuYW1lIjoiTWFsZXQiLCJjb21wYW55IjoiQm9sbGluZ2VyIE1hY2ggU2hwIFx1MDAyNiBTaGlweWFyZCIsInN0cmVldCI6IjIwOSBEZWNrZXIgRHIiLCJjaXR5IjoiUGhpbGFkZWxwaGlhIiwiY291bnR5IjoiUGhpbGFkZWxwaGlhIiwic3RhdGUiOiJQQSIsInppcCI6IjE5MTMyIiwiaG9tZVBob25lIjoiMjE1LTkwNy05MTExIiwiY2VsbFBob25lIjoiMjE1LTc5NC00NTE5IiwiZW1haWwiOiJibWFsZXRAeWFob28uY29tIiwid2Vic2l0ZSI6Imh0dHA6Ly93d3cuYm9sbGluZ2VybWFjaHNocHNoaXB5YXJkLmNvbSJ9\",\n"
			+ "            \"brokerInTime\": 1687328148493,\n"
			+ "            \"brokerOutTime\": 1687328529586\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:99\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148582,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-99\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": true,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJBcmxlbmUiLCJsYXN0bmFtZSI6IktsdXNtYW4iLCJjb21wYW55IjoiQmVjayBIb3Jpem9uIEJ1aWxkZXJzIiwic3RyZWV0IjoiMyBTZWNvciBSZCIsImNpdHkiOiJOZXcgT3JsZWFucyIsImNvdW50eSI6Ik9ybGVhbnMiLCJzdGF0ZSI6IkxBIiwiemlwIjoiNzAxMTIiLCJob21lUGhvbmUiOiI1MDQtNzEwLTU4NDAiLCJjZWxsUGhvbmUiOiI1MDQtOTQ2LTE4MDciLCJlbWFpbCI6ImFybGVuZV9rbHVzbWFuQGdtYWlsLmNvbSIsIndlYnNpdGUiOiJodHRwOi8vd3d3LmJlY2tob3Jpem9uYnVpbGRlcnMuY29tIn0=\",\n"
			+ "            \"brokerInTime\": 1687328148583,\n"
			+ "            \"brokerOutTime\": 1687328529593\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:67\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148524,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-67\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": true,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJFbGx5IiwibGFzdG5hbWUiOiJNb3JvY2NvIiwiY29tcGFueSI6IktpbGxpb24gSW5kdXN0cmllcyIsInN0cmVldCI6IjcgVyAzMm5kIFN0IiwiY2l0eSI6IkVyaWUiLCJjb3VudHkiOiJFcmllIiwic3RhdGUiOiJQQSIsInppcCI6IjE2NTAyIiwiaG9tZVBob25lIjoiODE0LTM5My01NTcxIiwiY2VsbFBob25lIjoiODE0LTQyMC0zNTUzIiwiZW1haWwiOiJlbGx5X21vcm9jY29AZ21haWwuY29tIiwid2Vic2l0ZSI6Imh0dHA6Ly93d3cua2lsbGlvbmluZHVzdHJpZXMuY29tIn0=\",\n"
			+ "            \"brokerInTime\": 1687328148525,\n"
			+ "            \"brokerOutTime\": 1687328529607\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:41\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148476,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-41\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": true,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJEeWFuIiwibGFzdG5hbWUiOiJPbGRyb3lkIiwiY29tcGFueSI6IkludGVybmF0aW9uYWwgRXllbGV0cyBJbmMiLCJzdHJlZXQiOiI3MjE5IFdvb2RmaWVsZCBSZCIsImNpdHkiOiJPdmVybGFuZCBQYXJrIiwiY291bnR5IjoiSm9obnNvbiIsInN0YXRlIjoiS1MiLCJ6aXAiOiI2NjIwNCIsImhvbWVQaG9uZSI6IjkxMy00MTMtNDYwNCIsImNlbGxQaG9uZSI6IjkxMy02NDUtODkxOCIsImVtYWlsIjoiZG9sZHJveWRAYW9sLmNvbSIsIndlYnNpdGUiOiJodHRwOi8vd3d3LmludGVybmF0aW9uYWxleWVsZXRzaW5jLmNvbSJ9\",\n"
			+ "            \"brokerInTime\": 1687328148477,\n"
			+ "            \"brokerOutTime\": 1687328529613\n"
			+ "        }\n"
			+ "    ]\n"
			+ "}";

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

		ObjectMapper om = new ObjectMapper();
		ActiveMQEvent event = null;
		try {
			event = om.readValue(mqEventJson, ActiveMQEvent.class);
			for(ActiveMQEvent.ActiveMQMessage msg : event.getMessages()){
				String base64EncodedData = msg.getData();
				String decodedData = "";
				if (null != base64EncodedData) {
					byte[] decodedDataBytes = Base64.getDecoder().decode(base64EncodedData);
					decodedData = new String(decodedDataBytes);
				}
				Person thisPerson = om.readValue(decodedData, Person.class);
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
				PutItemOutcome putOutcome = ddbUpdater.insertIntoDynamoDB(msg, thisPerson, logger, System.currentTimeMillis(), event.getEventSource(), event.getEventSourceArn());
				assertNotNull(putOutcome);
			}
		} catch (JsonMappingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (JsonProcessingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	    
	}
}

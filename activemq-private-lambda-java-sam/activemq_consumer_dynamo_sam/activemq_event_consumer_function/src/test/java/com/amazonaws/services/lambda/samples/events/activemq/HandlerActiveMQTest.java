package com.amazonaws.services.lambda.samples.events.activemq;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.mock;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
//import com.amazonaws.services.dynamodbv2.document.PutItemOutcome;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.events.ActiveMQEvent;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

class HandlerSQSTest {
	private static final String mqEventJson = "{\n"
			+ "    \"eventSource\": \"aws:mq\",\n"
			+ "    \"eventSourceArn\": \"arn:aws:mq:us-west-2:664251831272:broker:ib-activemq-broker:b-aeb08c0d-6e46-412a-ad45-1507816242b0\",\n"
			+ "    \"messages\": [\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:1\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148384,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-1\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": false,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJKb3NlcGhpbmUiLCJsYXN0bmFtZSI6IkRhcmFrankiLCJjb21wYW55IjoiXCJDaGFuYXksIEplZmZyZXkgQSBFc3FcIiIsInN0cmVldCI6IjQgQiBCbHVlIFJpZGdlIEJsdmQiLCJjaXR5IjoiQnJpZ2h0b24iLCJjb3VudHkiOiJMaXZpbmdzdG9uIiwic3RhdGUiOiJNSSIsInppcCI6IjQ4MTE2IiwiaG9tZVBob25lIjoiODEwLTI5Mi05Mzg4IiwiY2VsbFBob25lIjoiODEwLTM3NC05ODQwIiwiZW1haWwiOiJqb3NlcGhpbmVfZGFyYWtqeUBkYXJha2p5Lm9yZyIsIndlYnNpdGUiOiJodHRwOi8vd3d3LmNoYW5heWplZmZyZXlhZXNxLmNvbSJ9\",\n"
			+ "            \"brokerInTime\": 1687328148385,\n"
			+ "            \"brokerOutTime\": 1687328148385\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:38\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148471,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-38\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": false,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJWYWxlbnRpbmUiLCJsYXN0bmFtZSI6IkdpbGxpYW4iLCJjb21wYW55IjoiRmJzIEJ1c2luZXNzIEZpbmFuY2UiLCJzdHJlZXQiOiI3NzUgVyAxN3RoIFN0IiwiY2l0eSI6IlNhbiBBbnRvbmlvIiwiY291bnR5IjoiQmV4YXIiLCJzdGF0ZSI6IlRYIiwiemlwIjoiNzgyMDQiLCJob21lUGhvbmUiOiIyMTAtODEyLTk1OTciLCJjZWxsUGhvbmUiOiIyMTAtMzAwLTYyNDQiLCJlbWFpbCI6InZhbGVudGluZV9naWxsaWFuQGdtYWlsLmNvbSIsIndlYnNpdGUiOiJodHRwOi8vd3d3LmZic2J1c2luZXNzZmluYW5jZS5jb20ifQ==\",\n"
			+ "            \"brokerInTime\": 1687328148472,\n"
			+ "            \"brokerOutTime\": 1687328148495\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:48\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148491,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-48\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": false,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJFbWVyc29uIiwibGFzdG5hbWUiOiJCb3dsZXkiLCJjb21wYW55IjoiS25pZ2h0cyBJbm4iLCJzdHJlZXQiOiI3NjIgUyBNYWluIFN0IiwiY2l0eSI6Ik1hZGlzb24iLCJjb3VudHkiOiJEYW5lIiwic3RhdGUiOiJXSSIsInppcCI6IjUzNzExIiwiaG9tZVBob25lIjoiNjA4LTMzNi03NDQ0IiwiY2VsbFBob25lIjoiNjA4LTY1OC03OTQwIiwiZW1haWwiOiJlbWVyc29uLmJvd2xleUBib3dsZXkub3JnIiwid2Vic2l0ZSI6Imh0dHA6Ly93d3cua25pZ2h0c2lubi5jb20ifQ==\",\n"
			+ "            \"brokerInTime\": 1687328148492,\n"
			+ "            \"brokerOutTime\": 1687328148534\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:53\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148498,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-53\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": false,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJNYXJqb3J5IiwibGFzdG5hbWUiOiJNYXN0ZWxsYSIsImNvbXBhbnkiOiJWaWNvbiBDb3Jwb3JhdGlvbiIsInN0cmVldCI6IjcxIFNhbiBNYXRlbyBBdmUiLCJjaXR5IjoiV2F5bmUiLCJjb3VudHkiOiJEZWxhd2FyZSIsInN0YXRlIjoiUEEiLCJ6aXAiOiIxOTA4NyIsImhvbWVQaG9uZSI6IjYxMC04MTQtNTUzMyIsImNlbGxQaG9uZSI6IjYxMC0zNzktNzEyNSIsImVtYWlsIjoibW1hc3RlbGxhQG1hc3RlbGxhLmNvbSIsIndlYnNpdGUiOiJodHRwOi8vd3d3LnZpY29uY29ycG9yYXRpb24uY29tIn0=\",\n"
			+ "            \"brokerInTime\": 1687328148503,\n"
			+ "            \"brokerOutTime\": 1687328148538\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:58\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148514,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-58\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": false,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJEZWxteSIsImxhc3RuYW1lIjoiQWhsZSIsImNvbXBhbnkiOiJXeWUgVGVjaG5vbG9naWVzIEluYyIsInN0cmVldCI6IjY1ODk1IFMgMTZ0aCBTdCIsImNpdHkiOiJQcm92aWRlbmNlIiwiY291bnR5IjoiUHJvdmlkZW5jZSIsInN0YXRlIjoiUkkiLCJ6aXAiOiIyOTA5IiwiaG9tZVBob25lIjoiNDAxLTQ1OC0yNTQ3IiwiY2VsbFBob25lIjoiNDAxLTU1OS04OTYxIiwiZW1haWwiOiJkZWxteS5haGxlQGhvdG1haWwuY29tIiwid2Vic2l0ZSI6Imh0dHA6Ly93d3cud3lldGVjaG5vbG9naWVzaW5jLmNvbSJ9\",\n"
			+ "            \"brokerInTime\": 1687328148514,\n"
			+ "            \"brokerOutTime\": 1687328148552\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:63\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148520,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-63\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": false,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJDYXJtZWxpbmEiLCJsYXN0bmFtZSI6IkxpbmRhbGwiLCJjb21wYW55IjoiR2VvcmdlIEplc3NvcCBDYXJ0ZXIgSmV3ZWxlcnMiLCJzdHJlZXQiOiIyNjY0IExld2lzIFJkIiwiY2l0eSI6IkxpdHRsZXRvbiIsImNvdW50eSI6IkRvdWdsYXMiLCJzdGF0ZSI6IkNPIiwiemlwIjoiODAxMjYiLCJob21lUGhvbmUiOiIzMDMtNzI0LTczNzEiLCJjZWxsUGhvbmUiOiIzMDMtODc0LTUxNjAiLCJlbWFpbCI6ImNhcm1lbGluYV9saW5kYWxsQGxpbmRhbGwuY29tIiwid2Vic2l0ZSI6Imh0dHA6Ly93d3cuZ2VvcmdlamVzc29wY2FydGVyamV3ZWxlcnMuY29tIn0=\",\n"
			+ "            \"brokerInTime\": 1687328148520,\n"
			+ "            \"brokerOutTime\": 1687328148556\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:68\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148526,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-68\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": false,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJJbGVuZSIsImxhc3RuYW1lIjoiRXJvbWFuIiwiY29tcGFueSI6IlwiUm9iaW5zb24sIFdpbGxpYW0gSiBFc3FcIiIsInN0cmVldCI6IjI4NTMgUyBDZW50cmFsIEV4cHkiLCJjaXR5IjoiR2xlbiBCdXJuaWUiLCJjb3VudHkiOiJBbm5lIEFydW5kZWwiLCJzdGF0ZSI6Ik1EIiwiemlwIjoiMjEwNjEiLCJob21lUGhvbmUiOiI0MTAtOTE0LTkwMTgiLCJjZWxsUGhvbmUiOiI0MTAtOTM3LTQ1NDMiLCJlbWFpbCI6ImlsZW5lLmVyb21hbkBob3RtYWlsLmNvbSIsIndlYnNpdGUiOiJodHRwOi8vd3d3LnJvYmluc29ud2lsbGlhbWplc3EuY29tIn0=\",\n"
			+ "            \"brokerInTime\": 1687328148527,\n"
			+ "            \"brokerOutTime\": 1687328148559\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:75\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148534,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-75\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": false,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJNb29uIiwibGFzdG5hbWUiOiJQYXJsYXRvIiwiY29tcGFueSI6IlwiQW1iZWxhbmcsIEplc3NpY2EgTSBNZFwiIiwic3RyZWV0IjoiNzQ5ODkgQnJhbmRvbiBTdCIsImNpdHkiOiJXZWxsc3ZpbGxlIiwiY291bnR5IjoiQWxsZWdhbnkiLCJzdGF0ZSI6Ik5ZIiwiemlwIjoiMTQ4OTUiLCJob21lUGhvbmUiOiI1ODUtODY2LTgzMTMiLCJjZWxsUGhvbmUiOiI1ODUtNDk4LTQyNzgiLCJlbWFpbCI6Im1vb25AeWFob28uY29tIiwid2Vic2l0ZSI6Imh0dHA6Ly93d3cuYW1iZWxhbmdqZXNzaWNhbW1kLmNvbSJ9\",\n"
			+ "            \"brokerInTime\": 1687328148534,\n"
			+ "            \"brokerOutTime\": 1687328148574\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:78\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148537,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-78\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": false,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJWaXZhIiwibGFzdG5hbWUiOiJUb2Vsa2VzIiwiY29tcGFueSI6Ik1hcmsgSXYgUHJlc3MgTHRkIiwic3RyZWV0IjoiNDI4NCBEb3JpZ28gTG4iLCJjaXR5IjoiQ2hpY2FnbyIsImNvdW50eSI6IkNvb2siLCJzdGF0ZSI6IklMIiwiemlwIjoiNjA2NDciLCJob21lUGhvbmUiOiI3NzMtNDQ2LTU1NjkiLCJjZWxsUGhvbmUiOiI3NzMtMzUyLTM0MzciLCJlbWFpbCI6InZpdmEudG9lbGtlc0BnbWFpbC5jb20iLCJ3ZWJzaXRlIjoiaHR0cDovL3d3dy5tYXJraXZwcmVzc2x0ZC5jb20ifQ==\",\n"
			+ "            \"brokerInTime\": 1687328148538,\n"
			+ "            \"brokerOutTime\": 1687328148576\n"
			+ "        },\n"
			+ "        {\n"
			+ "            \"messageID\": \"ID:ip-10-192-10-195.us-west-2.compute.internal-33249-1687328148123-1:1:1:1:81\",\n"
			+ "            \"messageType\": \"jms/text-message\",\n"
			+ "            \"timestamp\": 1687328148540,\n"
			+ "            \"deliveryMode\": 1,\n"
			+ "            \"correlationID\": \"TestMessage07-06-21-2023-06-06-02-81\",\n"
			+ "            \"replyTo\": \"null\",\n"
			+ "            \"destination\": {\n"
			+ "                \"physicalName\": \"LambdaActiveMQQueue\"\n"
			+ "            },\n"
			+ "            \"redelivered\": false,\n"
			+ "            \"type\": \"TextMessage\",\n"
			+ "            \"expiration\": 0,\n"
			+ "            \"priority\": 4,\n"
			+ "            \"data\": \"eyJmaXJzdG5hbWUiOiJUaW1vdGh5IiwibGFzdG5hbWUiOiJNdWxxdWVlbiIsImNvbXBhbnkiOiJTYXJvbml4IE55bXBoIFByb2R1Y3RzIiwic3RyZWV0IjoiNDQgVyA0dGggU3QiLCJjaXR5IjoiU3RhdGVuIElzbGFuZCIsImNvdW50eSI6IlJpY2htb25kIiwic3RhdGUiOiJOWSIsInppcCI6IjEwMzA5IiwiaG9tZVBob25lIjoiNzE4LTMzMi02NTI3IiwiY2VsbFBob25lIjoiNzE4LTY1NC03MDYzIiwiZW1haWwiOiJ0aW1vdGh5X211bHF1ZWVuQG11bHF1ZWVuLm9yZyIsIndlYnNpdGUiOiJodHRwOi8vd3d3LnNhcm9uaXhueW1waHByb2R1Y3RzLmNvbSJ9\",\n"
			+ "            \"brokerInTime\": 1687328148541,\n"
			+ "            \"brokerOutTime\": 1687328148578\n"
			+ "        }\n"
			+ "    ]\n"
			+ "}";

	@Mock
	DynamoDBUpdater ddbUpdater;	
	
	@Test
	@ExtendWith(MockitoExtension.class)
	void invokeTest() {
		
		ObjectMapper om = new ObjectMapper();
		//SQSEvent event = gson.fromJson(sqsEventJson, SQSEvent.class);
		ActiveMQEvent event = null;
		try {
			event = om.readValue(mqEventJson, ActiveMQEvent.class);
		} catch (JsonMappingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (JsonProcessingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		Context context = new TestContext();
		//PutItemOutcome putItemOutcome = mock(PutItemOutcome.class);
		DynamoDBUpdater dbUpdater = mock(DynamoDBUpdater.class);
		HandlerActiveMQ handler = new HandlerActiveMQ();
		handler.ddbUpdater = dbUpdater;
		//when(handler.ddbUpdater.insertIntoDynamoDB(ArgumentMatchers.any(ActiveMQEvent.ActiveMQMessage.class), ArgumentMatchers.any(Gson.class), ArgumentMatchers.any(LambdaLogger.class), ArgumentMatchers.anyLong(), ArgumentMatchers.anyString(), ArgumentMatchers.anyString())).thenReturn(putItemOutcome);
		String result = handler.handleRequest(event, context);
		assertEquals(result, "200");
	}

}

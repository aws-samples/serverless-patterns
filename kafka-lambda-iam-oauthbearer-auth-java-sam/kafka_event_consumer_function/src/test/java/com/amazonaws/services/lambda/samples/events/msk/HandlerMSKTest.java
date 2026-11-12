package com.amazonaws.services.lambda.samples.events.msk;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.events.KafkaEvent;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;


class HandlerMSKTest {
	private static final String kafkaEventJson = "{\n"
			+ "   \"records\":{\n"
			+ "      \"myTopic-0\":[\n"
			+ "         {\n"
			+ "            \"topic\":\"myTopic\",\n"
			+ "            \"partition\":0,\n"
			+ "            \"offset\":250,\n"
			+ "            \"timestamp\":1678072110111,\n"
			+ "            \"timestampType\":\"CREATE_TIME\",\n"
			+ "            \"value\":\"Zg==\",\n"
			+ "            \"headers\":[\n"
			+ "               \n"
			+ "            ]\n"
			+ "         },\n"
			+ "         {\n"
			+ "            \"topic\":\"myTopic\",\n"
			+ "            \"partition\":0,\n"
			+ "            \"offset\":251,\n"
			+ "            \"timestamp\":1678072111086,\n"
			+ "            \"timestampType\":\"CREATE_TIME\",\n"
			+ "            \"value\":\"Zw==\",\n"
			+ "            \"headers\":[\n"
			+ "               \n"
			+ "            ]\n"
			+ "         }\n"
			+ "      ]\n"
			+ "   },\n"
			+ "   \"eventSource\":\"aws:kafka\",\n"
			+ "   \"eventSourceArn\":\"arn:aws:kafka:us-west-2:123456789012:cluster/MSKWorkshopCluster/a93759a9-c9d0-4952-984c-492c6bfa2be8-13\",\n"
			+ "   \"bootstrapServers\":\"b-2.mskworkshopcluster.z9kc4f.c13.kafka.us-west-2.amazonaws.com:9098,b-3.mskworkshopcluster.z9kc4f.c13.kafka.us-west-2.amazonaws.com:9098,b-1.mskworkshopcluster.z9kc4f.c13.kafka.us-west-2.amazonaws.com:9098\"\n"
			+ "}";

	  @Test
	  void invokeTest() {
		Gson gson = new GsonBuilder().setPrettyPrinting().create();
		KafkaEvent event = gson.fromJson(kafkaEventJson, KafkaEvent.class);
	    Context context = new TestContext();
	    HandlerMSK handler = new HandlerMSK();
	    String result = handler.handleRequest(event, context);
	    assertEquals(result, "200 OK");
	    assertEquals(handler.listOfMessages.size(), 2);
	    assertEquals(handler.listOfMessages.get(0).getTopic(), "myTopic");
	    assertEquals(handler.listOfMessages.get(0).getPartition(), 0);
	    assertEquals(handler.listOfMessages.get(0).getOffset(), 250L);
	    assertEquals(handler.listOfMessages.get(0).getTimestamp(), 1678072110111L);
	    assertEquals(handler.listOfMessages.get(0).getTimestampType(), "CREATE_TIME");
	    assertEquals(handler.listOfMessages.get(0).getDecodedKey(), "null");
	    assertEquals(handler.listOfMessages.get(0).getDecodedValue(), "f");
	    assertEquals(handler.listOfMessages.get(1).getTopic(), "myTopic");
	    assertEquals(handler.listOfMessages.get(1).getPartition(), 0);
	    assertEquals(handler.listOfMessages.get(1).getOffset(), 251L);
	    assertEquals(handler.listOfMessages.get(1).getTimestamp(), 1678072111086L);
	    assertEquals(handler.listOfMessages.get(1).getTimestampType(), "CREATE_TIME");
	    assertEquals(handler.listOfMessages.get(1).getDecodedKey(), "null");
	    assertEquals(handler.listOfMessages.get(1).getDecodedValue(), "g");
	  }
}

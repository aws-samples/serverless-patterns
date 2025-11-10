package com.amazonaws.services.lambda.samples.events.documentdbstreams;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;
import static org.mockito.Mockito.mock;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import com.amazonaws.services.lambda.runtime.Context;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

class HandlerDocumentDBStreamsTest {
	
	@Mock
	DynamoDBUpdater ddbUpdater;	
	
	@Test
	@ExtendWith(MockitoExtension.class)
	void invokeTest() {
		try {
			InputStream fis = HandlerDocumentDBStreamsTest.class.getClassLoader().getResourceAsStream("event.json");
			OutputStream baos = new ByteArrayOutputStream();
			Context context = new TestContext();
			DynamoDBUpdater dbUpdater = mock(DynamoDBUpdater.class);
			HandlerDocumentDBStreams handler = new HandlerDocumentDBStreams();
			handler.ddbUpdater = dbUpdater;
			handler.handleRequest(fis, baos, context);
			fis.close();
			assertEquals(1,1);
		} catch (Exception e) {
			e.printStackTrace();
			fail();
		}

		
	}

}

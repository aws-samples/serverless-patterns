package com.example.sqsfunction;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

import com.amazonaws.services.lambda.runtime.events.SQSBatchResponse;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.events.SQSEvent;
import org.junit.Test;

import java.util.ArrayList;

public class AppTest {
  @Test
  public void successfulResponse() {
    App app = new App();

    SQSEvent sqsEvent = new SQSEvent();
    sqsEvent.setRecords(new ArrayList<>());

    SQSBatchResponse result = app.handleRequest(sqsEvent, new TestContext());
    assertEquals(0, result.getBatchItemFailures().size());
  }
}

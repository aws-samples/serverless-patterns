package com.example;

import com.amazonaws.services.lambda.runtime.LambdaLogger;

import java.util.Map;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

public class EventBridgeFunction implements RequestHandler<Map<String,String>, String>{
    @Override
    public String handleRequest(Map<String,String> event, Context context)
    {
      LambdaLogger logger = context.getLogger();
      // Print the event from EventBridge Scheduler
      logger.log("EVENT: " + event.toString());
      return event.toString();
    }
  }
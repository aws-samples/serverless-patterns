package com.myorg;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestStreamHandler;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

public class App implements RequestStreamHandler {
    private static final ObjectMapper objectMapper = new ObjectMapper();

    @Override
    public void handleRequest(InputStream input, OutputStream output, Context context) throws IOException {
        // Parse the input stream to JsonNode
        JsonNode event = objectMapper.readTree(input);

         LambdaLogger logger = context.getLogger();

        try {
            // Check if the event indicates a failure
            if (event.has("detail") && event.get("detail").has("failure") 
                    && event.get("detail").get("failure").asBoolean()) {
                throw new Exception("Failure Exception");
            } else {
                // Log the request
                 logger.log("Request: " + objectMapper.writeValueAsString(event));

                // Create a success response
                ObjectNode response = objectMapper.createObjectNode();
                response.put("statusCode", 200);

                ObjectNode processedInput = objectMapper.createObjectNode();
                processedInput.put("transactionStatus", "completed");

                response.set("processedInput", processedInput);
                response.set("sourceEvent", event);

                // Write the response to the output stream
                objectMapper.writeValue(output, response);
            }
        } catch (Exception e) {
            // Log the error
             logger.log("Error: " + e.getMessage());

             throw new RuntimeException(e);
        }
    }
}

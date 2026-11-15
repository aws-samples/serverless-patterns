package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyRequestEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyResponseEvent;
import com.example.model.Ticket;
import com.example.utils.DDBUtils;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.UUID;

public class TicketFunction implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger logger = LoggerFactory.getLogger(TicketFunction.class);
    ObjectMapper mapper = new ObjectMapper();
    DDBUtils ddbUtils = new DDBUtils();

    @Override
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent event, Context context) {

        APIGatewayProxyResponseEvent response = new APIGatewayProxyResponseEvent();

        String ticketId = "";
        try {
            Ticket ticket = mapper.readValue(event.getBody(), Ticket.class);

            logger.info("[ticket userId] " + ticket.getUserId());
            logger.info("[ticket description] " + ticket.getDescription());

            ticketId = ddbUtils.persistTicket(ticket);

            response.setBody(mapper.writeValueAsString(ticketId));

        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
        return response;
    }
}

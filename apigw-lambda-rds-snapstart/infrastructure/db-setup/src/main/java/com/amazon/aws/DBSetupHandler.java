package com.amazon.aws;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyRequestEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyResponseEvent;
import org.apache.commons.io.IOUtils;

import java.io.IOException;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBSetupHandler implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    private static final String DB_CONNECTION = System.getenv("DB_CONNECTION_URL");
    private static final String DB_USER = System.getenv("DB_USER");
    private static final String DB_PASSWORD = System.getenv("DB_PASSWORD");

    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        try(var connection = DriverManager.getConnection(DB_CONNECTION, DB_USER, DB_PASSWORD)) {
            try(var statement = connection.createStatement()) {
                try(var sqlFile = getClass().getClassLoader().getResourceAsStream("setup.sql")) {
                    statement.executeUpdate(IOUtils.toString(sqlFile));
                    return new APIGatewayProxyResponseEvent()
                            .withStatusCode(200)
                            .withBody("DB Setup successful");
                }
            }
        } catch (SQLException | IOException sqlException) {
            context.getLogger().log("Error connection to the database:" + sqlException.getMessage());
            return new APIGatewayProxyResponseEvent()
                    .withStatusCode(500)
                    .withBody("Error initializing the database");
        }
    }
}

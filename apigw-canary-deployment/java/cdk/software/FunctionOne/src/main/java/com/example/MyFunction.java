package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyRequestEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyResponseEvent;


import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.regions.Region;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.net.URL;
import java.security.KeyStore;
import java.security.cert.CertificateFactory;
import java.security.cert.X509Certificate;
import java.sql.*;
import java.util.Properties;

public class MyFunction implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    static Logger logger = LoggerFactory.getLogger(MyFunction.class);


    @Override
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent event, Context context) {

       APIGatewayProxyResponseEvent response = new APIGatewayProxyResponseEvent();

       logger.info("Starting");

       response.setBody("Production Verison");

       return response;
    }
}

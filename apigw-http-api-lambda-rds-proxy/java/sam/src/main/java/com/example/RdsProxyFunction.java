package com.example;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyRequestEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyResponseEvent;


import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rds.RdsUtilities;
import software.amazon.awssdk.services.rds.model.GenerateAuthenticationTokenRequest;

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

public class RdsProxyFunction implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    static Logger logger = LoggerFactory.getLogger(RdsProxyFunction.class);

    private static final String RDS_INSTANCE_HOSTNAME = System.getenv("rds_endpoint");
    private static final int RDS_INSTANCE_PORT = Integer.parseInt(System.getenv("port"));
    private static final String DB_USER = System.getenv("username");
    private static final String REGION = System.getenv("region");
    private static final String JDBC_URL = "jdbc:mysql://" + RDS_INSTANCE_HOSTNAME + ":" + RDS_INSTANCE_PORT;

    private static final String SSL_CERTIFICATE = "AmazonRootCA1.pem";

    private static final String KEY_STORE_TYPE = "JKS";
    private static final String KEY_STORE_PROVIDER = "SUN";
    private static final String KEY_STORE_FILE_PREFIX = "sys-connect-via-ssl-test-cacerts";
    private static final String KEY_STORE_FILE_SUFFIX = ".jks";
    private static final String DEFAULT_KEY_STORE_PASSWORD = "changeit";



    static String generateAuthToken() {
        String region = REGION;
        String dbEndpoint = RDS_INSTANCE_HOSTNAME;
        int port = RDS_INSTANCE_PORT;
        String username = DB_USER;

        RdsUtilities utilities = RdsUtilities.builder()
                .credentialsProvider(DefaultCredentialsProvider.create())
                .region(Region.of(region))
                .build();

        GenerateAuthenticationTokenRequest authTokenRequest = GenerateAuthenticationTokenRequest.builder()
                .username(username)
                .hostname(dbEndpoint)
                .port(port)
                .build();

        String authenticationToken = utilities.generateAuthenticationToken(authTokenRequest);

        return authenticationToken;
    }


    private static X509Certificate createCertificate() throws Exception {
        CertificateFactory certFactory = CertificateFactory.getInstance("X.509");
        URL url = new File(SSL_CERTIFICATE).toURI().toURL();
        if (url == null) {
            throw new Exception();
        }
        try (InputStream certInputStream = url.openStream()) {
            return (X509Certificate) certFactory.generateCertificate(certInputStream);
        }
    }


    private static Properties setMySqlConnectionProperties() {
        Properties mysqlConnectionProperties = new Properties();
        //mysqlConnectionProperties.setProperty("verifyServerCertificate","true");
        mysqlConnectionProperties.setProperty("useSSL", "true");
        mysqlConnectionProperties.setProperty("user",DB_USER);
        mysqlConnectionProperties.setProperty("password",generateAuthToken());
        return mysqlConnectionProperties;
    }
    /**
     * This method returns the path of the Key Store File needed for the SSL verification during the IAM Database Authentication to
     * the db instance.
     * @return
     * @throws Exception
     */
    private static String createKeyStoreFile() throws Exception {
        X509Certificate cert= createCertificate();
        logger.info("cert info "+cert.toString());
        File file =createKeyStoreFile(cert);
        logger.info("Cert file "+file.getPath());
        return file.getPath();
    }

    /**
     * This method creates the Key Store File
     * @param rootX509Certificate - the SSL certificate to be stored in the KeyStore
     * @return
     * @throws Exception
     */
    private static File createKeyStoreFile(X509Certificate rootX509Certificate) throws Exception {
        File keyStoreFile = File.createTempFile(KEY_STORE_FILE_PREFIX, KEY_STORE_FILE_SUFFIX);
        try (FileOutputStream fos = new FileOutputStream(keyStoreFile.getPath())) {
            KeyStore ks = KeyStore.getInstance(KEY_STORE_TYPE, KEY_STORE_PROVIDER);
            ks.load(null);
            ks.setCertificateEntry("rootCaCertificate", rootX509Certificate);
            ks.store(fos, DEFAULT_KEY_STORE_PASSWORD.toCharArray());
        }
        return keyStoreFile;
    }


    private static void setSslProperties() throws Exception {
        System.setProperty("javax.net.ssl.trustStore", createKeyStoreFile());
        System.setProperty("javax.net.ssl.trustStoreType", KEY_STORE_TYPE);
        System.setProperty("javax.net.ssl.trustStorePassword", DEFAULT_KEY_STORE_PASSWORD);
    }
    private static Connection getDBConnectionUsingIam() throws Exception {
        setSslProperties();
        return DriverManager.getConnection(JDBC_URL, setMySqlConnectionProperties());
    }

    @Override
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent event, Context context) {

        APIGatewayProxyResponseEvent response = new APIGatewayProxyResponseEvent();

       logger.info("Starting");
       String token = generateAuthToken();
       try {
           Connection conn = getDBConnectionUsingIam();
           Statement statement = conn.createStatement();

           // Get current date and current time
           String sql = "SELECT CURDATE(),CURTIME()";
           ResultSet rs = statement.executeQuery(sql);
           while (rs.next()) {
               Date date =rs.getDate(1);
               Time time =rs.getTime(2);

               logger.info("Current Date : "+ date);
               logger.info("Current Time : "+time );
               response.setBody("Demo  : Working fine date/time from mysql "+date+" Time: "+time);
           }
         statement.close();

       }catch (Exception e){
           logger.error(e.getMessage());
           e.printStackTrace();
           response.setBody(e.getMessage());
       }

        return response;
    }
}

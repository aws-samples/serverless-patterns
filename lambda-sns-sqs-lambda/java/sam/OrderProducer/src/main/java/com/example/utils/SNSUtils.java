package com.example.utils;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.services.sns.SnsClient;
import software.amazon.awssdk.services.sns.model.*;
public class SNSUtils {

    private static final SnsClient SNS_CLIENT = SnsClient.create();
    private static final Logger LOGGER = LoggerFactory.getLogger(SNSUtils.class);

    public static String publishMessage(String message, String topicName){
        String topicArn = getTopicArn(SNS_CLIENT, topicName);
        PublishRequest request = PublishRequest.builder()
                .message(message)
                .topicArn(topicArn)
                .build();

        PublishResponse result = SNS_CLIENT.publish(request);

        LOGGER.info("[SNS messageID]" + result.messageId());

        return result.messageId();

    }

    private static String getTopicArn(SnsClient snsClient,String topicName){

        String topicArn = "";

        try {
            ListTopicsRequest request = ListTopicsRequest.builder()
                    .build();

            ListTopicsResponse result = snsClient.listTopics(request);

            topicArn = result.topics()
                    .stream().filter(t -> t.topicArn().contains(topicName))
                    .findAny()
                    .get()
                    .topicArn();

            return topicArn;

        } catch (SnsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return topicArn;
    }
}



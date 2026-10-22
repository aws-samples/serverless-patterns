package sns.producer;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import software.amazon.awssdk.services.sns.SnsClient;
import software.amazon.awssdk.services.sns.model.ListTopicsRequest;
import software.amazon.awssdk.services.sns.model.ListTopicsResponse;
import software.amazon.awssdk.services.sns.model.MessageAttributeValue;
import software.amazon.awssdk.services.sns.model.PublishRequest;
import software.amazon.awssdk.services.sns.model.PublishResponse;
import software.amazon.awssdk.services.sns.model.Topic;

/**
 * SNS Message Sender for triggering Lambda Durable Function examples.
 *
 * Usage:
 *   java -cp target/sns-message-sender-1.0-SNAPSHOT.jar sns.producer.DurableFunctionsTrigger <TopicName> <Pattern>
 *
 * Patterns:
 *   chaining         - Order processing with sequential steps
 *   fanout           - Parallel data analysis
 *   approval         - Human-in-the-loop approval workflow
 *   monitoring       - Job status polling
 *   timer            - Scheduled reminders with delays
 *   errorhandling    - Resilient payment with saga compensation
 *   mapprocessing    - Batch data processing
 *   suborchestration - Order fulfillment with sub-workflows
 */
public class DurableFunctionsTrigger {

    private static final ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: DurableFunctionsTrigger <TopicName> <Pattern>");
            System.out.println("Patterns: chaining, fanout, approval, monitoring, timer, errorhandling, mapprocessing, suborchestration");
            System.exit(1);
        }

        String topicName = args[0];
        String pattern = args[1];

        Map<String, Object> message = buildMessage(pattern);
        sendToSNS(topicName, message, pattern);
    }

    private static Map<String, Object> buildMessage(String pattern) {
        switch (pattern) {
            case "chaining":
                return Map.of(
                        "orderId", "ORD-" + System.currentTimeMillis(),
                        "customerId", "CUST-001",
                        "customerEmail", "customer@example.com",
                        "totalAmount", 299.99,
                        "shippingAddress", "123 Main St, Seattle, WA 98101"
                );
            case "fanout":
                return Map.of(
                        "dataId", "DATA-" + System.currentTimeMillis(),
                        "source", "s3://my-bucket/documents/report.pdf",
                        "analysisTypes", List.of("sentiment", "entities", "summary")
                );
            case "approval":
                return Map.of(
                        "requestId", "REQ-" + System.currentTimeMillis(),
                        "requestor", "employee@example.com",
                        "amount", 15000.00,
                        "description", "Conference travel budget request"
                );
            case "monitoring":
                return Map.of(
                        "jobId", "JOB-" + System.currentTimeMillis(),
                        "jobType", "DATA_EXPORT",
                        "maxPolls", 5
                );
            case "timer":
                return Map.of(
                        "taskId", "TASK-" + System.currentTimeMillis(),
                        "assignee", "developer@example.com",
                        "reminderIntervalSeconds", 30,
                        "escalationSeconds", 60
                );
            case "errorhandling":
                return Map.of(
                        "orderId", "ORD-" + System.currentTimeMillis(),
                        "amount", 199.99,
                        "simulateInventoryFailure", false
                );
            case "mapprocessing":
                return Map.of(
                        "batchSize", 10,
                        "maxConcurrency", 3,
                        "toleratedFailures", 2
                );
            case "suborchestration":
                return Map.of(
                        "orderId", "ORD-" + System.currentTimeMillis(),
                        "customerId", "CUST-" + System.currentTimeMillis(),
                        "amount", 499.99,
                        "items", List.of(
                                Map.of("productId", "PROD-001", "name", "Widget", "qty", 2),
                                Map.of("productId", "PROD-002", "name", "Gadget", "qty", 1)
                        )
                );
            default:
                System.err.println("Unknown pattern: " + pattern);
                System.exit(1);
                return Map.of();
        }
    }

    private static void sendToSNS(String topicName, Map<String, Object> message, String pattern) {
        SnsClient snsClient = SnsClient.builder().build();
        String topicArn = getTopicArnFromName(snsClient, topicName);

        if (topicArn.isEmpty()) {
            System.err.println("Topic not found: " + topicName);
            System.exit(1);
        }

        try {
            String messageBody = mapper.writeValueAsString(message);

            Map<String, MessageAttributeValue> attributes = new HashMap<>();
            attributes.put("pattern", MessageAttributeValue.builder()
                    .dataType("String").stringValue(pattern).build());

            PublishRequest request = PublishRequest.builder()
                    .topicArn(topicArn)
                    .message(messageBody)
                    .messageAttributes(attributes)
                    .subject("Durable Functions Trigger - " + pattern)
                    .build();

            System.out.println("============================================================");
            System.out.println("Sending SNS message to trigger: " + pattern);
            System.out.println("Topic: " + topicArn);
            System.out.println("Message: " + messageBody);
            System.out.println("============================================================");

            PublishResponse response = snsClient.publish(request);
            System.out.println("Message sent! ID: " + response.messageId());
            System.out.println("Status: " + response.sdkHttpResponse().statusCode());
            System.out.println("============================================================");

        } catch (JsonProcessingException e) {
            System.err.println("Failed to serialize message: " + e.getMessage());
            System.exit(1);
        }
    }

    private static String getTopicArnFromName(SnsClient snsClient, String topicName) {
        ListTopicsResponse response = snsClient.listTopics(ListTopicsRequest.builder().build());
        for (Topic topic : response.topics()) {
            if (topic.topicArn().endsWith(topicName)) {
                return topic.topicArn();
            }
        }
        return "";
    }
}

package software.amazon.samples.eventbridge;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.SendMessageBatchRequest;
import software.amazon.awssdk.services.sqs.model.SendMessageBatchRequestEntry;

import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

public class DeadLetterQFacade {

    private static final Logger log = LogManager.getLogger(DeadLetterQFacade.class);

    private final SqsClient client;

    private final String dlqUrl;

    public DeadLetterQFacade(String dlqUrl) {
        this (SqsClient.create(), dlqUrl);
    }

    public DeadLetterQFacade(SqsClient client, String dlqUrl) {
        this.client = client;
        this.dlqUrl = dlqUrl;
    }

    public void sendErrorMessageToDLQ(List<Object> failedMessages) {
        if (failedMessages.isEmpty()) {
            return;
        }

        SendMessageBatchRequest sendMessageBatchRequest = SendMessageBatchRequest.builder()
                .queueUrl(dlqUrl)
                .entries(
                    failedMessages.stream().map(message -> SendMessageBatchRequestEntry.builder()
                            .messageBody(message.toString())
                            .id(UUID.randomUUID().toString())
                            .build())
                        .collect(Collectors.toList())
                ).build();

        client.sendMessageBatch(sendMessageBatchRequest);
    }

    public String getDlqUrl() {
        return dlqUrl;
    }
}

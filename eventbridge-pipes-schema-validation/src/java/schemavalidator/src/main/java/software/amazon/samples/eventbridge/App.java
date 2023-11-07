package software.amazon.samples.eventbridge;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestStreamHandler;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.avro.generic.GenericRecord;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Base64;
import java.util.List;


public class App implements RequestStreamHandler {

    public static final String REGISTRY_NAME = "REGISTRY_NAME";
    public static final String SCHEMA_NAME = "SCHEMA_NAME";
    public static final String TOPIC_NAME = "TOPIC_NAME";
    public static final String DLQ_URL = "DLQ_URL";

    private final static Logger log = LogManager.getLogger(App.class);

    private final GlueSchemaRegistryDeSerializationFacade glueSchemaRegistryDeSerializationFacadeWrapper;
    private final DeadLetterQFacade deadLetterQFacade;
    private final String topicName;
    private final ObjectMapper objectMapper;


    public App(GlueSchemaRegistryDeSerializationFacade glueSchemaRegistryDeSerializationFacadeWrapper, DeadLetterQFacade deadLetterQFacade, String topicName) {
        this.glueSchemaRegistryDeSerializationFacadeWrapper = glueSchemaRegistryDeSerializationFacadeWrapper;
        this.deadLetterQFacade = deadLetterQFacade;
        this.topicName = topicName;
        this.objectMapper = new ObjectMapper();
        this.objectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
    }


    public App() {
        this(
            new GlueSchemaRegistryDeSerializationFacade(System.getenv(REGISTRY_NAME), System.getenv(SCHEMA_NAME)),
            new DeadLetterQFacade(System.getenv(DLQ_URL)),
                System.getenv(TOPIC_NAME)
        );
    }

    /**
     * We are using the Streams instead of Pojos to control serialization of the serialized avro messages.
     * @param inputStream
     * @param outputStream
     * @param context
     * @throws IOException
     */
    @Override
    public void handleRequest(InputStream inputStream, OutputStream outputStream, Context context) throws IOException {
        //Serialize the input into a Kafka Pipe event
        KafkaPipeEvent[] input = objectMapper.readValue(inputStream, KafkaPipeEvent[].class);

        log.debug("Input event {}", input);

        List<String> results = new ArrayList<>();
        List<Object> failedMessages = new ArrayList<>();

        for (KafkaPipeEvent event : input) {
            log.debug("Processing event {}", event);

            try {
                //Payloads are Base64 encoded you need to decode them first
                byte[] decodedBody = Base64.getDecoder().decode(event.getValue());

                //Deserialize the Kafka Pipe event event into a generic Avro message
                var genericMessage = glueSchemaRegistryDeSerializationFacadeWrapper.deserialize(decodedBody, topicName);
                var jsonString = glueSchemaRegistryDeSerializationFacadeWrapper.convertToJsonString((GenericRecord) genericMessage);
                results.add(jsonString);

            } catch (Exception e) {
                log.error("Could not deserialize Kafka Pipe event {}", event);
                log.error(e);
                failedMessages.add(event);
            }
        }

        //Send errors in case you could not deserialize a Avro message
        deadLetterQFacade.sendErrorMessageToDLQ(failedMessages);

        //Write results back to output stream
        writeConvertedMessageToOutPutStream(results, outputStream);

        log.info("Successfully deserialized {} out of {} Avro messages, see {} for failed messages", results.size(), input.length, deadLetterQFacade.getDlqUrl());

        //Close the output stream as the last step
        outputStream.close();
    }


    public void writeConvertedMessageToOutPutStream(List<String> jsonMessages, OutputStream outputStream) throws IOException {
        for (String message : jsonMessages) {
            outputStream.write(message.getBytes());
        }
        outputStream.flush();
    }


}

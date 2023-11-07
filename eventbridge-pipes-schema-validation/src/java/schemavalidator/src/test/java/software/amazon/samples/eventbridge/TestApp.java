package software.amazon.samples.eventbridge;

import com.fasterxml.jackson.databind.ObjectMapper;
import example.avro.Customer;
import org.apache.avro.generic.GenericRecord;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.ArgumentCaptor;
import org.mockito.Captor;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.junit.MockitoJUnitRunner;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.SendMessageBatchRequest;

import java.io.*;
import java.util.Base64;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;


@RunWith(MockitoJUnitRunner.class)
public class TestApp {

    private App lambdaApp;

    @Mock
    private SqsClient sqsClient;

    @Mock
    private GlueSchemaRegistryDeSerializationFacade glueSchemaRegistryDeSerializationFacade;

    @Before
    public void setUp () {
        DeadLetterQFacade deadLetterQFacade = new DeadLetterQFacade(sqsClient, "someurl");
        lambdaApp = new App(glueSchemaRegistryDeSerializationFacade, deadLetterQFacade, "sometopic");
    }

    @Captor
    private ArgumentCaptor<SendMessageBatchRequest> sendMessageBatchRequestArgumentCaptor;


    @Test
    public void testUnhappyPath () throws IOException {

        when(glueSchemaRegistryDeSerializationFacade.deserialize(Mockito.any(), Mockito.any())).thenThrow(RuntimeException.class);

        KafkaPipeEvent pipeEvent = new KafkaPipeEvent();
        pipeEvent.setEventSource("testcase");

        String value = Base64.getEncoder().encodeToString("SomeValue".getBytes());
        pipeEvent.setValue(value);
        ObjectMapper mapper = new ObjectMapper();
        var serializedKafkaEvent = mapper.writeValueAsString(new KafkaPipeEvent[]{pipeEvent});

        InputStream inputStream = new ByteArrayInputStream(serializedKafkaEvent.getBytes());
        OutputStream outputStream = new ByteArrayOutputStream();

        lambdaApp.handleRequest(inputStream, outputStream, null);
        verify(sqsClient).sendMessageBatch(sendMessageBatchRequestArgumentCaptor.capture());

        assertEquals(sendMessageBatchRequestArgumentCaptor.getValue().hasEntries(), true);
        var firstEntry = sendMessageBatchRequestArgumentCaptor.getValue().entries().get(0);
        assertEquals(firstEntry.messageBody(), pipeEvent.toString());
        assertNotNull(firstEntry.id());
    }

    @Test
    public void testHappyPath () throws IOException {

        when(glueSchemaRegistryDeSerializationFacade.deserialize(Mockito.any(), Mockito.any())).thenReturn(new Customer());
        when(glueSchemaRegistryDeSerializationFacade.convertToJsonString((GenericRecord) Mockito.any())).thenReturn("JSON");

        InputStream inputStream = new FileInputStream("src/test/resources/testevent.json");
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();

        lambdaApp.handleRequest(inputStream, outputStream, null);

        String result = new String (outputStream.toByteArray());
        assertEquals(result, "JSON");
    }






}
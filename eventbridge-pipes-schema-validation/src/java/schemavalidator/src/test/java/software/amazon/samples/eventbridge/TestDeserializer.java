package software.amazon.samples.eventbridge;

import example.avro.Customer;
import org.apache.avro.Schema;
import org.apache.avro.generic.GenericDatumReader;
import org.apache.avro.generic.GenericRecord;
import org.apache.avro.io.*;
import org.apache.avro.specific.SpecificDatumReader;
import org.apache.avro.specific.SpecificDatumWriter;
import org.apache.avro.specific.SpecificRecord;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.junit.MockitoJUnitRunner;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.util.Arrays;

import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.when;

@RunWith(MockitoJUnitRunner.class)
public class TestDeserializer {

    public static final String CONVERTED_JASON_PAYLOAD = "{\"customer_account_no\":123,\"first_name\":\"Max\",\"middle_name\":null,\"last_name\":\"Mustermann\",\"email_addresses\":{\"array\":[\"Mail\"]},\"customer_address\":\"Somewhere\",\"mode_of_payment\":\"CARD\",\"customer_rating\":null}";
    private byte[] avroByteInput;
    private Schema schema;

    @Mock
    public GlueSchemaRegistryDeSerializationFacade glueSchemaRegistryDeSerializationFacade;

    @Before
    public void setupAvro () throws IOException {

        schema = new Schema.Parser().parse(new File("../../../shared/customer_schema.avsc"));

        Customer customer = Customer.newBuilder()
                .setFirstName("Max")
                .setLastName("Mustermann")
                .setCustomerAddress("Somewhere")
                .setCustomerAccountNo(123)
                .setEmailAddresses(Arrays.asList("Mail"))
                .build();



        ByteArrayOutputStream out = new ByteArrayOutputStream();
        BinaryEncoder encoder = EncoderFactory.get().directBinaryEncoder(out, null);
        DatumWriter<Customer> writer = new SpecificDatumWriter<Customer>(schema);

        writer.write(customer, encoder);
        out.close();

        avroByteInput = out.toByteArray();
    }

    @Test
    public void testGenericRecordDeserialization () throws IOException {
        when(glueSchemaRegistryDeSerializationFacade.convertToJsonString(Mockito.any(GenericRecord.class))).thenCallRealMethod();

        DatumReader<GenericRecord> reader = new GenericDatumReader<>(schema);
        Decoder decoder = DecoderFactory.get().binaryDecoder(avroByteInput, null);

        GenericRecord payload = reader.read(null, decoder);

        var conversation = glueSchemaRegistryDeSerializationFacade.convertToJsonString(payload);

        assertEquals(conversation, CONVERTED_JASON_PAYLOAD);
    }

    @Test
    public void testSpecifcRecordDeserialization () throws IOException {
        when(glueSchemaRegistryDeSerializationFacade.convertToJsonString(Mockito.any(SpecificRecord.class))).thenCallRealMethod();

        DatumReader<SpecificRecord> reader = new SpecificDatumReader<>(schema);
        Decoder decoder = DecoderFactory.get().binaryDecoder(avroByteInput, null);

        SpecificRecord payload = reader.read(null, decoder);


        var conversation = glueSchemaRegistryDeSerializationFacade.convertToJsonString(payload);

        assertEquals(conversation, CONVERTED_JASON_PAYLOAD);
    }



}

package software.amazon.samples.eventbridge;

import com.amazonaws.services.schemaregistry.common.AWSDeserializerInput;
import com.amazonaws.services.schemaregistry.common.AWSSchemaRegistryClient;
import com.amazonaws.services.schemaregistry.deserializers.GlueSchemaRegistryDeserializationFacade;
import com.amazonaws.services.schemaregistry.utils.AWSSchemaRegistryConstants;
import com.amazonaws.services.schemaregistry.utils.AvroRecordType;
import org.apache.avro.generic.GenericContainer;
import org.apache.avro.generic.GenericDatumWriter;
import org.apache.avro.generic.GenericRecord;
import org.apache.avro.io.DatumWriter;
import org.apache.avro.io.EncoderFactory;
import org.apache.avro.io.JsonEncoder;
import org.apache.avro.specific.SpecificDatumWriter;
import org.apache.avro.specific.SpecificRecord;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.services.glue.GlueClient;
import software.amazon.awssdk.services.glue.model.Compatibility;
import software.amazon.awssdk.services.glue.model.DataFormat;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.util.Properties;

/**
 * The module containing all dependencies required by the {@link App}.
 */
public class GlueSchemaRegistryDeSerializationFacade {

    private static final Logger log = LogManager.getLogger(GlueSchemaRegistryDeSerializationFacade.class);

    private final GlueSchemaRegistryDeserializationFacade glueSchemaRegistrySerializationFacade;

    public GlueSchemaRegistryDeSerializationFacade(String schemaName, String registryName) {
        Properties props = new Properties();
        props.put(AWSSchemaRegistryConstants.SCHEMA_NAME, schemaName);
        props.put(AWSSchemaRegistryConstants.REGISTRY_NAME, registryName);
        props.put(AWSSchemaRegistryConstants.DATA_FORMAT, DataFormat.AVRO.name());
        props.put(AWSSchemaRegistryConstants.AVRO_RECORD_TYPE, AvroRecordType.GENERIC_RECORD.name());
        props.put(AWSSchemaRegistryConstants.COMPATIBILITY_SETTING, Compatibility.FULL);

        log.debug("Creating Glue Schema registry {}", props);

        glueSchemaRegistrySerializationFacade = GlueSchemaRegistryDeserializationFacade.builder()
                .credentialProvider(DefaultCredentialsProvider.builder().build())
                .schemaRegistryClient(new AWSSchemaRegistryClient(GlueClient.create()))
                .properties(props)
                .build();

    }

    public Object deserialize (byte[] data, String transportName) {
            log.debug("Trying Deserializing Message");

            Object result = glueSchemaRegistrySerializationFacade.deserialize(
                    new AWSDeserializerInput(ByteBuffer.wrap(data), transportName)
            );

            log.debug("Deserialized Message");
            log.debug(result);

            return result;
    }

    public String convertToJsonString (SpecificRecord record) {
        return this.convertToJsonString((GenericContainer) record);
    }

    public String convertToJsonString (GenericRecord record) {
        return this.convertToJsonString((GenericContainer) record);
    }

    private String convertToJsonString (GenericContainer record) {
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        JsonEncoder encoder = null;
        try {
            encoder = EncoderFactory.get().jsonEncoder(record.getSchema(), outputStream);
            DatumWriter writer = record instanceof SpecificRecord ?
                    new SpecificDatumWriter<>(record.getSchema()) :
                    new GenericDatumWriter<>(record.getSchema());
            writer.write(record, encoder);
            encoder.flush();

            String jsonString = outputStream.toString();
            log.debug("Converted {} into {}", record.getClass(), jsonString);
            return jsonString;
        } catch (IOException e) {
            log.error(e);
            throw new RuntimeException(e);
        }
    }


}

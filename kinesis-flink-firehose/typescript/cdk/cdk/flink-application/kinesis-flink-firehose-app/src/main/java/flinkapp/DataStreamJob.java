package flinkapp;

import com.amazonaws.services.kinesisanalytics.runtime.KinesisAnalyticsRuntime;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import org.apache.flink.api.common.typeinfo.Types;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.connector.aws.config.AWSConfigConstants;
import org.apache.flink.connector.firehose.sink.KinesisFirehoseSink;
import org.apache.flink.shaded.jackson2.com.fasterxml.jackson.databind.JsonNode;
import org.apache.flink.shaded.jackson2.com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.windowing.assigners.SlidingProcessingTimeWindows;
import org.apache.flink.streaming.api.windowing.time.Time;
import org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer;
import org.apache.flink.streaming.connectors.kinesis.config.ConsumerConfigConstants;

import java.io.IOException;
import java.util.Map;
import java.util.Properties;

import static org.apache.flink.connector.aws.config.AWSConfigConstants.AWS_REGION;

public class DataStreamJob {

	private static final ObjectMapper jsonParser = new ObjectMapper();

	private static DataStream<String> createSourceFromStaticConfig(StreamExecutionEnvironment env) throws IOException {
		Map<String, Properties> applicationProperties = KinesisAnalyticsRuntime.getApplicationProperties();
		String inputStreamName = String.valueOf(applicationProperties.get("ConsumerStreamName").get("ConsumerStreamName"));
		return env.addSource(new FlinkKinesisConsumer<>(inputStreamName,
				new SimpleStringSchema(), applicationProperties.get("ConsumerStreamProperties")));
	}

	private static KinesisFirehoseSink<String> createFirehoseSinkFromStaticConfig() throws IOException {
		Map<String, Properties> applicationProperties = KinesisAnalyticsRuntime.getApplicationProperties();
		String outputDeliveryStreamName = String.valueOf(applicationProperties.get("DeliveryFirehoseName").get("DeliveryFirehoseName"));
		return KinesisFirehoseSink.<String>builder()
				.setFirehoseClientProperties(applicationProperties.get("DeliveryFirehoseProperties"))
				.setSerializationSchema(new SimpleStringSchema())
				.setDeliveryStreamName(outputDeliveryStreamName)
				.build();
	}

	public static void main(String[] args) throws Exception {
		final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

		DataStream<String> input = createSourceFromStaticConfig(env); // Create Kinesis Data Stream source

		input.sinkTo(createFirehoseSinkFromStaticConfig()); // Write to Firehose Delivery Stream sink

		env.execute("Stock Price"); // Execute the stream job
	}
}

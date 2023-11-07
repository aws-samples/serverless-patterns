/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.amazon.sample.flinkglue.producer;

import com.amazonaws.regions.Regions;
import com.amazonaws.services.kinesisanalytics.runtime.KinesisAnalyticsRuntime;
import com.amazonaws.services.schemaregistry.flink.avro.GlueSchemaRegistryAvroSerializationSchema;
import com.amazonaws.services.schemaregistry.utils.AWSSchemaRegistryConstants;
import com.amazonaws.services.schemaregistry.utils.AvroRecordType;
import example.avro.Customer;
import org.apache.commons.lang3.RandomStringUtils;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.functions.source.SourceFunction;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaProducer;
import org.apache.kafka.clients.CommonClientConfigs;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.common.config.SaslConfigs;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.*;

/**
 * Skeleton for a Flink DataStream Job.
 *
 * <p>For a tutorial how to write a Flink application, check the
 * tutorials and examples on the <a href="https://flink.apache.org">Flink Website</a>.
 *
 * <p>To package your application into a JAR file for execution, run
 * 'mvn clean package' on the command line.
 *
 * <p>If you change the name of the main class (with the public static void main(String[] args))
 * method, change the respective entry in the POM.xml file (simply search for 'mainClass').
 */
public class DataStreamJob {

	private static final Logger LOG = LoggerFactory.getLogger(DataStreamJob.class);

	public static final String BOOTSTRAP_SERVERS = "BOOTSTRAP_SERVERS";
	public static final String SCHEMA_NAME = "SCHEMA_NAME";
	public static final String REPOSITORY_NAME = "REPOSITORY_NAME";
	public static final String TOPIC = "TOPIC";
	public static final String GROUP_ID = "GROUP_ID";
	public static final String NUMBER_MESSAGES = "NUMBER_MESSAGES";

	private static final List<String> MANDATORY_PARAMETERS = Arrays.asList(BOOTSTRAP_SERVERS, SCHEMA_NAME, REPOSITORY_NAME, TOPIC, GROUP_ID, NUMBER_MESSAGES);



	public static void main(String[] args) throws Exception {

		final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

		Properties flinkProperties = KinesisAnalyticsRuntime.getApplicationProperties().get("FlinkApplicationProperties");

		if (flinkProperties == null) {
			LOG.error("Unable to load FlinkApplicationProperties properties from the Kinesis Analytics Runtime. Exiting.");

			return;
		}

		if (! flinkProperties.keySet().containsAll(MANDATORY_PARAMETERS)) {
			LOG.error("Missing mandatory parameters. Expected '{}' but found '{}'. Exiting.",
					String.join(", ", MANDATORY_PARAMETERS),
					flinkProperties.keySet());
			return;
		}

		Properties kafkaConfig = new Properties();
		kafkaConfig.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, flinkProperties.getProperty(BOOTSTRAP_SERVERS));
		kafkaConfig.setProperty(ConsumerConfig.GROUP_ID_CONFIG,flinkProperties.getProperty("GroupId", GROUP_ID));
		kafkaConfig.setProperty(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SASL_SSL");
		kafkaConfig.setProperty(SaslConfigs.SASL_MECHANISM, "AWS_MSK_IAM");
		kafkaConfig.setProperty(SaslConfigs.SASL_JAAS_CONFIG, "software.amazon.msk.auth.iam.IAMLoginModule required;");
		kafkaConfig.setProperty(SaslConfigs.SASL_CLIENT_CALLBACK_HANDLER_CLASS, "software.amazon.msk.auth.iam.IAMClientCallbackHandler");

		Map<String, Object> schemaRegistryConfigs = new HashMap<>();
		schemaRegistryConfigs.put(AWSSchemaRegistryConstants.AWS_REGION, flinkProperties.getProperty("Region", Regions.getCurrentRegion().getName()));
		schemaRegistryConfigs.put(AWSSchemaRegistryConstants.AVRO_RECORD_TYPE, AvroRecordType.SPECIFIC_RECORD.getName());
		schemaRegistryConfigs.put(AWSSchemaRegistryConstants.REGISTRY_NAME, flinkProperties.getProperty(REPOSITORY_NAME));
		schemaRegistryConfigs.put(AWSSchemaRegistryConstants.SCHEMA_NAME, flinkProperties.get(SCHEMA_NAME));

		String topic = flinkProperties.getProperty(TOPIC);

		FlinkKafkaProducer<Customer> producer = new FlinkKafkaProducer<>(
				topic,
				GlueSchemaRegistryAvroSerializationSchema.forSpecific(Customer.class, topic, schemaRegistryConfigs),
				kafkaConfig);


		int numberOfMessages = Integer.parseInt(flinkProperties.getProperty(NUMBER_MESSAGES));

		DataStream<Customer> stream = env.addSource(new SourceFunction<Customer>() {
			@Override
			public void run(SourceContext<Customer> ctx) throws Exception {

				for (int i=0;i<numberOfMessages;i++){
					Customer customer = Customer.newBuilder().
							setCustomerAccountNo((int) (Math.random() * 100))
							.setCustomerAddress(RandomStringUtils.randomAlphabetic(10))
							.setEmailAddresses(Arrays.asList(RandomStringUtils.randomAlphabetic(10)))
							.setFirstName(RandomStringUtils.randomAlphabetic(10))
							.setLastName(RandomStringUtils.randomAlphabetic(10)).build();

					LOG.info(customer.toString());
					Thread.sleep(100);
					ctx.collect(customer);
				}
			}

			@Override
			public void cancel() {

			}
		});

		stream.addSink(producer);
		env.execute();


		env.execute("Send Messages");
	}
}

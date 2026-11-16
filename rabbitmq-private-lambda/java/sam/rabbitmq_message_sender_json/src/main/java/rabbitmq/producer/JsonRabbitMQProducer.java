package rabbitmq.producer;

import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.AMQP;
import com.rabbitmq.client.BuiltinExchangeType;
import com.rabbitmq.client.Channel;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class JsonRabbitMQProducer {

	Properties prop;

	public static void main(String[] args) {
		
		String rabbitMQEndpoint = args[0];
		String rabbitMQUsername = SecretsManagerDecoder.getUsernameAndPassword().getUsername();
		String rabbitMQPassword = SecretsManagerDecoder.getUsernameAndPassword().getPassword();
		String rabbitMQVirtualHost = args[1];
		String rabbitMQExchange = args[2];
		String rabbitMQQueue = args[3];
		String seederKeyString = args[4];
		int numberOfMessages = Integer.parseInt(args[5]);
		String rabbitMQMessageKey = seederKeyString + "-" + JsonRabbitMQProducer.getTodayDate();
		try {
			
			JsonRabbitMQProducer.rabbitMQQueueSender(rabbitMQEndpoint, rabbitMQUsername, rabbitMQPassword, rabbitMQVirtualHost, rabbitMQExchange, rabbitMQQueue, rabbitMQMessageKey, numberOfMessages);
			System.exit(0);
		} catch (Exception e) {
			System.out.println("Exception occurred");
			e.printStackTrace();
			System.exit(-1);
		}
	}

	public static void rabbitMQQueueSender(String rabbitMQEndpoint, String rabbitMQUsername, String rabbitMQPassword, String rabbitMQVirtualHost, String rabbitMQExchange, String rabbitMQQueue, String seederKeyString, int numberOfMessages) throws Exception {
		List<String> people = JsonRabbitMQProducer.readDataFile();
		int numberOfMessagesToSend=0;
		if (people.size() > numberOfMessages) {
			numberOfMessagesToSend = numberOfMessages;
		} else {
			numberOfMessagesToSend = people.size();
		}
		
		ConnectionFactory factory = new ConnectionFactory();

		factory.setUsername(rabbitMQUsername);
		factory.setPassword(rabbitMQPassword);

		//Replace the URL with your information
		factory.setHost(rabbitMQEndpoint);
		factory.setPort(5671);
		factory.setVirtualHost(rabbitMQVirtualHost);

		// Allows client to establish a connection over TLS
		factory.useSslProtocol();

		// Create a connection
		Connection conn = factory.newConnection();

		// Create a channel
		Channel channel = conn.createChannel();
		channel.exchangeDeclare(rabbitMQExchange, BuiltinExchangeType.FANOUT, true);
		channel.queueDeclare(rabbitMQQueue, true, false, false, null);
		channel.queueBind(rabbitMQQueue, rabbitMQExchange, rabbitMQExchange.concat("-").concat(rabbitMQQueue));
		try {
			for (int i = 1; i <= numberOfMessagesToSend; i++) {
				Person thisPerson = JsonRabbitMQProducer.getPersonFromLine(people.get(i));
				String thisPersonJson = thisPerson.toJson();
				byte[] messageBodyBytes = thisPersonJson.getBytes();
				Map<String,Object>headerMap = new HashMap<String, Object>();
				headerMap.put("MessageBatchIdentifier", seederKeyString);
				headerMap.put("MessageNumberInBatch", Integer.valueOf(i));
				AMQP.BasicProperties basicProperties = new AMQP.BasicProperties.Builder()
						                               .appId("rabbitmq.producer.JsonRabbitMQProducer")
						                               .clusterId(rabbitMQEndpoint)
						                               .contentEncoding("UTF-8")
						                               .contentType("text/plain")
						                               .correlationId(seederKeyString.concat("-").concat(Integer.toString(i)))
						                               .deliveryMode(2)
						                               .expiration("60000")
						                               .headers(headerMap)
						                               .messageId(seederKeyString.concat(":").concat(Integer.toString(i)))
						                               .priority(1)
						                               .timestamp(new Date(System.currentTimeMillis()))
						                               .type("JsonRabbitMQProducer")
						                               .userId(rabbitMQUsername)
						                               .build();
				System.out.println("Now sending out one message - Number " + i);
				channel.basicPublish(rabbitMQExchange, 
						             rabbitMQExchange.concat("-").concat(rabbitMQQueue),
						             basicProperties,
			                         messageBodyBytes);
				
				
			    
			    System.out.println("Sent out one message - Number " + i + " at time = " + System.currentTimeMillis());
			}
		} catch (Exception e) {
			System.out.println("An exception occurred - " + e.getMessage());
			e.printStackTrace();
		}

	}

	public static Properties readPropertiesFile(String fileName) throws FileNotFoundException, IOException {
		FileInputStream fis = null;
		Properties prop = null;
		try {
			fis = new FileInputStream(fileName);
			prop = new Properties();
			prop.load(fis);
		} catch (FileNotFoundException fnfe) {
			fnfe.printStackTrace();
			throw new FileNotFoundException("Not a valid property file path");
		} catch (IOException ioe) {
			ioe.printStackTrace();
			throw new IOException("Problem reading property file. Check permissions");
		} finally {
			fis.close();
		}
		return prop;
	}
	
	public static List<String> readDataFile() {
		List<String> personList = new ArrayList<String>();
		InputStream is = JsonRabbitMQProducer.class.getClassLoader().getResourceAsStream("us-500.csv");
		BufferedReader bf = new BufferedReader(new InputStreamReader(is));
		String thisLine = null;
		try {
			thisLine = bf.readLine();
			while (null != thisLine) {
				personList.add(thisLine);
				thisLine = bf.readLine();
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return personList;
	}
	
	public static Person getPersonFromLine(String line) {
		
		//String[] fields = line.split(",");
		String[] fields = line.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", -1);
		Person thisPerson = new Person();
		thisPerson.setFirstname(fields[0]);
		thisPerson.setLastname(fields[1]);
		thisPerson.setCompany(fields[2]);
		thisPerson.setStreet(fields[3]);
		thisPerson.setCity(fields[4]);
		thisPerson.setCounty(fields[5]);
		thisPerson.setState(fields[6]);
		thisPerson.setZip(fields[7]);
		thisPerson.setHomePhone(fields[8]);
		thisPerson.setCellPhone(fields[9]);
		thisPerson.setEmail(fields[10]);
		thisPerson.setWebsite(fields[11]);
		return thisPerson;
	}
	
	public static String getTodayDate() {
		
		LocalDateTime ldt = LocalDateTime.now();
        String formattedDateStr = DateTimeFormatter.ofPattern("MM-dd-YYYY-HH-MM-SS").format(ldt);
        return formattedDateStr;
	}
}

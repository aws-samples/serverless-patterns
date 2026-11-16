package activemq.producer;

import java.util.ArrayList;
import java.util.List;
import java.util.Properties;


import org.apache.activemq.ActiveMQConnectionFactory;
import org.apache.activemq.jms.pool.PooledConnectionFactory;
import javax.jms.TextMessage;
import javax.jms.Connection;
import javax.jms.Session;
import javax.jms.Destination;
import javax.jms.MessageProducer;
import javax.jms.DeliveryMode;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class JsonActiveMQProducer {

	Properties prop;

	public static void main(String[] args) {
		
		String activeMQEndpoint = args[0];
		String activeMQUsername = SecretsManagerDecoder.getUsernameAndPassword().getUsername();
		String activeMQPassword = SecretsManagerDecoder.getUsernameAndPassword().getPassword();
		String activeMQQueue = args[1];
		String seederKeyString = args[2];
		int numberOfMessages = Integer.parseInt(args[3]);
		String activeMQMessageKey = seederKeyString + "-" + JsonActiveMQProducer.getTodayDate();
		try {
			JsonActiveMQProducer.activeMQQueueReceiver(activeMQEndpoint, activeMQUsername, activeMQPassword, activeMQQueue, activeMQMessageKey, numberOfMessages);
			System.exit(0);
		} catch (Exception e) {
			System.out.println("Exception occurred");
			e.printStackTrace();
			System.exit(-1);
		}
	}

	public static void activeMQQueueReceiver(String activeMQEndpoint, String activeMQUsername, String activeMQPassword, String activeMQQueue, String seederKeyString, int numberOfMessages) throws Exception {
		List<String> people = JsonActiveMQProducer.readDataFile();
		int numberOfMessagesToSend=0;
		if (people.size() > numberOfMessages) {
			numberOfMessagesToSend = numberOfMessages;
		} else {
			numberOfMessagesToSend = people.size();
		}
		
		final ActiveMQConnectionFactory connectionFactory =
                createActiveMQConnectionFactory(activeMQEndpoint, activeMQUsername, activeMQPassword);
        final PooledConnectionFactory pooledConnectionFactory =
                createPooledConnectionFactory(connectionFactory);
		
        final Connection producerConnection = pooledConnectionFactory
                .createConnection();
        producerConnection.start();
    
        // Create a session.
        final Session producerSession = producerConnection
                .createSession(false, Session.AUTO_ACKNOWLEDGE);
    
        // Create a queue 
   
        Destination producerDestination;
		try {
			producerDestination = producerSession
			        .createQueue(activeMQQueue);
			// Create a producer from the session to the queue.
	        final MessageProducer producer = producerSession
	                .createProducer(producerDestination);
	        producer.setDeliveryMode(DeliveryMode.NON_PERSISTENT);
	        
	        for (int i = 1; i <= numberOfMessagesToSend; i++) {
				Person thisPerson = JsonActiveMQProducer.getPersonFromLine(people.get(i));
				String thisPersonJson = thisPerson.toJson();
				// Create a message.
		        TextMessage producerMessage = producerSession
		                .createTextMessage(thisPersonJson);
		        producerMessage.setJMSCorrelationID(seederKeyString + "-" + i);
		        producerMessage.setJMSType("TextMessage");
		        producerMessage.setStringProperty("MessageBatchIdentifier", seederKeyString);
		        producerMessage.setIntProperty("MessageNumberInBatch", i);
		        producerMessage.setJMSExpiration(1800000);
		        producerMessage.setJMSDeliveryMode(DeliveryMode.PERSISTENT);
		        // Send the message.
		        long currentTime = System.currentTimeMillis();
		        producer.send(producerMessage);
		        System.out.println("Sent out one message - Number " + i + " at time = " + currentTime);
			}
	        producer.close();
	        
		} catch (Exception e1) {
			System.out.println("Queue creation failed. Queue may already exist");
			System.out.println(e1.getMessage());
			e1.printStackTrace();
		} finally {
			producerSession.close();
	        producerConnection.close();
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
		InputStream is = JsonActiveMQProducer.class.getClassLoader().getResourceAsStream("us-500.csv");
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
	
	private static PooledConnectionFactory
    createPooledConnectionFactory(ActiveMQConnectionFactory connectionFactory) {
        // Create a pooled connection factory.
        final PooledConnectionFactory pooledConnectionFactory =
                new PooledConnectionFactory();
        pooledConnectionFactory.setConnectionFactory(connectionFactory);
        pooledConnectionFactory.setMaxConnections(10);
        return pooledConnectionFactory;
    }
    
    private static ActiveMQConnectionFactory createActiveMQConnectionFactory(String activeMQEndpoint, String activeMQUsername, String activeMQPassword) {
        // Create a connection factory.
        final ActiveMQConnectionFactory connectionFactory =
                new ActiveMQConnectionFactory(activeMQEndpoint);
    
        // Pass the sign-in credentials.
        connectionFactory.setUserName(activeMQUsername);
        connectionFactory.setPassword(activeMQPassword);
        return connectionFactory;
    }

}

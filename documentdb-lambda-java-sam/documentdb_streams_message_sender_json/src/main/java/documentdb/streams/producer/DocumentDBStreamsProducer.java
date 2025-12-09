package documentdb.streams.producer;

import java.util.ArrayList;
import java.util.List;
import org.bson.Document;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

/*
 * Create two secrets in Secret Manager
 * Create one secret of type DocumentDB Secret and name it AmazonDocumentDBCredentials
 * In this secret configure the username and password for the DocumentDB cluster
 * Create another secret that is not of any specific database
 * Name this secret AmazonDocumentDBTruststore
 * In this secret, create two string secrets truststore and truststorepassword
 * For details on how to create the truststore refer to the following document
 * https://docs.aws.amazon.com/documentdb/latest/developerguide/connect_programmatically.html
 * refer to the Java tab under Connecting with TLS Enabled
 * The truststore secret should refer to the location of the truststore on the machine from where
 * you will run this program (Cloud9 or an EC2 machine or even your local machine)
 * The truststorepassword secret should have the password of the truststore
 * 
 * To run this program pass the DocumentDB Database Name and Collection Name as the first two parameters
 * You can use the Mongo Shell to create the database and the collection
 * 
 * Refer to Step 8 in the document https://docs.aws.amazon.com/documentdb/latest/developerguide/connect-ec2.html
 * on how to create databases and collections using the Mongo Client
 * 
 */

public class DocumentDBStreamsProducer {

	public static void main(String[] args) {
		try {
			DocumentDBStreamsProducer.documentdbUpdater(args[0], args[1],
					args[2].concat("-").concat(DocumentDBStreamsProducer.getTodayDate()), Integer.parseInt(args[3]));
		} catch (Exception e) {
			System.out.println(
					"Pass four parameters: 1 - DocumentDB Database Name, 2 - DocumentDB Collection Name, 3 - A string to be used as key for this batch of messages, 3 - Number of Messages in this batch");
			e.printStackTrace();
		}
	}

	public static void documentdbUpdater(String documentdbDatabase, String documentdbCollection, String messageKey,
			int numberOfMessages) {

		AmazonDocumentDBCredentials amazonDocumentDBCredentials = SecretsManagerDecoder.getAmazonDocumentDBCredentials();
		AmazonDocumentDBTruststore amazonDocumentDBTruststore = SecretsManagerDecoder.getAmazonDocumentDBTruststore();
		
		String documentdbHost = amazonDocumentDBCredentials.getHost();
		String documentdbPort = amazonDocumentDBCredentials.getPort();
		String username = amazonDocumentDBCredentials.getUsername();
		String password = amazonDocumentDBCredentials.getPassword();
		String truststore = amazonDocumentDBTruststore.getTruststore();
		String truststorePassword = amazonDocumentDBTruststore.getTruststorepassword();
		
		String clusterEndpoint = documentdbHost + ":" + documentdbPort;
		
		String template = "mongodb://%s:%s@%s/sample-database?ssl=true&replicaSet=rs0&readpreference=%s";
		
		String readPreference = "secondaryPreferred";
        String connectionString = String.format(template, username, password, clusterEndpoint, readPreference);
        
        System.out.println("Connection String = " + connectionString);
        
        System.setProperty("javax.net.ssl.trustStore", truststore);
        System.setProperty("javax.net.ssl.trustStorePassword", truststorePassword);
        
        MongoClient mongoClient = MongoClients.create(connectionString);
        MongoDatabase documentDBStreamsLambdaTriggerDB = mongoClient.getDatabase(documentdbDatabase);
        MongoCollection<Document> customersCollection = documentDBStreamsLambdaTriggerDB.getCollection(documentdbCollection);

		
		List<String> people = DocumentDBStreamsProducer.readDataFile();
		int numberOfMessagesToSend = 0;
		if (people.size() > numberOfMessages) {
			numberOfMessagesToSend = numberOfMessages;
		} else {
			numberOfMessagesToSend = people.size();
		}
		
		for (int i = 1; i <= numberOfMessagesToSend; i++) {
			Person thisPerson = DocumentDBStreamsProducer.getPersonFromLine(people.get(i), messageKey + "-" + i);
			DocumentDBStreamsProducer.sendMessage(customersCollection, thisPerson);
		}
	}

	public static void sendMessage(MongoCollection<Document> customersCollection, Person thisPerson) {

		System.out.println("Now going to insert a row in DynamoDB for messageID = " + thisPerson.get_id());
		customersCollection.insertOne(DocumentDBStreamsProducer.getDocument(thisPerson));
		System.out.println("Now done inserting a row in DynamoDB for messageID = " + thisPerson.get_id());
	}

	public static List<String> readDataFile() {
		List<String> personList = new ArrayList<String>();
		InputStream is = DocumentDBStreamsProducer.class.getClassLoader().getResourceAsStream("us-500.csv");
		BufferedReader bf = new BufferedReader(new InputStreamReader(is));
		String thisLine = null;
		try {
			thisLine = bf.readLine();
			while (null != thisLine) {
				personList.add(thisLine);
				thisLine = bf.readLine();
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		return personList;
	}

	public static Person getPersonFromLine(String line, String id) {
		String[] fields = line.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", -1);
		Person thisPerson = new Person();
		thisPerson.set_id(id);
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
	
	public static Document getDocument(Person person) {
		Document document = new Document();
		document.append("_id", person.get_id());
		document.append("Firstname", person.getFirstname());
		document.append("Lastname", person.getLastname());
		document.append("Street", person.getStreet());
		document.append("City", person.getCity());
		document.append("County", person.getCounty());
		document.append("State", person.getState());
		document.append("Zip", person.getZip());
		document.append("HomePhone", person.getHomePhone());
		document.append("CellPhone", person.getCellPhone());
		document.append("Email", person.getEmail());
		document.append("Company", person.getCompany());
		document.append("Website", person.getWebsite());
		return document;
	}
}

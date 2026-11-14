package documentdb.streams.producer;

import java.util.Objects;

public class AmazonDocumentDBTruststore {

	String truststore;
	String truststorepassword;
	
	
	
	/**
	 * 
	 */
	public AmazonDocumentDBTruststore() {
		super();
	}



	/**
	 * @param truststore
	 * @param truststorepassword
	 */
	public AmazonDocumentDBTruststore(String truststore, String truststorepassword) {
		super();
		this.truststore = truststore;
		this.truststorepassword = truststorepassword;
	}



	/**
	 * @return the truststore
	 */
	public String getTruststore() {
		return truststore;
	}



	/**
	 * @param truststore the truststore to set
	 */
	public void setTruststore(String truststore) {
		this.truststore = truststore;
	}



	/**
	 * @return the truststorepassword
	 */
	public String getTruststorepassword() {
		return truststorepassword;
	}



	/**
	 * @param truststorepassword the truststorepassword to set
	 */
	public void setTruststorepassword(String truststorepassword) {
		this.truststorepassword = truststorepassword;
	}



	@Override
	public int hashCode() {
		return Objects.hash(truststore, truststorepassword);
	}



	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		AmazonDocumentDBTruststore other = (AmazonDocumentDBTruststore) obj;
		return Objects.equals(truststore, other.truststore)
				&& Objects.equals(truststorepassword, other.truststorepassword);
	}



	@Override
	public String toString() {
		return "AmazonDocumentDBTruststore [truststore=" + truststore + ", truststorepassword=" + truststorepassword
				+ "]";
	}
	
	
	
}

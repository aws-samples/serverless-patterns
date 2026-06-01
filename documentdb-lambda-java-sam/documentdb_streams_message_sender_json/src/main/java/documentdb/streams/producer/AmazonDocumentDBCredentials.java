package documentdb.streams.producer;

import java.util.Objects;

public class AmazonDocumentDBCredentials {

	String username;
	String password;
	String engine;
	String host;
	String port;
	String ssl;
	String dbClusterIdentifier;

	/**
	 * 
	 */
	public AmazonDocumentDBCredentials() {
		super();
	}

	/**
	 * @param username
	 * @param password
	 * @param engine
	 * @param host
	 * @param port
	 * @param ssl
	 * @param dbClusterIdentifier
	 */
	public AmazonDocumentDBCredentials(String username, String password, String engine, String host, String port,
			String ssl, String dbClusterIdentifier) {
		super();
		this.username = username;
		this.password = password;
		this.engine = engine;
		this.host = host;
		this.port = port;
		this.ssl = ssl;
		this.dbClusterIdentifier = dbClusterIdentifier;
	}

	/**
	 * @return the username
	 */
	public String getUsername() {
		return username;
	}

	/**
	 * @param username the username to set
	 */
	public void setUsername(String username) {
		this.username = username;
	}

	/**
	 * @return the password
	 */
	public String getPassword() {
		return password;
	}

	/**
	 * @param password the password to set
	 */
	public void setPassword(String password) {
		this.password = password;
	}

	/**
	 * @return the engine
	 */
	public String getEngine() {
		return engine;
	}

	/**
	 * @param engine the engine to set
	 */
	public void setEngine(String engine) {
		this.engine = engine;
	}

	/**
	 * @return the host
	 */
	public String getHost() {
		return host;
	}

	/**
	 * @param host the host to set
	 */
	public void setHost(String host) {
		this.host = host;
	}

	/**
	 * @return the port
	 */
	public String getPort() {
		return port;
	}

	/**
	 * @param port the port to set
	 */
	public void setPort(String port) {
		this.port = port;
	}

	/**
	 * @return the ssl
	 */
	public String getSsl() {
		return ssl;
	}

	/**
	 * @param ssl the ssl to set
	 */
	public void setSsl(String ssl) {
		this.ssl = ssl;
	}

	/**
	 * @return the dbClusterIdentifier
	 */
	public String getDbClusterIdentifier() {
		return dbClusterIdentifier;
	}

	/**
	 * @param dbClusterIdentifier the dbClusterIdentifier to set
	 */
	public void setDbClusterIdentifier(String dbClusterIdentifier) {
		this.dbClusterIdentifier = dbClusterIdentifier;
	}

	@Override
	public int hashCode() {
		return Objects.hash(dbClusterIdentifier, engine, host, password, port, ssl, username);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		AmazonDocumentDBCredentials other = (AmazonDocumentDBCredentials) obj;
		return Objects.equals(dbClusterIdentifier, other.dbClusterIdentifier) && Objects.equals(engine, other.engine)
				&& Objects.equals(host, other.host) && Objects.equals(password, other.password)
				&& Objects.equals(port, other.port) && Objects.equals(ssl, other.ssl)
				&& Objects.equals(username, other.username);
	}

	@Override
	public String toString() {
		return "AmazonDocumentDBCredentials [username=" + username + ", password=" + password + ", engine=" + engine
				+ ", host=" + host + ", port=" + port + ", ssl=" + ssl + ", dbClusterIdentifier=" + dbClusterIdentifier
				+ "]";
	}
	
	
	
}

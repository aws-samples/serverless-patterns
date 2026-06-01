package com.amazonaws.services.lambda.samples.events.documentdbstreams.models;

import java.util.Objects;

public class NS {
    private String db;
    private String coll;
	/**
	 * 
	 */
	public NS() {
		super();
	}
	/**
	 * @param db
	 * @param coll
	 */
	public NS(String db, String coll) {
		super();
		this.db = db;
		this.coll = coll;
	}
	/**
	 * @return the db
	 */
	public String getDb() {
		return db;
	}
	/**
	 * @param db the db to set
	 */
	public void setDb(String db) {
		this.db = db;
	}
	/**
	 * @return the coll
	 */
	public String getColl() {
		return coll;
	}
	/**
	 * @param coll the coll to set
	 */
	public void setColl(String coll) {
		this.coll = coll;
	}
	@Override
	public int hashCode() {
		return Objects.hash(coll, db);
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		NS other = (NS) obj;
		return Objects.equals(coll, other.coll) && Objects.equals(db, other.db);
	}
	@Override
	public String toString() {
		return "NS [db=" + db + ", coll=" + coll + "]";
	}
    
}
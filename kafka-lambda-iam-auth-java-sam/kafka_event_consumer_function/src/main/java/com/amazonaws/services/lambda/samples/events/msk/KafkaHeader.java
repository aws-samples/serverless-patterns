package com.amazonaws.services.lambda.samples.events.msk;

import java.util.Objects;

public class KafkaHeader {
	String key;
	String value;
	/**
	 * 
	 */
	public KafkaHeader() {
		super();
	}
	/**
	 * @param key
	 * @param value
	 */
	public KafkaHeader(String key, String value) {
		super();
		this.key = key;
		this.value = value;
	}
	/**
	 * @return the key
	 */
	public String getKey() {
		return key;
	}
	/**
	 * @param key the key to set
	 */
	public void setKey(String key) {
		this.key = key;
	}
	/**
	 * @return the value
	 */
	public String getValue() {
		return value;
	}
	/**
	 * @param value the value to set
	 */
	public void setValue(String value) {
		this.value = value;
	}
	@Override
	public int hashCode() {
		return Objects.hash(key, value);
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		KafkaHeader other = (KafkaHeader) obj;
		return Objects.equals(key, other.key) && Objects.equals(value, other.value);
	}
	@Override
	public String toString() {
		return "KafkaHeader [key=" + key + ", value=" + value + "]";
	}
	
}

package com.amazonaws.services.lambda.samples.events.documentdbstreams.models;

import java.util.Objects;

public class Timestamp {
    private long t;
    private long i;
	/**
	 * 
	 */
	public Timestamp() {
		super();
	}
	/**
	 * @param t
	 * @param i
	 */
	public Timestamp(long t, long i) {
		super();
		this.t = t;
		this.i = i;
	}
	/**
	 * @return the t
	 */
	public long getT() {
		return t;
	}
	/**
	 * @param t the t to set
	 */
	public void setT(long t) {
		this.t = t;
	}
	/**
	 * @return the i
	 */
	public long getI() {
		return i;
	}
	/**
	 * @param i the i to set
	 */
	public void setI(long i) {
		this.i = i;
	}
	@Override
	public int hashCode() {
		return Objects.hash(i, t);
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Timestamp other = (Timestamp) obj;
		return i == other.i && t == other.t;
	}
	@Override
	public String toString() {
		return "Timestamp [t=" + t + ", i=" + i + "]";
	}
    
}

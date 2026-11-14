package com.amazonaws.services.lambda.samples.events.documentdbstreams.models;

import java.util.Objects;

public class ClusterTime {
    private Timestamp $timestamp;

	/**
	 * 
	 */
	public ClusterTime() {
		super();
	}

	/**
	 * @param $timestamp
	 */
	public ClusterTime(Timestamp $timestamp) {
		super();
		this.$timestamp = $timestamp;
	}

	/**
	 * @return the $timestamp
	 */
	public Timestamp get$timestamp() {
		return $timestamp;
	}

	/**
	 * @param $timestamp the $timestamp to set
	 */
	public void set$timestamp(Timestamp $timestamp) {
		this.$timestamp = $timestamp;
	}

	@Override
	public int hashCode() {
		return Objects.hash($timestamp);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		ClusterTime other = (ClusterTime) obj;
		return Objects.equals($timestamp, other.$timestamp);
	}

	@Override
	public String toString() {
		return "ClusterTime [$timestamp=" + $timestamp + "]";
	}
    
	
}

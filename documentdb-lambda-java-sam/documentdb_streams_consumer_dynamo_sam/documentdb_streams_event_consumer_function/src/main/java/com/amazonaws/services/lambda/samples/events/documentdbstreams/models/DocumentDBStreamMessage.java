package com.amazonaws.services.lambda.samples.events.documentdbstreams.models;

import java.util.Arrays;
import java.util.Objects;

public class DocumentDBStreamMessage {
    private String eventSourceArn;
    private String eventSource;
    private EventElement[] events;
	/**
	 * 
	 */
	public DocumentDBStreamMessage() {
		super();
	}
	/**
	 * @param eventSourceArn
	 * @param eventSource
	 * @param events
	 */
	public DocumentDBStreamMessage(String eventSourceArn, String eventSource, EventElement[] events) {
		super();
		this.eventSourceArn = eventSourceArn;
		this.eventSource = eventSource;
		this.events = events;
	}
	/**
	 * @return the eventSourceArn
	 */
	public String getEventSourceArn() {
		return eventSourceArn;
	}
	/**
	 * @param eventSourceArn the eventSourceArn to set
	 */
	public void setEventSourceArn(String eventSourceArn) {
		this.eventSourceArn = eventSourceArn;
	}
	/**
	 * @return the eventSource
	 */
	public String getEventSource() {
		return eventSource;
	}
	/**
	 * @param eventSource the eventSource to set
	 */
	public void setEventSource(String eventSource) {
		this.eventSource = eventSource;
	}
	/**
	 * @return the events
	 */
	public EventElement[] getEvents() {
		return events;
	}
	/**
	 * @param events the events to set
	 */
	public void setEvents(EventElement[] events) {
		this.events = events;
	}
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + Arrays.hashCode(events);
		result = prime * result + Objects.hash(eventSource, eventSourceArn);
		return result;
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		DocumentDBStreamMessage other = (DocumentDBStreamMessage) obj;
		return Objects.equals(eventSource, other.eventSource) && Objects.equals(eventSourceArn, other.eventSourceArn)
				&& Arrays.equals(events, other.events);
	}
	@Override
	public String toString() {
		return "DocumentDBStreamMessage [eventSourceArn=" + eventSourceArn + ", eventSource=" + eventSource
				+ ", events=" + Arrays.toString(events) + "]";
	}
    
}
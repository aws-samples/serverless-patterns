package com.amazonaws.services.lambda.samples.events.documentdbstreams.models;

import java.util.Objects;

public class EventElement {
    private EventEvent event;

	/**
	 * 
	 */
	public EventElement() {
		super();
	}

	/**
	 * @param event
	 */
	public EventElement(EventEvent event) {
		super();
		this.event = event;
	}

	/**
	 * @return the event
	 */
	public EventEvent getEvent() {
		return event;
	}

	/**
	 * @param event the event to set
	 */
	public void setEvent(EventEvent event) {
		this.event = event;
	}

	@Override
	public int hashCode() {
		return Objects.hash(event);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		EventElement other = (EventElement) obj;
		return Objects.equals(event, other.event);
	}

	@Override
	public String toString() {
		return "EventElement [event=" + event + "]";
	}
    
}
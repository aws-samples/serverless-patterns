package com.amazonaws.services.lambda.samples.events.documentdbstreams.models;

import java.util.Objects;

public class DocumentKey {
    private String _id;

	/**
	 * 
	 */
	public DocumentKey() {
		super();
	}

	/**
	 * @param _id
	 */
	public DocumentKey(String _id) {
		super();
		this._id = _id;
	}

	/**
	 * @return the _id
	 */
	public String get_id() {
		return _id;
	}

	/**
	 * @param _id the _id to set
	 */
	public void set_id(String _id) {
		this._id = _id;
	}

	@Override
	public int hashCode() {
		return Objects.hash(_id);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		DocumentKey other = (DocumentKey) obj;
		return Objects.equals(_id, other._id);
	}

	@Override
	public String toString() {
		return "DocumentKey [_id=" + _id + "]";
	}
    
}
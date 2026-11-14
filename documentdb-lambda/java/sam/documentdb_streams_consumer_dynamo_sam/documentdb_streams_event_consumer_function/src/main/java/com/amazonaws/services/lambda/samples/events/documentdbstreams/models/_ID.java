package com.amazonaws.services.lambda.samples.events.documentdbstreams.models;

import java.util.Objects;

public class _ID {
	private String _data;

	/**
	 * 
	 */
	public _ID() {
		super();
	}

	/**
	 * @param _data
	 */
	public _ID(String _data) {
		super();
		this._data = _data;
	}

	/**
	 * @return the _data
	 */
	public String get_data() {
		return _data;
	}

	/**
	 * @param _data the _data to set
	 */
	public void set_data(String _data) {
		this._data = _data;
	}

	@Override
	public int hashCode() {
		return Objects.hash(_data);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		_ID other = (_ID) obj;
		return Objects.equals(_data, other._data);
	}

	@Override
	public String toString() {
		return "_ID [_data=" + _data + "]";
	}
    
}
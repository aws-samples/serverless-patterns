/**
 * 
 */
package com.amazonaws.services.lambda.samples.events.das.models.aurorastreams;

import java.io.Serializable;
import java.util.Objects;

/*
 * Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with
 * the License. A copy of the License is located at
 *
 * http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
 * CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions
 * and limitations under the License.
 * 
 * This class recplicated the structure of the Aurora DAS message
 * The databaseActivityEvents contains a base 64 encoded version of 
 * the byte array for an encrypted JSON string that is replicated by the 
 * PostgresActivityRecords class.
 * The Key contains the base 64 encoded byte array that contains the key
 * that is used to encrypt the Aurora DAS message
 */
public class PostgresActivity implements Cloneable, Serializable {
	private static final long serialVersionUID = -5117472785374732554L;
	String type;
	String version;
	String databaseActivityEvents;
	String key;

	/**
	 * 
	 */
	public PostgresActivity() {
		super();
	}

	/**
	 * @param type
	 * @param version
	 * @param databaseActivityEvents
	 * @param key
	 */
	public PostgresActivity(String type, String version, String databaseActivityEvents, String key) {
		super();
		this.type = type;
		this.version = version;
		this.databaseActivityEvents = databaseActivityEvents;
		this.key = key;
	}

	/**
	 * @return the type
	 */
	public String getType() {
		return type;
	}

	/**
	 * @param type the type to set
	 */
	public void setType(String type) {
		this.type = type;
	}

	/**
	 * @return the version
	 */
	public String getVersion() {
		return version;
	}

	/**
	 * @param version the version to set
	 */
	public void setVersion(String version) {
		this.version = version;
	}

	/**
	 * @return the databaseActivityEvents
	 */
	public String getDatabaseActivityEvents() {
		return databaseActivityEvents;
	}

	/**
	 * @param databaseActivityEvents the databaseActivityEvents to set
	 */
	public void setDatabaseActivityEvents(String databaseActivityEvents) {
		this.databaseActivityEvents = databaseActivityEvents;
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

	@Override
	public int hashCode() {
		return Objects.hash(databaseActivityEvents, key, type, version);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}
		if (!(obj instanceof PostgresActivity)) {
			return false;
		}
		PostgresActivity other = (PostgresActivity) obj;
		return Objects.equals(databaseActivityEvents, other.databaseActivityEvents) && Objects.equals(key, other.key)
				&& Objects.equals(type, other.type) && Objects.equals(version, other.version);
	}

	@Override
	public String toString() {
		return "PostgresActivity [type=" + type + ", version=" + version + ", databaseActivityEvents="
				+ databaseActivityEvents + ", key=" + key + "]";
	}

}

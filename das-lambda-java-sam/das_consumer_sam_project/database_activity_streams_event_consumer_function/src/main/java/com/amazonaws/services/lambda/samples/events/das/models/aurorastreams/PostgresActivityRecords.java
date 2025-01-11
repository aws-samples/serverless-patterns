/**
 * 
 */
package com.amazonaws.services.lambda.samples.events.das.models.aurorastreams;

import java.io.Serializable;
import java.util.List;
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
 */
public class PostgresActivityRecords implements Cloneable, Serializable {
	/**
	 * 
	 */
	private static final long serialVersionUID = -8723512993989716213L;
	String type;
	String clusterId;
	String instanceId;
	List<PostgresActivityEvent> databaseActivityEventList;

	/**
	 * 
	 */
	public PostgresActivityRecords() {
		super();
	}

	/**
	 * @param type
	 * @param clusterId
	 * @param instanceId
	 * @param databaseActivityEventList
	 */
	public PostgresActivityRecords(String type, String clusterId, String instanceId,
			List<PostgresActivityEvent> databaseActivityEventList) {
		super();
		this.type = type;
		this.clusterId = clusterId;
		this.instanceId = instanceId;
		this.databaseActivityEventList = databaseActivityEventList;
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
	 * @return the clusterId
	 */
	public String getClusterId() {
		return clusterId;
	}

	/**
	 * @param clusterId the clusterId to set
	 */
	public void setClusterId(String clusterId) {
		this.clusterId = clusterId;
	}

	/**
	 * @return the instanceId
	 */
	public String getInstanceId() {
		return instanceId;
	}

	/**
	 * @param instanceId the instanceId to set
	 */
	public void setInstanceId(String instanceId) {
		this.instanceId = instanceId;
	}

	/**
	 * @return the databaseActivityEventList
	 */
	public List<PostgresActivityEvent> getDatabaseActivityEventList() {
		return databaseActivityEventList;
	}

	/**
	 * @param databaseActivityEventList the databaseActivityEventList to set
	 */
	public void setDatabaseActivityEventList(List<PostgresActivityEvent> databaseActivityEventList) {
		this.databaseActivityEventList = databaseActivityEventList;
	}

	@Override
	public int hashCode() {
		return Objects.hash(clusterId, databaseActivityEventList, instanceId, type);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}
		if (!(obj instanceof PostgresActivityRecords)) {
			return false;
		}
		PostgresActivityRecords other = (PostgresActivityRecords) obj;
		return Objects.equals(clusterId, other.clusterId)
				&& Objects.equals(databaseActivityEventList, other.databaseActivityEventList)
				&& Objects.equals(instanceId, other.instanceId) && Objects.equals(type, other.type);
	}

	@Override
	public String toString() {
		return "PostgresActivityRecords [type=" + type + ", clusterId=" + clusterId + ", instanceId=" + instanceId
				+ ", databaseActivityEventList=" + databaseActivityEventList + "]";
	}

}

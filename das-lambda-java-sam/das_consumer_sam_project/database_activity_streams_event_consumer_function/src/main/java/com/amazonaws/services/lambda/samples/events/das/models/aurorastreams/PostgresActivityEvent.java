package com.amazonaws.services.lambda.samples.events.das.models.aurorastreams;

import java.io.Serializable;
import java.util.List;
import java.util.Objects;

import com.google.gson.annotations.SerializedName;

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
public class PostgresActivityEvent implements Serializable, Cloneable {

	/**
	 * 
	 */
	private static final long serialVersionUID = 5556123487821392857L;
	@SerializedName("class")
	String _class;
	String clientApplication;
	String command;
	String commandText;
	String databaseName;
	String dbProtocol;
	String dbUserName;
	String endTime;
	String errorMessage;
	String exitCode;
	String logTime;
	String netProtocol;
	String objectName;
	String objectType;
	List<String> paramList;
	String pid;
	String remoteHost;
	String remotePort;
	String rowCount;
	String serverHost;
	String serverType;
	String serverVersion;
	String serviceName;
	String sessionId;
	String startTime;
	String statementId;
	String substatementId;
	String transactionId;
	String type;

	/**
	 * 
	 */
	public PostgresActivityEvent() {
		super();
	}

	/**
	 * @param clientApplication
	 * @param command
	 * @param commandText
	 * @param databaseName
	 * @param dbProtocol
	 * @param dbUserName
	 * @param endTime
	 * @param errorMessage
	 * @param exitCode
	 * @param logTime
	 * @param netProtocol
	 * @param objectName
	 * @param objectType
	 * @param paramList
	 * @param pid
	 * @param remoteHost
	 * @param remotePort
	 * @param rowCount
	 * @param serverHost
	 * @param serverType
	 * @param serverVersion
	 * @param serviceName
	 * @param sessionId
	 * @param startTime
	 * @param statementId
	 * @param substatementId
	 * @param transactionId
	 * @param type
	 */
	public PostgresActivityEvent(String _class, String clientApplication, String command, String commandText,
			String databaseName, String dbProtocol, String dbUserName, String endTime, String errorMessage,
			String exitCode, String logTime, String netProtocol, String objectName, String objectType,
			List<String> paramList, String pid, String remoteHost, String remotePort, String rowCount,
			String serverHost, String serverType, String serverVersion, String serviceName, String sessionId,
			String startTime, String statementId, String substatementId, String transactionId, String type) {
		super();
		this._class = _class;
		this.clientApplication = clientApplication;
		this.command = command;
		this.commandText = commandText;
		this.databaseName = databaseName;
		this.dbProtocol = dbProtocol;
		this.dbUserName = dbUserName;
		this.endTime = endTime;
		this.errorMessage = errorMessage;
		this.exitCode = exitCode;
		this.logTime = logTime;
		this.netProtocol = netProtocol;
		this.objectName = objectName;
		this.objectType = objectType;
		this.paramList = paramList;
		this.pid = pid;
		this.remoteHost = remoteHost;
		this.remotePort = remotePort;
		this.rowCount = rowCount;
		this.serverHost = serverHost;
		this.serverType = serverType;
		this.serverVersion = serverVersion;
		this.serviceName = serviceName;
		this.sessionId = sessionId;
		this.startTime = startTime;
		this.statementId = statementId;
		this.substatementId = substatementId;
		this.transactionId = transactionId;
		this.type = type;
	}

	/**
	 * @return the _class
	 */
	public String get_class() {
		return _class;
	}

	/**
	 * @param _class the _class to set
	 */
	public void set_class(String _class) {
		this._class = _class;
	}

	/**
	 * @return the clientApplication
	 */
	public String getClientApplication() {
		return clientApplication;
	}

	/**
	 * @param clientApplication the clientApplication to set
	 */
	public void setClientApplication(String clientApplication) {
		this.clientApplication = clientApplication;
	}

	/**
	 * @return the command
	 */
	public String getCommand() {
		return command;
	}

	/**
	 * @param command the command to set
	 */
	public void setCommand(String command) {
		this.command = command;
	}

	/**
	 * @return the commandText
	 */
	public String getCommandText() {
		return commandText;
	}

	/**
	 * @param commandText the commandText to set
	 */
	public void setCommandText(String commandText) {
		this.commandText = commandText;
	}

	/**
	 * @return the databaseName
	 */
	public String getDatabaseName() {
		return databaseName;
	}

	/**
	 * @param databaseName the databaseName to set
	 */
	public void setDatabaseName(String databaseName) {
		this.databaseName = databaseName;
	}

	/**
	 * @return the dbProtocol
	 */
	public String getDbProtocol() {
		return dbProtocol;
	}

	/**
	 * @param dbProtocol the dbProtocol to set
	 */
	public void setDbProtocol(String dbProtocol) {
		this.dbProtocol = dbProtocol;
	}

	/**
	 * @return the dbUserName
	 */
	public String getDbUserName() {
		return dbUserName;
	}

	/**
	 * @param dbUserName the dbUserName to set
	 */
	public void setDbUserName(String dbUserName) {
		this.dbUserName = dbUserName;
	}

	/**
	 * @return the endTime
	 */
	public String getEndTime() {
		return endTime;
	}

	/**
	 * @param endTime the endTime to set
	 */
	public void setEndTime(String endTime) {
		this.endTime = endTime;
	}

	/**
	 * @return the errorMessage
	 */
	public String getErrorMessage() {
		return errorMessage;
	}

	/**
	 * @param errorMessage the errorMessage to set
	 */
	public void setErrorMessage(String errorMessage) {
		this.errorMessage = errorMessage;
	}

	/**
	 * @return the exitCode
	 */
	public String getExitCode() {
		return exitCode;
	}

	/**
	 * @param exitCode the exitCode to set
	 */
	public void setExitCode(String exitCode) {
		this.exitCode = exitCode;
	}

	/**
	 * @return the logTime
	 */
	public String getLogTime() {
		return logTime;
	}

	/**
	 * @param logTime the logTime to set
	 */
	public void setLogTime(String logTime) {
		this.logTime = logTime;
	}

	/**
	 * @return the netProtocol
	 */
	public String getNetProtocol() {
		return netProtocol;
	}

	/**
	 * @param netProtocol the netProtocol to set
	 */
	public void setNetProtocol(String netProtocol) {
		this.netProtocol = netProtocol;
	}

	/**
	 * @return the objectName
	 */
	public String getObjectName() {
		return objectName;
	}

	/**
	 * @param objectName the objectName to set
	 */
	public void setObjectName(String objectName) {
		this.objectName = objectName;
	}

	/**
	 * @return the objectType
	 */
	public String getObjectType() {
		return objectType;
	}

	/**
	 * @param objectType the objectType to set
	 */
	public void setObjectType(String objectType) {
		this.objectType = objectType;
	}

	/**
	 * @return the paramList
	 */
	public List<String> getParamList() {
		return paramList;
	}

	/**
	 * @param paramList the paramList to set
	 */
	public void setParamList(List<String> paramList) {
		this.paramList = paramList;
	}

	/**
	 * @return the pid
	 */
	public String getPid() {
		return pid;
	}

	/**
	 * @param pid the pid to set
	 */
	public void setPid(String pid) {
		this.pid = pid;
	}

	/**
	 * @return the remoteHost
	 */
	public String getRemoteHost() {
		return remoteHost;
	}

	/**
	 * @param remoteHost the remoteHost to set
	 */
	public void setRemoteHost(String remoteHost) {
		this.remoteHost = remoteHost;
	}

	/**
	 * @return the remotePort
	 */
	public String getRemotePort() {
		return remotePort;
	}

	/**
	 * @param remotePort the remotePort to set
	 */
	public void setRemotePort(String remotePort) {
		this.remotePort = remotePort;
	}

	/**
	 * @return the rowCount
	 */
	public String getRowCount() {
		return rowCount;
	}

	/**
	 * @param rowCount the rowCount to set
	 */
	public void setRowCount(String rowCount) {
		this.rowCount = rowCount;
	}

	/**
	 * @return the serverHost
	 */
	public String getServerHost() {
		return serverHost;
	}

	/**
	 * @param serverHost the serverHost to set
	 */
	public void setServerHost(String serverHost) {
		this.serverHost = serverHost;
	}

	/**
	 * @return the serverType
	 */
	public String getServerType() {
		return serverType;
	}

	/**
	 * @param serverType the serverType to set
	 */
	public void setServerType(String serverType) {
		this.serverType = serverType;
	}

	/**
	 * @return the serverVersion
	 */
	public String getServerVersion() {
		return serverVersion;
	}

	/**
	 * @param serverVersion the serverVersion to set
	 */
	public void setServerVersion(String serverVersion) {
		this.serverVersion = serverVersion;
	}

	/**
	 * @return the serviceName
	 */
	public String getServiceName() {
		return serviceName;
	}

	/**
	 * @param serviceName the serviceName to set
	 */
	public void setServiceName(String serviceName) {
		this.serviceName = serviceName;
	}

	/**
	 * @return the sessionId
	 */
	public String getSessionId() {
		return sessionId;
	}

	/**
	 * @param sessionId the sessionId to set
	 */
	public void setSessionId(String sessionId) {
		this.sessionId = sessionId;
	}

	/**
	 * @return the startTime
	 */
	public String getStartTime() {
		return startTime;
	}

	/**
	 * @param startTime the startTime to set
	 */
	public void setStartTime(String startTime) {
		this.startTime = startTime;
	}

	/**
	 * @return the statementId
	 */
	public String getStatementId() {
		return statementId;
	}

	/**
	 * @param statementId the statementId to set
	 */
	public void setStatementId(String statementId) {
		this.statementId = statementId;
	}

	/**
	 * @return the substatementId
	 */
	public String getSubstatementId() {
		return substatementId;
	}

	/**
	 * @param substatementId the substatementId to set
	 */
	public void setSubstatementId(String substatementId) {
		this.substatementId = substatementId;
	}

	/**
	 * @return the transactionId
	 */
	public String getTransactionId() {
		return transactionId;
	}

	/**
	 * @param transactionId the transactionId to set
	 */
	public void setTransactionId(String transactionId) {
		this.transactionId = transactionId;
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

	@Override
	public int hashCode() {
		return Objects.hash(_class, clientApplication, command, commandText, databaseName, dbProtocol, dbUserName,
				endTime, errorMessage, exitCode, logTime, netProtocol, objectName, objectType, paramList, pid,
				remoteHost, remotePort, rowCount, serverHost, serverType, serverVersion, serviceName, sessionId,
				startTime, statementId, substatementId, transactionId, type);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}
		if (!(obj instanceof PostgresActivityEvent)) {
			return false;
		}
		PostgresActivityEvent other = (PostgresActivityEvent) obj;
		return Objects.equals(_class, other._class) && Objects.equals(clientApplication, other.clientApplication)
				&& Objects.equals(command, other.command) && Objects.equals(commandText, other.commandText)
				&& Objects.equals(databaseName, other.databaseName) && Objects.equals(dbProtocol, other.dbProtocol)
				&& Objects.equals(dbUserName, other.dbUserName) && Objects.equals(endTime, other.endTime)
				&& Objects.equals(errorMessage, other.errorMessage) && Objects.equals(exitCode, other.exitCode)
				&& Objects.equals(logTime, other.logTime) && Objects.equals(netProtocol, other.netProtocol)
				&& Objects.equals(objectName, other.objectName) && Objects.equals(objectType, other.objectType)
				&& Objects.equals(paramList, other.paramList) && Objects.equals(pid, other.pid)
				&& Objects.equals(remoteHost, other.remoteHost) && Objects.equals(remotePort, other.remotePort)
				&& Objects.equals(rowCount, other.rowCount) && Objects.equals(serverHost, other.serverHost)
				&& Objects.equals(serverType, other.serverType) && Objects.equals(serverVersion, other.serverVersion)
				&& Objects.equals(serviceName, other.serviceName) && Objects.equals(sessionId, other.sessionId)
				&& Objects.equals(startTime, other.startTime) && Objects.equals(statementId, other.statementId)
				&& Objects.equals(substatementId, other.substatementId)
				&& Objects.equals(transactionId, other.transactionId) && Objects.equals(type, other.type);
	}

	@Override
	public String toString() {
		return "PostgresActivityEvent [_class=" + _class + ", clientApplication=" + clientApplication + ", command="
				+ command + ", commandText=" + commandText + ", databaseName=" + databaseName + ", dbProtocol="
				+ dbProtocol + ", dbUserName=" + dbUserName + ", endTime=" + endTime + ", errorMessage=" + errorMessage
				+ ", exitCode=" + exitCode + ", logTime=" + logTime + ", netProtocol=" + netProtocol + ", objectName="
				+ objectName + ", objectType=" + objectType + ", paramList=" + paramList + ", pid=" + pid
				+ ", remoteHost=" + remoteHost + ", remotePort=" + remotePort + ", rowCount=" + rowCount
				+ ", serverHost=" + serverHost + ", serverType=" + serverType + ", serverVersion=" + serverVersion
				+ ", serviceName=" + serviceName + ", sessionId=" + sessionId + ", startTime=" + startTime
				+ ", statementId=" + statementId + ", substatementId=" + substatementId + ", transactionId="
				+ transactionId + ", type=" + type + "]";
	}

}

package com.amazonaws.services.lambda.samples.events.documentdbstreams.models;

import java.util.Objects;

public class EventEvent {
    private _ID _id;
    private ClusterTime clusterTime;
    private DocumentKey documentKey;
    private FullDocument fullDocument;
    private NS ns;
    private String operationType;
	/**
	 * 
	 */
	public EventEvent() {
		super();
	}
	/**
	 * @param _id
	 * @param clusterTime
	 * @param documentKey
	 * @param fullDocument
	 * @param ns
	 * @param operationType
	 */
	public EventEvent(_ID _id, ClusterTime clusterTime, DocumentKey documentKey, FullDocument fullDocument, NS ns,
			String operationType) {
		super();
		this._id = _id;
		this.clusterTime = clusterTime;
		this.documentKey = documentKey;
		this.fullDocument = fullDocument;
		this.ns = ns;
		this.operationType = operationType;
	}
	/**
	 * @return the _id
	 */
	public _ID get_id() {
		return _id;
	}
	/**
	 * @param _id the _id to set
	 */
	public void set_id(_ID _id) {
		this._id = _id;
	}
	/**
	 * @return the clusterTime
	 */
	public ClusterTime getClusterTime() {
		return clusterTime;
	}
	/**
	 * @param clusterTime the clusterTime to set
	 */
	public void setClusterTime(ClusterTime clusterTime) {
		this.clusterTime = clusterTime;
	}
	/**
	 * @return the documentKey
	 */
	public DocumentKey getDocumentKey() {
		return documentKey;
	}
	/**
	 * @param documentKey the documentKey to set
	 */
	public void setDocumentKey(DocumentKey documentKey) {
		this.documentKey = documentKey;
	}
	/**
	 * @return the fullDocument
	 */
	public FullDocument getFullDocument() {
		return fullDocument;
	}
	/**
	 * @param fullDocument the fullDocument to set
	 */
	public void setFullDocument(FullDocument fullDocument) {
		this.fullDocument = fullDocument;
	}
	/**
	 * @return the ns
	 */
	public NS getNs() {
		return ns;
	}
	/**
	 * @param ns the ns to set
	 */
	public void setNs(NS ns) {
		this.ns = ns;
	}
	/**
	 * @return the operationType
	 */
	public String getOperationType() {
		return operationType;
	}
	/**
	 * @param operationType the operationType to set
	 */
	public void setOperationType(String operationType) {
		this.operationType = operationType;
	}
	@Override
	public int hashCode() {
		return Objects.hash(_id, clusterTime, documentKey, fullDocument, ns, operationType);
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		EventEvent other = (EventEvent) obj;
		return Objects.equals(_id, other._id) && Objects.equals(clusterTime, other.clusterTime)
				&& Objects.equals(documentKey, other.documentKey) && Objects.equals(fullDocument, other.fullDocument)
				&& Objects.equals(ns, other.ns) && Objects.equals(operationType, other.operationType);
	}
	@Override
	public String toString() {
		return "EventEvent [_id=" + _id + ", clusterTime=" + clusterTime + ", documentKey=" + documentKey
				+ ", fullDocument=" + fullDocument + ", ns=" + ns + ", operationType=" + operationType + "]";
	}
    
}
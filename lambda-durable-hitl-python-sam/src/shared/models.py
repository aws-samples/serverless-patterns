"""
Data models for the Lambda Durable HITL pattern.

This module defines the core data structures used throughout the approval workflow,
including approval requests, workflow events, and decision requests.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from enum import Enum
import json


class ApprovalStatus(Enum):
    """Status values for approval requests."""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXPIRED = "expired"
    TIMEOUT = "timeout"


class Decision(Enum):
    """Decision values for approval outcomes."""
    APPROVED = "approved"
    REJECTED = "rejected"
    TIMEOUT = "timeout"


@dataclass
class ApprovalRequest:
    """
    Represents an approval request in the system.
    
    This model stores all information about a pending or completed approval,
    including the callback token needed to resume workflow execution.
    """
    
    approval_id: str
    callback_token: str
    document_id: str
    document_name: str
    requester: str
    status: ApprovalStatus
    created_at: datetime
    updated_at: datetime
    expires_at: datetime
    decision: Optional[Decision] = None
    comments: Optional[str] = None
    decided_by: Optional[str] = None
    decided_at: Optional[datetime] = None
    ttl: Optional[int] = None  # Unix timestamp for DynamoDB TTL
    
    def to_dynamodb_item(self) -> dict:
        """
        Convert to DynamoDB item format.
        
        Returns:
            dict: DynamoDB item with all fields serialized appropriately
        """
        item = {
            "approval_id": self.approval_id,
            "callback_token": self.callback_token,
            "document_id": self.document_id,
            "document_name": self.document_name,
            "requester": self.requester,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "expires_at": self.expires_at.isoformat(),
        }
        
        if self.decision:
            item["decision"] = self.decision.value
        if self.comments:
            item["comments"] = self.comments
        if self.decided_by:
            item["decided_by"] = self.decided_by
        if self.decided_at:
            item["decided_at"] = self.decided_at.isoformat()
        if self.ttl:
            item["ttl"] = self.ttl
            
        return item
    
    @classmethod
    def from_dynamodb_item(cls, item: dict) -> 'ApprovalRequest':
        """
        Create from DynamoDB item.
        
        Args:
            item: DynamoDB item dictionary
            
        Returns:
            ApprovalRequest: Deserialized approval request object
        """
        return cls(
            approval_id=item["approval_id"],
            callback_token=item["callback_token"],
            document_id=item["document_id"],
            document_name=item["document_name"],
            requester=item["requester"],
            status=ApprovalStatus(item["status"]),
            created_at=datetime.fromisoformat(item["created_at"]),
            updated_at=datetime.fromisoformat(item["updated_at"]),
            expires_at=datetime.fromisoformat(item["expires_at"]),
            decision=Decision(item["decision"]) if "decision" in item else None,
            comments=item.get("comments"),
            decided_by=item.get("decided_by"),
            decided_at=datetime.fromisoformat(item["decided_at"]) if "decided_at" in item else None,
            ttl=item.get("ttl")
        )
    
    def is_expired(self) -> bool:
        """
        Check if approval request has expired.
        
        Returns:
            bool: True if current time is past expires_at, False otherwise
        """
        return datetime.now() > self.expires_at
    
    def is_pending(self) -> bool:
        """
        Check if approval request is still pending.
        
        Returns:
            bool: True if status is PENDING and not expired, False otherwise
        """
        return self.status == ApprovalStatus.PENDING and not self.is_expired()


@dataclass
class WorkflowEvent:
    """
    Input event for workflow lambda.
    
    This represents the initial request to start an approval workflow.
    """
    
    document_id: str
    document_name: str
    requester: str
    timeout_seconds: Optional[int] = 3600  # Default 1 hour
    
    @classmethod
    def from_lambda_event(cls, event: dict) -> 'WorkflowEvent':
        """
        Parse from Lambda event.
        
        Args:
            event: Lambda event dictionary
            
        Returns:
            WorkflowEvent: Parsed workflow event object
        """
        return cls(
            document_id=event["document_id"],
            document_name=event["document_name"],
            requester=event["requester"],
            timeout_seconds=event.get("timeout_seconds", 3600)
        )


@dataclass
class ApprovalDecisionRequest:
    """
    Request to submit an approval decision.
    
    This represents a decision (approve/reject) submitted by a human approver.
    """
    
    approval_id: str
    decision: Decision
    comments: Optional[str] = None
    decided_by: Optional[str] = None
    
    @classmethod
    def from_api_event(cls, event: dict) -> 'ApprovalDecisionRequest':
        """
        Parse from API Gateway event or Lambda invocation event.
        
        Args:
            event: API Gateway or Lambda event dictionary
            
        Returns:
            ApprovalDecisionRequest: Parsed decision request object
        """
        # Handle both API Gateway format (with body) and direct Lambda invocation
        if "body" in event:
            body = json.loads(event["body"])
        else:
            body = event
            
        return cls(
            approval_id=body["approval_id"],
            decision=Decision(body["decision"]),
            comments=body.get("comments"),
            decided_by=body.get("decided_by")
        )


@dataclass
class WorkflowResult:
    """
    Result of workflow execution.
    
    This represents the final outcome of an approval workflow.
    """
    
    approval_id: str
    document_id: str
    decision: Decision
    comments: Optional[str] = None
    decided_at: Optional[datetime] = None
    
    def to_dict(self) -> dict:
        """
        Convert to dictionary for Lambda response.
        
        Returns:
            dict: Serialized workflow result
        """
        result = {
            "approval_id": self.approval_id,
            "document_id": self.document_id,
            "decision": self.decision.value,
        }
        
        if self.comments:
            result["comments"] = self.comments
        if self.decided_at:
            result["decided_at"] = self.decided_at.isoformat()
            
        return result

from unittest.mock import patch

import pytest
from botocore.exceptions import ClientError
from kb_sync_status_check_handler.index import handler

# Test events
TEST_EVENT = {
    "knowledgeBaseId": "test-kb-id",
    "ingestionJobId": "test-job-id",
    "dataSourceId": "test-ds-id",
}

# Mock responses for different statuses
MOCK_RESPONSES = {
    "RUNNING": {
        "ingestionJob": {
            "knowledgeBaseId": TEST_EVENT["knowledgeBaseId"],
            "dataSourceId": TEST_EVENT["dataSourceId"],
            "ingestionJobId": TEST_EVENT["ingestionJobId"],
            "status": "RUNNING",
        }
    },
    "COMPLETED": {
        "ingestionJob": {
            "knowledgeBaseId": TEST_EVENT["knowledgeBaseId"],
            "dataSourceId": TEST_EVENT["dataSourceId"],
            "ingestionJobId": TEST_EVENT["ingestionJobId"],
            "status": "COMPLETED",
        }
    },
    "FAILED": {
        "ingestionJob": {
            "knowledgeBaseId": TEST_EVENT["knowledgeBaseId"],
            "dataSourceId": TEST_EVENT["dataSourceId"],
            "ingestionJobId": TEST_EVENT["ingestionJobId"],
            "status": "FAILED",
            "failureReason": "Test failure reason",
        }
    },
}


class TestKBSyncStatusCheckHandler:
    @pytest.fixture(autouse=True)
    def mock_bedrock_client(self):
        """Mock the Bedrock client at the module level"""
        with patch("kb_sync_status_check_handler.index.bedrock") as mock_client:
            self.mock_client = mock_client
            yield mock_client

    @pytest.mark.parametrize("status", ["RUNNING", "COMPLETED", "FAILED"])
    def test_successful_status_check(self, status):
        """Test successful status check for different statuses"""
        # Setup mock response
        self.mock_client.get_ingestion_job.return_value = MOCK_RESPONSES[status]

        # Call handler
        response = handler(TEST_EVENT, {})

        # Verify response structure
        assert response["knowledgeBaseId"] == TEST_EVENT["knowledgeBaseId"]
        assert response["ingestionJobId"] == TEST_EVENT["ingestionJobId"]
        assert response["status"] == status

    def test_missing_kb_id(self):
        """Test handling of missing knowledge base ID"""
        with pytest.raises(KeyError) as exc_info:
            handler({"ingestionJobId": "test-job-id"}, {})
        assert "knowledgeBaseId" in str(exc_info.value)

    def test_missing_job_id(self):
        """Test handling of missing ingestion job ID"""
        with pytest.raises(KeyError) as exc_info:
            handler({"knowledgeBaseId": "test-kb-id"}, {})
        assert "ingestionJobId" in str(exc_info.value)

    @pytest.mark.parametrize(
        "error_code,error_message",
        [
            ("ResourceNotFoundException", "Ingestion job not found"),
            ("ValidationException", "Invalid parameter"),
            ("ThrottlingException", "Rate exceeded"),
            ("InternalServerException", "Internal error"),
        ],
    )
    def test_bedrock_errors(self, error_code, error_message):
        """Test handling of various Bedrock API errors"""
        # Setup mock error
        error_response = {"Error": {"Code": error_code, "Message": error_message}}
        self.mock_client.get_ingestion_job.side_effect = ClientError(error_response, "GetIngestionJob")

        # Test error handling
        with pytest.raises(ClientError) as exc_info:
            handler(TEST_EVENT, {})

        error = exc_info.value.response["Error"]
        assert error["Code"] == error_code
        assert error["Message"] == error_message

    def test_malformed_response(self):
        """Test handling of malformed response from Bedrock"""
        # Setup mock response missing required fields
        self.mock_client.get_ingestion_job.return_value = {}

        # Test error handling
        with pytest.raises(KeyError) as exc_info:
            handler(TEST_EVENT, {})
        assert "status" in str(exc_info.value)

    def test_empty_event(self):
        """Test handling of empty event"""
        with pytest.raises(KeyError) as exc_info:
            handler({}, {})
        assert "knowledgeBaseId" in str(exc_info.value)

    def test_none_values(self):
        """Test handling of None values"""
        test_event = {
            "knowledgeBaseId": None,
            "ingestionJobId": None,
            "dataSourceId": None,
        }
        with pytest.raises(TypeError):
            handler(test_event, {})

    def test_additional_response_fields(self):
        """Test handling of additional fields in response"""
        # Setup mock response with additional fields
        mock_response = {
            "ingestionJob": {
                "ingestionJobId": "test-job-id",
                "status": "COMPLETED",
                "startTime": "2024-01-01T00:00:00Z",
                "endTime": "2024-01-01T01:00:00Z",
                "statistics": {"totalDocuments": 100, "processedDocuments": 100},
            }
        }
        self.mock_client.get_ingestion_job.return_value = mock_response

        # Call handler
        response = handler(TEST_EVENT, {})

        # Verify only required fields are returned
        assert set(response.keys()) == {"dataSourceId", "knowledgeBaseId", "ingestionJobId", "status"}

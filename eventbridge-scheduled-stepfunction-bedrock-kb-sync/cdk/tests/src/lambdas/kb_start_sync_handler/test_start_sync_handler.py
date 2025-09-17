from datetime import datetime
from unittest.mock import patch

import pytest
from botocore.exceptions import ClientError
from kb_start_sync_handler.index import handler

# Test events
TEST_EVENT = {"knowledgeBaseId": "test-kb-id", "dataSourceId": "test-ds-id"}

# Mock responses
MOCK_INGESTION_RESPONSE = {
    "ingestionJob": {
        "knowledgeBaseId": TEST_EVENT["knowledgeBaseId"],
        "dataSourceId": TEST_EVENT["dataSourceId"],
        "ingestionJobId": "job-123",
        "status": "STARTED",
    }
}


class TestKBStartSyncHandler:
    @pytest.fixture(autouse=True)
    def mock_bedrock_client(self):
        """Mock the Bedrock client at the module level"""
        with patch("kb_start_sync_handler.index.bedrock") as mock_client:
            self.mock_client = mock_client
            yield mock_client

    @pytest.fixture(autouse=True)
    def mock_datetime(self):
        """Mock datetime to return a fixed value"""
        with patch("kb_start_sync_handler.index.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2024, 1, 1, 12, 0)
            yield mock_dt

    def test_successful_start_sync(self):
        """Test successful start of ingestion job"""
        # Setup mock response
        self.mock_client.start_ingestion_job.return_value = MOCK_INGESTION_RESPONSE

        # Call handler
        response = handler(TEST_EVENT, {})

        # Verify response structure
        assert response["knowledgeBaseId"] == TEST_EVENT["knowledgeBaseId"]
        assert response["dataSourceId"] == TEST_EVENT["dataSourceId"]
        assert response["ingestionJobId"] == MOCK_INGESTION_RESPONSE["ingestionJob"]["ingestionJobId"]

        # Verify bedrock client was called correctly
        self.mock_client.start_ingestion_job.assert_called_once_with(
            knowledgeBaseId=TEST_EVENT["knowledgeBaseId"],
            dataSourceId=TEST_EVENT["dataSourceId"],
            description="Scheduled sync started at 2024-01-01T12:00:00",
        )

    def test_missing_kb_id(self):
        """Test handling of missing knowledge base ID"""
        with pytest.raises(KeyError) as exc_info:
            handler({"dataSourceId": "test-ds-id"}, {})
        assert "knowledgeBaseId" in str(exc_info.value)

    def test_missing_ds_id(self):
        """Test handling of missing data source ID"""
        with pytest.raises(KeyError) as exc_info:
            handler({"knowledgeBaseId": "test-kb-id"}, {})
        assert "dataSourceId" in str(exc_info.value)

    @pytest.mark.parametrize(
        "error_code,error_message",
        [
            ("ResourceNotFoundException", "Knowledge base not found"),
            ("ValidationException", "Invalid parameter"),
            ("ThrottlingException", "Rate exceeded"),
            ("InternalServerException", "Internal error"),
        ],
    )
    def test_bedrock_errors(self, error_code, error_message):
        """Test handling of various Bedrock API errors"""
        # Setup mock error
        error_response = {"Error": {"Code": error_code, "Message": error_message}}
        self.mock_client.start_ingestion_job.side_effect = ClientError(error_response, "StartIngestionJob")

        # Test error handling
        with pytest.raises(ClientError) as exc_info:
            handler(TEST_EVENT, {})

        error = exc_info.value.response["Error"]
        assert error["Code"] == error_code
        assert error["Message"] == error_message

    def test_malformed_response(self):
        """Test handling of malformed response from Bedrock"""
        # Setup mock response missing ingestionJobId
        self.mock_client.start_ingestion_job.return_value = {}

        # Test error handling
        with pytest.raises(KeyError) as exc_info:
            handler(TEST_EVENT, {})
        assert "ingestionJobId" in str(exc_info.value)

    def test_empty_event(self):
        """Test handling of empty event"""
        with pytest.raises(KeyError) as exc_info:
            handler({}, {})
        assert "knowledgeBaseId" in str(exc_info.value)

    def test_none_values(self):
        """Test handling of None values"""
        test_event = {"knowledgeBaseId": None, "dataSourceId": None}
        with pytest.raises(TypeError):
            handler(test_event, {})

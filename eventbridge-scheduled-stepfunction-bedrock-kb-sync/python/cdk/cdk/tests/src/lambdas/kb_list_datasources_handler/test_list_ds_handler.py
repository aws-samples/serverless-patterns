from unittest.mock import patch

import pytest
from botocore.exceptions import ClientError
from kb_list_datasources_handler.index import handler

# Test events
TEST_EVENT = {"knowledgeBaseId": "test-kb-id"}

# Mock responses
MOCK_DATA_SOURCES = {
    "dataSourceSummaries": [
        {
            "dataSourceId": "ds-1",
            "name": "Test Data Source 1",
            "status": "ACTIVE",
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-01T00:00:00Z",
        },
        {
            "dataSourceId": "ds-2",
            "name": "Test Data Source 2",
            "status": "ACTIVE",
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-01T00:00:00Z",
        },
    ]
}


class TestKBListDataSourcesHandler:
    @pytest.fixture(autouse=True)
    def mock_bedrock_client(self):
        """Mock the Bedrock client at the module level"""
        with patch("kb_list_datasources_handler.index.bedrock") as mock_client:
            self.mock_client = mock_client
            yield mock_client

    def test_successful_list_datasources(self):
        """Test successful listing of data sources"""
        # Setup mock response
        self.mock_client.list_data_sources.return_value = MOCK_DATA_SOURCES

        # Call handler
        response = handler(TEST_EVENT, {})

        # Verify response structure
        assert "dataSources" in response
        assert len(response["dataSources"]) == 2

        # Verify first data source
        first_ds = response["dataSources"][0]
        assert first_ds["knowledgeBaseId"] == TEST_EVENT["knowledgeBaseId"]
        assert first_ds["dataSourceId"] == "ds-1"
        assert first_ds["name"] == "Test Data Source 1"
        assert first_ds["status"] == "ACTIVE"

        # Verify bedrock client was called correctly
        self.mock_client.list_data_sources.assert_called_once_with(knowledgeBaseId=TEST_EVENT["knowledgeBaseId"])

    def test_missing_kb_id(self):
        """Test handling of missing knowledge base ID"""
        with pytest.raises(ValueError) as exc_info:
            handler({}, {})
        assert "Missing required field" in str(exc_info.value)

    def test_bedrock_client_error(self):
        """Test handling of Bedrock API error"""
        # Setup mock error
        error_response = {"Error": {"Code": "ValidationException", "Message": "Invalid knowledge base ID"}}
        self.mock_client.list_data_sources.side_effect = ClientError(error_response, "ListDataSources")

        # Test error handling
        with pytest.raises(ClientError) as exc_info:
            handler(TEST_EVENT, {})
        assert error_response["Error"]["Code"] in str(exc_info.value)

    def test_empty_datasources(self):
        """Test handling of empty data sources list"""
        # Setup mock response with no data sources
        self.mock_client.list_data_sources.return_value = {"dataSourceSummaries": []}

        # Call handler
        response = handler(TEST_EVENT, {})

        # Verify response
        assert "dataSources" in response
        assert len(response["dataSources"]) == 0

    @pytest.mark.parametrize(
        "error_code,error_message",
        [
            ("ResourceNotFoundException", "Knowledge base not found"),
            ("ValidationException", "Invalid parameter"),
            ("ThrottlingException", "Rate exceeded"),
            ("InternalServerException", "Internal error"),
        ],
    )
    def test_specific_bedrock_errors(self, error_code, error_message):
        """Test handling of specific Bedrock API errors"""
        # Setup mock error
        error_response = {"Error": {"Code": error_code, "Message": error_message}}
        self.mock_client.list_data_sources.side_effect = ClientError(error_response, "ListDataSources")

        # Test error handling
        with pytest.raises(ClientError) as exc_info:
            handler(TEST_EVENT, {})

        error = exc_info.value.response["Error"]
        assert error["Code"] == error_code
        assert error["Message"] == error_message

    def test_malformed_response(self):
        """Test handling of malformed response from Bedrock"""
        # Setup mock response with missing dataSourceSummaries
        self.mock_client.list_data_sources.return_value = {}

        # Call handler
        response = handler(TEST_EVENT, {})

        # Verify response handles missing data gracefully
        assert "dataSources" in response
        assert len(response["dataSources"]) == 0

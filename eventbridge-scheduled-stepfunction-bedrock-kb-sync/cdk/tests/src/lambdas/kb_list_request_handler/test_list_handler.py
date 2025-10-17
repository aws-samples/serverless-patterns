import pytest
from kb_list_request_handler.index import handler

# Test event
TEST_SINGLE_KB_EVENT = {"knowledgeBaseId": "kb-1"}

TEST_MULTIPLE_KB_EVENT = {"knowledgeBaseIds": ["kb-1", "kb-2"]}


class TestKBListHandler:
    def test_successful_single_kb_event(self):
        """Test successful processing of a valid CSV file"""

        response = handler(TEST_SINGLE_KB_EVENT, {})
        # Verify response structure
        assert "knowledgeBaseIds" in response
        assert isinstance(response["knowledgeBaseIds"], list)
        assert len(response["knowledgeBaseIds"]) == 1
        assert response["knowledgeBaseIds"][0]["knowledgeBaseId"] == "kb-1"

    def test_successful_multiple_kb_event(self):
        """Test processing of multiple knowledge base IDs"""
        response = handler(TEST_MULTIPLE_KB_EVENT, {})

        # Verify response structure
        assert "knowledgeBaseIds" in response
        assert isinstance(response["knowledgeBaseIds"], list)
        assert len(response["knowledgeBaseIds"]) == 2
        assert response["knowledgeBaseIds"][0]["knowledgeBaseId"] == "kb-1"
        assert response["knowledgeBaseIds"][1]["knowledgeBaseId"] == "kb-2"

    def test_missing_kb_id(self):
        """Test handling of missing knowledge base ID"""
        with pytest.raises(ValueError) as exc_info:
            handler({}, {})
        assert "No knowledge base ids found in the event" in str(exc_info.value)

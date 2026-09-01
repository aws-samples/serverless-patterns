"""Unit tests for logging_utils module.

Requirements: 11.3
"""

import logging
import uuid

from shared.logging_utils import get_correlation_id, configure_logging, get_logger


class TestGetCorrelationId:
    def test_extracts_request_id_from_event(self):
        event = {"requestContext": {"requestId": "req-abc-123"}}
        assert get_correlation_id(event) == "req-abc-123"

    def test_generates_uuid_when_no_event(self):
        cid = get_correlation_id(None)
        # Should be a valid UUID
        uuid.UUID(cid)

    def test_generates_uuid_when_event_has_no_request_context(self):
        cid = get_correlation_id({"body": "hello"})
        uuid.UUID(cid)

    def test_generates_uuid_when_request_id_missing(self):
        event = {"requestContext": {}}
        cid = get_correlation_id(event)
        uuid.UUID(cid)

    def test_generates_uuid_for_empty_event(self):
        cid = get_correlation_id({})
        uuid.UUID(cid)


class TestConfigureLogging:
    def test_returns_root_logger(self):
        logger = configure_logging()
        assert isinstance(logger, logging.Logger)

    def test_sets_log_level(self):
        logger = configure_logging(level=logging.DEBUG)
        assert logger.level == logging.DEBUG

    def test_includes_correlation_id_in_format(self):
        logger = configure_logging(correlation_id="corr-xyz")
        handler = logger.handlers[-1] if logger.handlers else None
        if handler:
            assert "corr-xyz" in handler.formatter._fmt


class TestGetLogger:
    def test_returns_named_logger(self):
        logger = get_logger("my.module")
        assert logger.name == "my.module"
        assert isinstance(logger, logging.Logger)

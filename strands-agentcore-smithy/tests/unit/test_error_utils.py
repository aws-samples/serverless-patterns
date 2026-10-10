"""Unit tests for error_utils module.

Requirements: 11.3
"""

import logging

from shared.error_utils import (
    format_error_response,
    format_unauthorized_response,
    format_internal_error_response,
)


class TestFormatErrorResponse:
    def test_returns_failed_response(self):
        resp = format_error_response("something broke")
        assert resp.success is False
        assert resp.response == ""
        assert resp.error == "something broke"

    def test_logs_server_error_at_error_level(self, caplog):
        with caplog.at_level(logging.ERROR):
            format_error_response("server fail", status_code=500)
        assert "server fail" in caplog.text

    def test_logs_client_error_at_warning_level(self, caplog):
        with caplog.at_level(logging.WARNING):
            format_error_response("bad request", status_code=400)
        assert "bad request" in caplog.text

    def test_custom_log_message(self, caplog):
        with caplog.at_level(logging.ERROR):
            format_error_response("user msg", status_code=500, log_message="internal detail")
        assert "internal detail" in caplog.text


class TestFormatUnauthorizedResponse:
    def test_default_message(self):
        resp = format_unauthorized_response()
        assert resp.success is False
        assert resp.error == "Unauthorized"

    def test_custom_detail(self):
        resp = format_unauthorized_response("Token expired")
        assert resp.error == "Token expired"


class TestFormatInternalErrorResponse:
    def test_default_message(self):
        resp = format_internal_error_response()
        assert resp.success is False
        assert resp.error == "Internal server error"

    def test_with_exception(self, caplog):
        exc = ValueError("division by zero")
        with caplog.at_level(logging.ERROR):
            resp = format_internal_error_response("calc failed", exception=exc)
        assert resp.error == "calc failed"
        assert "division by zero" in caplog.text

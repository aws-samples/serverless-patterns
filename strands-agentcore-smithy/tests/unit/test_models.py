"""Unit tests for shared data models (UserContext, AgentRequest, AgentResponse).

Requirements: 11.3
"""

from shared.models import UserContext, AgentRequest, AgentResponse


class TestUserContext:
    def test_creation(self):
        ctx = UserContext(username="alice", token="tok-123")
        assert ctx.username == "alice"
        assert ctx.token == "tok-123"

    def test_equality(self):
        a = UserContext(username="bob", token="t")
        b = UserContext(username="bob", token="t")
        assert a == b

    def test_inequality(self):
        a = UserContext(username="bob", token="t1")
        b = UserContext(username="bob", token="t2")
        assert a != b


class TestAgentRequest:
    def test_creation(self):
        ctx = UserContext(username="u", token="t")
        req = AgentRequest(prompt="hello", user_context=ctx)
        assert req.prompt == "hello"
        assert req.user_context.username == "u"

    def test_equality(self):
        ctx = UserContext(username="u", token="t")
        a = AgentRequest(prompt="p", user_context=ctx)
        b = AgentRequest(prompt="p", user_context=ctx)
        assert a == b


class TestAgentResponse:
    def test_success_response(self):
        resp = AgentResponse(success=True, response="ok")
        assert resp.success is True
        assert resp.response == "ok"
        assert resp.error is None

    def test_error_response(self):
        resp = AgentResponse(success=False, response="", error="bad")
        assert resp.success is False
        assert resp.error == "bad"

    def test_error_defaults_to_none(self):
        resp = AgentResponse(success=True, response="ok")
        assert resp.error is None

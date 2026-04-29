import logging
import os
from strands import Agent
from strands.multiagent.a2a import A2AServer
from a2a.types import AgentSkill
import uvicorn
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)

runtime_url = os.environ.get('CLOUDFRONT_URL', os.environ.get('AGENTCORE_RUNTIME_URL', 'http://127.0.0.1:9000/'))

strands_agent = Agent(
    name="Test Agent",
    description="A helpful assistant that answers questions clearly and concisely.",
    callback_handler=None
)

a2a_server = A2AServer(
    agent=strands_agent,
    http_url=runtime_url,
    serve_at_root=True,
    enable_a2a_compliant_streaming=True,
    skills=[
        AgentSkill(
            id="general-assistant",
            name="General Assistant",
            description="Answers questions and provides helpful information",
            tags=["assistant", "qa"],
            examples=["What is the capital of France?"]
        )
    ]
)

a2a_app = a2a_server.to_fastapi_app()

@a2a_app.get("/ping")
def ping():
    return {"status": "healthy"}

app = a2a_app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)

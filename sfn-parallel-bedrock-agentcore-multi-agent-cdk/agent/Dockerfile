FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app

ENV UV_SYSTEM_PYTHON=1 \
    UV_COMPILE_BYTECODE=1

COPY requirements.txt requirements.txt
RUN uv pip install -r requirements.txt

RUN adduser -D -u 1000 bedrock_agentcore
USER bedrock_agentcore

EXPOSE 8080 8000

COPY . .

CMD ["python", "-m", "agent"]

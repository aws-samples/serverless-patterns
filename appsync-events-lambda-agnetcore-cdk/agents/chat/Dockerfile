FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

WORKDIR /app

ENV UV_SYSTEM_PYTHON=1 UV_COMPILE_BYTECODE=1

COPY chat/requirements.txt requirements.txt
RUN uv pip install --system --no-cache -r requirements.txt

ARG AWS_REGION
ENV AWS_REGION=${AWS_REGION}
ENV DOCKER_CONTAINER=1

RUN useradd -m -u 1000 bedrock_agentcore
USER bedrock_agentcore

EXPOSE 8080

COPY chat/ /app

CMD ["opentelemetry-instrument", "python", "-m", "entrypoint"]

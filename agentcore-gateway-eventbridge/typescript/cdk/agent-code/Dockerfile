FROM public.ecr.aws/docker/library/python:3.12-slim
WORKDIR /app
# Apply Debian security updates published after the base image was built.
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd -m -u 1000 bedrock_agentcore
USER bedrock_agentcore
EXPOSE 8080
COPY . .
# No Docker HEALTHCHECK: AgentCore Runtime polls the agent's /ping endpoint
# itself, so the image does not need curl (or the libraries it pulls in).
CMD ["python", "agent.py"]

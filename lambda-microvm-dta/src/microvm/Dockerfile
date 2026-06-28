# Lambda MicroVM application image. The MicroVM operating-system base image is
# selected separately by the Lambda MicroVMs create/update API via --base-image-arn.
# selected separately by the Lambda MicroVMs create/update API via --base-image-arn.
# strace provides the user-space syscall collector (no eBPF/Tracee/Falco in v0.2).
FROM python:3.13-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends strace \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY rules ./rules

ENV DTA_ANALYSIS_ROOT=/analysis
ENV DTA_RULES_FILE=/app/rules/default.yaml
ENV DTA_SOURCE_BASE=/app
ENV PYTHONUNBUFFERED=1

EXPOSE 8080
CMD ["python", "-m", "app.server"]

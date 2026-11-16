# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
FROM public.ecr.aws/docker/library/python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    HF_HOME=/tmp/hf-cache \
    TOKENIZERS_PARALLELISM=false

WORKDIR /opt/program

# CPU-only PyTorch keeps the image small. On CPU the model runs in float32, about 7 GiB of weights.
COPY requirements.txt .
RUN pip install "torch==2.7.1" --index-url https://download.pytorch.org/whl/cpu \
 && pip install -r requirements.txt

COPY serve.py .

# No USER instruction: Amazon SageMaker AI expects inference containers to run as root and warns that
# other users can cause permission issues. The container is reachable only through the SageMaker
# runtime API.
EXPOSE 8080
ENTRYPOINT ["python", "/opt/program/serve.py"]

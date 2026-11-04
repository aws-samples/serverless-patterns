# Dockerfile for the vulnerability scanner MicroVM image.
#
# Lambda MicroVMs builds this Dockerfile into a Firecracker snapshot during
# create-microvm-image. The image BUILD sandbox has no general internet egress
# (only Amazon package mirrors for dnf), so we do NOT download Trivy here.
# Instead, scripts/deploy.sh fetches the Trivy ARM64 binary at package time
# (on your machine, which has internet) and places it in this build context,
# and we COPY it in below. The Trivy vulnerability database is downloaded at
# RUN time by the scanner (the running MicroVM has INTERNET_EGRESS), not here.
# Base image pinned to an immutable digest for reproducible builds (tag: al2023-minimal).
# To update, re-resolve the digest:
#   docker buildx imagetools inspect public.ecr.aws/lambda/microvms:al2023-minimal
FROM public.ecr.aws/lambda/microvms@sha256:9a1139c88e5e8c99a7b26511d5ce52cd5c5eaac1e881235fa13a019418e1c182

RUN dnf install -y python3 shadow-utils tar gzip ca-certificates && dnf clean all

# Trivy binary is provided by deploy.sh in the build context (not committed to
# the repo, not downloaded during the build).
COPY trivy /usr/local/bin/trivy
RUN chmod +x /usr/local/bin/trivy && /usr/local/bin/trivy --version

WORKDIR /app
COPY app.py hooks.py start.sh /app/
RUN chmod +x /app/start.sh

# app -> 8080 (ingress), hooks -> 9000 (lifecycle hooks)
EXPOSE 8080 9000

CMD ["/app/start.sh"]

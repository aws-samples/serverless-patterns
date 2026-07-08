# ============================================================
# AgentCore Smithy Bedrock - SAM Makefile build target
# ============================================================
# Used by `sam build` via the AgentLambdaFunction resource's
# `Metadata: BuildMethod: makefile`. This replaces the previous
# manual packaging in deploy.sh and requires NO Docker.
#
# SAM invokes `make build-AgentLambdaFunction` with ARTIFACTS_DIR
# set to the directory SAM expects the built artifacts in.
#
# Two-step install reproduces the original packaging behaviour:
#   1. Install all dependencies as manylinux2014 x86_64 wheels
#   2. Re-install pure-Python packages with --no-deps so nothing
#      is skipped by the binary-only constraint
# ============================================================

build-AgentLambdaFunction:
	pip3 install \
		--target "$(ARTIFACTS_DIR)" \
		--platform manylinux2014_x86_64 \
		--python-version 3.12 \
		--only-binary=:all: \
		-r requirements.txt
	pip3 install \
		--target "$(ARTIFACTS_DIR)" \
		--platform manylinux2014_x86_64 \
		--python-version 3.12 \
		--only-binary=:all: \
		--no-deps \
		requests urllib3 charset-normalizer idna certifi PyJWT cryptography cffi
	cp -r src "$(ARTIFACTS_DIR)/"

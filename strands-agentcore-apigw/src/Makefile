# =============================================================================
# SAM custom build (BuildMethod: makefile) for the Agent Lambda.
#
# SAM calls the `build-AgentLambdaFunction` target and passes ARTIFACTS_DIR —
# whatever lands there becomes the Lambda deployment package.
#
# We download prebuilt manylinux (Linux) wheels via pip's --platform flag so
# binary dependencies (cryptography, cffi) match the Lambda runtime regardless
# of the host OS. This needs no Docker and no local python3.12 — pip resolves
# the wheels for the target platform from PyPI.
#
# Two-step install: `--only-binary=:all:` with `--platform` silently skips
# pure-Python packages, so a second `--no-deps` pass installs those explicitly.
# =============================================================================

PLATFORM := manylinux2014_x86_64
PYVER := 3.12
PIP := python3 -m pip

build-AgentLambdaFunction:
	# Step 1 — binary packages (strands, mcp, and their native deps)
	$(PIP) install \
		--target "$(ARTIFACTS_DIR)" \
		--platform $(PLATFORM) \
		--python-version $(PYVER) \
		--only-binary=:all: \
		--requirement requirements.txt

	# Step 2 — pure-Python packages skipped by step 1
	$(PIP) install \
		--target "$(ARTIFACTS_DIR)" \
		--platform $(PLATFORM) \
		--python-version $(PYVER) \
		--only-binary=:all: \
		--no-deps \
		requests urllib3 charset-normalizer idna certifi PyJWT cryptography cffi

	# Remove .egg-info dirs only — preserve .dist-info (opentelemetry needs them)
	find "$(ARTIFACTS_DIR)" -type d -name '*.egg-info' -exec rm -rf {} + 2>/dev/null || true

	# Application code
	cp -r agent "$(ARTIFACTS_DIR)/agent"
	cp -r shared "$(ARTIFACTS_DIR)/shared"
	touch "$(ARTIFACTS_DIR)/agent/__init__.py"
	touch "$(ARTIFACTS_DIR)/shared/__init__.py"

# Build Makefile — Docker-free Lambda packaging for AWS SAM (BuildMethod: makefile)
#
# SAM's BuildMethod: makefile invokes a target named build-<FunctionLogicalId>
# for each function, passing $(ARTIFACTS_DIR) (provided by SAM per function) as
# the destination for the finished build artifact (dependencies + source).
#
# Target names MUST match the function logical IDs in infrastructure/template.yaml
# EXACTLY (build-AgentLambdaFunction, build-McpServerLambda) or SAM cannot resolve
# them.
#
# The recipes reuse the project's proven two-step pip3 manylinux install so wheels
# are Linux/manylinux2014_x86_64-correct even when `sam build` runs on macOS —
# without Docker.
#
# Conventions (project-conventions.md):
#   - Use pip3, never bare pip
#   - Two steps: --only-binary=:all: against requirements.txt, then --no-deps for
#     the pure-Python set (--only-binary silently skips pure-Python packages)
#   - Do NOT delete .dist-info directories (OpenTelemetry reads them at runtime)
#   - Preserve the src/ prefix so src.agent.handler.lambda_handler and
#     src.mcp_server.handler.lambda_handler resolve

build-AgentLambdaFunction:
	# Step A: binary packages from requirements.txt (manylinux wheels)
	pip3 install --target "$(ARTIFACTS_DIR)" \
	  --platform manylinux2014_x86_64 --python-version 3.12 \
	  --only-binary=:all: -r requirements.txt
	# Step B: pure-Python packages skipped by --only-binary in Step A
	pip3 install --target "$(ARTIFACTS_DIR)" \
	  --platform manylinux2014_x86_64 --python-version 3.12 \
	  --only-binary=:all: --no-deps \
	  requests urllib3 charset-normalizer idna certifi PyJWT cryptography cffi mcp
	# Copy the src/ tree into the artifact, preserving the src/ prefix so
	# src.agent.handler.lambda_handler resolves
	cp -r src "$(ARTIFACTS_DIR)/src"

build-McpServerLambda:
	# Step A: binary packages from requirements.txt (manylinux wheels)
	pip3 install --target "$(ARTIFACTS_DIR)" \
	  --platform manylinux2014_x86_64 --python-version 3.12 \
	  --only-binary=:all: -r requirements.txt
	# Step B: pure-Python packages skipped by --only-binary in Step A
	pip3 install --target "$(ARTIFACTS_DIR)" \
	  --platform manylinux2014_x86_64 --python-version 3.12 \
	  --only-binary=:all: --no-deps \
	  requests urllib3 charset-normalizer idna certifi PyJWT cryptography cffi mcp
	# Copy the src/ tree into the artifact, preserving the src/ prefix so
	# src.mcp_server.handler.lambda_handler resolves
	cp -r src "$(ARTIFACTS_DIR)/src"

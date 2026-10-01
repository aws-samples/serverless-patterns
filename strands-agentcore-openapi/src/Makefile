# SAM custom build for the Agent Lambda.
#
# The target name must be build-<FunctionLogicalId> (build-AgentFunction).
# SAM invokes this from the CodeUri directory (src/) and passes ARTIFACTS_DIR,
# the folder it will zip and upload.
#
# We install dependencies as Linux manylinux wheels via pip's --platform flag,
# so the build works on macOS/Windows without Docker.

build-AgentFunction:
	python3 -m pip install \
		-r requirements.txt \
		--platform manylinux2014_x86_64 \
		--python-version 3.12 \
		--implementation cp \
		--only-binary=:all: \
		--target "$(ARTIFACTS_DIR)"
	cp -r agent "$(ARTIFACTS_DIR)/agent"
	cp -r shared "$(ARTIFACTS_DIR)/shared"

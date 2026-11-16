.PHONY: build-CombinedLayer clean

# Default target
build-CombinedLayer:
	mkdir -p "$(ARTIFACTS_DIR)/python"
	pip install requests -t "$(ARTIFACTS_DIR)/python"
	pip install python-jose -t "$(ARTIFACTS_DIR)/python"
	pip install cryptography -t "$(ARTIFACTS_DIR)/python"

clean:
	rm -rf "$(ARTIFACTS_DIR)"

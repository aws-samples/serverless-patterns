build-TelemetryS3ExtensionsLayer:
	cp -R extensions "$(ARTIFACTS_DIR)"
	mkdir -p "$(ARTIFACTS_DIR)/extensions/lib"
	python -m pip install -r requirements.txt -t "$(ARTIFACTS_DIR)/extensions/lib"
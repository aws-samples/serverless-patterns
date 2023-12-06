build:
	sam build
run-api: build
	sam local start-api --skip-pull-image
deploy: build
	sam deploy
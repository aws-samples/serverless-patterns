build: 
	cdk synth

teardown:
	cdk destroy

build-and-deploy:
	make build
	cdk deploy

test-success:
	make build
	sam local invoke CorsLambdaFunction -t cdk.out/CorsWhitelist.template.json --env-vars environment.json --event src/cors-function/test-events/api-origin.json

test-failure:
	make build
	sam local invoke CorsLambdaFunction -t cdk.out/CorsWhitelist.template.json --env-vars environment.json --event src/cors-function/test-events/api-no-origin.json	
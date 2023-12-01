
### Project Structure within src/lex-gen-ai-demo-cdk:
```
AWSLexKoiosBlogDemo/src/lex-gen-ai-demo-cdk
- app.py
- cdk.json
- endpoint_handler.py
- upload_file_to_s3.py
- shutdown_endpoint.py
- index-creation-docker-image/
   - index_creation_app.py
   - Dockerfile
   - index_creation_requirements.txt
- lex_gen_ai_demo_cdk_files/
   - __init__.py
   - lex_gen_ai_demo_file_stack.py
- lex-gen-ai-demo-docker-image/
   - runtime_lambda_app.py
   - Dockerfile
   - runtime_lambda_requirements.txt
- requirements.txt
- source.bat
```

## Common Errors & Troubleshooting

### "ValueError: Must setup local AWS configuration with a region supported by SageMaker."
Solution: You must set an aws region with `export AWS_DEFAULT_REGION=<your-region>`

### Error creating role
```
botocore.exceptions.ClientError: An error occurred (AccessDenied) when calling the CreateRole operation: User: <user-arn> is not authorized to perform: iam:CreateRole on resource: <role-arn> because no identity-based policy allows the iam:CreateRole action
```
Solution: you must ensure the Iam role you are using has sufficient permissions to create Iam roles

### Error LexGenAIDemoFilesStack:  fail: docker push <IMAGE> exited with error code 1: tag does not exist
Issue: Error while building the image. Here are some common ones 

#### Error processing tar file(exit status 1): write /path/libcublas.so.11: no space left on device
Issue: Docker has run out of memory due to too many images
Solution: Delete unused images in the Docker application and then [prune docker](https://docs.docker.com/config/pruning/) in command line 

#### ConnectionResetError: [Errno 104] Connection reset by peer
Issue: Pip issue
Solution: Clear pip cache (`python3 -m pip cache purge`) and run again

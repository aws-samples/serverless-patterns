
### Project Structure within eventbridge-lambda-comprehend-custom-cdk-python:
```
eventbridge-lambda-comprehend-custom-cdk-python
- app.py
- cdk.json
- src/
   - lambda_function.py
   - architecture.png
   - Screenshot_1.png
   - Screenshot_2.png
   - Screenshot_3.png
   - Screenshot_4.png
   - Screenshot_5.png
   - Screenshot_6.png
   - Screenshot_7.png
- requirements.txt
```

## Common Errors & Troubleshooting

### "ValueError: Must setup local AWS configuration with a region supported by AWS Services."
Solution: You must set an AWS region with `export AWS_DEFAULT_REGION=<your-region>`

### Error creating role
```
botocore.exceptions.ClientError: An error occurred (AccessDenied) when calling the CreateRole operation: User: <user-arn> is not authorized to perform: iam:CreateRole on resource: <role-arn> because no identity-based policy allows the iam:CreateRole action
```
Solution: you must ensure the IAM role you are using has sufficient permissions to create IAM roles

#### Error processing tar file(exit status 1): write /path/libcublas.so.11: no space left on device
Issue: Docker has run out of memory due to too many images
Solution: Delete unused images in the Docker application and then [prune docker](https://docs.docker.com/config/pruning/) in command line 

#### ConnectionResetError: [Errno 104] Connection reset by peer
Issue: Pip issue
Solution: Clear pip cache (`python3 -m pip cache purge`) and run again

FROM public.ecr.aws/lambda/python:3.13

# Copy requirements file
COPY approval_api/requirements.txt ${LAMBDA_TASK_ROOT}/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy function code
COPY approval_api/app.py ${LAMBDA_TASK_ROOT}/
COPY shared/*.py ${LAMBDA_TASK_ROOT}/

# Set the CMD to your handler
CMD ["app.lambda_handler"]

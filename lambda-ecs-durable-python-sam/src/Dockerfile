FROM public.ecr.aws/lambda/python:3.13

# Copy requirements file
COPY requirements.txt ${LAMBDA_TASK_ROOT}/

# Install dependencies including durable SDK
RUN pip install -r requirements.txt

# Copy function code
COPY sync_handler.py ${LAMBDA_TASK_ROOT}/
COPY callback_handler.py ${LAMBDA_TASK_ROOT}/

# Default handler (will be overridden by template)
CMD [ "sync_handler.lambda_handler" ]

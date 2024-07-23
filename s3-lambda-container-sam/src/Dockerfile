FROM public.ecr.aws/lambda/python:3.11

WORKDIR ${LAMBDA_TASK_ROOT} 

# Add dependencies
ADD ./requirements.txt  ${LAMBDA_TASK_ROOT}/requirements.txt

# install dependencies
RUN pip3 install -r requirements.txt

ADD . ${LAMBDA_TASK_ROOT} 

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.lambda_handler" ]

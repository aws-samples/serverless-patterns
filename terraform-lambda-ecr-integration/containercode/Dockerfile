FROM amazon/aws-lambda-python:3.11

RUN yum update -y

COPY app.py ./
COPY sample-bash.sh ./

RUN pip install --upgrade pip

CMD ["app.handler"]

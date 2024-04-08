FROM amazon/aws-lambda-python:3.11

RUN yum update -y

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY app.py ./

CMD ["app.handler"]

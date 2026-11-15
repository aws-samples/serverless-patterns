FROM public.ecr.aws/lambda/python:3.14

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY app.py ./

CMD ["app.handler"]

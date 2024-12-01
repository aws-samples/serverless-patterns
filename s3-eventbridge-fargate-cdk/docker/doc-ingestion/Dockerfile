FROM public.ecr.aws/docker/library/python:3.10-slim

RUN apt-get update

RUN python -m pip install --upgrade setuptools pip

COPY requirements.txt ./
RUN pip install --default-timeout=100 -r requirements.txt
CMD ["pip", "freeze"]

COPY app.py ./
CMD [ "python", "app.py" ]

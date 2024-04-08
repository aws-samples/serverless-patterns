FROM public.ecr.aws/docker/library/python:3.9-slim

WORKDIR /tmp

COPY requirements.txt .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY task.py .
CMD ["pip", "freeze"]
CMD ["python","task.py"]
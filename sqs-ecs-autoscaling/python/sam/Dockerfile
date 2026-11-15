FROM python:3-alpine3.22

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY consumer/app.py .

CMD ["python", "app.py"]
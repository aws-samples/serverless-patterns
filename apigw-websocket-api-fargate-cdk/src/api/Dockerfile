FROM public.ecr.aws/docker/library/python:3.11.6-slim-bullseye

# Install lambda web adapter
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.7.0 /lambda-adapter /opt/extensions/lambda-adapter

WORKDIR /api

COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./app ./app

ENV PORT=8000
EXPOSE ${PORT}
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
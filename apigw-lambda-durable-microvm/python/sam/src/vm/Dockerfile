# Built server-side by AWS::Lambda::MicrovmImage on the al2023 base image.
# The app answers the lifecycle hooks on port 8080 and, on the run hook, executes
# the command from runHookPayload and posts the result to the callback URL.
FROM python:3.13-slim
COPY app.py /app/app.py
EXPOSE 8080
CMD ["python3", "/app/app.py"]

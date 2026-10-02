# Worker image for AWS Lambda MicroVMs, built server-side by the
# AWS::Lambda::MicrovmImage resource in template.yaml.
FROM public.ecr.aws/amazonlinux/amazonlinux:2023

# The default python3 on Amazon Linux 2023 is 3.9, which current boto3 no longer
# supports, so install Python 3.12.
RUN dnf -y install python3.12 python3.12-pip \
    && dnf clean all \
    && rm -rf /var/cache/dnf

RUN python3.12 -m pip install --no-cache-dir boto3==1.43.107

WORKDIR /app
COPY app.py /app/app.py

# 9000: lifecycle hooks. The worker serves no application traffic.
EXPOSE 9000

CMD ["python3.12", "-u", "/app/app.py"]

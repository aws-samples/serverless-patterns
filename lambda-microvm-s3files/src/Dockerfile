# S3 Files demo image for AWS Lambda MicroVMs.
#
# Amazon Linux 2023 so we can install `amazon-efs-utils` straight from Amazon's
# repos. amazon-efs-utils provides the `mount -t s3files` helper (TLS + IAM) that
# S3 Files requires; nfs-utils provides the underlying NFS 4.2 client.
FROM public.ecr.aws/amazonlinux/amazonlinux:2023

# amazon-efs-utils >= 3.0.0 is required for S3 Files. It bundles the efs-proxy
# binary used to establish the TLS-encrypted NFS connection to the mount target.
RUN dnf -y install amazon-efs-utils nfs-utils python3 python3-pip \
    && dnf clean all \
    && rm -rf /var/cache/dnf

RUN pip3 install --no-cache-dir flask==3.0.3

WORKDIR /app
COPY app.py /app/app.py

# 8080: application traffic (proxied via X-aws-proxy-port). 9000: lifecycle hooks.
EXPOSE 8080 9000

CMD ["python3", "-u", "/app/app.py"]

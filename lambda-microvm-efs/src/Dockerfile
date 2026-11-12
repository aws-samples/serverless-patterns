# Amazon EFS demo image for AWS Lambda MicroVMs.
#
# Amazon Linux 2023 so we can install `amazon-efs-utils` straight from Amazon's
# repos. amazon-efs-utils provides the `mount -t efs` helper (TLS + IAM auth via
# the efs-proxy binary); nfs-utils provides the underlying NFS 4.1 client.
#
# Using a different container base image is fine — the guest OS is always the
# Lambda-managed AL2023 base image regardless. A RHEL 9 (UBI 9) userspace works
# and measures within 0.5% of this image on EFS throughput. The one catch is that
# `nfs-utils` is NOT in the UBI 9 repositories, so `mount -t efs` has no NFS
# helper to call; on UBI 9 you either add amazon-efs-utils' RPM explicitly or
# call mount(2) directly with addr=/clientaddr=. See README "Other base images".
FROM public.ecr.aws/amazonlinux/amazonlinux:2023

RUN dnf -y install amazon-efs-utils nfs-utils python3 python3-pip \
    && dnf clean all \
    && rm -rf /var/cache/dnf

RUN pip3 install --no-cache-dir flask==3.0.3

WORKDIR /app
COPY app.py /app/app.py

# 8080: application traffic (proxied via X-aws-proxy-port). 9000: lifecycle hooks.
EXPOSE 8080 9000

CMD ["python3", "-u", "/app/app.py"]

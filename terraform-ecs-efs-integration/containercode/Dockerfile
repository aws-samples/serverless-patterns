FROM amazon/aws-cli:latest
RUN yum update -y

COPY sample-bash.sh ./

CMD ["sample-bash.sh"]
ENTRYPOINT ["sh"]
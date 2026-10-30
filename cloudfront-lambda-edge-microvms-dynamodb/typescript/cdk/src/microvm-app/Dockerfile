# The service builds this Dockerfile server-side; the stack's baseImageArn (managed
# AL2023) is the base it runs on. No local Docker is needed to deploy.
FROM public.ecr.aws/amazonlinux/amazonlinux:2023
# AL2023's default `nodejs` is Node 18; pin Node 22. If the app never starts, /ready never
# answers and the image build ends in CREATE_FAILED.
RUN dnf install -y nodejs22 && dnf clean all
WORKDIR /app
COPY package.json ./
COPY server.js ./
EXPOSE 8080 9000
CMD ["node", "server.js"]

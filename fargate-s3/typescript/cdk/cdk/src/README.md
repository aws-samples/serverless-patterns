# TypeScript Express server without Docker

Run the following to start the server on port 80:

```bash
npm install
npm run start
```

# TypeScript Express server with Docker

This requires slight modifications to `AWS.config`. Please add the `accessKeyId` and `secretAccessKey` to it. Alternatively, register the respective credentials within the container. Run the following to start the server on port 80:

```bash
docker build . -t ts-express-s3
docker run -p 80:80 \
    --env region=ap-southeast-2 \
    --env bucketName=demo-bucket-serverless-patterns \
    --name ts-app ts-express-s3
```
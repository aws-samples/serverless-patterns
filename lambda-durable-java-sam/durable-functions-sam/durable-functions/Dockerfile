FROM --platform=linux/amd64 amazoncorretto:21-alpine AS builder
WORKDIR /build
COPY pom.xml .
COPY src ./src
RUN apk add --no-cache maven && mvn clean package

FROM public.ecr.aws/lambda/java:21
COPY --from=builder /build/target/*.jar ${LAMBDA_TASK_ROOT}/lib/

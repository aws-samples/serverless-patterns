FROM maven:3.9-amazoncorretto-17 AS build
WORKDIR /app
COPY pom.xml .
COPY main/ src/main/
RUN mvn clean package -DskipTests

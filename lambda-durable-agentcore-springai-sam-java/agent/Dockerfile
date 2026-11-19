# AgentCore Runtime requires an ARM64 container listening on port 8080.
FROM --platform=linux/arm64 amazoncorretto:21-alpine3.23

RUN addgroup -S agent && adduser -S agent -G agent

WORKDIR /app
COPY target/document-review-agent.jar app.jar
RUN chown agent:agent /app/app.jar

USER agent
EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]

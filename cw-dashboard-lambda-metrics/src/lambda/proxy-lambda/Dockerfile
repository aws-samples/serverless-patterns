FROM public.ecr.aws/lambda/dotnet:6 AS base

ARG URL
ARG INSIGHTSEXTENSION

FROM mcr.microsoft.com/dotnet/sdk:6.0-bullseye-slim as build
WORKDIR /src
COPY ["proxy-lambda.csproj", "proxy-lambda/"]
RUN dotnet restore "proxy-lambda/proxy-lambda.csproj"

WORKDIR "/proxy-lambda"
COPY . .
RUN dotnet build "proxy-lambda.csproj" --configuration Release --output /app/build

FROM build AS publish
RUN dotnet publish "proxy-lambda.csproj" \
            --configuration Release \ 
            --runtime linux-x64 \
            --self-contained false \ 
            --output /app/publish \
            -p:PublishReadyToRun=true  

FROM base AS final
ARG URL
ARG INSIGHTSEXTENSION

ENV FULLURL=$URL$INSIGHTSEXTENSION
RUN echo $FULLURL
RUN curl -O $FULLURL && \
    rpm -U $INSIGHTSEXTENSION && \
    rm -f $INSIGHTSEXTENSION

WORKDIR /var/task
RUN echo $REGION
COPY --from=publish /app/publish .
CMD ["proxy-lambda::proxy_lambda.Function::FunctionHandler"]
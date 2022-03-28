FROM public.ecr.aws/lambda/dotnet:6 AS base

FROM mcr.microsoft.com/dotnet/sdk:6.0-bullseye-slim as build
WORKDIR /src
COPY ["lambda.csproj", "lambda/"]
RUN dotnet restore "lambda/lambda.csproj"

WORKDIR "/src/lambda"
COPY . .
RUN dotnet build "lambda.csproj" --configuration Release --output /app/build

FROM build AS publish
RUN dotnet publish "lambda.csproj" \
            --configuration Release \ 
            --runtime linux-x64 \
            --self-contained false \ 
            --output /app/publish \
            -p:PublishReadyToRun=true  

FROM base AS final
WORKDIR /var/task
COPY --from=publish /app/publish .
CMD ["lambda::lambda.Function::FunctionHandler"]
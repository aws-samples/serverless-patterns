FROM public.ecr.aws/lambda/dotnet:6 as base

FROM mcr.microsoft.com/dotnet/sdk:6.0 as build
WORKDIR /src
COPY ["AWSLamdaDemo.csproj", "AWSLamdaDemo/"]
RUN dotnet restore "AWSLamdaDemo/AWSLamdaDemo.csproj"

WORKDIR "/src/AWSLamdaDemo"
COPY . .
RUN dotnet build "AWSLamdaDemo.csproj" --configuration Release --output /app/build

FROM build AS publish
RUN dotnet publish "AWSLamdaDemo.csproj" \
            --configuration Release \ 
            --runtime linux-x64 \
            --self-contained false \ 
            --output /app/publish \
            -p:PublishReadyToRun=true  

FROM base AS final
WORKDIR /var/task
COPY --from=publish /app/publish .
CMD ["AWSLamdaDemo::AWSLamdaDemo.LambdaEntryPoint::FunctionHandlerAsync"]
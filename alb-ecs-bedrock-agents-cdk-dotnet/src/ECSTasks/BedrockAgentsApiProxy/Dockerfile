# Use the official .NET SDK image to build the project
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Copy csproj and restore dependencies
COPY ["BedrockAgentsApiProxy.csproj", "./"]
RUN dotnet restore

# Copy the rest of the code and build the project
COPY . .
RUN dotnet publish -c Release -o /app/publish

# Build runtime image
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime

# install packages
RUN apt-get update && apt-get install -y curl procps && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the published app to the /app directory
COPY --from=build /app/publish .

# Create a non-root user
RUN adduser --disabled-password --gecos '' appuser

# Give ownership of the /app directory to appuser
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Expose the port the app will run on
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Set the entry point for the application
ENTRYPOINT ["dotnet", "BedrockAgentsApiProxy.dll"]



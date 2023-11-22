using Amazon.QLDB.Driver;

namespace dotnet_core_web_api;

public interface IDriver
{
    IAsyncQldbDriver Instance { get; }
}
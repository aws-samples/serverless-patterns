using Amazon.IonObjectMapper;
using Amazon.QLDB.Driver;
using Amazon.QLDB.Driver.Serialization;
using Amazon.QLDBSession;

namespace dotnet_core_web_api;

public class Driver : IDriver
{
    public Driver(string? ledgerName)
    {
        var qldbSessionConfig = new AmazonQLDBSessionConfig();
        
        Instance = AsyncQldbDriver.Builder()
            .WithQLDBSessionConfig(qldbSessionConfig)
            .WithLedger(ledgerName)
            .WithSerializer(new ObjectSerializer(new IonSerializationOptions() 
                { Format = IonSerializationFormat.PRETTY_TEXT } ))
            .Build();
    }
    public IAsyncQldbDriver Instance { get; }
}
using System.Diagnostics.CodeAnalysis;

[assembly: SuppressMessage("Performance", "CA1812:Avoid uninstantiated internal classes",
    Justification = "CDK stack classes are instantiated by the CDK framework entry point.")]

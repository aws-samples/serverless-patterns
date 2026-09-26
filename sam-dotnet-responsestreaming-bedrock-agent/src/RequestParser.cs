using Amazon.Lambda.APIGatewayEvents;

namespace TripPlannerStreaming;

/// <summary>
/// Parses trip planning parameters from an API Gateway request.
/// </summary>
public static class RequestParser
{
    public static TripRequest Parse(APIGatewayProxyRequest request)
    {
        var destination = TripRequest.DefaultDestination;
        var days = TripRequest.DefaultDays;
        var interests = TripRequest.DefaultInterests;

        if (request.QueryStringParameters is null)
            return new TripRequest(destination, days, interests);

        if (request.QueryStringParameters.TryGetValue("destination", out var d) && !string.IsNullOrWhiteSpace(d))
            destination = d;

        if (request.QueryStringParameters.TryGetValue("days", out var n) &&
            int.TryParse(n, out var parsedDays) && parsedDays >= 1 && parsedDays <= TripRequest.MaxDays)
            days = parsedDays;

        if (request.QueryStringParameters.TryGetValue("interests", out var i) && !string.IsNullOrWhiteSpace(i))
            interests = i;

        return new TripRequest(destination, days, interests);
    }
}

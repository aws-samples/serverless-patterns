using System.Text.Json;
using Amazon.Lambda.Core;
using ActionGroupLambdaFunction.Models;
using ActionGroupLambdaFunction.Serialization;

namespace ActionGroupLambdaFunction;

public class Function
{
    public static Task<ApiResponse> FunctionHandler(ApiRequest request, ILambdaContext context)
    {
        context.Logger.LogInformation("Processing request: " +
            $"{JsonSerializer.Serialize(request, LambdaFunctionJsonSerializerContext.Default.ApiRequest)}");
        context.Logger.LogInformation($"Processing request: {request.HttpMethod}:{request.ApiPath}");

        // Return the list of flights as the response
        var apiResponse = new ApiResponse
        {
            messageVersion = "1.0",
            response = new Response
            {
                actionGroup = request.ActionGroup,
                apiPath = request.ApiPath,
                httpMethod = request.HttpMethod,
                httpStatusCode = 200,
            }
        };

        try
        {
            // Get the flight search request from the API request and search for flights
            var flights = GenerateMockFlights(GetFlightSearchRequest(request));

            // Set the response body to the list of flights
            apiResponse.response.responseBody =
                new Dictionary<string, ResponseBody>
                {
                    {
                        "application/json",
                        new ResponseBody
                        {
                            body = JsonSerializer.Serialize(flights, LambdaFunctionJsonSerializerContext.Default.ListFlight)
                        }
                    }
                };

            var serializedResponse = JsonSerializer.Serialize(apiResponse, LambdaFunctionJsonSerializerContext.Default.ApiResponse);
            context.Logger.LogInformation($"Returning response: {serializedResponse}");
        }
        catch (Exception ex)
        {
            context.Logger.LogError($"Error processing request. Error: {ex.Message}");
            apiResponse.response.httpStatusCode = 400;
            apiResponse.response.responseBody =
                new Dictionary<string, ResponseBody>
                {
                    {
                        "application/json",
                        new ResponseBody
                        {
                            body = JsonSerializer.Serialize(new Error
                            {
                                Message = ex.Message,
                                Code = ex.HResult
                            }, LambdaFunctionJsonSerializerContext.Default.Error)
                        }
                    }
                };
        }
        return Task.FromResult(apiResponse);
    }

    /// <summary>
    /// Creates <see cref="FlightSearchRequest"/> from <see cref="ApiRequest"/>
    /// </summary>
    /// <param name="apiRequest">API Request (from user)</param>
    /// <returns><see cref="FlightSearchRequest"/></returns>
    /// <exception cref="Exception">If invalid API request</exception>
    private static FlightSearchRequest GetFlightSearchRequest(ApiRequest apiRequest)
    {
        var properties = apiRequest?.RequestBody?.Content?.JsonProperties?.Properties
            ?? throw new Exception("Invalid request body, cannot find properties");

        // Departure Date
        var departureDateStr = properties?.FirstOrDefault(p => p.Name == "departureDate")?.Value?.ToString()
            ?? throw new Exception("Invalid request body, cannot find departureDate");
        if (!DateTime.TryParse(departureDateStr, out DateTime departureDatetime))
            throw new Exception("Invalid departure date");
        if (departureDatetime < DateTime.Now)
            throw new Exception("Departure date must be in the future");

        // Return Date
        DateTime returnDatetime = DateTime.MinValue;
        var returnDateStr = properties?.FirstOrDefault(p => p.Name == "returnDate")?.Value?.ToString();
        if (!string.IsNullOrEmpty(returnDateStr))
        {
            if (!DateTime.TryParse(returnDateStr, out returnDatetime))
                throw new Exception("Invalid return date");
            if (returnDatetime < departureDatetime)
                throw new Exception("Return date must be after departure date");
        }

        var request = new FlightSearchRequest
        {
            Origin = properties?.FirstOrDefault(p => p.Name == "origin")?.Value?.ToString() 
                ?? throw new Exception("Invalid request body, cannot find origin"),

            Destination = properties?.FirstOrDefault(p => p.Name == "destination")?.Value?.ToString() 
                ?? throw new Exception("Invalid request body, cannot find destination"),
            
            DepartureDate = departureDatetime,
            
            ReturnDate = returnDatetime == DateTime.MinValue ? null : returnDatetime,

            Passengers = int.Parse(properties?.FirstOrDefault(p => p.Name == "passengers")?.Value?.ToString() ?? "1")
        };

        return request;
    }

    /// <summary>
    /// Creates mock flight data from request
    /// </summary>
    /// <param name="request"><see cref="FlightSearchRequest"/></param>
    /// <returns>List of <see cref="Flight"/></returns>
    private static List<Flight> GenerateMockFlights(FlightSearchRequest request)
    {
        var random = new Random();
        var flights = new List<Flight>();

        for (int i = 0; i < 5; i++)
        {
            var airlineCode = RandomAirlineCode();

            var departureTime = request.DepartureDate.AddHours(random.Next(24));
            var arrivalTime = departureTime.AddHours(random.Next(1, 24));

            flights.Add(
                new Flight
                {
                    FlightNumber = $"{airlineCode}{random.Next(1000, 9999)}",
                    Airline = Airlines[airlineCode],
                    DepartureTime = departureTime.ToString("o"),
                    ArrivalTime = arrivalTime.ToString("o"),
                    Price = Math.Round(random.NextDouble() * (1000 - 100) + 100, 2)
                });

            if (request.ReturnDate != null)
            {
                departureTime = request.ReturnDate.Value.AddHours(random.Next(24));
                arrivalTime = departureTime.AddHours(random.Next(1, 24));

                flights[i].ReturnFlight = new Flight
                {
                    FlightNumber = $"{airlineCode}{random.Next(1000, 9999)}",
                    Airline =  Airlines[airlineCode],
                    DepartureTime = departureTime.ToString("o"),
                    ArrivalTime = arrivalTime.ToString("o"),
                    Price = Math.Round(random.NextDouble() * (1000 - 100) + 100, 2)
                };
            }
        }

        return flights;
    }

    /// <summary>
    /// Gets random airline code
    /// </summary>
    /// <returns>Airline code</returns>
    private static string RandomAirlineCode() => new string[] { "AA", "DL", "UA", "BA", "LH" }[new Random().Next(5)];

    /// <summary>
    /// List of airlines
    /// </summary>
    private static readonly Dictionary<string, string> Airlines = new()
    {
        { "AA", "American Airlines" },
        { "DL", "Delta Air Lines" },
        { "UA", "United Airlines" },
        { "BA", "British Airways" },
        { "LH", "Lufthansa" }
    };
}
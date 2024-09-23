using System.Text.Json;
using Amazon.Lambda.Core;
using ActionGroupLambdaFunction.Models;
using ActionGroupLambdaFunction.Serialization;

namespace ActionGroupLambdaFunction;

public class Function
{
    public Task<ApiResponse> FunctionHandler(ApiRequest request, ILambdaContext context)
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

    private static FlightSearchRequest GetFlightSearchRequest(ApiRequest apiRequest)
    {
        var properties = apiRequest?.RequestBody?.Content?.JsonProperties?.Properties
            ?? throw new Exception("Invalid request body, cannot find properties");

        var request = new FlightSearchRequest
        {
            Origin = properties?.FirstOrDefault(p => p.Name == "origin")?.Value?.ToString() 
                ?? throw new Exception("Invalid request body, cannot find origin"),

            Destination = properties?.FirstOrDefault(p => p.Name == "destination")?.Value?.ToString() 
                ?? throw new Exception("Invalid request body, cannot find destination"),
            
            DepartureDate = properties?.FirstOrDefault(p => p.Name == "departureDate")?.Value?.ToString() 
                ?? throw new Exception("Invalid request body, cannot find departureDate"),
            
            ReturnDate = properties?.FirstOrDefault(p => p.Name == "returnDate")?.Value?.ToString() 
                ?? throw new Exception("Invalid request body, cannot find returnDate"),
            Passengers = int.Parse(properties?.FirstOrDefault(p => p.Name == "passengers")?.Value?.ToString() ?? "1")
        };

        return request;
    }

    // private static APIGatewayProxyResponse HandleFlightSearch(APIGatewayProxyRequest request)
    // {
    //     try
    //     {
    //         var searchRequest = JsonSerializer.Deserialize(
    //             request.Body,
    //             LambdaFunctionJsonSerializerContext.Default.FlightSearchRequest)
    //             ?? throw new Exception("Invalid request body");

    //         var flights = GenerateMockFlights(searchRequest);

    //         return new APIGatewayProxyResponse
    //         {
    //             StatusCode = 200,
    //             Body = JsonSerializer.Serialize(flights, LambdaFunctionJsonSerializerContext.Default.ListFlight),
    //             Headers = new Dictionary<string, string>
    //             {
    //                 { "Content-Type", "application/json" },
    //                 { "Access-Control-Allow-Origin", "*" }
    //             },
    //             IsBase64Encoded = false
    //         };
    //     }
    //     catch (Exception ex)
    //     {   
    //         var error = new Error
    //         {
    //             Message = ex.Message,
    //             Code = ex.HResult
    //         };

    //         return new APIGatewayProxyResponse
    //         {
    //             StatusCode = 400,
    //             Body = JsonSerializer.Serialize(error, LambdaFunctionJsonSerializerContext.Default.Error),
    //             Headers = new Dictionary<string, string>
    //             {
    //                 { "Content-Type", "application/json" },
    //                 { "Access-Control-Allow-Origin", "*" },
    //                 { "x-amzn-ErrorType", ex.HResult.ToString() }
    //             },
    //             IsBase64Encoded = false                
    //         };
    //     }
    // }

    private static List<Flight> GenerateMockFlights(FlightSearchRequest request)
    {
        var random = new Random();
        var flights = new List<Flight>();

        var departureDatetime = DateTime.Parse(request.DepartureDate);
        if (departureDatetime < DateTime.Now)
            throw new Exception("Departure date must be in the future");

        var returnDatetime = DateTime.Parse(request.ReturnDate);
        if (returnDatetime < departureDatetime)
            throw new Exception("Return date must be after departure date");

        for (int i = 0; i < 5; i++)
        {
            var airlineCode = RandomAirlineCode();

            var departureTime = departureDatetime.AddHours(random.Next(24));
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

            departureTime = returnDatetime.AddHours(random.Next(24));
            arrivalTime = departureTime.AddHours(random.Next(1, 24));

            if (request.ReturnDate != null)
            {
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

    private static string RandomAirlineCode() => new string[] { "AA", "DL", "UA", "BA", "LH" }[new Random().Next(5)];

    private static readonly Dictionary<string, string> Airlines = new Dictionary<string, string>
    {
        { "AA", "American Airlines" },
        { "DL", "Delta Air Lines" },
        { "UA", "United Airlines" },
        { "BA", "British Airways" },
        { "LH", "Lufthansa" }
    };
}
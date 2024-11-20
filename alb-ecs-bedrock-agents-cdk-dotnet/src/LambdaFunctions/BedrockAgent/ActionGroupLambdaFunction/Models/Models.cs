namespace ActionGroupLambdaFunction.Models;

public class FlightSearchRequest
{
    public required string Origin { get; set; }
    
    public required string Destination { get; set; }

    public required DateTime DepartureDate { get; set; }

    public required DateTime? ReturnDate { get; set; }

    public int Passengers { get; set; }
}

public class Flight
{
    public string? FlightNumber { get; set; }

    public string? Airline { get; set; }

    public string? DepartureTime { get; set; }

    public string? ArrivalTime { get; set; }

    public double? Price { get; set; }

    public Flight? ReturnFlight { get; set; }
}

public class Error
{
    public string? Message { get; set; }

    public int? Code { get; set; }
}

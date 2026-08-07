namespace TripPlannerStreaming;

/// <summary>
/// Formats and streams trip planner output to a StreamWriter.
/// </summary>
public class ResponseFormatter
{
    private readonly StreamWriter _writer;

    public ResponseFormatter(StreamWriter writer)
    {
        _writer = writer;
    }

    public async Task WriteHeaderAsync(TripRequest trip)
    {
        await _writer.WriteLineAsync($"✈️  Trip Planner — {trip.Destination} ({trip.Days} days)");
        await _writer.WriteLineAsync($"   Interests: {trip.Interests}");
        await _writer.WriteLineAsync(new string('═', 60));
        await _writer.WriteLineAsync();
        await _writer.FlushAsync();
    }

    public async Task WriteDayPlanAsync(DayPlan day)
    {
        await _writer.WriteLineAsync($"📅 Day {day.DayNumber}: {day.Title}");
        await _writer.WriteLineAsync($"   🌅 Morning: {day.Morning}");
        await _writer.WriteLineAsync($"   ☀️  Afternoon: {day.Afternoon}");
        await _writer.WriteLineAsync($"   🌙 Evening: {day.Evening}");
        await _writer.WriteLineAsync($"   💡 Tips: {day.Tips}");
        await _writer.WriteLineAsync();
        await _writer.FlushAsync();
    }

    public async Task WriteSummaryAsync(string summary)
    {
        await _writer.WriteLineAsync(new string('═', 60));
        await _writer.WriteLineAsync();
        await _writer.WriteLineAsync(summary);
        await _writer.FlushAsync();
    }

    public async Task WriteFooterAsync()
    {
        await _writer.WriteLineAsync();
        await _writer.WriteLineAsync("✅ Happy travels!");
        await _writer.FlushAsync();
    }

    public async Task WriteErrorAsync(string message)
    {
        await _writer.WriteLineAsync($"\n\n[Error generating trip plan: {message}]");
        await _writer.FlushAsync();
    }
}

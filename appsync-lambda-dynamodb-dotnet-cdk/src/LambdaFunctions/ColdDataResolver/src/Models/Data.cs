using System.Text.Json.Serialization;

namespace ColdDataResolver.Models
{
    public class Data
    {
        [JsonPropertyName("id")]
        public string? Id { get; set; } = string.Empty;
        
        [JsonPropertyName("content")]
        public string? Content { get; set; } = string.Empty;

        [JsonPropertyName("timestamp")]
        public string? Timestamp { get; set; } = null;
    }
}
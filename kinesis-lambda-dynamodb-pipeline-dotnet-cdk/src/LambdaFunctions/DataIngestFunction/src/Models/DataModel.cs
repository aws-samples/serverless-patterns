namespace DataIngestFunction.Models
{
    /// <summary>
    /// This class represents the data model for the data ingested into the Kinesis stream.
    /// </summary>
    public class DataModel
    {
        public string? Id { get; set; }
        public DateTime Timestamp { get; set; }
        public int Value { get; set; }
        public string? Category { get; set; }
    }
}
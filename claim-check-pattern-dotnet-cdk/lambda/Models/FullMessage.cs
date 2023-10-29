namespace ClaimCheckPattern.Models;
public class FullMessage
{
    public Guid Id { get; set; }
    public DateTime CreatedAt { get; set; }
    public string? CreatedBy { get; set; }
    public Dictionary<string, string>? Data { get; set; }
}

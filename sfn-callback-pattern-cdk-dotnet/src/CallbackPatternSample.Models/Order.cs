namespace CallbackPatternSample.Models
{
    public class Order
    {
        public Guid OrderId { get; set; }
        public string? OrderDetails { get; set; }
        public bool IsConfirmed { get; set; }
    }
}
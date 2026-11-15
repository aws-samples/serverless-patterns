using Microsoft.AspNetCore.Mvc;
namespace HttpApi.Controllers;

[Route("/api")]
public class ValuesController : ControllerBase
{
    [HttpGet]
    public IEnumerable<string> Get()
    {
        return new string[] { "value1", "value2" };
    }

}
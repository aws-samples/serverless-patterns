using dotnet_core_web_api.Models;
using Microsoft.AspNetCore.Mvc;

namespace dotnet_core_web_api.Controllers;

[ApiController]
[Route("[controller]")]
public class PersonController : ControllerBase
{
    private readonly IDriver _driver;
    public PersonController()
    {
        _driver = new Driver(Environment.GetEnvironmentVariable("LEDGER_NAME"));
    }
    
    [HttpGet("{email}")]
    public async Task<Person?> Get(string email)
    {
        return await _driver.Instance.Execute(async txn =>
        {
            var myQuery = txn.Query<Person>("SELECT * FROM Person WHERE email = ?", email);
            var resultQuery = await txn.Execute(myQuery);

            return await resultQuery.FirstOrDefaultAsync();
        });
    }
    
    [HttpPost]
    public async Task<ActionResult<Person>> Create(Person person)
    {
        await _driver.Instance.Execute(async txn =>
        {
            var query = txn.Query<Person>("INSERT INTO Person ?", person);
            await txn.Execute(query);
        });
        
        return CreatedAtAction("Get", new { email = person.Email }, person);
    }
}
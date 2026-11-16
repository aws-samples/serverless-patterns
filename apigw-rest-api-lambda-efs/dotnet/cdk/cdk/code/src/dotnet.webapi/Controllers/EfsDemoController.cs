using Microsoft.AspNetCore.Mvc;
using System.Text;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace dotnet.webapi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class EfsDemoController : ControllerBase
    {
        // GET: api/<EfsDemoController>
        [HttpGet]
        public IEnumerable<string> Get()
        {
            return new string[] { "value1", "value2" };
        }

        // GET api/<EfsDemoController>/5
        [HttpGet("{id}")]
        public string Get(int id)
        {
            return "value";
        }

        // POST api/<EfsDemoController>
        [HttpPost]
        public IEnumerable<string> Post([FromBody] string value)
        {
            string directory = @"/mnt/lambdaefs/";
            string path = directory + value + ".txt";
            List<string> result = new List<string>();

            // Create the file, or overwrite if the file exists.
            using (FileStream fs = System.IO.File.Create(path))
            {
                byte[] info = new UTF8Encoding(true).GetBytes("This is some text in the file.");
                // Add some information to the file.
                fs.Write(info, 0, info.Length);
            }

            // Process the list of files found in the directory.
            string[] fileEntries = Directory.GetFiles(directory);
            foreach (string fileName in fileEntries)
            {
                result.Add(fileName);
            }
            return result;
        }

        // PUT api/<EfsDemoController>/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] string value)
        {
        }

        // DELETE api/<EfsDemoController>/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}

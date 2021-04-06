const AWS = require("aws-sdk");
const rdsDataService = new AWS.RDSDataService();

async function RunCommand(sqlStatement){
  // Prepare the SQL parameters required for Data API
  const sqlParams = {
    secretArn: process.env.SecretArn,
    resourceArn: process.env.DBClusterArn,
    sql: sqlStatement,
    database: process.env.DBName,
    includeResultMetadata: true,
  };
  console.log("SQL Parameters:\n", JSON.stringify(sqlParams));

  // Use the Data API ExecuteStatement operation to run the SQL command
  const result = await rdsDataService.executeStatement(sqlParams).promise();
  //console.log("Result:\n", result);
  return result;
}

exports.handler = async (event, context) => {
  try {
    // Log event and context object to CloudWatch Logs
    console.log("Event:\n", JSON.stringify(event, null, 2));
    console.log("Context:\n", JSON.stringify(context, null, 2));
    console.log("Database Name: ", process.env.DBName);

    // Get data from event
    const artist = event.body.artist;
    const album = event.body.album;

    // Create SQL statements
    const sqlCreate = "CREATE TABLE IF NOT EXISTS music (id INT AUTO_INCREMENT PRIMARY KEY, artist VARCHAR(128), album VARCHAR(128));";
    const sqlInsert = `INSERT INTO music (artist, album) VALUES ('${artist}', '${album}');`;
    const sqlSelect = "SELECT id, artist, album FROM music WHERE id=(SELECT LAST_INSERT_ID());";
    
    // Run the SQL commands one at a time
    await RunCommand(sqlCreate);
    await RunCommand(sqlInsert);
    const result = await RunCommand(sqlSelect);

    // Parse through result to build record set
    let rows = [];
    let cols = [];

    // Build an array of columns
    result.columnMetadata.map((v, i) => {
      cols.push(v.name);
    });

    // Build an array of rows
    result.records.map((r) => {
      var row = {};
      r.map((v, i) => {
        if (v.stringValue !== "undefined") {
          row[cols[i]] = v.stringValue;
        } else if (v.blobValue !== "undefined") {
          row[cols[i]] = v.blobValue;
        } else if (v.doubleValue !== "undefined") {
          row[cols[i]] = v.doubleValue;
        } else if (v.longValue !== "undefined") {
          row[cols[i]] = v.longValue;
        } else if (v.booleanValue !== "undefined") {
          row[cols[i]] = v.booleanValue;
        } else if (v.isNull) {
          row[cols[i]] = null;
        }
      });
      rows.push(row);
    });

    console.log("Record Count: ", rows.length);
    console.log("Records:\n", JSON.stringify(rows));

    const response = {
      statusCode: 200,
      body: JSON.stringify(rows),
    };
    return response;
  } catch (error) {
    console.error(error);
    throw new Error("Function Error");
  }
};

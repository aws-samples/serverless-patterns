const AWS = require("aws-sdk");
const rdsDataService = new AWS.RDSDataService();

async function RunCommand(sqlStatement, sqlValues){
  // Prepare the SQL parameters required for Data API
  let sqlParams = {
    secretArn: process.env.SecretArn,
    resourceArn: process.env.DBClusterArn,
    sql: sqlStatement,
    database: process.env.DBName,
    includeResultMetadata: true,
  };
  // Add an array of SqlParameter objects to the SQL statement
  // https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_SqlParameter.html
  if (sqlValues !== undefined) {
    sqlParams.parameters = [
      { name: "artist", value: { stringValue: sqlValues.artist } },
      { name: "album", value: { stringValue: sqlValues.album } },
    ];
  }
  console.log("SQL Parameters:\n", JSON.stringify(sqlParams));

  // Use the Data API ExecuteStatement operation to run the SQL command
  const result = await rdsDataService.executeStatement(sqlParams).promise();
  //console.log("Result:\n", result);
  return result;
}

exports.handler = async (event, context) => {
  try {
    // Log event object and database name to CloudWatch Logs
    console.log("Event:\n", JSON.stringify(event, null, 2));
    console.log("Database Name: ", process.env.DBName);

    // Get data from test event
    // Use default data if test event is not configured properly
    const body = event.body;
    let artist = "The Beatles";
    let album = "Abbey Road";
    if (body !== undefined) {
      if (body.artist !== undefined) {
        artist = body.artist;
      }
      if (body.album !== undefined) {
        album = body.album;
      }
    }

    // Create SQL statements
    const sqlCreate = "CREATE TABLE IF NOT EXISTS music (id INT AUTO_INCREMENT PRIMARY KEY, artist VARCHAR(128), album VARCHAR(128));";
    const sqlInsert = "INSERT INTO music (artist, album) VALUES (:artist, :album);";
    const sqlSelect = "SELECT id, artist, album FROM music WHERE id=(SELECT LAST_INSERT_ID());";
    const sqlValues = {
      artist: artist,
      album: album,
    };

    // Run the SQL commands one at a time
    await RunCommand(sqlCreate);
    await RunCommand(sqlInsert, sqlValues);
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
        if (v.stringValue !== undefined) {
          row[cols[i]] = v.stringValue;
        } else if (v.blobValue !== undefined) {
          row[cols[i]] = v.blobValue;
        } else if (v.doubleValue !== undefined) {
          row[cols[i]] = v.doubleValue;
        } else if (v.longValue !== undefined) {
          row[cols[i]] = v.longValue;
        } else if (v.booleanValue !== undefined) {
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
    throw new Error(error);
  }
};

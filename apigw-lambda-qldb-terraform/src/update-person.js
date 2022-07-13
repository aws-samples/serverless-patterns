/*
 * Lambda function that implements the create licence functionality
 */
const { QldbDriver } = require('amazon-qldb-driver-nodejs');

module.exports.handler = async (event) => {

  const { personid } = event.pathParameters;
  const { address } = JSON.parse(event.body);

  console.log(`In the update person handler with: personid ${personid} address ${address}`);

  try {
    const qldbDriver = new QldbDriver(process.env.LEDGER_NAME);

    await qldbDriver.executeLambda(async (txn) => {

        // Update the person address
        const statement = 'UPDATE Person SET address = ? WHERE personId = ?';
        const result = await txn.execute(statement, address, personid);
        const recordCount = result.getResultList().length;

        if (recordCount === 0) {
          const existsError = new Error(`No record exists for personId: ${personid}`);
          existsError.code = 404;
          throw existsError;
        }
        
    }, () => console.log("Retrying due to OCC conflict..."));
    return {
        'statusCode': 200,
        'body': JSON.stringify({'message': 'Address successfully updated'})
    };

  } catch (error) {
    console.log(JSON.stringify(error));

    return {
      statusCode: error.code,
      body: JSON.stringify({'code': error.code, 'message': error.message}),
    };

  }
};
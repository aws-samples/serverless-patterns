/*
 * Lambda function that implements the create licence functionality
 */
const { QldbDriver } = require('amazon-qldb-driver-nodejs');

module.exports.handler = async (event) => {

  const { personid } = event.pathParameters;
  console.log(`In the delete person handler with: personid ${personid}`);

  try {
    const qldbDriver = new QldbDriver(process.env.LEDGER_NAME);

    await qldbDriver.executeLambda(async (txn) => {
        console.log(`In the executeLambda call`);
        // Insert an order doc
        const statement = 'DELETE FROM Person WHERE personId = ?'
        const result = await txn.execute(statement, personid);
        const resultList = result.getResultList();

        if (resultList.length === 0) {
          const existsError = new Error(`Record does not exist for id: ${personid}`);
          existsError.code = 404;
          throw existsError;

        } 

    }, () => console.log("Retrying due to OCC conflict..."));

    return {
      statusCode: 200,
      body: JSON.stringify({'message': 'Person record successfully deleted'}),
    };

  } catch (error) {
    console.log(JSON.stringify(error));

    return {
      statusCode: error.code,
      body: JSON.stringify({'code': error.code, 'message': error.message}),
    };

  }
};
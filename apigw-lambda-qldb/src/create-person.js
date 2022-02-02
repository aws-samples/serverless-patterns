/*
 * Lambda function that implements the create licence functionality
 */
const { QldbDriver } = require('amazon-qldb-driver-nodejs');

module.exports.handler = async (event) => {
  const {
    firstName, lastName, email, address
  } = JSON.parse(event.body);
  console.log(`In the create person handler with: first name ${firstName} last name ${lastName} email ${email} address ${address}`);

  try {
    const qldbDriver = new QldbDriver(process.env.LEDGER_NAME);
    let person = {};

    await qldbDriver.executeLambda(async (txn) => {
        // Check email address is unique
        const recordsReturned = await checkEmailUnique(txn, email);

        if (recordsReturned === 0) {
          // Insert a new person doc
          const personDoc = [{"firstName": firstName, "lastName": lastName, "email": email, "address": address }]
          const statement = `INSERT INTO Person ?`;
          const result = await txn.execute(statement, personDoc);
          const docIdArray = result.getResultList();
          docId = docIdArray[0].get('documentId').stringValue();

          // Update person doc with unique ID
          await addGuid(txn, docId, email);

          // Format person object to return
          person = {
            personId: docId,
            firstName,
            lastName,
            email,
            address
          };

        } else {
          const existsError = new Error(`Record already exists for email: ${email}`);
          existsError.code = 404;
          throw existsError;
        }
        
    }, () => console.log("Retrying due to OCC conflict..."));

    return {
        'statusCode': 200,
        'body': JSON.stringify(person)
    };

  } catch (error) {
    console.log(JSON.stringify(error));


    return {
      statusCode: error.code,
      body: JSON.stringify({'code': error.code, 'message': error.message}),
    };

  }
};

async function checkEmailUnique(txn, email) {
  const query = 'SELECT email FROM Person WHERE email = ?';
  let recordsReturned;
  await txn.execute(query, email).then((result) => {
    recordsReturned = result.getResultList().length;
  });
  return recordsReturned;
}

async function addGuid(txn, id, email) {
  const statement = 'UPDATE Person SET personId = ? WHERE email = ?';
  return txn.execute(statement, id, email);
}
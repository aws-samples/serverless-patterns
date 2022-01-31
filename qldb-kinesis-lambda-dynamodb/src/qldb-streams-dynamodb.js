/*
 * Lambda function that consumes messages from a Kinesis data stream that uses the
 * Kinesis Aggregated Data Format
 */
const deagg = require('aws-kinesis-agg');
const ion = require('ion-js');
const { deleteLicence, updateLicence } = require('./lib/dyanamodb-licence');

const computeChecksums = true;
const REVISION_DETAILS = "REVISION_DETAILS";

/**
 * Promisified function to deaggregate Kinesis record
 * @param record An individual Kinesis record from the aggregated records
 * @returns The resolved Promise object containing the deaggregated records
 */
const promiseDeaggregate = (record) => new Promise((resolve, reject) => {
  deagg.deaggregateSync(record, computeChecksums, (err, responseObject) => {
    if (err) {
      // handle/report error
      return reject(err);
    }
    return resolve(responseObject);
  });
});

/**
 * Processes each Ion record, and takes the appropriate action to
 * create, update or delete a record in DynamoDB
 * @param ionRecord The Ion data loaded from a Uint8Array
 */
async function processIon(ionRecord) {
  // retrieve the version and id from the metadata section of the message
  const version = ionRecord.payload.revision.metadata.version.numberValue();
  const id = ionRecord.payload.revision.metadata.id.stringValue();

  // Check to see if the data section exists.
  if (ionRecord.payload.revision.data == null) {
    console.log('No data section so handle as a delete');
    await deleteLicence(id, version);
  } else {
    const firstName = ionRecord.payload.revision.data.firstName.stringValue();
    const lastName = ionRecord.payload.revision.data.lastName.stringValue();
    const email = ionRecord.payload.revision.data.email.stringValue();
    const address = ionRecord.payload.revision.data.address.stringValue();

    console.log(`Create/Update message with firstName: ${firstName}, lastName: ${lastName}, email: ${email}, address: ${address}`);

    // do an upsert so it doesn't matter if it is the initial version or not
    await updateLicence(id, firstName, lastName, email, address, version);
  }
}

/**
 * Processes each deaggregated Kinesis record in order. The function
 * ignores all records apart from those of typee REVISION_DETAILS
 * @param records The deaggregated Kinesis records to be processed
 */
async function processRecords(records) {
  await Promise.all(
    records.map(async (record) => {
      // Kinesis data is base64 encoded so decode here
      const payload = Buffer.from(record.data, 'base64');

      // payload is the actual ion binary record published by QLDB to the stream
      const ionRecord = ion.load(payload);

      // Only process records where the record type is REVISION_DETAILS
      if (ionRecord.recordType.stringValue() !== REVISION_DETAILS) {
        console.log(`Skipping record of type ${ion.dumpPrettyText(ionRecord.recordType)}`);
      } else {
        await processIon(ionRecord);
      }
    }),
  );
}

module.exports.handler = async (event, context) => {
  console.log(`In ${context.functionName} processing ${event.Records.length} Kinesis Input Records`);
  console.log(`Input message: ${JSON.stringify(event, null, 2)}`);

  await Promise.all(
    event.Records.map(async (kinesisRecord) => {
      const records = await promiseDeaggregate(kinesisRecord.kinesis);
      await processRecords(records);
    }),
  );
};
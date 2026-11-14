import {
    Context,
    FirehoseTransformationResult,
    FirehoseTransformationResultRecord
} from 'aws-lambda';
import { FirehoseTransformationEvent } from 'aws-lambda/trigger/kinesis-firehose-transformation'
import { Buffer } from 'buffer';

export const handler = async (event: FirehoseTransformationEvent, context: Context): Promise<FirehoseTransformationResult> => {

    console.log(`Event: ${JSON.stringify(event, null, 2)}`);
    console.log(`Context: ${JSON.stringify(context, null, 2)}`);
    const records: FirehoseTransformationResultRecord[] = []

    for (const record of event.records) {
        const recordData = JSON.parse(Buffer.from(record.data, 'base64').toString('utf8'));

        /** do some record transformation here */     

        /** 
         *  This example assumes source data is similar to Kinesis Data Firehose console demo data
         *  simulated stock ticker data: https://docs.aws.amazon.com/firehose/latest/dev/test-drive-firehose.html
         * */
       
        const oldPrice = recordData["PRICE"] - recordData["CHANGE"];
        recordData["CUSTOM_RECORDID"] = record.recordId
        recordData["CUSTOM_OLDPRICE"] = oldPrice.toFixed(2)

        records.push({
            recordId: record.recordId,
            result: 'Ok',
            data: Buffer.from(JSON.stringify(recordData), 'utf-8').toString('base64')
        });
    }

    
    console.log(`Processing completed.  Successful records ${records.length}.`);
    console.log(`Results: ${JSON.stringify(records)}`)
    
    return { 
        records: records 
    };

};

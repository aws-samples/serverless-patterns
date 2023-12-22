import {
    Context,
    FirehoseTransformationResult,
    FirehoseTransformationResultRecord
} from 'aws-lambda';
import { FirehoseTransformationEvent } from 'aws-lambda/trigger/kinesis-firehose-transformation'

export const handler = async (event: FirehoseTransformationEvent, context: Context): Promise<FirehoseTransformationResult> => {

    console.log(`Event: ${JSON.stringify(event, null, 2)}`);
    console.log(`Context: ${JSON.stringify(context, null, 2)}`);
    const records: FirehoseTransformationResultRecord[] = []

    for (const record of event.records) {
        /* This transformation is the "identity" transformation, the data is left intact */
        records.push({
            recordId: record.recordId,
            result: 'Ok',
            data: record.data,
        });
    }

    
    console.log(`Processing completed.  Successful records ${records.length}.`);
    console.log(`Results: ${JSON.stringify(records)}`)
    
    return { 
        records: records 
    };

};

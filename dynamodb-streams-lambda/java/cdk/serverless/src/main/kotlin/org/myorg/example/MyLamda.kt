package org.myorg.example

import com.amazonaws.services.lambda.runtime.Context
import com.amazonaws.services.lambda.runtime.LambdaLogger
import com.amazonaws.services.lambda.runtime.RequestHandler
import com.amazonaws.services.lambda.runtime.events.DynamodbEvent

class MyLambda : RequestHandler<DynamodbEvent, String> {

    override fun handleRequest(ddbEvent: DynamodbEvent, context: Context): String {
        val logger: LambdaLogger = context.logger
        if (ddbEvent.records != null) {
            logger.log("Event received " + ddbEvent.records)
            for (record in ddbEvent.records) {
                logger.log("Record $record")
            }
        }
        return "Validated " + ddbEvent.records.size + " records."
    }
}
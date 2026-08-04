import { withDurableExecution, DurableContext } from "@aws/durable-execution-sdk-js";
import { BedrockAgentCoreClient, InvokeAgentRuntimeCommand } from "@aws-sdk/client-bedrock-agentcore";

const agentRuntimeArn = process.env.AGENT_RUNTIME_ARN;
const agentRegion = process.env.AGENT_REGION || 'us-east-1';

interface transaction {
    id: number;
    amount: number;
    location: string;
    vendor: string;
    score?: number;
}

interface TransactionResult {
    statusCode: number;
    body: {
        transaction_id: number;
        amount: number;
        fraud_score?: number;
        result?: string;
        customerVerificationResult?: string;
    };

}

class fraudTransaction implements transaction {

    constructor(
        public id: number,
        public amount: number,
        public location: string,
        public vendor: string,
        public score: number = 0
    ){}

    async authorize(tx: fraudTransaction, cusRejection: boolean = false): Promise<TransactionResult> {
        //IMPLEMENT LOGIC TO AUTHORIZE TRANSCATION
        console.log(`Authorizing transactionId: ${tx.id}`)
        
        let result: TransactionResult = {
                statusCode: 200, 
                body: {
                    transaction_id: tx.id, 
                    amount: tx.amount, 
                    fraud_score: tx.score, 
                    result: 'authorized'
                }
            };

        //IF AUTHORIZATION CAME FROM CUSTOMER, INDICATE IN RESPONSE
        if (cusRejection){result.body.customerVerificationResult = 'TransactionApproved'};
       
        return result;
    }

    async suspend(tx: fraudTransaction): Promise<boolean> {
        //IMPLEMENT LOGIC TO SUSPEND TRANSCATION
        console.log(`Suspending transactionId: ${tx.id}`)
        return true;
    }
    
    async sendToFraud(tx: fraudTransaction, cusRejection: boolean = false): Promise<TransactionResult> {
        //IMPLEMENT LOGIC TO SEND TO FRAUD DEPARTMENT
        console.log(`Escalating to fraud department - transactionId: ${tx.id}`)

        let result: TransactionResult = {
                statusCode: 200, 
                body: {
                    transaction_id: tx.id, 
                    amount: tx.amount, 
                    fraud_score: tx.score, 
                    result: 'SentToFraudDept'
                }
            };

         //IF DECLINE CAME FROM CUSTOMER, INDICATE IN RESPONSE
        if (cusRejection){result.body.customerVerificationResult = 'TransactionDeclined'};
       
        return result;
    }

    async sendCustomerNotification(callbackId: string, type: string, tx: fraudTransaction): Promise<void> {
        //IMPLEMENT LOGIC TO SEND CUSTOMER NOTIFICATION
        if(type === 'email'){
            console.log(`Email Notification with callbackId: ${callbackId}`);
        } else{
            console.log(`SMS Notification with callbackId: ${callbackId}`);
        };
    }
}



export const handler = withDurableExecution(async (event: transaction, context: DurableContext) => {
    
    // Extract transaction information
    const tx = new fraudTransaction(event.id, event.amount, event.location, event.vendor, event?.score ?? 0)

    
    // Step 1: Check Transaction Fraud Score by invoking the Agent
    tx.score = await context.step("fraudCheck", async () => {
        
        if (tx.score === 0){
            console.log("No score submitted, sending to Fraud Agent for assessment");
            if (!agentRuntimeArn) {
                throw new Error('AGENT_RUNTIME_ARN environment variable is not set');
            }
            
            const client = new BedrockAgentCoreClient({ region: agentRegion });
            
            // Prepare the payload for AgentCore
            const payloadJson = JSON.stringify({ input: { amount: tx.amount } });
            
            // Invoke the agent - payload should be Buffer or Uint8Array
            const command = new InvokeAgentRuntimeCommand({
                agentRuntimeArn: agentRuntimeArn,
                qualifier: 'DEFAULT',
                payload: Buffer.from(payloadJson, 'utf-8'),
                contentType: 'application/json',
                accept: 'application/json'
            });
            
            const response = await client.send(command);
            
            // Parse the streaming response from AgentCore
            // Use the SDK's helper method to transform the stream to string
            if (response.response) {
                const responseText = await response.response.transformToString();
                const result = JSON.parse(responseText);
                console.log(result);
                // Extract risk_score from the agent's output
                if (result.output && result.output.risk_score !== undefined) {
                    return result.output.risk_score;
                }
            }
            
            // IF NO VALID RESPONSE FROM AGENT, SEND TO FRAUD
            console.log("No valid response from agent, sending to Fraud department for manual review.")
            return 5;
        }else{
            return tx.score;
        }
  });
  
console.log("Transaction Score = " + tx.score.toString());

  //Low Risk, Authorize Transaction
  if (tx.score < 3) return context.step("Authorize", async() => await tx.authorize(tx));
  if (tx.score >= 5) return context.step("sendToFraud", async() => await tx.sendToFraud(tx));  //High Risk, Send to Fraud Department
  
  //Potential Fraud Detected
  if (tx.score > 2 && tx.score < 5){

    //Step 2: Suspend the transaction 
    const tx_suspended = await context.step("suspendTransaction", async () => await tx.suspend(tx));

    //Step 3: Ask cardholder to authorize transaction
    const verified = await context.parallel("human-verification", [
         // Push verification with callback
        (ctx: DurableContext) => ctx.waitForCallback("SendVerificationEmail", async (callbackId: string) => {
            await tx.sendCustomerNotification(callbackId, 'email', tx);  
        }, { timeout: { days: 1 } }),
        // SMS verification with callback
        (ctx: DurableContext) => ctx.waitForCallback("SendVerificationSMS", async (callbackId: string) => {
            await tx.sendCustomerNotification(callbackId, 'sms', tx); 
        }, { timeout: { days: 1 } })
    ],
      {
        maxConcurrency: 2,
        completionConfig: {
            minSuccessful: 1, // Continue after cardholder verifies (email or sms)
            toleratedFailureCount: 0 // Fail immediately if any callback fails
        }
      }
    );

    //Step 4: Authorize Transaction or Send to Fraud Department
    const result = await context.step("advanceTransaction", async () => {
        // Check if verification succeeded (at least one callback succeeded)
        // Use hasFailure to check if any verification failed
        if(!verified.hasFailure && verified.successCount > 0){
            return await tx.authorize(tx, true);
        }else{
            // Verification failed or was rejected - send to fraud department
            return await tx.sendToFraud(tx, true);
        }
    })

    return result;
  }

  return {
            statusCode: 400, 
            body: {
                transaction_id: tx.id, 
                amount: tx.amount, 
                fraud_score: tx.score, 
                result: 'Unknown'
            }
        };;
});
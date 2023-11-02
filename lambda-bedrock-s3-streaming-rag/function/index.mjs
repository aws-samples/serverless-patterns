import { LanceDB } from "langchain/vectorstores/lancedb";
import { BedrockEmbeddings } from "langchain/embeddings/bedrock";
import { connect } from "vectordb"; // LanceDB
import { PromptTemplate } from "langchain/prompts";
import { ChatBedrock } from "langchain/chat_models/bedrock";
import { StringOutputParser } from "langchain/schema/output_parser";
import { RunnableSequence, RunnablePassthrough } from "langchain/schema/runnable";
import { formatDocumentsAsString } from "langchain/util/document";

const lanceDbSrc = process.env.s3BucketName;
const lanceDbTable = process.env.lanceDbTable;
const awsRegion = process.env.region;


const runChain = async ({query, model, streamingFormat}, responseStream) => {
    const db = await connect(`s3://${lanceDbSrc}/`);
    const table = await db.openTable(lanceDbTable);
    console.log('query', query);
    console.log('model', model);
    console.log('streamingFormat', streamingFormat);
  
    const embeddings = new BedrockEmbeddings({region:awsRegion});
    const vectorStore = new LanceDB(embeddings, {table});
    const retriever = vectorStore.asRetriever();

    const prompt = PromptTemplate.fromTemplate(
        `Answer the following question based only on the following context:
        {context}

        Question: {question}`
    );

    const llmModel = new ChatBedrock({
        model: model || 'anthropic.claude-instant-v1',
        region: awsRegion,
        streaming: true,
        maxTokens: 1000,
    });

    const chain = RunnableSequence.from([
        {
            context: retriever.pipe(formatDocumentsAsString),
            question: new RunnablePassthrough()
        },
        prompt,
        llmModel,
        new StringOutputParser()
    ]);

    const stream = await chain.stream(query);
    for await (const chunk of stream){
        console.log(chunk);
        switch (streamingFormat) {
            case 'fetch-event-source':
                responseStream.write(`event: message\n`);
                responseStream.write(`data: ${chunk}\n\n`);
                break;
            default:
                responseStream.write(chunk);
                break;
        }
    }
    responseStream.end();

  };

function parseBase64(message) {
    return JSON.parse(Buffer.from(message, "base64").toString("utf-8"));
}

export const handler = awslambda.streamifyResponse(async (event, responseStream, _context) => {
    console.log(JSON.stringify(event));
    let body = event.isBase64Encoded ? parseBase64(event.body) : JSON.parse(event.body);
    await runChain(body, responseStream);
    console.log(JSON.stringify({"status": "complete"}));
});

/*
Sample event 1:
{
    "query": "What models are available in Amazon Bedrock?",
}
Sample event 2:
{
    "query": "What models are available in Amazon Bedrock?",
    "model": "anthropic.claude-instant-v1"
}
Sample event 3:
{
    "query": "What models are available in Amazon Bedrock?",
    "model": "anthropic.claude-v2",
    "streamingFormat": "fetch-event-source"
}
*/
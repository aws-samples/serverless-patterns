import { LoremIpsum } from 'lorem-ipsum';
import { gzipSync } from 'zlib';

const lorem = new LoremIpsum(); 

const generateData = (length) => {
    console.log('> generateData');
    const arr = [];
    for (let i=0; i<length; i++){
        arr.push({
            text: lorem.generateParagraphs(3)
        });
    }
    return JSON.stringify(arr);
}

export const handler = async (event) => {
    console.log(`> handler`);
    
    // Generates ~1MB of random data
    let data = generateData(1000);
    
    // Compresses data using gzip and encodes to base64
    data = gzipSync(data).toString('base64');

    const response = {
        isBase64Encoded: true,
        headers: {
            'content-type': 'application/json',
            'content-encoding': 'gzip'
        },
        statusCode: 200,
        body: data
    };
    
    return response;

};


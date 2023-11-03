import { Handler } from 'aws-cdk-lib/aws-lambda';
import { httpsGet } from '../utils/https';

export const handler: Handler = async () => {
    console.log('calling a 3rd party api over the internet to fetch a random VIN...');
    const thirdPartyUrl = 'https://randomvin.com/getvin.php?type=real';

    try {
        const response = await httpsGet(thirdPartyUrl);
        console.log(`your random VIN is: ${response}`);
        return response;
    } catch (error: any) {
        console.error(`Error Fetching VIN: ${error.message}`);
        throw error;
    }
};

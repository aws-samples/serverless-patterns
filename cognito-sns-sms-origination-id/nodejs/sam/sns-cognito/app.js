const AWS = require('aws-sdk');
const b64 = require('base64-js');
const encryptionSdk = require('@aws-crypto/client-node');

console.log('Lambda function invoked');

// Mapping object to map numeric country codes to ISO2 country codes
const countryCodeMap = {
    '+1': 'US',
    '+91': 'IN',
    '+61': 'AU',
    '+56': 'CL',
    '+33': 'FR'
    // Add more mappings as needed
};

exports.handler = async (event) => {

    //Configure the encryption SDK client with the KMS key from the environment variables.
    const { encrypt, decrypt } = encryptionSdk.buildClient(encryptionSdk.CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT);
    const generatorKeyId = process.env.KEY_ALIAS;
    const keyIds = [ process.env.KEY_ARN ];
    const keyring = new encryptionSdk.KmsKeyringNode({ generatorKeyId, keyIds });
    console.log('Keyring is: ', keyring);
    console.log('Event is:', event);
    const sns = new AWS.SNS();
    const countryCode = event.request.userAttributes.phone_number.substring(0, 2);
    console.log('Country code:', countryCode);
    let plainTextCode;

    try {
    //Decrypt the secret code using encryption SDK.
    if(event.request.code){
        console.log("Trying to decrypt the code...");
        const { plaintext, messageHeader } = await decrypt(keyring, b64.toByteArray(event.request.code));
        plainTextCode = plaintext;
        console.log("Code decrypted: ",plainTextCode);
    }
    }
    catch (error) {
        console.error('Error decrypting the code:', error);
    }

    try {
        // Retrieve Origination Numbers using the listOriginationNumbers API
        const originationNumbersResponse = await sns.listOriginationNumbers().promise();
        const originationNumbers = originationNumbersResponse.PhoneNumbers;

        // Filter Origination Numbers based on the countryCode
        const filteredNumbers = originationNumbers.filter(
            (number) => number.Iso2CountryCode === countryCodeMap[countryCode]
        );

        console.log('Filtered Origination Numbers:', filteredNumbers);

        let originationNumber;

        if (filteredNumbers.length > 0) {
            // Generate a random index to select a random Origination Number
            const randomIndex = Math.floor(Math.random() * filteredNumbers.length);
            originationNumber = filteredNumbers[randomIndex].PhoneNumber;
        } else {
            console.log('No Origination Number available for the country code:', countryCode);
            originationNumber = process.env.SenderId;
            return;
        }

        console.log('Selected Origination Number:', originationNumber);

        // Send SMS using the determined origination number
        await sns.publish({
            PhoneNumber: event.request.userAttributes.phone_number,
            Message: 'Your verification code is: '+plainTextCode,
            MessageAttributes: {
                'AWS.MM.SMS.OriginationNumber': {
                    DataType: 'String',
                    StringValue: originationNumber,
                },
            },
        }).promise();

        console.log('SMS sent');
    } catch (error) {
        console.error('Error retrieving Origination Numbers:', error);
    }
};
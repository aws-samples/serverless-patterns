const AWS = require('aws-sdk');
const s3 = new AWS.S3();
const translate = new AWS.Translate();

const apig = new AWS.ApiGatewayManagementApi({
    endpoint: process.env.APIG_ENDPOINT,
});

module.exports.handler = async (event, context) => {
    console.log(event)
    const jobName = event.jobName,
        outputBucket = event.outputBucket,
        connectionId = event.connectionId,
        inputLanguageCode = event.inputLanguageCode,
        outputLanguageCode = event.outputLanguageCode;

    let params = {
        Bucket: outputBucket,
        Key: jobName+'.json'
    };

    let sourceLanguageCode = 'en';
    if(inputLanguageCode != '') {
        switch(inputLanguageCode) {
            case 'af-ZA': sourceLanguageCode = 'af'; break;
            case 'ar-AE': sourceLanguageCode = 'ar'; break;
            case 'ar-SA': sourceLanguageCode = 'ar'; break;
            case 'zh-CN': sourceLanguageCode = 'zh'; break;
            case 'zh-TW': sourceLanguageCode = 'zh-TW'; break;
            case 'da-DK': sourceLanguageCode = 'da'; break;
            case 'nl-NL': sourceLanguageCode = 'nl'; break;
            case 'en-AU': sourceLanguageCode = 'en'; break;
            case 'en-GB': sourceLanguageCode = 'en'; break;
            case 'en-IN': sourceLanguageCode = 'en'; break;
            case 'en-IE': sourceLanguageCode = 'en'; break;
            case 'en-NZ': sourceLanguageCode = 'en'; break;
            case 'en-AB': sourceLanguageCode = 'en'; break;
            case 'en-ZA': sourceLanguageCode = 'en'; break;
            case 'en-US': sourceLanguageCode = 'en'; break;
            case 'en-WL': sourceLanguageCode = 'en'; break;
            case 'fr-FR': sourceLanguageCode = 'fr'; break;
            case 'fr-CA': sourceLanguageCode = 'fr-CA'; break;
            case 'fa-IR': sourceLanguageCode = 'fa'; break;
            case 'de-DE': sourceLanguageCode = 'de'; break;
            case 'de-CH': sourceLanguageCode = 'de'; break;
            case 'he-IL': sourceLanguageCode = 'he'; break;
            case 'hi-IN': sourceLanguageCode = 'hi'; break;
            case 'id-ID': sourceLanguageCode = 'id'; break;
            case 'it-IT': sourceLanguageCode = 'it'; break;
            case 'ja-JP': sourceLanguageCode = 'ja'; break;
            case 'ko-KR': sourceLanguageCode = 'ko'; break;
            case 'ms-MY': sourceLanguageCode = 'ms'; break;
            case 'pt-PT': sourceLanguageCode = 'pt-PT'; break;
            case 'pt-BR': sourceLanguageCode = 'pt'; break;
            case 'ru-RU': sourceLanguageCode = 'ru'; break;
            case 'es-ES': sourceLanguageCode = 'es'; break;
            case 'es-US': sourceLanguageCode = 'es-MX'; break;
            case 'sv-SE': sourceLanguageCode = 'sv'; break;
            case 'ta-IN': sourceLanguageCode = 'ta'; break;
            case 'te-IN': sourceLanguageCode = 'te'; break;
            case 'th-TH': sourceLanguageCode = 'th'; break;
            case 'tr-TR': sourceLanguageCode = 'tr'; break;
            case 'vi-VN': sourceLanguageCode = 'vi'; break;
        }
    }

    let targetLanguageCode = 'hi';
    if(outputLanguageCode!='') {
        switch(outputLanguageCode) {
            case 'Arabic |arb': targetLanguageCode = 'ar'; break;
            case 'Arabic (Gulf) |ar-AE': targetLanguageCode = 'ar'; break;
            case 'Catalan |ca-ES': targetLanguageCode = 'ca'; break;
            case 'Chinese (Cantonese) |yue-CN': targetLanguageCode = 'zh'; break;
            case 'Chinese (Mandarin) |cmn-CN': targetLanguageCode = 'zh-TW'; break;
            case 'Danish |da-DK': targetLanguageCode = 'da'; break;
            case 'Dutch |nl-NL': targetLanguageCode = 'nl'; break;
            case 'English (Australian) |en-AU': targetLanguageCode = 'en'; break;
            case 'English (British) |en-GB': targetLanguageCode = 'en'; break;
            case 'English (Indian) |en-IN': targetLanguageCode = 'en'; break;
            case 'English (New Zealand) |en-NZ': targetLanguageCode = 'en'; break;
            case 'English (South African) |en-ZA': targetLanguageCode = 'en'; break;
            case 'English (US) |en-US': targetLanguageCode = 'en'; break;
            case 'English (Welsh) |en-GB-WLS': targetLanguageCode = 'en'; break;
            case 'Finnish |fi-FI': targetLanguageCode = 'fi'; break;
            case 'French |fr-FR': targetLanguageCode = 'fr'; break;
            case 'French (Canadian) |fr-CA': targetLanguageCode = 'fr-CA'; break;
            case 'Hindi |hi-IN': targetLanguageCode = 'hi'; break;
            case 'German |de-DE': targetLanguageCode = 'de'; break;
            case 'German (Austrian) |de-AT': targetLanguageCode = 'de'; break;
            case 'Icelandic |is-IS': targetLanguageCode = 'is'; break;
            case 'Italian |it-IT': targetLanguageCode = 'it'; break;
            case 'Japanese |ja-JP': targetLanguageCode = 'ja'; break;
            case 'Korean |ko-KR': targetLanguageCode = 'ko'; break;
            case 'Norwegian |nb-NO': targetLanguageCode = 'no'; break;
            case 'Polish |pl-PL': targetLanguageCode = 'pl'; break;
            case 'Portuguese (Brazilian) |pt-BR': targetLanguageCode = 'pt'; break;
            case 'Portuguese (European) |pt-PT': targetLanguageCode = 'pt-PT'; break;
            case 'Romanian |ro-RO': targetLanguageCode = 'ro'; break;
            case 'Russian |ru-RU': targetLanguageCode = 'ru'; break;
            case 'Spanish (European) |es-ES': targetLanguageCode = 'es'; break;
            case 'Spanish (Mexican) |es-MX': targetLanguageCode = 'es-MX'; break;
            case 'Spanish (US) |es-US': targetLanguageCode = 'es-MX'; break;
            case 'Swedish |sv-SE': targetLanguageCode = 'sv'; break;
            case 'Turkish |tr-TR': targetLanguageCode = 'tr'; break;
            case 'Welsh |cy-GB': targetLanguageCode = 'cy'; break;
        }
    }

    const s3Body = await s3.getObject(params).promise()
    const transcribedOutput = s3Body.Body.toString('utf-8');
    console.log(transcribedOutput)
    const originalText = JSON.parse(transcribedOutput).results.transcripts[0].transcript;
    let translateParams = {
        Text: originalText,
        SourceLanguageCode: sourceLanguageCode,
        TargetLanguageCode: targetLanguageCode
      }
    const translatedResponse = await translate.translateText(translateParams).promise();
    const translatedText = translatedResponse.TranslatedText;
    console.log(translatedText)

    params = {
        Bucket: outputBucket,
        Key: "translatedText",
        Body: translatedText
    };

    await s3.putObject(params).promise();


    await apig.postToConnection({
        ConnectionId: connectionId,
        Data: translatedText
    }).promise();

    return { outputBucket, connectionId, outputLanguageCode }
    
}
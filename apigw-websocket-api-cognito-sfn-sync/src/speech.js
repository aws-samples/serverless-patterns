const AWS = require('aws-sdk');
const s3 = new AWS.S3();
const polly = new AWS.Polly();
const uuidv1 = require('uuidv1');

const apig = new AWS.ApiGatewayManagementApi({
  endpoint: process.env.APIG_ENDPOINT,
});

module.exports.handler = async (event, context) => {
    console.log(event)
    const outputBucket = event.outputBucket,
        connectionId = event.connectionId,
        outputLanguageCode = event.outputLanguageCode;

    let targetLanguageCode = "hi-IN";
    if(outputLanguageCode != "") {
      targetLanguageCode = outputLanguageCode.split("|")[1]
    }
    let voiceId = "Aditi";
    switch(targetLanguageCode) {
      case "arb": voiceId = "Zeina"; break;
      case 'ar-AE': voiceId = 'Hala'; break;
      case 'ca-ES': voiceId = 'Arlet'; break;
      case 'yue-CN': voiceId = 'Hiujin'; break;
      case 'cmn-CN': voiceId = 'Zhiyu'; break;
      case 'da-DK': voiceId = 'Naja'; break;
      case 'nl-NL': voiceId = 'Laura'; break;
      case 'en-AU': voiceId = 'Nicole'; break;
      case 'en-GB': voiceId = 'Amy'; break;
      case 'en-IN': voiceId = 'Aditi'; break;
      case 'en-NZ': voiceId = 'Aria'; break;
      case 'en-ZA': voiceId = 'Ayanda'; break;
      case 'en-US': voiceId = 'Ivy'; break;
      case 'en-GB-WLS': voiceId = 'Geraint'; break;
      case 'fi-FI': voiceId = 'Suvi'; break;
      case 'fr-FR': voiceId = 'Celine'; break;
      case 'fr-CA': voiceId = 'Chantal'; break;
      case 'hi-IN': voiceId = 'Aditi'; break;
      case 'de-DE': voiceId = 'Marlene'; break;
      case 'de-AT': voiceId = 'Hannah'; break;
      case 'is-IS': voiceId = 'Dora'; break;
      case 'it-IT': voiceId = 'Carla'; break;
      case 'ja-JP': voiceId = 'Mizuki'; break;
      case 'ko-KR': voiceId = 'Seoyeon'; break;
      case 'nb-NO': voiceId = 'Liv'; break;
      case 'pl-PL': voiceId = 'Ewa'; break;
      case 'pt-BR': voiceId = 'Camila'; break;
      case 'pt-PT': voiceId = 'Cristiano'; break;
      case 'ro-RO': voiceId = 'Carmen'; break;
      case 'ru-RU': voiceId = 'Tatyana'; break;
      case 'es-ES': voiceId = 'Conchita'; break;
      case 'es-MX': voiceId = 'Mia'; break;
      case 'es-US': voiceId = 'Lupe'; break;
      case 'sv-SE': voiceId = 'Astrid'; break;
      case 'tr-TR': voiceId = 'Filiz'; break;
      case 'cy-GB': voiceId = 'Gwyneth'; break;
    }

    let params = {
      Bucket: outputBucket,
      Key: "translatedText"
    };

    const s3Body = await s3.getObject(params).promise()
    const text = s3Body.Body.toString('utf-8');

    const speechParams = {
        "LanguageCode": targetLanguageCode,
        "OutputFormat": "mp3",
        "Text": text,
        "VoiceId": voiceId
    }

    console.log(speechParams)

    const response = await polly.synthesizeSpeech(speechParams).promise();
    let audioStream = response.AudioStream;
    let key = uuidv1();
    params = {
      Bucket: outputBucket,
      Key: key + '.mp3',
      Body: audioStream
    };

    await apig.postToConnection({
        ConnectionId: connectionId,
        Data: "Speech Synthesize complete"
      }).promise();

    const s3Response = await s3.putObject(params).promise();
    let s3params = {
        Bucket: outputBucket,
        Key: key + '.mp3',
      };
    let url = s3.getSignedUrl("getObject", s3params);
    console.log(url);
    await apig.postToConnection({
      ConnectionId: connectionId,
      Data: url
    }).promise();
    return { outputBucket, key: key + '.mp3' };
}
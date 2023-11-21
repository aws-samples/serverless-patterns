# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import json

client = boto3.client('comprehend')

def lambda_handler(event, context):
    text = event['text']

    response = client.detect_dominant_language(
    Text=text        
    )
    
    lang = response["Languages"][0]["LanguageCode"]
    print(lang)
    if lang == 'af':
        comp_response = "The detected language (dominant language) is Afrikaans."
    elif lang == 'am':
        comp_response = "The detected language (dominant language) is Amharic."
    elif lang == 'ar':
        comp_response = "The detected language (dominant language) is Arabic."
    elif lang == 'as':
        comp_response = "The detected language (dominant language) is Assamese."
    elif lang == 'az':
        comp_response = "The detected language (dominant language) is Azerbaijani."
    elif lang == 'ba':
        comp_response = "The detected language (dominant language) is Bashkir."
    elif lang == 'be':
        comp_response = "The detected language (dominant language) is Belarusian."
    elif lang == 'bn':
        comp_response = "The detected language (dominant language) is Bengali."
    elif lang == 'bs':
        comp_response = "The detected language (dominant language) is Bosnian."
    elif lang == 'bg':
        comp_response = "The detected language (dominant language) is Bulgarian."
    elif lang == 'ca':
        comp_response = "The detected language (dominant language) is Catalan."
    elif lang == 'ceb':
        comp_response = "The detected language (dominant language) is Cebuano."
    elif lang == 'cz':
        comp_response = "The detected language (dominant language) is Czech."
    elif lang == 'cv':
        comp_response = "The detected language (dominant language) is Chuvash."
    elif lang == 'cy':
        comp_response = "The detected language (dominant language) is Welsh."
    elif lang == 'da':
        comp_response = "The detected language (dominant language) is Danish."
    elif lang == 'de':
        comp_response = "The detected language (dominant language) is German."
    elif lang == 'el':
        comp_response = "The detected language (dominant language) is Greek."
    elif lang == 'en':
        comp_response = "The detected language (dominant language) is English."
    elif lang == 'eo':
        comp_response = "The detected language (dominant language) is Esperanto."
    elif lang == 'et':
        comp_response = "The detected language (dominant language) is Estonian."
    elif lang == 'eu':
        comp_response = "The detected language (dominant language) is Basque."
    elif lang == 'fa':
        comp_response = "The detected language (dominant language) is Persian."
    elif lang == 'fi':
        comp_response = "The detected language (dominant language) is Finnish."
    elif lang == 'fr':
        comp_response = "The detected language (dominant language) is French."
    elif lang == 'gd':
        comp_response = "The detected language (dominant language) is Scottish Gaelic."
    elif lang == 'ga':
        comp_response = "The detected language (dominant language) is Irish."
    elif lang == 'gl':
        comp_response = "The detected language (dominant language) is Galician."
    elif lang == 'gu':
        comp_response = "The detected language (dominant language) is Gujarati."
    elif lang == 'ht':
        comp_response = "The detected language (dominant language) is Haitian."
    elif lang == 'he':
        comp_response = "The detected language (dominant language) is Herbew."
    elif lang == 'ha':
        comp_response = "The detected language (dominant language) is Hausa."
    elif lang == 'hi':
        comp_response = "The detected language (dominant language) is Hindi."
    elif lang == 'hr':
        comp_response = "The detected language (dominant language) is Croatian."
    elif lang == 'hu':
        comp_response = "The detected language (dominant language) is Hungarian."
    elif lang == 'hy':
        comp_response = "The detected language (dominant language) is Armenian."
    elif lang == 'ilo':
        comp_response = "The detected language (dominant language) is Iloko."
    elif lang == 'id':
        comp_response = "The detected language (dominant language) is Indonesian."
    elif lang == 'is':
        comp_response = "The detected language (dominant language) is Icelandic."
    elif lang == 'it':
        comp_response = "The detected language (dominant language) is Italian."
    elif lang == 'jv':
        comp_response = "The detected language (dominant language) is Javanese."
    elif lang == 'ja':
        comp_response = "The detected language (dominant language) is Japanese."
    elif lang == 'kn':
        comp_response = "The detected language (dominant language) is Kannada."
    elif lang == 'ka':
        comp_response = "The detected language (dominant language) is Georgian."
    elif lang == 'kk':
        comp_response = "The detected language (dominant language) is Kazakh."
    elif lang == 'km':
        comp_response = "The detected language (dominant language) is Central Khmer."
    elif lang == 'ky':
        comp_response = "The detected language (dominant language) is Kirghiz."
    elif lang == 'ko':
        comp_response = "The detected language (dominant language) is Korean."
    elif lang == 'ku':
        comp_response = "The detected language (dominant language) is Kurdish."
    elif lang == 'lo':
        comp_response = "The detected language (dominant language) is Lao."
    elif lang == 'la':
        comp_response = "The detected language (dominant language) is Latin."
    elif lang == 'lv':
        comp_response = "The detected language (dominant language) is Latvian."
    elif lang == 'lt':
        comp_response = "The detected language (dominant language) is Lithuanian."
    elif lang == 'lb':
        comp_response = "The detected language (dominant language) is Luxembourgish."
    elif lang == 'ml':
        comp_response = "The detected language (dominant language) is Malayalam."
    elif lang == 'mt':
        comp_response = "The detected language (dominant language) is Maltese."
    elif lang == 'mr':
        comp_response = "The detected language (dominant language) is Marathi."
    elif lang == 'mk':
        comp_response = "The detected language (dominant language) is Macedonian."
    elif lang == 'mg':
        comp_response = "The detected language (dominant language) is Malagasy."
    elif lang == 'mn':
        comp_response = "The detected language (dominant language) is Mongolian."
    elif lang == 'ms':
        comp_response = "The detected language (dominant language) is Malay."
    elif lang == 'my':
        comp_response = "The detected language (dominant language) is Burmese."
    elif lang == 'ne':
        comp_response = "The detected language (dominant language) is Nepali."
    elif lang == 'new':
        comp_response = "The detected language (dominant language) is Newari."
    elif lang == 'nl':
        comp_response = "The detected language (dominant language) is Dutch."
    elif lang == 'no':
        comp_response = "The detected language (dominant language) is Norwegian."
    elif lang == 'or':
        comp_response = "The detected language (dominant language) is Oriya."
    elif lang == 'om':
        comp_response = "The detected language (dominant language) is Oromo."
    elif lang == 'pa':
        comp_response = "The detected language (dominant language) is Punjabi."
    elif lang == 'pl':
        comp_response = "The detected language (dominant language) is Polish."
    elif lang == 'pt':
        comp_response = "The detected language (dominant language) is Portuguese."
    elif lang == 'ps':
        comp_response = "The detected language (dominant language) is Pushto."
    elif lang == 'qu':
        comp_response = "The detected language (dominant language) is Quechua."
    elif lang == 'ro':
        comp_response = "The detected language (dominant language) is Romainan."
    elif lang == 'ru':
        comp_response = "The detected language (dominant language) is Russian."
    elif lang == 'sa':
        comp_response = "The detected language (dominant language) is Sanskrit."
    elif lang == 'si':
        comp_response = "The detected language (dominant language) is Sinhala."
    elif lang == 'sk':
        comp_response = "The detected language (dominant language) is Slovak."
    elif lang == 'sl':
        comp_response = "The detected language (dominant language) is Slovenian."
    elif lang == 'sd':
        comp_response = "The detected language (dominant language) is Sindhi."
    elif lang == 'so':
        comp_response = "The detected language (dominant language) is Somali."
    elif lang == 'es':
        comp_response = "The detected language (dominant language) is Spanish."
    elif lang == 'sq':
        comp_response = "The detected language (dominant language) is Albanian."
    elif lang == 'sr':
        comp_response = "The detected language (dominant language) is Serbian."
    elif lang == 'su':
        comp_response = "The detected language (dominant language) is Sundanese."
    elif lang == 'sw':
        comp_response = "The detected language (dominant language) is Swahili."
    elif lang == 'sv':
        comp_response = "The detected language (dominant language) is Swedish."
    elif lang == 'ta':
        comp_response = "The detected language (dominant language) is Tamil."
    elif lang == 'tt':
        comp_response = "The detected language (dominant language) is Tatar."
    elif lang == 'te':
        comp_response = "The detected language (dominant language) is Telugu."
    elif lang == 'tg':
        comp_response = "The detected language (dominant language) is Tajik."
    elif lang == 'tl':
        comp_response = "The detected language (dominant language) is Tagalog."
    elif lang == 'th':
        comp_response = "The detected language (dominant language) is Thai."
    elif lang == 'tk':
        comp_response = "The detected language (dominant language) is Turkmen."
    elif lang == 'tr':
        comp_response = "The detected language (dominant language) is Turkish."
    elif lang == 'ug':
        comp_response = "The detected language (dominant language) is Uighur."
    elif lang == 'uk':
        comp_response = "The detected language (dominant language) is Ukranian."
    elif lang == 'ur':
        comp_response = "The detected language (dominant language) is Urdu."
    elif lang == 'uz':
        comp_response = "The detected language (dominant language) is Uzbek."
    elif lang == 'vi':
        comp_response = "The detected language (dominant language) is Vietnamese."
    elif lang == 'yi':
        comp_response = "The detected language (dominant language) is Yiddish."
    elif lang == 'yo':
        comp_response = "The detected language (dominant language) is Yoruba."
    elif lang == 'zh':
        comp_response = "The detected language (dominant language) is Chinese (Simplified)."
    elif lang == 'zh-TW':
        comp_response = "The detected language (dominant language) is Chinese (Traditional)."
    else:
        comp_response = "The language (dominant language) cannot be identified. Please refer - https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html"
    
        
    return comp_response
    

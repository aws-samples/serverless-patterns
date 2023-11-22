//Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
//SPDX-License-Identifier: MIT-0

const { ComprehendClient, DetectDominantLanguageCommand } = require("@aws-sdk/client-comprehend");
// Initailise Comprehend client 
const client = new ComprehendClient({
  apiVersion: "2017-11-27"});
exports.handler = async (event) => {
  
  const jasonObj= JSON.parse(event.body);
  const params = {
    Text: jasonObj['input_text']
  };
  console.log(params)
  try { 
    // Call DetectDominantLanguage
    const command = new DetectDominantLanguageCommand(params);
    const response = await client.send(command);
    // Obtain the language code and confidence score
    
    const languageCode = response.Languages[0].LanguageCode;
    const score = response.Languages[0].Score;
    
    // Return both in response
    if (languageCode === 'af') {
      let responseObj = {
      DetectedDominantlanguage: "Afrikaans",
      score : JSON.stringify(score),
      };
      
    return {
      statusCode: 200,
      body: JSON.stringify(responseObj)
    };
    }
    else if (languageCode === 'am') {
    let responseObj = {
      DetectedDominantlanguage: "Amharic",
      score : JSON.stringify(score),
      };
      
    return {
      statusCode: 200,
      body: JSON.stringify(responseObj)
    };
    }
    else if (languageCode === 'ar') {
    let responseObj = {
      DetectedDominantlanguage: "Arabic",
      score : JSON.stringify(score),
      };
      
    return {
      statusCode: 200,
      body: JSON.stringify(responseObj)
    };
    }
    else if (languageCode === 'as') {
    let responseObj = {
      DetectedDominantlanguage: "Assamese",
      score : JSON.stringify(score),
      };
      
    return {
      statusCode: 200,
      body: JSON.stringify(responseObj)
    };
    }
    else if (languageCode === 'az') {
    let responseObj = {
      DetectedDominantlanguage: "Azerbaijani",
      score : JSON.stringify(score),
      };
      
    return {
      statusCode: 200,
      body: JSON.stringify(responseObj)
    };
    }
    else if (languageCode === 'ba') {
    let responseObj = {
      DetectedDominantlanguage: "Bashkir",
      score : JSON.stringify(score),
      };
      
    return {
      statusCode: 200,
      body: JSON.stringify(responseObj)
    };
    }
    else if (languageCode === 'be') {
    let responseObj = {
      DetectedDominantlanguage: "Belarusian",
      score : JSON.stringify(score),
      };
      
    return {
      statusCode: 200,
      body: JSON.stringify(responseObj)
    };
    }
    else if (languageCode === 'bn') {
    let responseObj = {
      DetectedDominantlanguage: "Bengali",
      score : JSON.stringify(score),
      };
      
    return {
      statusCode: 200,
      body: JSON.stringify(responseObj)
    };
    }
    else if (languageCode === 'bs') {
    let responseObj = {
      DetectedDominantlanguage: "Bosnian",
      score : JSON.stringify(score),
      };
      
    return {
      statusCode: 200,
      body: JSON.stringify(responseObj)
    };
    }
    else if (languageCode === 'bg') {
    let responseObj = {
      DetectedDominantlanguage: "Bulgarian",
      score : JSON.stringify(score),
      };
      
    return {
      statusCode: 200,
      body: JSON.stringify(responseObj)
    };

    }
    else if (languageCode === 'ca') {
    let responseObj = {
      DetectedDominantlanguage: "Catalan",
      score : JSON.stringify(score),
      };
      
    return {
      statusCode: 200,
      body: JSON.stringify(responseObj)
    };
    }
    else if (languageCode === 'ceb') {
    let responseObj = {
      DetectedDominantlanguage: "Cebuano",
      score : JSON.stringify(score),
      };
      
    return {
      statusCode: 200,
      body: JSON.stringify(responseObj)
    };
    }
    else if (languageCode === 'cz') {
      let responseObj = {
        DetectedDominantlanguage: "Czech",
        score : JSON.stringify(score),
        };
        
      return {
        statusCode: 200,
        body: JSON.stringify(responseObj)
      };
      }
    else if (languageCode === 'cv') {
    let responseObj = {
      DetectedDominantlanguage: "Chuvash",
      score : JSON.stringify(score),
      };
      
    return {
      statusCode: 200,
      body: JSON.stringify(responseObj)
    };
    }
    else if (languageCode === 'cy') {
    let responseObj = {
      DetectedDominantlanguage: "Welsh",
      score : JSON.stringify(score),
      };
      
    return {
      statusCode: 200,
      body: JSON.stringify(responseObj)
    };
    }
    else if (languageCode === 'da') {
      let responseObj = {
        DetectedDominantlanguage: "Danish",
        score : JSON.stringify(score),
        };
        
      return {
        statusCode: 200,
        body: JSON.stringify(responseObj)
      };
      }
    else if (languageCode === 'de') {
    let responseObj = {
      DetectedDominantlanguage: "German",
      score : JSON.stringify(score),
      };
      
    return {
      statusCode: 200,
      body: JSON.stringify(responseObj)
    };
    }
    else if (languageCode === 'el') {
      let responseObj = {
        DetectedDominantlanguage: "Greek",
        score : JSON.stringify(score),
        };
        
      return {
        statusCode: 200,
        body: JSON.stringify(responseObj)
      };
      }
    else if (languageCode === 'en') {
        let responseObj = {
          DetectedDominantlanguage: "English",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'eo') {
        let responseObj = {
          DetectedDominantlanguage: "Esperanto",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'et') {
        let responseObj = {
          DetectedDominantlanguage: "Estonian",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'eu') {
        let responseObj = {
          DetectedDominantlanguage: "Basque",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'fa') {
        let responseObj = {
          DetectedDominantlanguage: "Persian",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'fi') {
        let responseObj = {
          DetectedDominantlanguage: "Finnish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'fr') {
        let responseObj = {
          DetectedDominantlanguage: "French",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'gd') {
        let responseObj = {
          DetectedDominantlanguage: "Scottish Gaelic",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'ga') {
        let responseObj = {
          DetectedDominantlanguage: "Irish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'gl') {
        let responseObj = {
          DetectedDominantlanguage: "Galician",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'gu') {
        let responseObj = {
          DetectedDominantlanguage: "Gujarati",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'ht') {
        let responseObj = {
          DetectedDominantlanguage: "Haitian",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'he') {
        let responseObj = {
          DetectedDominantlanguage: "Hebrew",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'ha') {
        let responseObj = {
          DetectedDominantlanguage: "Hausa",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'hi') {
        let responseObj = {
          DetectedDominantlanguage: "Hindi",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'hr') {
        let responseObj = {
          DetectedDominantlanguage: "Croatian",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'hu') {
        let responseObj = {
          DetectedDominantlanguage: "Hungarian",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'hy') {
        let responseObj = {
          DetectedDominantlanguage: "Armenian",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'ilo') {
        let responseObj = {
          DetectedDominantlanguage: "Iloko",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'id') {
        let responseObj = {
          DetectedDominantlanguage: "Indonesian",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'is') {
        let responseObj = {
          DetectedDominantlanguage: "Icelandic",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'it') {
        let responseObj = {
          DetectedDominantlanguage: "Italian",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'jv') {
        let responseObj = {
          DetectedDominantlanguage: "Javanese",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'ja') {
        let responseObj = {
          DetectedDominantlanguage: "Japanese",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'kn') {
        let responseObj = {
          DetectedDominantlanguage: "Kannada",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'ka') {
        let responseObj = {
          DetectedDominantlanguage: "Georgian",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'kk') {
        let responseObj = {
          DetectedDominantlanguage: "Kazakh",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'kh') {
        let responseObj = {
          DetectedDominantlanguage: "Central Khmer",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'ky') {
        let responseObj = {
          DetectedDominantlanguage: "Kirghiz",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'ko') {
        let responseObj = {
          DetectedDominantlanguage: "Korean",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    
    else if (languageCode === 'ku') {
        let responseObj = {
          DetectedDominantlanguage: "Kurdish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'es') {
        let responseObj = {
          DetectedDominantlanguage: "Spanish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lo') {
        let responseObj = {
          DetectedDominantlanguage: "Lao",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'la') {
        let responseObj = {
          DetectedDominantlanguage: "Latin",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lv') {
        let responseObj = {
          DetectedDominantlanguage: "Latvian",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lt') {
        let responseObj = {
          DetectedDominantlanguage: "Lithuanian",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }

    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }

    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }
    else if (languageCode === 'lb') {
        let responseObj = {
          DetectedDominantlanguage: "Luxembourgish",
          score : JSON.stringify(score),
          };
          
      return {
          statusCode: 200,
          body: JSON.stringify(responseObj)
        };
      }

    else {
      return {
        statusCode: 200,
        message: JSON.stringify("Language not supported. Please refer - https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html")}
    }
    
    
  } catch (error) {
    console.error(error);
    return {
      statusCode: 500,
      body: JSON.stringify(error)
    };
  }
};
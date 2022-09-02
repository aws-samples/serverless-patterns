import axios from 'axios';

export const handler = async (event: any = {}): Promise<any> => {
  const applicationId = process.env.APPCONFIG_APPLICATION_ID;
  const environment = process.env.APPCONFIG_ENVIRONMENT;
  const configurationId = process.env.APPCONFIG_CONFIGURATION_ID;
  const featureFlag = process.env.FEATURE_FLAG_NAME;

  const url = 'http://localhost:2772/applications/' + applicationId + '/environments/' + environment + '/configurations/' + configurationId + '?flag=' + featureFlag;

  try {
    const { data, status } = await axios.get(url);

    if (data.enabled == true) {
      return 'Feature flag ENABLED.'
    } else {
      return 'Feature flag DISABLED.'
    }
  } catch (error) {
    console.log(console.error);
  }
};

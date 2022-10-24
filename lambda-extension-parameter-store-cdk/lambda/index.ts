import axios from 'axios';

export const handler = async (event: any = {}): Promise<any> => {
  const parameterPath = process.env.PARAMETER_PATH;
  const url = 'http://localhost:2773/systemsmanager/parameters/get?name=' + parameterPath;

  try {
    const data = await axios.get(url, {
      headers: {
        'X-Aws-Parameters-Secrets-Token': process.env.AWS_SESSION_TOKEN
      }
    });

    return data.data.Parameter.Value;
  } catch (error) {
    console.log(error);
  }
};

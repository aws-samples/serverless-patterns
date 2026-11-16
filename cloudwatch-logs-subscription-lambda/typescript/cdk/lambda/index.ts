const zlib = require("zlib");

export const handler = async (event: any = {}): Promise<any> => {
  if (event.awslogs && event.awslogs.data) {
    const payload = Buffer.from(event.awslogs.data, 'base64');
    console.log(zlib.unzipSync(payload).toString());
  }
};

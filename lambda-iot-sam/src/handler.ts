import { IoTDataPlane } from "@aws-sdk/client-iot-data-plane";

const iotdata = new IoTDataPlane({ endpoint: process.env.IOT_DATA_ENDPOINT })

export const handler: any = async (event: any): Promise<any> => {
  const params = {
    topic: `${process.env.IOT_TOPIC}`,
    qos: 1,
    payload: JSON.stringify({
      type: "hello",
      detail: "world"
    })
  };
  await iotdata.publish(params);
};

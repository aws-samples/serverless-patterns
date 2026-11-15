"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.handler = void 0;
const client_iot_data_plane_1 = require("@aws-sdk/client-iot-data-plane");
const iotdata = new client_iot_data_plane_1.IoTDataPlane({ endpoint: process.env.IOT_DATA_ENDPOINT });
const handler = async (event) => {
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
exports.handler = handler;
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiaGFuZGxlci5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzIjpbImhhbmRsZXIudHMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6Ijs7O0FBQUEsMEVBQThEO0FBRTlELE1BQU0sT0FBTyxHQUFHLElBQUksb0NBQVksQ0FBQyxFQUFFLFFBQVEsRUFBRSxPQUFPLENBQUMsR0FBRyxDQUFDLGlCQUFpQixFQUFFLENBQUMsQ0FBQTtBQUV0RSxNQUFNLE9BQU8sR0FBUSxLQUFLLEVBQUUsS0FBVSxFQUFnQixFQUFFO0lBQzdELE1BQU0sTUFBTSxHQUFHO1FBQ2IsS0FBSyxFQUFFLEdBQUcsT0FBTyxDQUFDLEdBQUcsQ0FBQyxTQUFTLEVBQUU7UUFDakMsR0FBRyxFQUFFLENBQUM7UUFDTixPQUFPLEVBQUUsSUFBSSxDQUFDLFNBQVMsQ0FBQztZQUN0QixJQUFJLEVBQUUsT0FBTztZQUNiLE1BQU0sRUFBRSxPQUFPO1NBQ2hCLENBQUM7S0FDSCxDQUFDO0lBQ0YsTUFBTSxPQUFPLENBQUMsT0FBTyxDQUFDLE1BQU0sQ0FBQyxDQUFDO0FBQ2hDLENBQUMsQ0FBQztBQVZXLFFBQUEsT0FBTyxXQVVsQiJ9
"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.handler = void 0;
const iotdata_1 = __importDefault(require("aws-sdk/clients/iotdata"));
const iotdata = new iotdata_1.default({ endpoint: process.env.IOT_DATA_ENDPOINT });
const handler = async (event) => {
    const params = {
        topic: `${process.env.IOT_TOPIC}`,
        qos: 1,
        payload: JSON.stringify({
            type: "hello",
            detail: "world"
        })
    };
    await iotdata.publish(params).promise();
};
exports.handler = handler;
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiaGFuZGxlci5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzIjpbImhhbmRsZXIudHMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6Ijs7Ozs7O0FBQUEsc0VBQThDO0FBRTlDLE1BQU0sT0FBTyxHQUFHLElBQUksaUJBQU8sQ0FBQyxFQUFFLFFBQVEsRUFBRSxPQUFPLENBQUMsR0FBRyxDQUFDLGlCQUFpQixFQUFFLENBQUMsQ0FBQTtBQUVqRSxNQUFNLE9BQU8sR0FBUSxLQUFLLEVBQUUsS0FBVSxFQUFnQixFQUFFO0lBQzdELE1BQU0sTUFBTSxHQUFHO1FBQ2IsS0FBSyxFQUFFLEdBQUcsT0FBTyxDQUFDLEdBQUcsQ0FBQyxTQUFTLEVBQUU7UUFDakMsR0FBRyxFQUFFLENBQUM7UUFDTixPQUFPLEVBQUUsSUFBSSxDQUFDLFNBQVMsQ0FBQztZQUN0QixJQUFJLEVBQUUsT0FBTztZQUNiLE1BQU0sRUFBRSxPQUFPO1NBQ2hCLENBQUM7S0FDSCxDQUFDO0lBQ0YsTUFBTSxPQUFPLENBQUMsT0FBTyxDQUFDLE1BQU0sQ0FBQyxDQUFDLE9BQU8sRUFBRSxDQUFDO0FBQzFDLENBQUMsQ0FBQztBQVZXLFFBQUEsT0FBTyxXQVVsQiJ9
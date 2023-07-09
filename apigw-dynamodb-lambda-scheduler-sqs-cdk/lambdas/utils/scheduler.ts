import { CreateScheduleCommand, CreateScheduleCommandInput, CreateScheduleCommandOutput, DeleteScheduleCommand, DeleteScheduleCommandInput, DeleteScheduleCommandOutput, ListSchedulesCommand, ListSchedulesCommandInput, SchedulerClient } from "@aws-sdk/client-scheduler";
const REGION = process.env.CDK_DEFAULT_REGION;
const client = new SchedulerClient({ region: REGION });


export const createSchedules = async (params: CreateScheduleCommandInput): Promise<CreateScheduleCommandOutput> => {
  try {
    const command = new CreateScheduleCommand(params);
    const data = await client.send(command);
    console.log("Success, target added; requestID: ", data);
    return data; // For unit tests.
  } catch (err) {
    console.log("Error", err);
    throw new Error("Error");
  }
};

export const deleteSchdule = async (params: DeleteScheduleCommandInput): Promise<DeleteScheduleCommandOutput> => {
  try {
    const command = new DeleteScheduleCommand(params);
    const data = await client.send(command);
    console.log("Success, schedule deleted", data);
    return data; // For testing.
  } catch (err) {
    console.log("Error", err);
    throw new Error("Error");
  }
};

export const listSchedules = async (params: ListSchedulesCommandInput): Promise<any> => {
  try {
    const command = new ListSchedulesCommand(params);
    const data = await client.send(command);
    console.log("Success, target added; requestID: ", data);
    return data; // For testing.
  } catch (err) {
    console.log("Error", err);
    throw new Error("Error");
  }
};
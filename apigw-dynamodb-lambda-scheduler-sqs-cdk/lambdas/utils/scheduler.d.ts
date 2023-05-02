import { CreateScheduleCommandInput, CreateScheduleCommandOutput, DeleteScheduleCommandInput, DeleteScheduleCommandOutput, ListSchedulesCommandInput } from "@aws-sdk/client-scheduler";
export declare const createSchedules: (params: CreateScheduleCommandInput) => Promise<CreateScheduleCommandOutput>;
export declare const deleteSchdule: (params: DeleteScheduleCommandInput) => Promise<DeleteScheduleCommandOutput>;
export declare const listSchedules: (params: ListSchedulesCommandInput) => Promise<any>;

export interface messageBody {
    readonly id: string;
    readonly eventName: string;
    readonly eventType: string;
    readonly scheduleTime: string;
}

export interface ScheduledEvent {
    id: string;
    eventName: string;
    eventType: string;
    clientToken: string;
    scheduleTime : string;
  }
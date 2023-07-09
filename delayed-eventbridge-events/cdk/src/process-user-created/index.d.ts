import { EventBridgeEvent } from 'aws-lambda';
interface UserCreated {
    id: string;
    firstName: string;
    lastName: string;
}
export declare function handler(event: EventBridgeEvent<'UserCreated', UserCreated>): Promise<void>;
export {};

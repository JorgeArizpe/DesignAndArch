import { MessageSender } from "../senders/MessageSender";

export abstract class Task {
    protected  sender: MessageSender;
    protected name : string;
    protected estimatedHours : number;

    constructor(sender: MessageSender, name: string, estimatedHours: number) {
        this.sender = sender;
        this.name = name;
        this.estimatedHours = estimatedHours;
    }

    abstract complete(realHours: number): void;
}
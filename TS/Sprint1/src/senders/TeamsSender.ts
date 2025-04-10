import { MessageSender } from "./MessageSender";

export class TeamsSender implements MessageSender {
    sendMessage(content: string): void {
        console.log(`Enviando mensaje por Teams: ${content}`);
    }
}
import { MessageSender } from './MessageSender';

export class SlackSender implements MessageSender {
    sendMessage(content: string): void {
        console.log(`Enviando mensaje por Slack: ${content}`);
    }
}
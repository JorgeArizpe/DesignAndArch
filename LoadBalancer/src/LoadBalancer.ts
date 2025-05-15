import { Server } from './models/Server';
import { Subject } from './patterns/Observer';

export class LoadBalancer extends Subject {
    private servers: Server[];
    private currentIndex: number = 0;

    constructor(servers: Server[]) {
        super();
        this.servers = servers;
    }

    public distributeRequest(): void {
        if (this.servers.length === 0) return;

        const server = this.servers[this.currentIndex];

        server.handleRequest();
        this.notifyObservers(server.name);

        this.currentIndex = (this.currentIndex + 1) % this.servers.length;
    }
}
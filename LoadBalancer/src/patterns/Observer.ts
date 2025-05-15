export interface Observer {
    update(serveName: string): void;
}

export class Logger implements Observer {
    public update(serveName: string): void {
        console.log('Logger: Request hadled by server: ' + serveName);
    }
}

export class Subject {
    private oberserver: Observer[] = [];

    public addObserver(oberserver: Observer): void {
        this.oberserver.push(oberserver);
    }

    public notifyObservers(serveName: string): void {
        this.oberserver.forEach((observer) => observer.update(serveName));
    }
}
export abstract class ChainHandler {
    private nextHandler: ChainHandler | null = null;

    public setNext(handler: ChainHandler): ChainHandler {
        this.nextHandler = handler;
        return handler;
    }

    public handle(requestType: number): void {
        if (this.nextHandler) {
            this.nextHandler.handle(requestType);
        }
    }
}

export class AuthenticationHandler extends ChainHandler {
    public handle(requestType: number): void {
        if (requestType === 1) {
            console.log('AuthenticationHandler: Resolver Request')
        } else {
            super.handle(requestType)
        }
    }
}
export class LoggingHandler extends ChainHandler {
    public handle(requestType: number): void {
        if (requestType === 2) {
            console.log('LoggingHandler: Resolver Request')
        } else {
            super.handle(requestType)
        }
    }
}



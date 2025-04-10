interface Handler {
    setNext(handler: Handler): Handler;
    handle(request: string): void;
}

abstract class BaseHandler implements Handler {
    private nextHandler?: Handler;

    setNext(handler: Handler): Handler {
        this.nextHandler = handler;
        return handler;
    }

    handle(request: string): void {
        if (this.nextHandler) {
            return this.nextHandler.handle(request);
        }
    }
}

class BasicSupport extends BaseHandler {
    override handle(request: string): void {
        if (request === 'basic') {
            console.log('Soporte basico: Reuelto por el soporte basico');
            return;
        }
        console.log('Soporte basico: Pasando el problema al sopote avanzado');
        super.handle(request);
    }
}

class AdvancedSupport extends BaseHandler {
    override handle(request: string): void {
        if (request === 'advanced') {
            console.log('Soporte avanzado: Reuelto por el soporte avanzado');
            return;
        }
        console.log('Soporte avanzado: Pasando el problema al sopote experto');
        super.handle(request);
    }
}

class ExpertSupport extends BaseHandler {
    override handle(request: string): void {
        if (request === 'expert') {
            console.log('Soporte experto: Reuelto por el soporte experto');
            return;
        }
        console.log('Soporte experto: No se puede resolver el problema');
    }
}

function main() {
    const basicSupport = new BasicSupport();
    const advancedSupport = new AdvancedSupport();
    const expertSupport = new ExpertSupport();

    basicSupport.setNext(advancedSupport).setNext(expertSupport);

    basicSupport.handle('basic');
    console.log('------------------');
    basicSupport.handle('advanced');
    console.log('------------------');
    basicSupport.handle('expert');
    console.log('------------------');
    basicSupport.handle('unknown');
    console.log('------------------');
};

main();
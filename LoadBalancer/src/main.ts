import { LoadBalancer } from './LoadBalancer';
import { ServerFactory } from './models/ServerFactory';
import { AuthenticationHandler, LoggingHandler } from './patterns/ChainHandler';
import { Logger } from './patterns/Observer';

const main = () => {
    const factory = ServerFactory.getIntance();

    const server1 = factory.createServer('Server 1 ');
    const server2 = factory.createServer('Server 2 ');
    const server3 = factory.createServer('Server 3 ');

    const loadBalancer = new LoadBalancer(factory.getServers());
    const logger = new Logger();
    loadBalancer.addObserver(logger);

    console.log('Distributuing Requests:');

    loadBalancer.distributeRequest();
    loadBalancer.distributeRequest();
    loadBalancer.distributeRequest();
    loadBalancer.distributeRequest();

    console.log('\nHandling requests through Chain of Responsibility:');
    const authHandler = new AuthenticationHandler();
    const logHandler = new LoggingHandler();
    authHandler.setNext(logHandler);

    // Handle requests
    authHandler.handle(1); // Authentication
    authHandler.handle(2); // Logging
    authHandler.handle(3); // Unhandled case
};

main();
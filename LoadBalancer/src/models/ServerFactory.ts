import { Server } from './Server';

export class ServerFactory {
  private static intance: ServerFactory;
  private servers: Server[] = [];

  private constructor() {}

  // Patrón Singleton es el nucleo ya que devuelve una instancia unica

  public static getIntance(): ServerFactory {
    if (!ServerFactory.intance) {
      ServerFactory.intance = new ServerFactory();
    }
    return ServerFactory.intance;
  }

  // Factory ya que encapsula lo logica de creacion de objetos
  public createServer(name: string): Server {
    const server = new Server(name);
    this.servers.push(server);
    return server;
  }

  public getServers(): Server[] {
    return this.servers;
  }
}
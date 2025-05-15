export class Server {
    private connectionCount: number = 0;
  
    constructor(public readonly name: string) {
      this.connectionCount++;
      console.log(
        `Server ${this.name} is handling a request. Total connection ${this.connectionCount}`
      );
    }
  
    public handleRequest(): void {
      this.connectionCount++;
      console.log(
        'Server ' +
          this.name +
          'is handling request. Total connections: ' +
          this.connectionCount
      );
    }
  
    public getConnectionCount(): number {
      return this.connectionCount;
    }
  }
import { Task } from "./Task";

export class SimpleTask extends Task{
    complete(realHours: number): void {
        this.sender.sendMessage(`La tarea ${this.name} se completo en ${realHours} horas`);
    }
}
import { Task } from "./Task";

export class CompositeTask extends Task{
    private subTasks: Task[] = [];

    addSubTask(task: Task): void {
        this.subTasks.push(task);
    }

    complete(realHours: number): void {
        console.log(`La tarea compuesta ${this.name} se completo en ${realHours} horas`);
        this.subTasks.forEach(task => {
            task.complete(realHours/this.subTasks.length);
        });
    }
}
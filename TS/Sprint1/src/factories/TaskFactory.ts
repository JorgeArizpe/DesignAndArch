import { MessageSender } from "../senders/MessageSender";
import { CompositeTask } from "../tasks/CompositeTask";
import { SimpleTask } from "../tasks/SimpleTask";

export class TaskFactory {
    static createTask(name: string, sender: MessageSender, estimatedHours: number){
        if(estimatedHours > 4){
            console.log("La tarea es damasiado grande, se creara una tarea compuesta");
            const compositeTask = new CompositeTask(sender, name, estimatedHours);
            for(let i = 0; i < estimatedHours/4; i++){
                compositeTask.addSubTask(new SimpleTask(sender, `${name} - Subtarea ${i + 1}`, 4));
            }
            return compositeTask;
        } else {
            return new SimpleTask(sender, name, estimatedHours);
        }
    }
}
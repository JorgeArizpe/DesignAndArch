import { Database } from "./database/Database";
import { TaskFactory } from "./factories/TaskFactory";
import { TelegramSender, SlackSender, TeamsSender, WhatsappSender } from "./senders";

const telegramSender = new TelegramSender();
const slackSender = new SlackSender();
const teamsSender = new TeamsSender();
const whatsappSender = new WhatsappSender();

const db = Database.getInstance();

const task1 = TaskFactory.createTask("Implementar navbar con material", telegramSender, 4);
const task2 = TaskFactory.createTask("Implementar login con jwt", slackSender, 10);
const task3 = TaskFactory.createTask("Implementar dashboard", teamsSender, 8);
const task4 = TaskFactory.createTask("Implementar chat", whatsappSender, 2);

db.addTasks(task1);
db.addTasks(task2);
db.addTasks(task3);
db.addTasks(task4);

task1?.complete(5);
task2?.complete(20);
task3?.complete(16);
task4?.complete(1);


console.log("Tareas en la base de datos: ", db.getTasks());
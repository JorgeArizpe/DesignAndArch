export class Database {
    private static instance: Database;
    private tasks: any[] = [];

    private constructor() {}

    static getInstance(): Database {
        if (!Database.instance) {
            Database.instance = new Database();
        }
        return Database.instance;
    }

    addTasks(task: any) : void {
        this.tasks.push(task);
    }

    getTasks() : any[] {
        return this.tasks;
    }
}
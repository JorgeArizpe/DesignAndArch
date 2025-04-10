interface FyleSystemComponent{
    showDetails(indent?: string): void;
}

class Fyle implements FyleSystemComponent{
    private name: string;

    constructor(name: string){
        this.name = name;
    }

    showDetails(indent: string = ''){
        console.log(indent + '-Archivo: ' + this.name);
    }
}

class Folder implements FyleSystemComponent{
    private name: string;
    private content: FyleSystemComponent[] = [];

    constructor(name: string){
        this.name = name;
    }

    addContent(content: FyleSystemComponent){
        this.content.push(content);
    }


    showDetails(indent: string = " "): void {
        console.log(indent + '+Carpeta: ' + this.name);
        
        this.content.forEach((content) => {
            content.showDetails(indent + '  ');
        });
    }
}

function main(){
    const archivo1 = new Fyle('archivo1.js');
    const archivo2 = new Fyle('archivo2.js');

    const archivo3 = new Fyle('archivo3.js');
    const archivo4 = new Fyle('archivo4.js');

    const folder1 = new Folder('Carpeta1');
    const folder2 = new Folder('Carpeta2');

    folder1.addContent(archivo1);
    folder1.addContent(archivo2);

    folder2.addContent(archivo3);
    folder2.addContent(archivo4);

    folder1.showDetails();
    folder2.showDetails();
}

main();
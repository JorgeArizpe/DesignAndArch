// Interface for the image subject
interface Image {
    display(): void;
}

// Real subject - the actual image class
class RealImage implements Image {
    constructor(private filename: string) {
        this.loadFromDisk();
    }
    
    private loadFromDisk(): void {
        console.log("Cargando imagen...");
        // Simulate loading time
        for (let i = 0; i < 10000000000; i++) {} // Simple delay
    }
    
    display(): void {
        console.log("Mostrando imagen:", this.filename);
    }
}

// Proxy - controls access to the real image
class ProxyImage implements Image {
    private realImage: RealImage | null = null;
    
    constructor(private filename: string) {
        console.log("Imagen aún no cargada");
    }
    
    display(): void {
        if (!this.realImage) {
            this.realImage = new RealImage(this.filename);
        }
        this.realImage.display();
    }
}

function main() {
    // Create a proxy for an image
    const image: Image = new ProxyImage("foto1.jpg");
    
    console.log("\nPrimer intento de mostrar la imagen:");
    image.display();
    
    console.log("\nSegundo intento de mostrar la imagen:");
    image.display();
}

main(); 
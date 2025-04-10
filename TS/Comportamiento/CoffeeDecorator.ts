// Interface for the coffee component
interface Coffee {
    getDescription(): string;
    getCost(): number;
}

// Base coffee class
class Espresso implements Coffee {
    getDescription(): string {
        return "Espresso";
    }
    
    getCost(): number {
        return 2.00;
    }
}

// Base decorator class
abstract class CoffeeDecorator implements Coffee {
    constructor(protected coffee: Coffee) {}
    
    abstract getDescription(): string;
    abstract getCost(): number;
}

// Concrete decorators
class MilkDecorator extends CoffeeDecorator {
    getDescription(): string {
        return this.coffee.getDescription() + " + Leche";
    }
    
    getCost(): number {
        return this.coffee.getCost() + 0.50;
    }
}

class ChocolateDecorator extends CoffeeDecorator {
    getDescription(): string {
        return this.coffee.getDescription() + " + Chocolate";
    }
    
    getCost(): number {
        return this.coffee.getCost() + 0.75;
    }
}

class CinnamonDecorator extends CoffeeDecorator {
    getDescription(): string {
        return this.coffee.getDescription() + " + Canela";
    }
    
    getCost(): number {
        return this.coffee.getCost() + 0.25;
    }
}

// Example usage
function main() {
    // Create an espresso with milk and cinnamon
    let coffee: Coffee = new Espresso();
    coffee = new MilkDecorator(coffee);
    coffee = new CinnamonDecorator(coffee);
    
    console.log(`Pedido: ${coffee.getDescription()}`);
    console.log(`Precio: $${coffee.getCost().toFixed(2)}`);
}

// Run the example
main(); 
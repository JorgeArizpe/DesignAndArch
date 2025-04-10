
interface Ability {
    use(): void;
}

class SwordAttack implements Ability {
    use() {
        console.log('Sword Attack');
    }
}

class AxeAttack implements Ability {
    use() {
        console.log('Axe Attack');
    }
}

class MagicAttack implements Ability {
    use() {
        console.log('Magic Attack');
    }
}

class Heal implements Ability {
    use() {
        console.log('Heal');
    }
}

abstract class Characters {
    protected ability: Ability;

    constructor(ability: Ability) {
        this.ability = ability;
    }

    abstract performAbility(): void;
}

class Warriors extends Characters{
    performAbility() : void {
        console.log('Warrior attacks');
        this.ability.use();
    }
}

class Mage extends Characters{
    performAbility() : void {
        console.log('Mage attacks');
        this.ability.use();
    }
}

function main(){
    const warrior = new Warriors(new SwordAttack());
    warrior.performAbility();

    const warrior2 = new Warriors(new AxeAttack());
    warrior2.performAbility();

    const mage = new Mage(new MagicAttack());
    mage.performAbility();
}

main();
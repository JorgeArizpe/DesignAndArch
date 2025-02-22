from abc import ABC, abstractmethod

# Definición de la interfaz
class Aventurero(ABC):
    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def defender(self):
        pass

    @abstractmethod
    def usar_habilidad_especial(self):
        pass

# Implementación de la clase Mago
class Mago(Aventurero):
    def atacar(self):
        return "El mago lanza un hechizo de fuego."

    def defender(self):
        return "El mago crea un escudo mágico."

    def usar_habilidad_especial(self):
        return "El mago usa una bola de fuego gigante."

# Implementación de la clase Caballero
class Caballero(Aventurero):
    def atacar(self):
        return "El caballero ataca con su espada."

    def defender(self):
        return "El caballero levanta su escudo."

    def usar_habilidad_especial(self):
        return "El caballero usa un ataque sagrado."

# Clase que utiliza la interfaz sin depender de las implementaciones concretas
class Aventura:
    def __init__(self, aventurero: Aventurero):
        self.aventurero = aventurero

    def iniciar_aventura(self):
        print(self.aventurero.atacar())
        print(self.aventurero.defender())
        print(self.aventurero.usar_habilidad_especial())

# Ejemplo de uso
if __name__ == "__main__":
    mago = Mago()
    caballero = Caballero()

    aventura_mago = Aventura(mago)
    aventura_caballero = Aventura(caballero)

    print("Aventura con el Mago:")
    aventura_mago.iniciar_aventura()

    print("\nAventura con el Caballero:")
    aventura_caballero.iniciar_aventura()
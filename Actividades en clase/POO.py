class  Animal:
    def __init__(self, name, gender, age, color):
        self.name = name
        self.gender = gender
        self.age = age
        self.color = color
    
    def eat(self, food):
        print(f"{self.name} is eating {food}")
    
    def sleep(self, hours):
        print(f"{self.name} is sleeping for {hours} hours")
    
    def run(self, destination):
        print(f"{self.name} is running to {destination}")

    def breath(self):
        print(f"{self.name} is breathing")

class Cat(Animal):
    def __init__(self, name, gender, age, color, isNasty):
        super().__init__(name, gender, age, color)
        self.isNasty = isNasty
    
    def meow(self):
        print(f"{self.name} is meowing")

class Dog(Animal):
    def __init__(self, name, gender, age, color, bestFriend):
        super().__init__(name, gender, age, color)
        self.bestFriend = bestFriend
    
    def bark(self):
        print(f"{self.name} is barking")


gatoA = Cat("roberto", 2, "male", "blue")

gatoA.eat("doritos")
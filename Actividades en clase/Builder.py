class Computer:
    def __init__(self, cpu, ram, storage, gpu):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu
    
    def displaySystem(self):
        print(f'CPU: {self.cpu}\nRAM: {self.ram}\nStorage: {self.storage}\nGPU: {self.gpu}')
    
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer(None, None, None, None)
    
    def setCPU(self, cpu):
        self.computer.cpu = cpu
        return self

    def setRAM(self, ram):
        self.computer.ram = ram
        return self
    
    def setStorage(self, storage):
        self.computer.storage = storage
        return self
    
    def setGPU(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer


basicComputer = ComputerBuilder().setCPU('i5').setRAM('8GB').setStorage('1TB').setGPU('GTX 1050').build()
basicComputer.displaySystem()
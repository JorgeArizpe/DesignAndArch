from abc import ABC, abstractmethod

class BaseShipment(ABC):
    def __init__(self, package):
        self.package = package
    
    @abstractmethod
    def tax_cal(self):
        pass
    
    @abstractmethod
    def deliver(self):
        pass
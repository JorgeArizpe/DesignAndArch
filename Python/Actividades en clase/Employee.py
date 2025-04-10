from abc import ABC, abstractmethod

class Company(ABC):
    @abstractmethod
    def get_employee(self):
        pass
    
    @abstractmethod
    def create_software(self):
        pass
    
class Employee(ABC):
    @abstractmethod
    def do_work(self):
        pass
    
class Developer(Employee):
    def do_work(self):
        print("I am coding")

class Tester(Employee):
    def do_work(self):
        print("I am testing")
        
class Designer(Employee):
    def do_work(self):
        print("I am designing")

class GameDevCompany(Company):
    def get_employee(self):
        return [Developer(), Tester(), Designer()]
    
    def create_software(self):
        print("providing software for game development")

class OutsourcingCompany(Company):
    def get_employee(self):
        return [Developer(), Tester()]
    
    def create_software(self):
        print("providing software for outsourcing")

def main():
    game_dev_company = GameDevCompany()
    
    for emp in game_dev_company.get_employee():
        emp.do_work()
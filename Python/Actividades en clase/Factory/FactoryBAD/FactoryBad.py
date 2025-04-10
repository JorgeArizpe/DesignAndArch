class Package:
    def __init__(self, name, peso, category, costo_base):
        self.name = name
        self.peso = peso
        self.category = category
        self.costo_base = costo_base
    
    def calculate_total_price(self, envio):
        taxes = envio.tax_calculation()
        return self.costo_base + taxes

class EnvioAire:
    def __init__(self, package):
        self.package = package

    def tax_calculation(self):
        return self.package.peso * 0.3

    def deliver(self):
        print(f"Enviando: {self.package.name} por aire")
        print(f"Peso: {self.package.peso}kg Categoria: {self.package.category}")
        print(f"Impuestos: ${self.tax_calculation()}")
        print(f"Paquete entregado por aire")

class EnvioTierra:
    def __init__(self, package):
        self.package = package

    def tax_calculation(self):
        return self.package.peso * 0.2

    def deliver(self):
        print(f"Enviando: {self.package.name} por tierra")
        print(f"Peso: {self.package.peso}kg Categoria: {self.package.category}")
        print(f"Impuestos: ${self.tax_calculation()}")
        print(f"Paquete entregado por tierra")

class EnvioAgua:
    def __init__(self, package):
        self.package = package

    def tax_calculation(self):
        return self.package.peso * 0.8

    def deliver(self):
        print(f"Enviando: {self.package.name} por agua")
        print(f"Peso: {self.package.peso}kg Categoria: {self.package.category}")
        print(f"Impuestos: ${self.tax_calculation()}")
        print(f"Paquete entregado por agua")

class Logistic:
    def __init__(self, method, package):
        self.method = method
        self.package = package
    
    def process_delivery(self):
        if self.method == "aire":
            envio = EnvioAire(self.package)
        elif self.method == "tierra":
            envio = EnvioTierra(self.package)
        elif self.method == "agua":
            envio = EnvioAgua(self.package)
        else:
            raise ValueError("Metodo de envio no valido")
        envio.deliver()
        print(f"Costo total: ${self.package.calculate_total_price(envio)}")

packages = [
    Package("Laptop", 2.5, "Electronica", 100),
    Package("Muebles", 10, "Decoracion", 200),
    Package("Ropa", 1, "Moda", 50),
]

shipments = [
    Logistic("aire", packages[0]),
    Logistic("agua", packages[1]),
    Logistic("tierra", packages[2]),
]

for shipment in shipments:
    shipment.process_delivery()
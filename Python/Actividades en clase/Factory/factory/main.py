from models.package import Package
from factory.shipment_factory import ShipmentFactory

packages = [
    Package("Laptop", 2.5, "Electronico", 14000),
    Package("Joyeria", 24.5, "Joyeria", 140400)
]

method = ['ground', 'air']

for i in range(len(packages)):
    shipment = ShipmentFactory.create_shipment(method[i], packages[i])
    shipment.deliver()
    print(f"Total cost: {packages[i].calculate_total_cost(shipment)}")
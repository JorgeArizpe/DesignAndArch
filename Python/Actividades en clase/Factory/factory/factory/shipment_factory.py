from shipments.shipment_ground import ShipmentGround
from shipments.shipment_air import ShipmentAir
from shipments.shipment_water import ShipmentWater

class ShipmentFactory:
    @staticmethod
    def create_shipment(method, package):
        if method == 'ground':
            return ShipmentGround(package)
        elif method == 'air':
            return ShipmentAir(package)
        elif method == 'water':
            return ShipmentWater(package)
        else:
            raise ValueError('Invalid shipment method')
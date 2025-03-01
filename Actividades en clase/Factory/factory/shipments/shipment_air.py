from shipments.base_shipment import BaseShipment

class ShipmentAir(BaseShipment):
    def tax_cal(self):
        return self.package._weight * 0.2
    
    def deliver(self):
        print(f"Delivering {self.package} by air")
        print(f"Weight: {self.package._weight} kg, Category: {self.package._category}")
        print(f"Tax: {self.tax_cal()}")
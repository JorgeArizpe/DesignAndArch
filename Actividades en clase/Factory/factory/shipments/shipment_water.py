from shipments.base_shipment import BaseShipment

class ShipmentWater(BaseShipment):
    def tax_cal(self):
        return self.package._weight * 0.3
    
    def deliver(self):
        print(f"Delivering {self.package} by water")
        print(f"Weight: {self.package._weight} kg, Category: {self.package._category}")
        print(f"Tax: {self.tax_cal()}")
class Package:
    def __init__(self, name, weight, category, base_cost):
        self._name = name
        self._weight = weight
        self._category = category
        self._base_cost = base_cost
    
    def calculate_total_cost(self, shipment):
        tax = shipment.tax_cal()
        return self._base_cost + tax
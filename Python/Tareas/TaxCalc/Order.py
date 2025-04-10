class Order: 
    def __init__(self, items, country, state, city):
        self.__items = items
        self.__country = country
        self.__state = state
        self.__city = city
        self.__tax_calculator = TaxCalculator()
        
    def get_Items(self):
        return self.__items
    def get_Country(self):
        return self.__country
    def get_State(self):
        return self.__state
    def get_City(self):
        return self.__city
    
    def get_tax_order(self):
        total = 0
        for item in self.get_Items():
            total += item["price"] * item["quantity"]
            tax_rate = self.__tax_calculator.get_tax_rate(self.get_Country(), self.get_State(), self.get_City())
            total_tax = total * tax_rate
        return total + total_tax
        
class TaxCalculator:
    def get_tax_rate(self, country, state, city):
        if country == "US":
            return self.__get_us_tax()
        elif country == "MX":
            return self.__get_mx_tax()
        elif country == "UK":
            return self.__get_uk_tax()
        
    def __get_us_tax(self):
        return 0.12
    
    def __get_mx_tax(self):
        return 0.80
    
    def __get_uk_tax(self):
        return 0.20
from Sexto.DesignAndArch.TaxCalc.Order import Order

order = Order([{"name": "item1", "price": 10, "quantity": 2}], "US", "NY", "NYC")
order2 = Order([{"name": "item1", "price": 10, "quantity": 2}], "MX", "CDMX", "CDMX")
order3 = Order([{"name": "item1", "price": 10, "quantity": 2}], "UK", "London", "London")

print(order.get_tax_order())
print(order2.get_tax_order())
print(order3.get_tax_order())
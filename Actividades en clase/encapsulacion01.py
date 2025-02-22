#Encapsulacion a nivel metodo
def getOrder(order):
    total = 0
    for item in order.get("items"):
        total += item.get("price")
    total += getTaxes(order.get("country"), total)
    print(f"Total: {total}")

def getTaxes(country, price):
    if country == "US":
        return 0.2 * price
    elif country == "MX":
        return 0.8 * price
    elif country == "UK":
        return 0.1 * price

items1 = {
    "country": "US",
    "items": [
        {"name": "lap", "price": 3000},
        {"name": "ipad", "price": 5000},
        {"name": "iphone", "price": 4000}
    ]
}
items2 = {
    "country": "MX",
    "items": [
        {"name": "lap", "price": 3000},
        {"name": "ipad", "price": 5000},
        {"name": "iphone", "price": 4000}
    ]
}
items3 = {
    "country": "UK",
    "items": [
        {"name": "lap", "price": 3000},
        {"name": "ipad", "price": 5000},
        {"name": "iphone", "price": 4000}
    ]
}

getOrder(items1)
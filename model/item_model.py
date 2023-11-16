from dataclasses import dataclass

@dataclass
#Implementing Builder Pattern Desgin
class Item:

    def __init__(self, sku, name, description, price, quantity, expiration_date):
        self.sku: sku
        self.name: name
        self.description: description
        self.price: price 
        self.quantity: quantity
        self.expiration_date: expiration_date
    
#Implementing Builder Pattern Desgin
class ItemBuilder:

    def __init__(self):
        self.item = None
        self.sku = "AAA"
        self.name = "Nada"
        self.description = "Nada"
        self.price = 0
        self.quantity = 0
        self.expiration_date = None

    def with_sku(self, sku):
        self.sku = sku
        return self
    
    def with_name(self, name):
        self.name = name
        return self
    
    def with_description(self, description):
        self.description = description
        return self
    
    def with_price(self, price):
        self.price = price
        return self
    
    def with_quantity(self, quantity):
        self.quantity = quantity
        return self
    
    def with_expiration_date(self, expiration_date):
        self.expiration_date = expiration_date
        return self
    
    def build(self):
        self.item = Item(self.sku, self.name, self.description, self.price, self.quantity, self.expiration_date)
        return self.item
    
#Implementing Adapter Pattern Desgin to uppercase SKU input text
class Adapter():
    def with_sku(self, sku):
        self.sku = sku.upper()
        return self.sku 
    

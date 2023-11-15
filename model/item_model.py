from dataclasses import dataclass

@dataclass
class Item:
    sku: str
    name: str
    description: str
    price: float 
    quantity: float
    expiration_date: str
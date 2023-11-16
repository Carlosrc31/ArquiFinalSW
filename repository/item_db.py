from repository.item_abstract import ItemAbstract
from model import item_model


class ItemRepo(ItemAbstract):
    
    #def __init__(self):
    #    self.cursor = mysql.connection.cursor()
    
    def add(self, item: item_model.Item):
        from app import mysql
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO grocery_batch VALUES (%s, %s, %s, %s, %s, %s)', 
                       (item.sku, item.name, item.description, item.price, item.quantity, item.expiration_date))
        mysql.connection.commit()
        return True
    
    

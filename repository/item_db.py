from repository.item_abstract import ItemAbstract
from model import item_model


class ItemRepo(ItemAbstract):
    
    
    def add(self, item: item_model.Item):
        from app import mysql
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO grocery_batch VALUES (%s, %s, %s, %s, %s, %s)', 
                       (item.sku, item.name, item.description, item.price, item.quantity, item.expiration_date))
        mysql.connection.commit()
        return True
    

    def get_all(self):
        from app import mysql
        items = []

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM grocery_batch')
        items = cursor.fetchall()
        mysql.connection.commit()

        return items
    

    def delete(self, item_id):
        from app import mysql
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('DELETE FROM grocery_batch WHERE G_SKU = %s', (item_id,))
            mysql.connection.commit()

            return True
        except Exception as e:
            print(f"Error al intentar eliminar el elemento: {e}")
            return False
        finally:
            cursor.close()
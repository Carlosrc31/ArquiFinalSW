from flask import Blueprint, request, render_template
from model.item_model import Item
from repository.item_db import ItemRepo


blueprint = Blueprint('item_controller', __name__)
itemRepo = ItemRepo()

@blueprint.route('/')
def main():
    return render_template('index.html')

@blueprint.route('/add_item', methods=['POST'])
def addItem():
    
    if request.method == 'POST':

        sku = request.form['sku']
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        quantity = request.form['quantity']
        exp_date = request.form['exp_date']

        item = Item(
            sku = sku,
            name = name, 
            description=description, 
            price=price,
            quantity=quantity,
            expiration_date=exp_date
        )

        inserted = itemRepo.add(item)

        if inserted:
            return 'Insertado'
        
        return 'No se insertó'
       

        print(sku, name, description, price, quantity, exp_date)
        return 'recibido'


@blueprint.route('/get_item', methods=['GET'])
def getItems():
    return 'All items'
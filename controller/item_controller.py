from flask import Blueprint, request, render_template, jsonify
from model import item_model, facade, data_db
from repository.item_db import ItemRepo
import requests



blueprint = Blueprint('item_controller', __name__)
itemRepo = ItemRepo()

#Adapter
Adapter = item_model.Adapter()

@blueprint.route('/')
def main():
    #es para probar que funciona singleton 
    # db = data_db.DataDB.get_instance()
    # db2 = data_db.DataDB.get_instance()
    # print(db == db2)
    
    return render_template('index.html')

@blueprint.route('/add_item', methods=['POST'])
def addItem():
    
    if request.method == 'POST':

        sku = request.form['sku']
        #Using Adapter
        sku_adapter = Adapter.with_sku(sku)
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        quantity = request.form['quantity']
        exp_date = request.form['exp_date']

        #Using Builder Pattern Desgin
        item = (item_model.ItemBuilder()
                .with_sku(sku_adapter)
                .with_name(name)
                .with_description(description)
                .with_price(price)
                .with_quantity(quantity)
                .with_expiration_date(exp_date)
        )
        
        

        inserted = itemRepo.add(item)

        if inserted:
            return 'Insertado'
        
        return 'No se insertó'
       

@blueprint.route('/converter', methods=['GET', 'POST'])
def currency_converter(sku):
    #converter_api = 'http://api.exchangeratesapi.io/v1/latest?access_key=7b52c31d973e54a40972abb73d1e168a'
    #data = requests.get(converter_api).json()
    
    #return shows convertion from EUR to MXN, receive the sku, query a select with the sku and return the data
    
    #Using facade pattern
    #mxn, usd, jpy = facade.Facade().operations(data)
    # here convertion = get[currency] * mxn o usd o jpy
    #send convertion to the html view. 
    #Puede reutilizar el get hacer la conversión con cada dato y luego enviarlo a vista que usa el get (select)


    #return str(mxn_rate["rates"]["MXN"]) #Convertir string

    return 'API'



@blueprint.route('/get_item', methods=['GET'])
def getItems():
    return 'All items'



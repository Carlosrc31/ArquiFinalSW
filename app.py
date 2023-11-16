from flask import Flask
#from controller import item_controller
from flask_mysqldb import MySQL
from controller.item_controller import blueprint
from model.data_db import DataDB

app = Flask(__name__)

db = DataDB.get_instance()

app.config['MYSQL_HOST'] = db.host
app.config['MYSQL_USER'] = db.user
app.config['MYSQL_PASSWORD'] = db.password
app.config['MYSQL_DB'] = db.db_name 

mysql = MySQL(app)

app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(port=3000, debug=True)
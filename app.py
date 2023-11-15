from flask import Flask
#from controller import item_controller
from flask_mysqldb import MySQL
from controller.item_controller import blueprint

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'arquisw' 

mysql = MySQL(app)

app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(port=3000, debug=True)
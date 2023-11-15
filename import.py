import csv
import MySQLdb

with open('sample_grocery.csv', 'r') as file:
    reader = csv.reader(file)

    connection = MySQLdb.connect(host='localhost', user='root', password='', db='arquisw')

    cursor = connection.cursor()

    for row in reader:
        print(row)
        cursor.execute('INSERT INTO grocery_batch VALUES (%s, %s, %s, %s, %s, %s)', row)

    connection.commit()
    print('Listo')

cursor.close()

connection.close()
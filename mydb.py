import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='heisenberg',

)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE utsu_corp')

print("All Done!")


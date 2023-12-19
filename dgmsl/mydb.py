import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'juanmiguel05'
)

cursorObject = dataBase.cursor() 

cursorObject.execute("CREATE DATABASE django1")

print("All Done")


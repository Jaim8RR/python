import sqlite3
try:

    conection = sqlite3.connect("users.db")
    cursor = conection.cursor()
    #Escribo sentencias sql
    sql= "drop table if exists users"

    cursor.execute(sql)
    sql = "create table users(user text, password text)"
    cursor.execute(sql)
    sql = "insert into users values ('pepe','pepe1234')"
    cursor.execute(sql)

    conection.commit()
except Exception as ex:
    print("Error",ex)
    if conection:
        conection.rollback()
finally:
    if conection:
        conection.close()
conection.close()
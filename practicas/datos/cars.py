import os
import sys
import sqlite3


def clean_number(value):
    
    if not value or value == 'N/A':
        return None
    
    # Remove commas
    value = value.replace(',', '')
    
    number_str = ""
    found_digit = False
    
    for char in value:
        if char.isdigit():
            number_str += char
            found_digit = True
        elif char == '.' and found_digit and '.' not in number_str:
            number_str += char
        elif found_digit:
            # We found digits, and now hit a non-digit (like ' ' or '-')
            # Stop to capture just the first number 100-200 -> 100
            break
    
    return float(number_str) if number_str else None




def cars_data(file_path):
    # Database file
    db_file = os.path.join(os.path.dirname(file_path), 'cars.db')
    sql_file = os.path.join(os.path.dirname(file_path), 'cars.sql')
    csv_file = os.path.join(os.path.dirname(file_path), 'cars.csv')

    csv = open(csv_file,"r", encoding="cp1252")#utf8 XXXXX
    line_number = 0
    lina_aux = ""
    for line in csv:
        line_aux = line
        line_list = list()
        if line_number != 0:
            
            for char in line:
                if char != ",":#lo que hago es buscar las comas q separan los campos, todo lo anterior a la coma es un campo
                    line_list.append(line[0:line.index(",")])
                    line = line[line.index(",")+1:]#corto la linea para seguir buscando
                else:
                    line_list.append(line[0:line.index("\n")])#el ultimo campo no tiene coma, tiene salto de linea
                    break
                if char == "'":#tengo que buscar el que lo cierra
                    line_list.append(line[0:line.index("'",1)+1])
                    line = line[line.index("'",1)+1:]#corto la linea para segui          
        line_number += 1    
    
    print("Linea numero",line_number,":" ,line_list)
    
    """
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
#Para que de igual desde donde se ejecute la ruta sea relativa a la ubicacion del programa de python
"""
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'cars.csv')

print(f"En: {file_path}")
cars_data(file_path)


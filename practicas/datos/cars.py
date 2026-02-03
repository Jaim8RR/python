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
    line_list = list()
    for line in csv:
        
        
        if line_number != 0:
            current_field = ""
            inside_quotes = False
            field_number = 0
            record = list()    
            for char in line:
                if char == '"':
                    inside_quotes = not inside_quotes
                elif char == ',' and not inside_quotes:
                    # The fields that we want to clean are 3(2),4(3),5(4),6(5),7(6),8(7),11(10)
                    print("Campo encontrado:", current_field)
                    if field_number in [2,3,4,5,6,7,10]:
                        current_field = clean_number(current_field)
                        print("Campo limpiado:", current_field)                    
                    record.append(current_field)
                    current_field = ""
                    field_number += 1
                elif char == '\n':
                    break
                else:
                    current_field += char
        
            
            line_list.append(record)
        line_number += 1
    print(f"Lista de coches({len(line_list)}):")
    for record in line_list:
        print("El coche: ",record,"\n")

    
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


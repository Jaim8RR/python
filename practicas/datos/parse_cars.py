import csv
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

def parse_cars_data(file_path):
    
    #Parses the cars.csv file and inserts data into cars.db.
    
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    # Database file
    db_file = os.path.join(os.path.dirname(file_path), 'cars.db')
    sql_file = os.path.join(os.path.dirname(file_path), 'cars.sql')

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Execute the SQL script to create the table
        if os.path.exists(sql_file):
            with open(sql_file, 'r', encoding='utf-8') as f:
                sql_script = f.read()
                cursor.executescript(sql_script)
            print("Table 'cars' created/recreated successfully.")
        else:
            print(f"Warning: SQL file not found at {sql_file}. Table must verify manually.")

        with open(file_path, mode='r', encoding='latin-1') as csvfile:
            reader = csv.DictReader(csvfile)
            
            count = 0
            for row in reader:
                count += 1
                
                # Extract values and clean them
                company = row.get('Company Names', 'N/A')
                car_name = row.get('Cars Names', 'N/A')
                engine = row.get('Engines', 'N/A')
                
                capacity = clean_number(row.get('CC/Battery Capacity', 'N/A'))
                horsepower = clean_number(row.get('HorsePower', 'N/A'))
                top_speed = clean_number(row.get('Total Speed', 'N/A'))
                acceleration = clean_number(row.get('Performance(0 - 100 )KM/H', 'N/A'))
                price = clean_number(row.get('Cars Prices', 'N/A'))
                seats = clean_number(row.get('Seats', 'N/A'))
                
                fuel_type = row.get('Fuel Types', 'N/A')
                torque = row.get('Torque', 'N/A')

                # Insert into database
                sql = """INSERT INTO cars (company, model, engine, capacity, horsepower, top_speed, acceleration, price, fuel_type, seats, torque)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
                cursor.execute(sql, (company, car_name, engine, capacity, horsepower, top_speed, acceleration, price, fuel_type, seats, torque))
                
                # Sanitize strings for console output
                def safe_str(s):
                    return str(s).encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)

                # Print progress
                if count % 100 == 0:
                    print(safe_str(f"Inserted Car #{count}: {company} {car_name} (Price: {price})"))

            conn.commit()
            print(f"\nTotal cars inserted: {count}")

    except Exception as e:
        print(f"An error occurred: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

# ---------------------------------------------------------
# EJECUCIÓN DIRECTA (Modificado)
# ---------------------------------------------------------
# Calculamos la ruta y ejecutamos la función inmediatamente
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'cars.csv')

print(f"Buscando archivo en: {file_path}")
parse_cars_data(file_path)
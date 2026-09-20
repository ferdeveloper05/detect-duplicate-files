import sqlite3
from pathlib import Path


def create_file_databases(name_db: str, ext: str = '.db'): 
    concat_name = name_db + ext
    name_database = Path.home() / concat_name
    name_database.touch(exist_ok=True)
    
    return name_database

def connect_with_database(name_database): 
    conn = sqlite3.connect(name_database)

    cursor = conn.cursor()
    cursor.execute('CREATE TABLE archivos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, hash_sha256 TEXT UNIQUE, ruta_origen TEXT, fecha_procesado TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')
    conn.commit()
    
    conn.close()

if __name__ == "__main__":
    database = create_file_databases("Code/register_files")

def insert_into_database(): 
    pass

#todo: agregar una funcion insert_into_database tiene que recibir 3 parametros
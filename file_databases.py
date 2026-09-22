import sqlite3
from pathlib import Path


def create_file_databases(name_db: str, ext: str = '.db') -> Path: 
    concat_name = name_db + ext
    name_database = Path.home() / concat_name
    name_database.touch(exist_ok=True)
    
    return name_database

def connect_with_database(name_database: Path) -> None: 
    conn = sqlite3.connect(name_database)

    cursor = conn.cursor()
    cursor.execute('CREATE TABLE archivos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, hash_sha256 TEXT UNIQUE, ruta_origen TEXT, fecha_procesado TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')
    conn.commit()
    
    conn.close()

def insert_into_database(name_database: Path, nombre: str, hash_archivo: str, ruta_origen: Path) -> None: 
    
    conn = sqlite3.connect(name_database)
    
    cursor = conn.cursor()
    sql = "INSERT INTO archivos (nombre, hash_sha256, ruta_origen) VALUES (?, ?, ?)"
    cursor.execute(sql, (nombre, hash_archivo, ruta_origen))
    
    conn.commit()
    print(f"Registro insertado con éxito. ID generado: {cursor.lastrowid}")
    
    conn.close()
    
def query_in_database(name_database: Path, hash_val): 
    
    conn = sqlite3.connect(name_database)
    cursor = conn.cursor()
    
    cursor.execute("SELECT nombre FROM archivos WHERE hash_sha256 = ?",  hash_val)
    registro = cursor.fetchone()
    
    conn.commit()
    
    return registro
    
    
if __name__ == "__main__":
    database = create_file_databases("Code/register_files")
    print(type(database))


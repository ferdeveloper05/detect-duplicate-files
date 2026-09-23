import shutil

from config_entorn import get_environment, get_param_input, validate_path_dirs
from create_hash import calc_hash
from file_databases import (
    connect_with_database,
    create_file_databases,
    insert_into_database,
    query_in_database,
)


def main():
    #* Acceso a la variable de entorno
    environ = get_environment()

    #* Comprobando el pase de parametro al ejecutar el script
    param = get_param_input()
    
    #* Creacion de la base de datos
    name_databases: str = input("Ingrese la ruta o nombre de la base de datos: ")
    database = create_file_databases(name_databases)
    
    #* Creando la tabla que guardara los archivos del sistema
    connect_with_database(database)
    
    # Lista de archivos en el directorio original
    list_archivos, dir_dest = validate_path_dirs(environ, param)
    
    for archivo in list_archivos: 
        nombre = archivo.name
        hash_code = calc_hash(archivo)
        dir_origin = archivo.parent 
        
        #registro = query_in_database(name_database=database, hash_val=hash_code)
        
        
        # Insertando datos en la tabla de archivos
        print("Insertando el archivo en la base de datos")
        insert_into_database(database, nombre, hash_code, dir_origin)
        
        print(f"Moviendo el archivo {archivo.name} al directorio de destino {dir_dest.name}")
        shutil.copy2(str(archivo), str(dir_dest))
        print(f"Archivo movido al directorio {dir_dest.name}")
        
        #print(f"Nombre: {type(nombre)} | Hash: {type(hash_code)} | Directorio de Origen: {type(dir_origin)}")
        

main()
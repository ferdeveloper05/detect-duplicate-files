import os
import sys
from pathlib import Path

    
def get_environment() -> str:
    """ Obtiene el entorno STORAGE_DIR o crea un directorio por defecto """ 
    
    path_default = os.getenv("STORAGE_DIR")

    if path_default is None: 
        path_default = "Code/almacena_destino"
        
    return path_default

def get_param_input() -> str:
    """ Obtiene el parametro pasado por linea de comandos y lo retorna """
    
    if sys.argv[0]: 
        print("Debe ingresar una ruta como parametro antes de ejecutar el script. Ej: script.py [parametro]")
        sys.exit(1)
        
    elif sys.argv[1]: 
        print(f"La ruta que usted ingreso es: {sys.argv[1]}")
        param = sys.argv[1]
    
    return param

def validate_path_dirs(path_dest: str, path_origin: str) -> list:
    """ Valida la ruta de origen y devuelve una lista con los archivos de esta """
     
    dir_dest = Path.home() / path_dest
    dir_origin = Path.home() / path_origin
    
    print(f"\nRuta Destino: {dir_dest}")
    print(f"Ruta Origen: {dir_origin}\n")
    
    if dir_origin.exists() and dir_origin.is_dir(): 
        dir_dest.mkdir(parents=True, exist_ok=True)
        
        files = [file for file in dir_origin.rglob("*")]
    
    return files, dir_dest

if __name__ == "__main__": 

    validate_path_dirs(get_environment(), get_param_input())
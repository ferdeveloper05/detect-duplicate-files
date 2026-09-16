import os
import sys
from pathlib import Path

    
def get_environment() -> str:
    """ Obtiene el entorno STORAGE_DIR o crea un directorio por defecto """ 
    
    path_default = os.getenv("STORAGE_DIR")

    if path_default is None: 
        path_default = "Code/almacena_destino"
        
    return path_default

def get_paramm_input() -> str:
    """ Obtiene el parametro pasado por linea de comandos y lo retorna """
    
    paramm = sys.argv[1]
    if paramm: 
        print(f"La ruta que usted ingreso es: {sys.argv[1]}")
    else: 
        sys.exit(1)
    
    return paramm

def validate_path_dirs(path_dest: str, path_origin: str): 
    dir_dest = Path.home() / path_dest
    dir_origin = Path.home() / path_origin
    
    print(f"Ruta Destino: {dir_dest}")
    print(f"Ruta Origen: {dir_origin}")
    
    if dir_origin.exists() and dir_origin.is_dir(): 
        dir_dest.mkdir(parents=True, exist_ok=True)
        
        for file in dir_origin.rglob('*'): 
            print(file)
    

if __name__ == "__main__": 

    validate_path_dirs(get_environment(), get_paramm_input())
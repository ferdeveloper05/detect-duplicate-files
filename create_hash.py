import hashlib
from pathlib import Path


def calc_hash(file: Path, algo: str = "sha256") -> str: 
    hash = hashlib.new(algo)
    
    if file.exists() and file.is_file(): 
        
        with file.open('rb') as f: 
            while chunk := f.read(4096): 
                hash.update(chunk)
    
    return hash.hexdigest()


if __name__ == "__main__":
    path_input = Path.home() / input("Ingrese la ruta del archivo para calcular su hash: ")
    
    print(calc_hash(path_input))

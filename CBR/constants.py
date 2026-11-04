import pandas as pd
import json
from pathlib import Path

# Paths resolved from this file, so the code works from any working directory
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / 'data'
MODELS_DIR = ROOT_DIR / 'models'

# Ruta al archivo JSON con el diccionario
file_path = DATA_DIR / 'books_dict.txt'

# # Función para cargar el diccionario desde un archivo JSON
def cargar_diccionario():
    with open(file_path, 'r') as f:
        diction = eval(f.read())
        return diction

longituds = {
    'molt curt':(15,100), 
    'curt': (100,200), 
    'mig': (200,400), 
    'llarg': (400,600), 
    'molt llarg': (600,1000)
}

ratings = {
    'molt poc':(4,5), 
    'poc': (3.5,4.5), 
    'punt just': (2.5,3.5), 
    'bastant': (2,3), 
    'molt': (1,2)
}

generes = ['Fantasy', 'Fiction', 'Mystery', 'Poetry', 'History', 'Romance', 'Non-fiction', 'Children', 'Young-adult', 'Comics']


"""
Funció: Revisa i modifica les recomanacions proposades abans de presentar-les a l'usuari.

Components: Funcions per a la validació i ajust de recomanacions.
"""


from miniproto1.cases.index import Indexacio
from miniproto1.cases.case import Cas
from typing import Tuple, List
from scipy.spatial.distance import euclidean

import pickle
import xgboost as xgb

def assign(cas):
        vals = [int(input(f'Valoració {i+1}: ')) for i in range(3)]
        cas.avaluacio = [int(vals[0]), int(vals[1]), int(vals[2])]

def automatic(cas):
        with open('xgb_model.pkl', 'rb') as file:
                loaded_model = pickle.load(file)
        
        valoracions = []
        for i in cas.solucio:
                predictions = loaded_model.predict(i) #FALTEN COSES NO ES I
                valoracions.append(predictions)
        cas.avaluacio = valoracions

def predict_valoration(new_case):
    with open('xgb_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    # return model.predict(new_case)

def valorate(new_case:Cas, idx:int):
    '''
    Si val == 0, semanticament indica que no ha comprat el llibre recomanat
    '''
    val = float('-inf')
    while val not in list(range(6)):
        val = int(input(f"Què t'ha semblat el llibre {new_case.solucio[int]}, quantes estrelles li dones? (1-5): "))
    return val

def user_evaluation(new_case:Cas):
    for i in range(3):
        new_case.avaluacio = valorate(new_case, i)
    
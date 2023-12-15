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


def assingar_valoracions_a_ma(cas, valoracio1:int=None, valoracio2:int=None, valoracio3:int=None):
        cas.avaluacio([valoracio1, valoracio2, valoracio3])



def automatic(cas):
        with open('xgb_model.pkl', 'rb') as file:
                loaded_model = pickle.load(file)
        
        valoracions = []

        for i in cas.solucio:
                predictions = loaded_model.predict(i) #FALTEN COSES NO ES I
                valoracions.add(predictions)

        cas.avaluacio(valoracions)

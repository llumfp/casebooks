"""
Funció: Revisa i modifica les recomanacions proposades abans de presentar-les a l'usuari.

Components: Funcions per a la validació i ajust de recomanacions.
"""


from miniproto1.cases.index import Indexacio
from miniproto1.cases.case import Cas
from typing import Tuple, List
from scipy.spatial.distance import euclidean


def assingar_valoracions_a_ma(cas, valoracio1:int=None, valoracio2:int=None, valoracio3:int=None):
        cas.avaluacio([valoracio1, valoracio2, valoracio3])




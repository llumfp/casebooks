"""
Funció: Incorpora la nova experiència (cas d'ús actual) a la base de dades per a futurs usos.

Components: Mecanismes per a l'actualització de la base de dades amb nous casos.
"""

from miniproto1.cases.index import Indexacio
from miniproto1.cases.case import Cas
from typing import Tuple, List
from scipy.spatial.distance import euclidean


#Retain

# Retain
def redundant_cas(new: Cas, most_similars: List[Tuple[float, Cas]]):
    T = 1
    dicc = {new.solucio[i]: new.avaluacio[i] for i in range(3)}
    dicc_keys_set = set(dicc.keys())  # Convertir las claves en un conjunto

    for dist, case in most_similars:
        if dist < T:
            coincident_books = 0
            for book in dicc_keys_set.intersection(case.solucio):
                if abs(dicc[book] - case.avaluacio[case.solucio.index(book)]) <= 1.5:
                    coincident_books += 1
                    if coincident_books >= 2:
                        return True
        else:
            return False
    return False

"""
Funció: Incorpora la nova experiència (cas d'ús actual) a la base de dades per a futurs usos.

Components: Mecanismes per a l'actualització de la base de dades amb nous casos.
"""

from miniproto1.cases.index import Indexacio
from miniproto1.cases.case import Cas
from typing import Tuple, List
from scipy.spatial.distance import euclidean


#Retain
# CALCUL Utilitat Normalitzada
def recompte_valors_utilitxats(cas, casos_similares, listas_casos_utilitzats):
    pos, neg = 0, 0

    for index, puntuacio in enumerate(cas.avaluacio):
        if puntuacio is not None:
            casos_index = listas_casos_utilitzats[index]
            if puntuacio > 3.5:
                pos += 1
                for cas in casos_index:
                    cas.UaS += 1
            else:
                neg += 1
                for cas in casos_index:
                    cas.UaF += 1

    for cas in casos_similares:
        cas.S += pos
        cas.F += neg


def actualitzar_Utilitat_normalitzada_casos(llista_casos_similars):
    for cas in llista_casos_similars:
        cas.actualitzar_Utilitat_normalitzada()


# CALCUL Error Absoluto Medio Normalizado
def calcul__Sum_Dif_Abs__num_casos_valorats(indexacio: Indexacio, new: Cas, puntuaciones_confianza):
    num_punt = 0
    for index, valoracio in enumerate(new.avaluacio):
        if valoracio is not None and puntuaciones_confianza[index] is not None:
            num_punt += abs(valoracio - puntuaciones_confianza[index])
            indexacio.num_casos_valorats += 1

    if num_punt > 0:
        indexacio.Sum_Dif_Abs += num_punt
        return True
    return False


def actualixar_NMAE(indexacio: Indexacio):
    indexacio.NMAE= (indexacio.Sum_Dif_Abs/indexacio.num_casos_valorats)/4

# Retain
def redundant_optim(new: Cas, most_similars: List[Tuple[float, Cas]]):
    T = 1
    dicc = {new.solution[i]: new.avaluacio[i] for i in range(3)}
    dicc_keys_set = set(dicc.keys())  # Convertir las claves en un conjunto

    for dist, case in most_similars:
        if dist < T:
            coincident_books = 0
            for book in dicc_keys_set.intersection(case.solution):
                if abs(dicc[book] - case.avaluacio[case.solution.index(book)]) <= 1.5:
                    coincident_books += 1
                    if coincident_books >= 2:
                        return True
        else:
            return False
    return False

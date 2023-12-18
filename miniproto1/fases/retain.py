from miniproto1.cases.index import Indexacio
from miniproto1.cases.case import Cas
from typing import Tuple, List
from scipy.spatial.distance import euclidean
from statistics import mean

# Retain
def redundant_cas(new:Cas, most_similars:List[Tuple[float, Cas]], T:int = 2, learn:bool = True):
    '''
    Retorna:
        0 si NO és redundant
        1 si SÍ és redundant
        2 si SÍ és redundant però ÚTIL (Swap)
    '''
    dicc = {new.solucio[i]: new.avaluacio[i] for i in range(3)}
    dicc_keys_set = set(dicc.keys())  # Convertir las claves en un conjunto
    for dist, case in most_similars:
        if dist < T:
            coincident_books = 0
            for book in dicc_keys_set.intersection(case.solucio):
                if abs(dicc[book] - case.avaluacio[case.solucio.index(book)]) <= 1.5:
                    coincident_books += 1
                    if coincident_books >= 2:
                        
                        # APRENENTATGE
                        if learn and better(old=case, new=new):
                            swap(old=case,new=new)
                            return 2

                        return 1
        else:
            return 0
    return 0

def better(old:Cas, new:Cas):
    return mean(new.solucio) > mean(old.solucio)

def swap(old:Cas, new:Cas):
    old.__dict__, new.__dict__ = new.__dict__.copy(), old.__dict__.copy()
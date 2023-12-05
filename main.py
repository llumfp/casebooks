"""
Funció: Punt d'entrada del programa. Gestiona la interacció amb l'usuari i coordina els altres mòduls.

Contingut: Inicialització, menú d'usuari, crides a altres mòduls.
"""

from miniproto1 import *
import numpy as np
import random
import pandas as pd

#llegim els problemes de la base de dades
df_problemes = pd.read_csv('./data/problems.csv')

def createDB(df:pd.DataFrame) -> List[Cas]:
    '''
    Funció que donat un csv en format DataFrame de pandas retorna una llista de casos.
    '''
    problemes = []

    for cas in df_problemes[df_problemes.columns[2:-2]].values:
        problemes.append(Problem(*cas))

    recomendations = [eval(i) for i in df_problemes['recomendations'].tolist()]
    rating_recom = [eval(i) for i in df_problemes['recom_ratings'].tolist()]

    scaled_features = scale_features(problemes)

    db = [Cas(id=idx, descripcio=p, solucio= recomendations[idx], avaluacio= rating_recom[idx]) for idx,p in enumerate(scaled_features)]

    return db

db = createDB(df=df_problemes)

a = Indexacio(v=db)
a.creacio(db,5)

newp = Problem(0.5,0.5,1,0,0,0,0,0,0,0,0,0,0.5)

newp = Cas(id=len(db),descripcio=scale_features([newp])[0])

similar_cases,path = a.most_similar(newp, 3)

a.calcular_valor_confianza(similar_cases, newp)


#a.save("hola2")
#indexacio_instancia = Indexacio.load('hola2.pkl')

#similar_cases2, path2 = indexacio_instancia.most_similar(newp, 7)

# print("hola")
# print(similar_cases2)
# case_sim, ruta = a.most_similar(newp)
# print("\n--- CAS MES SIMILAR ---")
# print(case_sim)
# print(f"Ruta seguida: {ruta}")

# a_afegir = Cas(id=9, descripcio=[0.6744186, 0.5, 0])
# a.add(a_afegir,ruta)

# print("\n--- BASE DE DADES ---")
# print(a)


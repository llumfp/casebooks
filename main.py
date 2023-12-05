"""
Funció: Punt d'entrada del programa. Gestiona la interacció amb l'usuari i coordina els altres mòduls.

Contingut: Inicialització, menú d'usuari, crides a altres mòduls.
"""

from miniproto1 import *
import numpy as np
import random
import pandas as pd

df_problemes = pd.read_csv('./data/problems.csv')
casesbase = createDB(df=df_problemes) # Mètode a utils.py
a = Indexacio(casesbase=casesbase, casesxleaf=10)

newp = Problem(1,0,0,0,0,0,0,0,0,0,0.5,0.5,0.5)
newp = Cas(id=len(casesbase),descripcio=scale_features([newp])[0])

similar_cases,path = a.most_similar(newp, 3)

print(similar_cases)

print('\n', path)

#a.calcular_valor_confianza(similar_cases, newp)


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


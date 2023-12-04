"""
Funció: Punt d'entrada del programa. Gestiona la interacció amb l'usuari i coordina els altres mòduls.

Contingut: Inicialització, menú d'usuari, crides a altres mòduls.
"""

from miniproto1 import *
import numpy as np
import random
import pandas as pd

#llegim els problemes de la base de dades
df_problemes = pd.read_csv('data/problems.csv')
problemes = []

for cas in df_problemes[df_problemes.columns[2:]].values:
    print(len(cas))
    problemes.append(Problem(*cas))
    
print(problemes)

print("--- PROBLEMES ---")
for p in problemes:
    print(p)

scaled_features = scale_features(problemes)

db = [Cas(id=idx, descripcio=p) for idx,p in enumerate(scaled_features)]

print("\n--- BASE DE DADES ---")
for cas in db:
    print(cas)

a = Indexacio(v=db)
a.creacio(db)

newp = Problem(0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.5,0.5,0.5)

newp = Cas(id=len(db),descripcio=scale_features([newp])[0])

# case_sim, ruta = a.most_similar(newp)
# print("\n--- CAS MES SIMILAR ---")
# print(case_sim)
# print(f"Ruta seguida: {ruta}")

# a_afegir = Cas(id=9, descripcio=[0.6744186, 0.5, 0])
# a.add(a_afegir,ruta)

# print("\n--- BASE DE DADES ---")
# print(a)
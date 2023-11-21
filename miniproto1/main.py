"""
Funció: Punt d'entrada del programa. Gestiona la interacció amb l'usuari i coordina els altres mòduls.

Contingut: Inicialització, menú d'usuari, crides a altres mòduls.
"""

from cases import *
import numpy as np
import random


# Creem 10 instancies de Problem aleatòries que seran la nostra Database
random.seed(2003)
problems = [
    Problem(
        age=random.randint(10, 70), 
        time=random.choice(["mucho", "normal", "poco"]),
        genre=random.choice(["Ficcion", "No Ficcion"])
    ) for _ in range(10)
]

for p in problems:
    print(p)

scaled_features = scale_features(problems)


cases = [Cas(id=idx, descripcio=p) for idx,p in enumerate(scaled_features)]

db = [c.descripcio for c in cases]

print("--- BASE DE DADES ---")
for cas in db:
    print(cas)


a = BinTree(v=db)
a.creacio(db)
print(a.get_left())
print(a.get_right())

newp = Problem(age=25,time='poco',genre='Ficcion')
newp = scale_features([newp])[0]

sim = a.trobar_mes_similar(newp)
print(sim)


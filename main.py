"""
Funció: Punt d'entrada del programa. Gestiona la interacció amb l'usuari i coordina els altres mòduls.

Contingut: Inicialització, menú d'usuari, crides a altres mòduls.
"""

from miniproto1 import *


'''# Creem 10 instancies de Problem aleatòries que seran la nostra Database
random.seed(2003)
problems = [
    Problem(
        age=random.randint(10, 70), 
        time=random.choice(["mucho", "normal", "poco"]),
        genre=random.choice(["Ficcion", "No Ficcion"])
    ) for _ in range(10)
]

print("--- PROBLEMES ---")
for p in problems:
    print(p)

scaled_features = scale_features(problems)


db = [Cas(id=idx, descripcio=p) for idx,p in enumerate(scaled_features)]

print("\n--- BASE DE DADES ---")
for cas in db:
    print(cas)

a = Indexacio(v=db)
a.creacio(db)

newp = Problem(age=25,time='poco',genre='Ficcion')
print("\n--- PROBLEMA NOU ---")
print(newp)
newp = Cas(id=len(db),descripcio=scale_features([newp])[0])

case_sim, ruta = a.most_similar(newp)
print("\n--- CAS MES SIMILAR ---")
print(case_sim)
print(f"Ruta seguida: {ruta}")

a_afegir = Cas(id=9, descripcio=[0.6744186, 0.5, 0])
a.add(a_afegir,ruta)

print("\n--- BASE DE DADES ---")
print(a)'''

cas1 = Problem(6, 'Fansasy', 'Dark_Fantasy', 'soft', True, None, False, True,'short', None, None)

a = preprocess([cas1])
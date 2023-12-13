"""
Funció: Punt d'entrada del programa. Gestiona la interacció amb l'usuari i coordina els altres mòduls.

Contingut: Inicialització, menú d'usuari, crides a altres mòduls.
"""

from miniproto1 import *
import numpy as np
import random
import pandas as pd
import time
import matplotlib.pyplot as plt

df_problemes = pd.read_csv('./data/problems.csv')
casesbase = createDB(df=df_problemes) # Mètode a utils.py
# casesbase = redundant_clustering(casesbase)
a = Indexacio(casesbase=casesbase, casesxleaf=10)

newp = Problem(1,0,0,0,0,0,0,0,0,0,0.5,0.5,0.5)
newp = Cas(id=len(casesbase),descripcio=scale_features([newp])[0])

similar_cases,path = most_similar(a,newp,10)
print(similar_cases,path)

# tiempos = []
# for x in range(1,990):
    
#     inicio = time.time()
#     similar_cases,path = a.most_similar(newp,x)
#     fin = time.time()
#     tiempos.append(fin - inicio)

# # Graficar los resultados
# plt.figure(figsize=(20, 5))
# plt.plot(range(1,990), tiempos, marker='o')
# plt.xlabel('Valor de x')
# #plt.xticks(range(1,101), rotation=75)
# plt.ylabel('Tiempo de ejecución (s)')
# plt.title('Tiempo de Ejecución de most_similar() en función de x')
# plt.grid(True)
# #plt.subplots_adjust(left=0.1, right=0.9)
# plt.savefig('./images/most_similar_times')

#a.calcular_valor_confianza(similar_cases,newp)

# print(similar_cases)

# print('\n', path)

# print(newp.solucio)
# print(newp.avaluacio)

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

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
import ast


df_problemes = pd.read_csv('./data/problems4000(real).csv')



resposta = input('Precarregar (marca True) o de 0 False:  ')


if eval(resposta):
    rs = RecommenderSystem(indexacio="primer_arbre.pkl")
else:
    try:
        df_problemes.drop('Unnamed: 0',axis=1,inplace=True)
    except:
        pass
    rs = RecommenderSystem(maxcasesxleaf=10,casebase=df_problemes)


#rs.indexacio.save("primera")

# Rebem nou problema
newp = Problem(1,0,0,0,0,0,0,0,0,0,0.5,0.5,0.5)
newcas = Cas(id=(len(rs.indexacio)),descripcio=scale_features([newp])[0])
# Retrieve
most_similar_cases, path = rs.retrieve(newp)

print(f"most_similar_cases: {most_similar_cases}")
print(f"Path: {path}")

# Reuse
casos_para_confianza = [(distancia, cas) for distancia, cas, _ in most_similar_cases]
listas_casos_utilitzats, puntuaciones_confianza  = rs.reuse(casos_para_confianza, newcas)

print(f'listas_casos_utilitzats: {listas_casos_utilitzats}')
print(f'puntuaciones_confianza: {puntuaciones_confianza}')


print(f'llibres recomanat: {newcas.solucio}')


# Revise
#revise()
def valorate(new_case:Cas):
    val = float('-inf')
    while val not in list(range(1,6))+['-']:
        val = int(input(f"Què t'ha semblat el llibre {newcas.solucio[0]}, quantes estrelles li dones? (1-5): "))
    return val
        

valoracio1 = float('-inf')
while valoracio1 not in ['1','2','3','4','5','-']:
    valoracio1 = input(f'Com valores {newcas.solucio[0]}, si vols saltar la valoracio escriu -:  ')
if valoracio1 != '-':
    valoracio1 = int(valoracio1)
else:
    valoracio1 = None
valoracio2 = float('-inf')
while valoracio2 not in ['1','2','3','4','5','-']:
    valoracio2 = input(f'Com valores {newcas.solucio[1]}, si vols saltar la valoracio escriu -:  ')
if valoracio2 != '-':
    valoracio2 = int(valoracio2)
else:
    valoracio2 = None
valoracio3 = float('-inf')
while valoracio3 not in ['1','2','3','4','5','-']:
    valoracio3 = input(f'Com valores {newcas.solucio[2]}, si vols saltar la valoracio escriu -:  ')
if valoracio3 != '-':
    valoracio3 = int(valoracio3)
else:
    valoracio3 = None

rs.revise(valoracio1, valoracio2, valoracio3)

# Retain
if valoracio1 or valoracio2 or valoracio3:
    rs.retain(newcas, most_similar_cases,)


# Evaluacio
real = rs.evaluation(newcas, puntuaciones_confianza, casos_para_confianza)
print(f"es {real} real")


print("ara guardare")
rs.guardar("primer_arbre")
print("he guadat")

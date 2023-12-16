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

from_model = eval(input('Precarregar RecommenderSystem? (True/False):  '))
rs = createRS(from_model, path="", maxcasesxleaf=10, casebase=df_problemes)

newp = Problem(1,0,0,0,0,0,0,0,0,0,0.5,0.5,0.5)
newcas = Cas(id=(len(rs.indexacio)),descripcio=rs.scaler.transform([newp.array])[0])

# Retrieve
most_similar_cases = rs.retrieve(newp)

# Reuse
distancies, casos, paths = zip(*most_similar_cases)
cas_dists = list(zip(distancies, casos))

listas_casos_utilitzats, puntuaciones_confianza  = rs.reuse(cas_dists, newcas)


"""# Revise
rs.revise(newcas,3,4,5,metode=False)

# Retain
rs.retain(newcas, most_similar_cases,)


# Evaluacio
real = rs.evaluation(newcas, puntuaciones_confianza, casos_para_confianza)
print(f"es {real} real")


print("ara guardare")
rs.guardar("primer_arbre")
print("he guadat")
"""""""""
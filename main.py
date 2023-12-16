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


{150016: (2.5, [Cas(id=24613, solucio=[150016, 848, 17631], avaluacio=[5, 3, 0])]), 
 848: (0.0, [Cas(id=24613, solucio=[150016, 848, 17631], avaluacio=[5, 3, 0])]), 
 17631: (-3.75, [Cas(id=24613, solucio=[150016, 848, 17631], avaluacio=[5, 3, 0])]), 
 84777: (2.5, [Cas(id=669202, solucio=[84777, 33306, 84739], avaluacio=[5, 0, 0])]), 
 33306: (-3.75, [Cas(id=669202, solucio=[84777, 33306, 84739], avaluacio=[5, 0, 0])]), 
 84739: (-3.75, [Cas(id=669202, solucio=[84777, 33306, 84739], avaluacio=[5, 0, 0])]), 
 13705: (2.5, [Cas(id=53314, solucio=[13705, 38380, 11289], avaluacio=[5, 0, 5])]), 
 38380: (-3.75, [Cas(id=53314, solucio=[13705, 38380, 11289], avaluacio=[5, 0, 5])]), 
 11289: (2.5, [Cas(id=53314, solucio=[13705, 38380, 11289], avaluacio=[5, 0, 5])]), 
 7194: (1.25, [Cas(id=399929, solucio=[7194, 90244, 50331], avaluacio=[4, 5, 0])]), 
 90244: (2.5, [Cas(id=399929, solucio=[7194, 90244, 50331], avaluacio=[4, 5, 0])]), 
 50331: (-3.75, [Cas(id=399929, solucio=[7194, 90244, 50331], avaluacio=[4, 5, 0])]), 
 304747: (2.5, [Cas(id=123990, solucio=[304747, 423, 790], avaluacio=[5, 4, 5])]), 423: (1.25, [Cas(id=123990, solucio=[304747, 423, 790], avaluacio=[5, 4, 5])]), 790: (2.5, [Cas(id=123990, solucio=[304747, 423, 790], avaluacio=[5, 4, 5])]), 1313: (0.0, [Cas(id=745553, solucio=[1313, 8001, 
14599], avaluacio=[3, 4, 0])]), 8001: (1.25, [Cas(id=745553, solucio=[1313, 8001, 14599], avaluacio=[3, 4, 0])]), 14599: (-3.7500000000000004, [Cas(id=745553, solucio=[1313, 8001, 14599], avaluacio=[3, 4, 0])]), 12877: (1.2499999999999998, [Cas(id=434630, solucio=[12877, 58495, 14960], avaluacio=[4, 3, 2])]), 58495: (0.0, 
[Cas(id=434630, solucio=[12877, 58495, 14960], avaluacio=[4, 3, 2])]), 14960: (-1.2499999999999998, [Cas(id=434630, solucio=[12877, 58495, 14960], avaluacio=[4, 3, 2])]), 7135: (-3.75, [Cas(id=719094, solucio=[7135, 
54847, 370869], avaluacio=[0, 0, 2])]), 54847: (-3.75, [Cas(id=719094, solucio=[7135, 54847, 370869], avaluacio=[0, 0, 2])]), 370869: (-1.25, [Cas(id=719094, solucio=[7135, 54847, 370869], avaluacio=[0, 0, 2])]), 929: (1.2499999999999998, [Cas(id=61428, solucio=[929, 133751, 21452], avaluacio=[4, 0, 0])]), 133751: (-3.75, 
[Cas(id=61428, solucio=[929, 133751, 21452], avaluacio=[4, 0, 0])]), 21452: (-3.75, [Cas(id=61428, solucio=[929, 133751, 21452], avaluacio=[4, 0, 0])]), 23237: (-1.25, [Cas(id=698828, solucio=[23237, 28568, 49348], avaluacio=[2, 0, 0])]), 28568: (-3.75, [Cas(id=698828, solucio=[23237, 28568, 49348], avaluacio=[2, 0, 0])]), 49348: (-3.75, [Cas(id=698828, solucio=[23237, 28568, 49348], avaluacio=[2, 0, 0])])}



[[Cas(id=24613, solucio=[150016, 848, 17631], avaluacio=[5, 3, 0])], 
[Cas(id=669202, solucio=[84777, 33306, 
84739], avaluacio=[5, 0, 0])], [Cas(id=53314, solucio=[13705, 38380, 11289], avaluacio=[5, 0, 5])]]


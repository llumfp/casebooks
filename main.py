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

df_problemes = pd.read_csv(f'./data/problems4000(real).csv')
print(df_problemes.shape)
    
from_model = eval(input('Precarregar RecommenderSystem? (True/False):  '))
# rs = RecommenderSystem()

# newp = Problem(4,9,5,8,2,1,3,10,6,7,381,114,2.8026479371165514)
# newcas = Cas(id=rs.indexacio.ultim_id,descripcio=rs.scaler.transform([newp.array])[0])

# # Retrieve
# most_similar_cases = rs.retrieve(newp)

# # Reuse
# distancies, casos, paths = zip(*most_similar_cases)
# cas_dists = list(zip(distancies, casos))
# dicc_most_sim = rs.reuse(cas_dists, newcas)

# # Revise
# rs.revise(newcas, casos, dicc_most_sim, False)

# # Retain
# rs.retain(newcas, cas_dists,paths[0])

# # Manteniment
# print(f'Tenim {len(rs.indexacio)} casos a la indexacio')
# rs.maintenance()
# print(f'Després del manteniment tenim {len(rs.indexacio)} casos a la indexacio')


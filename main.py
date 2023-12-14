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

rs = RecommenderSystem(df_problemes, 10)

# Rebem nou problema
newp = Problem(1,0,0,0,0,0,0,0,0,0,0.5,0.5,0.5)

#Retrieve
most_similar_cases, path = rs.retrieve(newp)

print(most_similar_cases, path)

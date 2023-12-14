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

df_problemes = pd.read_csv('./data/problems8000.csv')


resposta = input('Precarregar (marca True) o de 0 False:  ')


if eval(resposta):
    rs = RecommenderSystem(indexacio="primer_arbre.pkl")

else:
    try:
        df_problemes.drop('Unnamed: 0',axis=1,inplace=True)
    except:
        pass

    rs = RecommenderSystem(10,df_problemes)


#rs.indexacio.save("primera")

# Rebem nou problema
newp = Problem(1,0,0,0,0,0,0,0,0,0,0.5,0.5,0.5)



# Retrieve
most_similar_cases, path = rs.retrieve(newp)
"""print(f"most_similar_cases: {most_similar_cases}")

print(f"Path: {path}")

for i in most_similar_cases:
    print(len(i[2]))
print(len(most_similar_cases))
"""

# Reuse


"""
print("ara guardare")
rs.guardar("primer_arbre")
print("he guadat")
"""
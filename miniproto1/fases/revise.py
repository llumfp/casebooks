"""
Funció: Revisa i modifica les recomanacions proposades abans de presentar-les a l'usuari.

Components: Funcions per a la validació i ajust de recomanacions.
"""

from miniproto1.cases.index import Indexacio
from miniproto1.cases.case import Cas
from typing import Tuple, List
from scipy.spatial.distance import euclidean
import pandas as pd
import pickle
import xgboost as xgb
import numpy as np

def assign(cas):
        vals = [int(input(f'Valoració {i+1}: ')) for i in range(3)]
        cas.avaluacio = [int(vals[0]), int(vals[1]), int(vals[2])]


# Funció per convertir un Cas a una representació vàlida per a obtenir la predicció del model xgboost
def convert_case_to_data(newcas):
    non_important = ['Fantasy_x', 'Poetry_x']
    newcas = [newcas]
    problems = [list(cas.descripcio) + [str(cas.solucio)] for i, cas in enumerate(newcas)]
    # Definir las columnas del DataFrame
    column_names = ['Fantasy', 'Fiction', 'Mystery', 'Poetry',
                    'History', 'Romance', 'Non-fiction', 'Children', 'Young-adult',
                    'Comics', 'mean_length', 'count_reads', 'avg_rating','books_ids']

    # Crear el DataFrame
    df = pd.DataFrame(problems, columns=column_names)
    df['books_ids'] = df['books_ids'].apply(eval)
    # Utilizar explode para expandir los elementos de la lista en filas separadas
    df_exploded = df.explode('books_ids')
    # Cambiar el nombre de la columna 'lista' a 'nuevo_nombre'
    df_exploded = df_exploded.rename(columns={'books_ids': 'book_id'})
    
    bk_merge = pd.read_csv('data/genres_pages_x_books.csv')
    bk_merge.drop('Unnamed: 0',axis=1,inplace=True)
    final_dataset = df_exploded.merge(bk_merge, on='book_id', how='inner')
    final_dataset.drop(non_important,axis=1,inplace=True)
    final_dataset.drop(['book_id'],axis=1,inplace=True)
    return final_dataset

def predict_valoration(newcas): # Se pot canviar el paràmetre per un path fixe si decidim quedarnos amb un model
    with open('xgb_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    dataset = convert_case_to_data(newcas)
    estimacio = np.clip(np.round(np.array(loaded_model.predict(dataset))), 0, 5).astype(int).tolist()
    newcas.avaluacio = estimacio

def valorate(new_case:Cas, idx:int):
    '''
    Si val == 0, semanticament indica que no ha comprat el llibre recomanat
    '''
    val = float('-inf')
    while val not in list(range(6)):
        val = int(input(f"Què t'ha semblat el llibre {new_case.solucio[int]}, quantes estrelles li dones? (1-5): "))
    return val

def user_evaluation(new_case:Cas):
    for i in range(3):
        new_case.avaluacio = valorate(new_case, i)


# CALCUL Utilitat Normalitzada
def recompte_valors_utilitxats(cas, llista_casos_similars, dic_casos_utilitzats):
    pos, neg = 0, 0
    for i, key in enumerate(dic_casos_utilitzats.keys()):
        if cas.avaluacio[i] > 3.5:
            pos += 1
            for cas in dic_casos_utilitzats[key][1]:
                cas.UaS += 1
            
        else:
            neg += 1
            for cas in dic_casos_utilitzats[key][1]:
                cas.UaF += 1

    for cas in llista_casos_similars:
        cas.S += pos
        cas.F += neg
 
        cas.actualitzar_Utilitat_normalitzada()


# CALCUL Error Absoluto Medio Normalizado
def calcul__Sum_Dif_Abs__num_casos_valorats(indexacio: Indexacio, new: Cas, dic_casos_utilitzats):
    
    num_punt = 0
    for index, llibre in enumerate(new.solucio):
        if new.avaluacio[index] is not None and dic_casos_utilitzats[llibre][0] is not None:
            num_punt += abs(new.avaluacio[index] - dic_casos_utilitzats[llibre][0])
            indexacio.num_casos_valorats += 1

    if num_punt > 0:
        indexacio.Sum_Dif_Abs += num_punt


def actualixar_NMAE(indexacio: Indexacio):
    indexacio.NMAE = (indexacio.Sum_Dif_Abs/indexacio.num_casos_valorats)/4


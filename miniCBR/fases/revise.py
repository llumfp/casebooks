'''
No necessitem cap funció auxiliar per aquesta fase en
aquest CBR simplificat.
'''
# import numpy as np
# import pandas as pd
# import pickle

# # Funció per convertir un Cas a una representació vàlida per a obtenir la predicció del model xgboost
# def convert_case_to_data(newcas):
#     non_important = ['Fantasy_x', 'Poetry_x']
#     newcas = [newcas]
#     problems = [list(cas.descripcio) + [str(cas.solucio)] for i, cas in enumerate(newcas)]
#     # Definir las columnas del DataFrame
#     column_names = ['Fantasy', 'Fiction', 'Mystery', 'Poetry',
#                     'History', 'Romance', 'Non-fiction', 'Children', 'Young-adult',
#                     'Comics', 'mean_length', 'count_reads', 'avg_rating','books_ids']

#     # Crear el DataFrame
#     df = pd.DataFrame(problems, columns=column_names)
#     df['books_ids'] = df['books_ids'].apply(eval)
#     # Utilizar explode para expandir los elementos de la lista en filas separadas
#     df_exploded = df.explode('books_ids')
#     # Cambiar el nombre de la columna 'lista' a 'nuevo_nombre'
#     df_exploded = df_exploded.rename(columns={'books_ids': 'book_id'})
    
#     bk_merge = pd.read_csv('data/genres_pages_x_books.csv')
#     bk_merge.drop('Unnamed: 0',axis=1,inplace=True)
#     final_dataset = df_exploded.merge(bk_merge, on='book_id', how='inner')
#     final_dataset.drop(non_important,axis=1,inplace=True)
#     final_dataset.drop(['book_id'],axis=1,inplace=True)
#     return final_dataset

# def predict_valoration(newcas,model_path): # Se pot canviar el paràmetre per un path fixe si decidim quedarnos amb un model
#     with open(model_path, 'rb') as file:
#         loaded_model = pickle.load(file)
#     dataset = convert_case_to_data(newcas)
#     estimacio = np.clip(np.round(np.array(loaded_model.predict(dataset))), 0, 5).astype(int)
#     return estimacio.tolist()
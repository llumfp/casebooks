import pandas as pd
pr = pd.read_csv('data/problems40000.csv')
pr = pr[pr['avg_rating'] != 0]
pr.drop(['read_books','recomendations','recom_ratings','Unnamed: 0'],axis=1,inplace=True)
df = pd.read_csv('D:\Escritorio\casebooks_SBC\interactions.csv') 
df.drop(['is_read','is_reviewed'],axis=1,inplace=True)
df_merged = pr.merge(df[['user_id', 'book_id', 'rating']], on='user_id', how='inner')

"""Codi per obtenir genres_pages_x_books.csv a partir de genresxbook.csv
bk = pd.read_csv('casebooks/data/genresxbook.csv')
import pandas as pd
import json

# Lista para almacenar los datos de cada línea
data_list = []

# Abre y lee el archivo línea por línea
with open('D:\Escritorio\casebooks_SBC\sm_filtered_books.json', 'r',encoding='utf-8') as file:
    for line in file:
        # Decodifica cada línea como un objeto JSON y añádela a la lista
        data_list.append(json.loads(line))

# Crea un DataFrame a partir de la lista
json_df = pd.DataFrame(data_list)

# Procesa y combina los datos como en el ejemplo anterior
json_df['book_id'] = json_df['book_id'].astype(str)
json_df['num_pages'] = pd.to_numeric(json_df['num_pages'], errors='coerce')
pages_df = json_df[['book_id', 'num_pages']]

# Suponiendo que tu dataframe bk está cargado y tiene una columna 'book_id'
bk['book_id'] = bk['book_id'].astype(str)
bk_merge = bk.merge(pages_df, on='book_id', how='left')

bk_merge.to_csv('casebooks/data/genres_pages_x_books.csv')

"""

bk_merge = pd.read_csv('data/genres_pages_x_books.csv')
bk_merge.drop('Unnamed: 0',axis=1,inplace=True)
final_dataset = df_merged.merge(bk_merge, on='book_id', how='inner')
#notnas = final_dataset.dropna()
a = final_dataset.drop(columns=["num_pages","Comics_y", "Children_y","Non-fiction_y", "History_y","Poetry_y","Mystery_y","Fantasy_y","Young-adult_y"])
notnas2 = a.dropna()
# ESTAN ELS NAS eliminats o nooo????? 


import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from tqdm import tqdm
from xgboost.callback import TrainingCallback

# Suponiendo que 'a' es tu DataFrame
X = a.drop(['rating','user_id','book_id'], axis=1)
y = a['rating']

# Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Clase para mostrar el progreso usando tqdm
class TQDMCallback(TrainingCallback):
    def __init__(self, total):
        self.pbar = tqdm(total=total)
    def after_iteration(self, model, epoch, evals_log):
        self.pbar.update(1)
        return False  # Return True para detener el entrenamiento

# Instanciar el modelo XGBoost con early_stopping_rounds
xgb_model = xgb.XGBRegressor(
    n_estimators=1000,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    gamma=0,
    reg_alpha=0.1,
    reg_lambda=1,
    early_stopping_rounds=10
)

# Entrenar el modelo con barra de progreso
xgb_model.fit(
    X_train, 
    y_train, 
    eval_set=[(X_test, y_test)],
    callbacks=[TQDMCallback(1000)],
    verbose=False   
)

# Predecir y evaluar
predictions = xgb_model.predict(X_test)
rmse = mean_squared_error(y_test, predictions, squared=False)
print(rmse) # -> 1.2621784328358439 Ha estat el millor model

import pickle

# Guardar el modelo a un archivo
with open('xgb_model.pkl', 'wb') as file:
    pickle.dump(xgb_model, file)




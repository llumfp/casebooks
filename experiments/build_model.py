"""Rebuild the recommender model from the synthetic case base.

Builds the RecommenderSystem (scaler, redundancy clustering and tree index)
from data/problems4000_not_0_0_0.csv and saves it to models/recomanador.pkl,
overwriting the versioned model.

Run from the repo root:
    python -m experiments.build_model
"""
from time import time

import pandas as pd

from CBR import createRS
from CBR.constants import DATA_DIR, MODELS_DIR

df_problemes = pd.read_csv(DATA_DIR / 'problems4000_not_0_0_0.csv')
init_time = time()
rs = createRS(from_model=False, casebase=df_problemes)
print(f'Model built in {time() - init_time:.1f} s with {len(rs.indexacio)} cases')

rs.save(MODELS_DIR / 'recomanador')

from typing import Any, Tuple, List
from miniCBR.cases.problem import Problem, scale_features
from numpy import ndarray
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from scipy.spatial.distance import pdist, squareform

class Cas:
    def __init__(
        self,
        id: str,
        descripcio: ndarray[Any], # El nostre problema ja preprocessat
        derivacio = None,
        historial = [],
        solucio: List[int] = [],
        avaluacio: List[int] = [],
        cops_us: int = 0,
        
        utilitat: None = None,
        UM: int = None,

        UaS: int = 0,
        S: int = 0,
        UaF: int = 0,
        F: int = 0,
        
    ) -> None:
        self.id = id
        self.descripcio = descripcio
        self.derivacio = derivacio
        self.solucio = solucio # llista de 3 llibres recomanats
        self.avaluacio = avaluacio # num del 1-5
        self.historial = historial
        self.cops_us = cops_us
        self.mesura_utilitat = utilitat # mirar els altres casos que tenim i valorar si val la pena
        
        #Calcul utilitat
        self.UM =UM # Utilitat normalitzada
        self.UaS = UaS #el nombre de vegades que es va utilitzar el cas i hi vahaver un èxit, quan el cas es trobava entre els casos recuperats
        self.S = S #quantitat total d'èxits quan el cas es trobava entre els casos recuperats
        self.UaF = UaF #número de vegades que s’ha utilitzat el cas i va ser un fracàs, quan el cas es trobava entre els casos recuperats
        self.F = F #número total de fracassos quan el cas es trobava entre els casos recuperats
        
    
    def __repr__(self) -> str:
        return f"Cas(id={self.id}, solucio={self.solucio}, avaluacio={self.avaluacio})"
    

    def actualitzar_Utilitat_normalitzada(self):
        self.UM = ((self.UaS/self.S)-(self.UaS/self.F)+1)/2
    
    
    def validate(self, casos): 
        # Òscar: potser seria millor això posar-ho al RecommenderSystem, 
        # llavors la funció seria def validate(self, cas:Cas) i ja 
        # tindriem accés a la base de casos
        '''
        mirar tots els casos que tenim a la base de casos
        - Si hi ha un cas molt similar amb mateix resultat no guardem
        - Si el self.avaluacio es molt intermedi (2.5) no ens està aportant 
            informació útil sobre si esta bé o no
        '''

    def obtenir_solucio(self):
        assert self.derivacio != []
        #Quan ja es tenen els casos similars, generar la resposta
        pass
    
    def evaluate(self):
        assert self.solucio != []
        '''
        un cop tenim la solució, preguntar a l'usuari, qunant de bona ha sigut la recomanació
        '''
        pass

def createDB(df:pd.DataFrame) -> List[Cas]:
    '''
    Funció que donat un csv en format DataFrame de pandas retorna una llista de casos.
    '''
    problemes = []

    for cas in df[df.columns[2:-2]].values:
        problemes.append(Problem(*cas))

    read_books = [eval(i) for i in df['read_books'].tolist()]
    recomendations = [eval(i) for i in df['recomendations'].tolist()]
    rating_recom = [eval(i) for i in df['recom_ratings'].tolist()]

    scaler, scaled_features = scale_features(problemes)

    db = [Cas(id=df['user_id'][idx], descripcio=p, historial=read_books[idx] ,solucio= recomendations[idx], avaluacio= rating_recom[idx]) for idx,p in enumerate(scaled_features)]
    
    return db, scaler

from typing import Any, Tuple, List
from miniproto1.ontology import Problem, scale_features
from numpy import ndarray
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

class Cas:
    def __init__(
        self,
        id: str,
        descripcio: ndarray[Any], # El nostre problema ja preprocessat
        derivacio = None,
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
        self.cops_us = cops_us
        self.mesura_utilitat = utilitat # mirar els altres casos que tenim i valorar si val la pena
        
        #Calcul utilitat
        self.UM =UM # Utilitat normalitzada
        self.UaS = UaS #el nombre de vegades que es va utilitzar el cas i hi vahaver un èxit, quan el cas es trobava entre els casos recuperats
        self.S = S #quantitat total d'èxits quan el cas es trobava entre els casos recuperats
        self.UaF = UaF #número de vegades que s’ha utilitzat el cas i va ser un fracàs, quan el cas es trobava entre els casos recuperats
        self.F = F #número total de fracassos quan el cas es trobava entre els casos recuperats
        
    
    def __repr__(self) -> str:
        return f"Cas(id={self.id}, descripcio={self.descripcio}, solucio={self.solucio}, avaluacio={self.avaluacio})"
    
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

    recomendations = [eval(i) for i in df['recomendations'].tolist()]
    rating_recom = [eval(i) for i in df['recom_ratings'].tolist()]

    scaled_features = scale_features(problemes)
    create_clustering(scaled_features)


    db = [Cas(id=df['user_id'][idx], descripcio=p, solucio= recomendations[idx], avaluacio= rating_recom[idx]) for idx,p in enumerate(scaled_features)]
    
    return db


def create_clustering(clustering_data):
    """crea un clustering amb totes les dades inicials. Aquest clustering
        servirà per a eliminar aquells casos redundants"""

    Z = linkage(clustering_data, method='ward')

    # Plotting the dendrogram to find the appropriate level for cutting
    plt.figure(figsize=(10, 7))
    dendrogram(Z, truncate_mode='lastp', p=12, show_contracted=True)
    plt.title("Dendrogram")
    plt.xlabel("Cluster Size")
    plt.ylabel("Distance")
    plt.show()

    # Estimating a distance threshold from the dendrogram
    # The exact value might require some trial and error
    estimated_distance_threshold = 150  # This is a guessed value based on the dendrogram

    # Create a new model with the estimated distance threshold
    final_model_adjusted = AgglomerativeClustering(n_clusters=None, 
                                                distance_threshold=estimated_distance_threshold, 
                                                linkage='ward')
    final_model_adjusted.fit(clustering_data)

    # Assign each sample to a cluster
    clusters_adjusted = final_model_adjusted.labels_

    # Count of samples in each cluster
    cluster_counts = np.unique(clusters_adjusted, return_counts=True)
    print(cluster_counts)

def delete_redundants():
    """"Donat un """
    pass
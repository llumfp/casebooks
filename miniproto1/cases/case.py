from typing import Any, Tuple, List
from miniproto1.ontology import Problem, scale_features
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

    scaled_features = scale_features(problemes)
    create_clustering(scaled_features, read_books, recomendations, rating_recom)


    db = [Cas(id=df['user_id'][idx], descripcio=p, solucio= recomendations[idx], avaluacio= rating_recom[idx]) for idx,p in enumerate(scaled_features)]
    
    return db


def create_clustering(clustering_data, read_books, recomendations, rating_recoms):
    """crea un clustering amb totes les dades inicials. Aquest clustering
        servirà per a eliminar aquells casos redundants"""

    # Z = linkage(clustering_data, method='ward')
    # # Plotting the dendrogram to find the appropriate level for cutting
    # plt.figure(figsize=(10, 7))
    # dendrogram(Z, truncate_mode='lastp', p=15, show_contracted=True)
    # plt.title("Dendrogram")
    # plt.xlabel("Cluster Size")
    # plt.ylabel("Distance")
    # plt.show()
    # estimated_distance_threshold = int(input("Veient el dendograma, per quina distància vols retallar l'arbre per a fer clusters?"))

    estimated_distance_threshold = 2
    # Creem un arbre jerarquic a partir d'obserbar el dendograma
    final_model_adjusted = AgglomerativeClustering(n_clusters=None,  
                                                   distance_threshold= estimated_distance_threshold,
                                                linkage='ward')
    final_model_adjusted.fit(clustering_data)

    #indica a quin cluster pertany cada cas. Llista de etiquetes
    clusters_adjusted = final_model_adjusted.labels_ 

    # Comprovació per veure que efectivament a cada clus
    cluster_counts = np.unique(clusters_adjusted, return_counts=True)
    print('Casos en cada cluster:', cluster_counts[1])

    cluster_to_analyze = 15  # Assuming cluster 15 is one of the clusters
    distance_threshold = 0.3

    # Agafem els índex casos del cluster a estudiar i els casos com a tal
    cluster_indices= np.where(clusters_adjusted == cluster_to_analyze)[0]
    cluster_data = clustering_data[cluster_indices]

    # Calculem la distancia entre tots els casos del cluster
    pairwise_distances = pdist(cluster_data, metric='euclidean')
    distance_matrix = squareform(pairwise_distances)

    #Calculem la similitud de les variables categòriques
    print('recomendations', recomendations[0])

    # Mirem quins casos son massa semblants, i ens quedem únicament amb aquells que
    
    redundant_cases = set()

    for i in range(distance_matrix.shape[0]):
        for j in range(i + 1, distance_matrix.shape[0]):
            #Quantitat de llibres que coincideixen
            common_read_books = len(set(read_books[i]) & set(read_books[j]))
            common_recom = len(set(recomendations[i]) & set(recomendations[j]))
            common_rating = (abs(np.mean(rating_recoms[i]) - np.mean(rating_recoms[j])))        
            if distance_matrix[i, j] < distance_threshold:
                # Add one of the redundant cases to the set
                redundant_cases.add(j)

    # Removing redundant cases
    #filtered_cluster_data = cluster_data(cluster_data.index[list(redundant_cases)])

    # Showing the result
    print("Number of original cases in the cluster:", cluster_data.shape[0])
    #print("Number of cases after removing redundancies:", filtered_cluster_data.shape[0])
    print("Cases removed:", redundant_cases)


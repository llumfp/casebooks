import numpy as np
from .bintreelinked import BinTree
from typing import List, Any, Tuple
from .case import Cas
from sklearn.cluster import KMeans


class Indexacio(BinTree):
    def __init__(self, v=None, left=None, right=None):
        super().__init__(v, left, right)

    def creacio(self,casos:List[Cas]) -> None:
        n_clusters = 2
        if len(casos) == 1:
            # Si només hi ha un cas, retorna un arbre amb aquest cas.
            self.set_root(casos[0])
        else:
            # Aplicar KMeans per a dividir els casos en grups.
            kmeans = KMeans(n_clusters=n_clusters, random_state=0, n_init='auto')
            kmeans.fit([cas.descripcio for cas in casos])

            # Dividir els casos segons les etiquetes del clustering.
            cluster1 = [casos[i] for i in range(len(casos)) if kmeans.labels_[i] == 0]
            cluster2 = [casos[i] for i in range(len(casos)) if kmeans.labels_[i] == 1]

            # Crear els subarbres per a cada cluster.
            subarbre1, subarbre2 = Indexacio(), Indexacio()

            subarbre1.creacio(cluster1)
            subarbre2.creacio(cluster2)

            # Retorna un arbre amb l'objecte KMeans com a arrel i els subarbres com a fills.
            self.set_root(kmeans)
            self.set_left(subarbre1)
            self.set_right(subarbre2)


    def creacio2(self, casos: List[Cas]) -> None:
        n_clusters = 2
        if len(casos) == 1:
            self.set_root(casos[0])
        else:
            kmeans = KMeans(n_clusters=n_clusters, random_state=0)
            descriptions = [cas.descripcio for cas in casos]
            kmeans.fit(descriptions)
            distances = kmeans.transform(descriptions)

            # Umbral basado en el percentil 95 de todas las distancias
            threshold = np.percentile(distances, 95)

            cluster1, cluster2 = [], []
            for i, cas in enumerate(casos):
                dist_to_cluster1, dist_to_cluster2 = distances[i]
                assigned_cluster = kmeans.labels_[i]

                # Asignación principal basada en KMeans
                if assigned_cluster == 0:
                    cluster1.append(cas)
                else:
                    cluster2.append(cas)

                # Asignación a ambos si la distancia es alta para ambos clusters
                if dist_to_cluster1 >= threshold and dist_to_cluster2 >= threshold:
                    if assigned_cluster == 0:
                        cluster2.append(cas)
                    else:
                        cluster1.append(cas)

            subarbre1, subarbre2 = Indexacio(), Indexacio()
            subarbre1.creacio(cluster1)
            subarbre2.creacio(cluster2)

            self.set_root(kmeans)
            self.set_left(subarbre1)
            self.set_right(subarbre2)


    def most_similar(self, cas: Cas) -> Tuple[Cas, List]:
        """
        Donat un  cas a comparar (Cas), retorna el cas més similar 
        en l'Indexacio i la llista de labels per després afegir el nou cas.
        """
        # Recorre l'arbre per a trobar el cas més similar.
        node_actual = self
        labels = []
        while not node_actual.leaf():
            kmeans = node_actual.get_root()
            label = kmeans.predict([cas.descripcio])[0]
            labels.append(label)
            
            # Seleccionar el subarbre adequat segons la predicció de KMeans.
            if label == 0:
                node_actual = node_actual.get_left()
            else:
                node_actual = node_actual.get_right()

        return node_actual.get_root(), labels
    
    
    def most_n_similars(self, cas:Cas ,n_similars:int) -> Tuple[Cas, List]:
        """
        Donat un  cas a comparar (Cas), retorna el cas més similar 
        en l'Indexacio i la llista de labels per després afegir el nou cas.
        """
        # Recorre l'arbre per a trobar el cas més similar.
        pre_orden = self.preorder()
        mas_similar = cas.most_similar()
        posicion = pre_orden.index(mas_similar)

        llista_sim = [mas_similar]

        i = posicion
        j = posicion - 1

        while (i < len(pre_orden) and j >= 0) or n_similars==1:
            if i < len(pre_orden):
                if  pre_orden[i].leaf():
                    llista_sim.append(pre_orden[i])
                    n_similars -=1
                i += 1
            if j >= 0:
                if  pre_orden[j].leaf():
                    llista_sim.append(pre_orden[i])
                    n_similars -=1
                j -= 1
        
        return llista_sim


    def add(self, new:Cas, ruta:List[Any]):
        """
        Afegeix un nou cas a l'arbre utilitzant la ruta del cas més similar.
        """
        # Recórrer l'arbre fins al node més similar.
        node_actual = self
        for label in ruta:
            if label == 0:
                node_actual = node_actual.get_left()
            else:
                node_actual = node_actual.get_right()

        # Obtenir el cas del node més similar i afegir el nou cas.
        leafcases = [node_actual.get_root(), new]

        # Crear un nou KMeans amb tots els casos.
        kmeans = KMeans(n_clusters=2, random_state=0, n_init='auto')
        kmeans.fit([cas.descripcio for cas in leafcases])
        
        kmeans.labels_[0]
        # Dividir els casos segons les etiquetes del clustering.
        for i in range(2):
            if kmeans.labels_[i] == 0:
                cluster1 = [leafcases[i]]
            else:
                cluster2 = [leafcases[i]]
        
        # Crear els nous subarbres.
        subarbre1, subarbre2 = Indexacio(), Indexacio()

        subarbre1.creacio(cluster1)
        subarbre2.creacio(cluster2)

        # Actualitzar el node actual amb el nou cluster i subarbres.
        node_actual.set_root(kmeans)
        node_actual.set_left(subarbre1)
        node_actual.set_right(subarbre2)

    def remove(self):
        """
        Treu cas al graf de casos. Per si no es cas rellevant
        """
        


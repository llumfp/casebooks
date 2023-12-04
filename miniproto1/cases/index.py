import numpy as np
from .bintreelinked import BinTree
from typing import List, Any, Tuple
from .case import Cas
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean
from generador_casos import *
from miniproto1.ontology import Book


class Indexacio(BinTree):
    def __init__(self, v=None, left=None, right=None): # type - str, per a determinar quin tipus
                                                       # de creacio s'executa.
        super().__init__(v, left, right)
        

    def creacio_setep1(self, ):
        pass


    def creacio(self,casos:List[Cas], num_casos_fulla:int) -> None:
        if len(casos) <= num_casos_fulla:
            # Si només hi ha un cas, retorna un arbre amb aquest cas.
            self.set_root(casos)
        else:
            # Aplicar KMeans per a dividir els casos en grups.
            kmeans = KMeans(n_clusters=2, random_state=0, n_init='auto')
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


    def creacio2(self, casos: List[Cas], num_casos_fulla:int) -> None:
        if len(casos) <= num_casos_fulla:
            self.set_root(casos)
        else:
            kmeans = KMeans(n_clusters=2, random_state=0)
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



    def creacio_3(self, casos: List[Cas], num_casos_fulla:int) -> None:
        n_clusters = 2
        if len(casos) <= num_casos_fulla:
            # Si només hi ha un cas, retorna un arbre amb aquest cas.
            self.set_root(casos[0])
        else:
            # Aplicar KMeans per a dividir els casos en grups.
            kmeans = KMeans(n_clusters=n_clusters, random_state=0, n_init='auto')
            kmeans.fit([cas.descripcio for cas in casos])

            # Emagatzemar els centroids dels clústers en lloc del model KMeans sencer.
            centroids = kmeans.cluster_centers_

            # Dividir els casos segons les etiquetes del clustering.
            cluster1 = [casos[i] for i in range(len(casos)) if kmeans.labels_[i] == 0]
            cluster2 = [casos[i] for i in range(len(casos)) if kmeans.labels_[i] == 1]

            # Crear els subarbres per a cada cluster.
            subarbre1, subarbre2 = Indexacio(), Indexacio()

            subarbre1.creacio_3(cluster1, num_casos_fulla)
            subarbre2.creacio_3(cluster2, num_casos_fulla)

            # Retorna un arbre amb el centroid del clúster com a arrel i els subarbres com a fills.
            self.set_root(centroids)
            self.set_left(subarbre1)
            self.set_right(subarbre2)


    def most_similar_1(self, cas: Cas) -> Tuple[Cas, List]:
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
    
    def most_similar_3(self, cas: Cas) -> Tuple[Cas, List]:
        """
        Donat un cas a comparar (Cas), retorna el cas més similar 
        en l'Indexacio i la llista de labels per després afegir el nou cas.
        """
        # Recorre l'arbre per a trobar el cas més similar.
        node_actual = self
        labels = []
        while not node_actual.leaf():
            centroids = node_actual.get_root()
            # Calcula la distància del cas a cada centroid i determina el més proper
            distancies = [euclidean(cas.descripcio, centroid) for centroid in centroids]
            label = distancies.index(min(distancies))
            labels.append(label)

            # Seleccionar el subarbre adequat segons la distància mínima.
            if label == 0:
                node_actual = node_actual.get_left()
            else:
                node_actual = node_actual.get_right()

        return node_actual.get_root(), labels

    def most_n_similars_2(self, new_cas: Cas, n_similars: int) -> Tuple[List[Tuple[Cas, float]], List[int]]:
        if self.leaf():
            return [(self._root, 0)]  # Asumiendo que _root es un Cas

        casos, recorrido = self.most_similar_1(new_cas)

        if len(casos) >= n_similars:
            return sorted([(cas, euclidean(new_cas.descripcio, cas.descripcio)) for cas in casos], key=lambda x: x[1])[:n_similars]

        node_actual = self
        recorrido[-1] = 0 if recorrido[-1] == 1 else 1

        for label in recorrido:
            node_actual = node_actual.get_left() if label == 0 else node_actual.get_right()

        num_casos = n_similars - len(casos)
        total_casos = casos + node_actual.most_n_similars_2(new_cas, num_casos)
        n_casos = [(cas, self.euclidean(new_cas.descripcio, cas.descripcio)) for cas in total_casos]

        # Ordenar los casos por distancia y seleccionar los n mejores
        return sorted(n_casos, key=lambda x: x[1])[:n_similars], recorrido


    #def most_n_similars(self, cas:Cas ,n_similars:int) -> Tuple[Cas, List]:
    #    """
    #    Donat un  cas a comparar (Cas), retorna el cas més similar 
    #    en l'Indexacio i la llista de labels per després afegir el nou cas.
    #    """
    #    # Recorre l'arbre per a trobar el cas més similar.
    #    pre_orden = self.preorder()
    #    mas_similar = cas.most_similar()
    #    posicion = pre_orden.index(mas_similar)
    #
    #    llista_sim = [mas_similar]
    #
    #    i = posicion
    #    j = posicion - 1
    #
    #    while (i < len(pre_orden) and j >= 0) or n_similars==1:
    #        if i < len(pre_orden):
    #            if  pre_orden[i].leaf():
    #                llista_sim.append(pre_orden[i])
    #                n_similars -=1
    #            i += 1
    #        if j >= 0:
    #            if  pre_orden[j].leaf():
    #                llista_sim.append(pre_orden[i])
    #                n_similars -=1
    #            j -= 1
    #    
    #    return llista_sim


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
        


    def calcular_valor_confianza(casos_similares: List[Tuple[Cas,float]], new_case: Cas) -> Tuple[Tuple['Book', float]]:
        # Diccionario para almacenar los valores acumulados de confianza para cada libro
        valor_confianza_libros = {}

        for caso in casos_similares:
            # Calcular la distancia (similitud inversa) entre el caso nuevo y cada caso similar
            #distancia = euclidean(new_case.descripcio, caso.descripcio)

            if caso.solucio and caso.avaluacio:
                for libro in caso[0].solucio:
                    # Inicializar el valor de confianza del libro si no existe
                    if libro not in valor_confianza_libros:
                        valor_confianza_libros[libro] = [0, 0]  # Suma de ponderaciones, Suma de distancias

                    # Sumar la ponderación (evaluación * similitud) y la distancia (similitud) para cada libro
                    valor_confianza_libros[libro][0] += caso[0].avaluacio * (1 / caso[1])
                    valor_confianza_libros[libro][1] += 1 / caso[1]

        # Calcular el valor final de confianza para cada libro
        resultado = [(libro, v[0] / v[1]) for libro, v in valor_confianza_libros.items()]

        # Ordenar los libros por su valor de confianza y seleccionar los tres mejores
        resultado_ordenado = sorted(resultado, key=lambda x: x[1], reverse=True)[:3]

        for i in resultado_ordenado:
            new_case.solucio.append(i[0])
            new_case.avaluacio.append(i[1])

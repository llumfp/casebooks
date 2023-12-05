import numpy as np
from .bintreelinked import BinTree
from typing import List, Any, Tuple
from .case import Cas
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean
from miniproto1.ontology import Book
import pickle



class Indexacio(BinTree):
    def __init__(self, v=None, left=None, right=None): # type - str, per a determinar quin tipus
                                                       # de creacio s'executa.
        super().__init__(v, left, right)

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

            subarbre1.creacio(cluster1, num_casos_fulla)
            subarbre2.creacio(cluster2, num_casos_fulla)

            # Retorna un arbre amb l'objecte KMeans com a arrel i els subarbres com a fills.
            self.set_root(kmeans)
            self.set_left(subarbre1)
            self.set_right(subarbre2)

    def find_leaf(self, cas: Cas) -> Tuple[Cas, List]:
        
        node_actual = self
        labels = []

        while not node_actual.leaf():
            kmeans = node_actual.get_root()
            label = kmeans.predict([cas.descripcio])[0]
            labels.append(label)
            
            if label == 0:
                node_actual = node_actual.get_left()
            else:
                node_actual = node_actual.get_right()

        return node_actual, labels # .get_root() si vols la llista de casos

    def collect_cases(self, node):
        """
        Recolecta todos los casos de un nodo y sus descendientes.
        """
        # Verificar si el nodo es None antes de intentar acceder a sus atributos
        if node is None:
            return []

        # Si el nodo actual contiene un modelo KMeans, no recoger casos de este nodo
        if isinstance(node.get_root(), KMeans):
            return []

        # Caso base: Si el nodo es una hoja, devolver los casos en este nodo
        if node.leaf():
            return [case for case in node.get_root()]

        # Caso recursivo: Recoger casos de los nodos hijos
        return self.collect_cases(node.get_left()) + self.collect_cases(node.get_right())

    def navigate_to_sibling(self, path):
        """
        Navega al nodo hermano basado en el camino proporcionado.
        """
        current = self
        for step in path[:-1]:  # Ignorar el último paso, que es hacia el nodo actual
            current = current.get_left() if step == 0 else current.get_right()
        
        # Si el camino está vacío, no hay hermano al que navegar
        if not path:
            return None
        
        # Ir al nodo hermano
        sibling = current.get_right() if path[-1] == 0 else current.get_left()
        return sibling
    
    def most_similar(self, new_case, n) -> Tuple[List[Tuple[Cas, float]], List[int]]:
        """
        Encuentra los n casos más similares al new_case.
        """
        # Encuentra la hoja más cercana y el recorrido
        leaf, path = self.find_leaf(new_case)

        originalpath = path.copy()

        # Recolecta casos de la hoja más cercana
        all_cases = self.collect_cases(leaf)

        # Si no hay suficientes casos, busca en los nodos hermanos
        while len(all_cases) < n and path:
            path.pop()  # Retroceder un nivel en el árbol

            if not path:  # Si hemos llegado a la raíz, terminar la búsqueda
                break

            node_to_explore = self.navigate_to_sibling(path)
            sibling_cases = self.collect_cases(node_to_explore)
            all_cases.extend(sibling_cases)

        # Calcular distancias y seleccionar los n más cercanos
        distances = [[euclidean(new_case.descripcio, case.descripcio), case] for case in all_cases]
        distances.sort(key=lambda x: x[0])
        closest_cases = distances[:n]

        return closest_cases, originalpath
    
    '''def most_similar(self, new_case, n):
        """
        Encuentra los n casos más similares al new_case.

        Problema: sols funciona si n < num_casos_fulla.
        """
        leaf, path = self.find_leaf(new_case) # El que retorna la llista de casos

        distances = []
        for case in leaf:
            distance = euclidean(new_case.descripcio, case.descripcio)
            distances.append((distance, case))

        distances.sort(key=lambda x: x[0])
        closest_cases = distances[:n]

        return closest_cases, path'''

    
    def most_n_similars_3(self, new_cas: Cas, n_similars: int) -> Tuple[List[Tuple[Cas, float]], List[int]]:
        if self.leaf():
            return ([(self._root, euclidean(new_cas.descripcio, self._root.descripcio))], [])

        # Búsqueda del caso más similar y el camino
        casos, recorrido = self.most_similar_1(new_cas)
        casos = [(cas, euclidean(new_cas.descripcio, cas.descripcio)) for cas in casos]

        if len(casos) >= n_similars:
            return (sorted(casos, key=lambda x: x[1])[:n_similars], recorrido)

        # Navegación al nodo hermano del último nodo visitado
        if recorrido:
            nodo_padre = self
            for label in recorrido[:-1]:  # Navegar hasta el nodo padre del último nodo visitado
                nodo_padre = nodo_padre.get_left() if label == 0 else nodo_padre.get_right()

            # Cambio al nodo hermano
            nodo_hermano = nodo_padre.get_left() if recorrido[-1] == 1 else nodo_padre.get_right()
            recorrido[-1] = 0 if recorrido[-1] == 1 else 1  # Actualizar el camino

            # Búsqueda adicional en el nodo hermano
            casos_adicionales, _ = nodo_hermano.most_n_similars_3(new_cas, n_similars - len(casos))
            casos.extend(casos_adicionales)

        return (recorrido, sorted(casos, key=lambda x: x[1])[:n_similars])
    
    
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
        en l'Indexacio i l  a llista de labels per després afegir el nou cas.
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
            return ([(self._root, 0)], recorrido)  # Asumiendo que _root es un Cas y recorrido es accesible

        casos, recorrido = self.most_similar_1(new_cas)

        if len(casos) >= n_similars:
            return (sorted([(cas, euclidean(new_cas.descripcio, cas.descripcio)) for cas in casos], key=lambda x: x[1])[:n_similars], recorrido)

        node_actual = self
        recorrido[-1] = 0 if recorrido[-1] == 1 else 1

        for label in recorrido:
            node_actual = node_actual.get_left() if label == 0 else node_actual.get_right()

        num_casos = n_similars - len(casos)
        total_casos, _ = node_actual.most_n_similars_2(new_cas, num_casos)
        n_casos = [(cas, self.euclidean(new_cas.descripcio, cas.descripcio)) for cas in total_casos]

        # Ordenar los casos por distancia y seleccionar los n mejores
        return (sorted(n_casos, key=lambda x: x[1])[:n_similars], recorrido)

        # Asumiendo que _root es un Cas y recorrido es accesible


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
        


    def calcular_valor_confianza(self, casos_similares: List[Tuple[float,Cas]], new_case: Cas):
        # Diccionario para almacenar los valores acumulados de confianza para cada libro
        valor_confianza_libros = {}

        for distancia, caso in casos_similares:
            # Calcular la distancia (similitud inversa) entre el caso nuevo y cada caso similar
            #distancia = euclidean(new_case.descripcio, caso.descripcio)
            if caso.solucio and caso.avaluacio:
                for index, libro in enumerate(caso.solucio):
                    # Inicializar el valor de confianza del libro si no existe
                    if libro not in valor_confianza_libros:
                        valor_confianza_libros[libro] = [0, 0]  # Suma de ponderaciones, Suma de distancias

                    # Sumar la ponderación (evaluación * similitud) y la distancia (similitud) para cada libro

                    ###MODIFICAR AIXO
                    valor_confianza_libros[libro][0] += caso[1].avaluacio * (1 / caso[0])
                    valor_confianza_libros[libro][1] += 1 / caso[0]

        # Calcular el valor final de confianza para cada libro
        resultado = [(libro, v[0] / v[1]) for libro, v in valor_confianza_libros.items()]

        # Ordenar los libros por su valor de confianza y seleccionar los tres mejores
        resultado_ordenado = sorted(resultado, key=lambda x: x[1], reverse=True)[:3]

        for i in resultado_ordenado:
            new_case.solucio.append(i[0])
            new_case.avaluacio.append(i[1])

    def guardar(self, nombre_archivo_sin_extension):
        nombre_archivo_completo = f"{nombre_archivo_sin_extension}.pkl"
        with open(nombre_archivo_completo, 'wb') as archivo:
            pickle.dump(self, archivo)

    @classmethod
    def cargar_desde_archivo(cls, nombre_archivo):
        with open(nombre_archivo, 'rb') as archivo:
            instancia = pickle.load(archivo)
        return instancia

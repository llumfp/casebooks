import numpy as np
from .bintreelinked import BinTree
from typing import List, Any, Tuple
from .case import Cas
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.spatial.distance import euclidean
import sys

class Indexacio(BinTree):
    def __init__(
        self, 
        casesbase=None, 
        left=None, right=None, 
        type:str='', 
        casesxleaf:int = 10,
        #Calcualr com de real es la prediccio
        NMAE: int = None,  # Error Absoluto Medio Normalizado
        AE:int = 0, # Sumatorio de las diferencias absolutas entre las puntuaciones predichas y las reales para todos los libros y todos los usuarios
        num_casos_valorats: int=0 # Numero de casos valorats

    ) -> None: # type - str, per a determinar quin tipus de creacio s'executa.
        '''
        r_max -> maxim d'estrelles a la valoració
        r_min -> minim d'estrelles a la valoració
        '''

        super().__init__(casesbase, left, right)
        self.casesbase = casesbase
        self.__length = len(self.casesbase)
        self.type = type
        self.casesxleaf = casesxleaf
        self.AE = AE
        self.num_casos_valorats = num_casos_valorats
        self.creacio(casos=casesbase)
        self.r_max = 5
        self.r_min = 1

    def __len__(self):
        return self.__length

    def creacio(self,casos:List[Cas]) -> None:
        if len(casos) <= self.casesxleaf:
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
            subarbre1 = Indexacio(casesbase=cluster1, casesxleaf=self.casesxleaf) 
            subarbre2 = Indexacio(casesbase=cluster2, casesxleaf=self.casesxleaf)

            # Retorna un arbre amb l'objecte KMeans com a arrel i els subarbres com a fills.
            self.set_root(kmeans)
            self.set_left(subarbre1)
            self.set_right(subarbre2)

    # ========================================================================
    def add(self, new:Cas, ruta:List[Any]):
        """
        Afegeix un nou cas a l'arbre utilitzant la ruta del cas més similar.
        """
        # Recórrer l'arbre fins al node més similar.
        self.__length += 1
        node_actual = self
        for label in ruta:
            if label == 0:
                node_actual = node_actual.get_left()
            else:
                node_actual = node_actual.get_right()

        # Obtenir el cas del node més similar i afegir el nou cas.
        leafcases = [node_actual.get_root(), new]
        self.casesbase.append(new)

        if len(leafcases) >= self.casesxleaf:
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
            subarbre1 = Indexacio(casesbase=cluster1, casesxleaf=self.casesxleaf) 
            subarbre2 = Indexacio(casesbase=cluster2, casesxleaf=self.casesxleaf)

            # Actualitzar el node actual amb el nou cluster i subarbres.
            node_actual.set_root(kmeans)
            node_actual.set_left(subarbre1)
            node_actual.set_right(subarbre2)
        
        else:
            node_actual.set_root(leafcases)


    def delete(self, cas, ruta):
        """
        Elimina un caso del árbol de casos. Si al eliminar el caso, el nodo hoja correspondiente
        queda vacío, el árbol se reestructura para eliminar dicho nodo hoja.
        """
        node_padre = self
        for label in ruta[:-1]:  # Ir al nodo padre del nodo hoja
            if label == 0:
                node_padre = node_padre.get_left()
            else:
                node_padre = node_padre.get_right()

        # Nodo hoja donde se encuentra el caso
        node_hoja = node_padre.get_left(
        ) if ruta[-1] == 0 else node_padre.get_right()

        # Eliminar el caso
        casos = node_hoja.get_root()
        casos.remove(cas)

        # Si el nodo hoja queda vacío después de eliminar el caso
        if not casos:
            # Reestructurar el árbol
            if ruta[-1] == 0:
                node_padre._root._left = None
            else:
                node_padre._root._right = None

            # Si el nodo padre ahora es una hoja, reemplazarlo por su nodo padre
            if node_padre.leaf():
                self._root = node_padre.get_root()

    '''
    MANTENIMENT DE LA BASE DE CASOS
    '''
    @property
    def NMAE(self):
        return (self.AE/self.num_casos_valorats)/(self.r_max - self.r_min)

    def refer_base(self):
        '''TODO
        self.casebase = funció(self.casebase):
            retorna la llista de casos utils
        '''
        llista_casos_utils = find_high_utility_cases(BinTree)
        self.creacio(llista_casos_utils)

    @property
    def space(self):
        return sys.getsizeof(self)
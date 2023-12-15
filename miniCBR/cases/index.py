import numpy as np
from .bintreelinked import BinTree
from typing import List, Any, Tuple
from .case import Cas
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.spatial.distance import euclidean

class Indexacio(BinTree):
    def __init__(
        self, 
        casesbase=None, 
        left=None, right=None, 
        type:str='', 
        casesxleaf:int = 10,
        #Calcualr com de real es la prediccio
        NMAE: int = None,  # Error Absoluto Medio Normalizado
        Sum_Dif_Abs:int = None, # Sumatorio de las diferencias absolutas entre las puntuaciones predichas y las reales para todos los libros y todos los usuarios
        num_casos_valorats: int=0 # Numero de casos valorats

    ) -> None: # type - str, per a determinar quin tipus de creacio s'executa.
        
        super().__init__(casesbase, left, right)
        self.casesbase = casesbase
        self.__length = len(self.casesbase)
        self.type = type
        self.casesxleaf = casesxleaf
        self.NMAE=NMAE
        self.Sum_Dif_Abs= Sum_Dif_Abs
        self.num_casos_valorats=num_casos_valorats
        self.creacio(casos=casesbase)

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
            
    #========================================================================
    #Reuse
    def calcular_valor_confianza(casos_similares: List[Tuple[float, 'Cas']], new_case: 'Cas'):
        # Diccionario para almacenar los valores acumulados de confianza para cada libro
        valor_confianza_libros = {}

        for distancia, caso in casos_similares:
            if caso.solucio and caso.avaluacio:
                for index, libro in enumerate(caso.solucio):
                    # Inicializar el valor de confianza del libro si no existe
                    if libro not in valor_confianza_libros:
                        valor_confianza_libros[libro] = [0, 0, []]  # Suma de ponderaciones, Suma de similitudes, Casos

                    # Asegúrate de que la distancia no sea cero para evitar la división por cero
                    if distancia == 0:
                        continue

                    similitud = 1 / distancia

                    # Sumar la ponderación (evaluación * similitud) y la similitud para cada libro
                    valor_confianza_libros[libro][0] += caso.avaluacio[index] * similitud
                    valor_confianza_libros[libro][1] += similitud
                    valor_confianza_libros[libro][2].append(caso)

        # Calcular el valor final de confianza para cada libro
        resultado = {libro: (valores[0] / valores[1] if valores[1] != 0 else 0, valores[2]) for libro, valores in valor_confianza_libros.items()}

        # Ordenar los libros por su valor de confianza y seleccionar los tres mejores
        resultado_ordenado = sorted(resultado.items(), key=lambda x: x[1][0], reverse=True)[:3]

        listas_casos_utilitzats = [[] for _ in range(3)]
        puntuaciones_confianza = []
        for i, (libro, (confianza, casos)) in enumerate(resultado_ordenado):
            new_case.solucio.append(libro)
            puntuaciones_confianza.append(confianza)
            listas_casos_utilitzats[i] = casos

        return listas_casos_utilitzats, puntuaciones_confianza

    # ========================================================================
    #Revise
    #...............................MODEL AI
    def assingar_valoracions_a_ma(cas, valoracio1:int=None, valoracio2:int=None, valoracio3:int=None):
        cas.avaluacio([valoracio1, valoracio2, valoracio3])

    # ========================================================================
    #Retain
    # CALCUL Utilitat Normalitzada
    def recompte_valors_utilitxats(self, cas, casos_similares, listas_casos_utilitzats):
        pos, neg = 0, 0

        for index, puntuacio in enumerate(cas.avaluacio):
            if puntuacio is not None:
                casos_index = listas_casos_utilitzats[index]
                if puntuacio > 3.5:
                    pos += 1
                    for cas in casos_index:
                        cas.UaS += 1
                else:
                    neg += 1
                    for cas in casos_index:
                        cas.UaF += 1

        for cas in casos_similares:
            cas.S += pos
            cas.F += neg


    def actualitzar_Utilitat_normalitzada_casos(self, llista_casos_similars):
        for cas in llista_casos_similars:
            cas.actualitzar_Utilitat_normalitzada()


    # CALCUL Error Absoluto Medio Normalizado
    def realness(self, new: Cas, puntuaciones_confianza):
        num_punt = 0
        for index, valoracio in enumerate(new.avaluacio):
            if valoracio is not None and puntuaciones_confianza[index] is not None:
                num_punt += abs(valoracio - puntuaciones_confianza[index])
                self.num_casos_valorats += 1

        if num_punt > 0:
            self.Sum_Dif_Abs += num_punt
            return True
        return False


    def actualixar_NMAE(self):
        self.NMAE= (self.Sum_Dif_Abs/self.num_casos_valorats)/4

    # Retain
    def redundant_optim(new: Cas, most_similars: List[Tuple[float, Cas]]):
        T = 1
        dicc = {new.solution[i]: new.avaluacio[i] for i in range(3)}
        dicc_keys_set = set(dicc.keys())  # Convertir las claves en un conjunto

        for dist, case in most_similars:
            if dist < T:
                coincident_books = 0
                for book in dicc_keys_set.intersection(case.solution):
                    if abs(dicc[book] - case.avaluacio[case.solution.index(book)]) <= 1.5:
                        coincident_books += 1
                        if coincident_books >= 2:
                            return True
            else:
                return False
        return False

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
        leafcases = node_actual.get_root() + [new]

        if len(leafcases) > self.casesxleaf:
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

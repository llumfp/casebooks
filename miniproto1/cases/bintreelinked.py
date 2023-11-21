from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import numpy as np
from sklearn.cluster import KMeans


class BinTree:

    #------------------- nested _Node class --------------------------
    
    class _Node:
        __slots__ = '_element', '_left', '_right'   # streamline memory usage

        def __init__(self, element, left = None, right = None):
            self._element = element
            self._left    = left
            self._right   = right

        
    #--------------- BinTree public methods ------------------------

    # Beware the distinction between an empty BinTree, and an empty _Node (that is None)
    
    def __init__(self,v=None,left=None,right=None):
        """
        Warning, an empty tree is NOT None
        An empty tree is a BinTree with self._root equal to None
        The object created by a call to BinTree() is an empty tree
        Requirement: If the value v is None, so must be the two children.
        """
        assert (v is None and left is None and right is None) or v is not None
        if v is None:
            self._root = None   # Empty tree
        else:
            l = left._root  if (left  is not None) else None    # <== ATENCIÓ!!!
            r = right._root if (right is not None) else None    # <== ATENCIÓ!!!
            self._root = self._Node(v, l, r)
            
    # Getters
    def get_root(self):
        """
        Pre: It is assumed that the BinTree is NOT empty
        returns the value at the root of the BinTree
        """
        return self._root._element
    
    def get_left(self):
        """
        Pre: It is assumed that the BinTree is NOT empty
        returns the left child of the BinTree
        """
        lft = BinTree()
        lft._root = self._root._left
        return lft
    
    def get_right(self):
        """
        Pre: It is assumed that the BinTree is NOT empty
        returns the right child of the BinTree
        """
        rft = BinTree()
        rft._root   = self._root._right
        return rft

    # Setters
    def set_root(self,v):
        """
        changes the value at the root of the BinTree
        """
        assert(v is not None)
        if not self.empty():
            self._root._element = v
        else:
            self._root = self._Node(v)
        
    def set_left(self,left):
        """
        Pre: left is a BinTree and the BinTree is not empty
        changes the left child of the BinTree
        """
        self._root._left = left._root
        
    def set_right(self,right):
        """
        Pre: right is a BinTree and the BinTree is not empty
        changes the right child of the BinTree
        """
        self._root._right = right._root
        
    # Other operations
    def empty(self):
        """
        returns True if the BinTree is empty, False in other case
        """
        return self._root == None
        
    def leaf(self):
        """
        returns True if the BinTree is a leaf, False if not. The BinTree is not empty
        """
        return self._root._left is None and self._root._right is None



    def __repr__(self):
        if self.empty():
            return 'BinTree()'
        elif self.leaf():
            rt = self.get_root().__repr__()
            return f"BinTree({rt})"
        else:  #  Algun dels fills no és buit
            rt = self.get_root().__repr__()
            if self.get_right().empty():  # El fill dret és buit?
                r_esq = self.get_left().__repr__()
                return f"BinTree({rt}, left={r_esq})"
            elif self.get_left().empty(): # El fill esquerre és buit?
                r_dre = self.get_right().__repr__()
                return f"BinTree({rt}, right={r_dre})"
            else:                         # Cap fill és buit
                r_esq = self.get_left().__repr__()
                r_dre = self.get_right().__repr__()
                return f"BinTree({rt}, left={r_esq}, right={r_dre})"


    def creacio(self,casos):
        n_clusters = 2
        if len(casos) == 1:
            # Si només hi ha un cas, retorna un arbre amb aquest cas.
            self.set_root(casos[0])
        else:
            vectors = casos
            #vectors = [cas.descripcio for cas in casos]

            # Aplicar KMeans per a dividir els casos en grups.
            kmeans = KMeans(n_clusters=n_clusters, random_state=0, n_init='auto')
            kmeans.fit(vectors)

            # Dividir els casos segons les etiquetes del clustering.
            cluster1 = [casos[i] for i in range(len(casos)) if kmeans.labels_[i] == 0]
            cluster2 = [casos[i] for i in range(len(casos)) if kmeans.labels_[i] == 1]

            # Crear els subarbres per a cada cluster.
            subarbre1 = BinTree()
            subarbre2 = BinTree()
            subarbre1.creacio(cluster1)
            subarbre2.creacio(cluster2)

            # Retorna un arbre amb l'objecte KMeans com a arrel i els subarbres com a fills.
            self.set_root(kmeans)
            self.set_left(subarbre1)
            self.set_right(subarbre2)

    def trobar_mes_similar(self, cas_a_comparar):
        """
        Donat un  cas a comparar (Cas), retorna el cas més similar 
        en l'Indexacio i la llista de labels per després afegir el nou cas.
        """
        # Recorre l'arbre per a trobar el cas més similar.
        node_actual = self
        labels = []
        while not node_actual.leaf():
            kmeans = node_actual.get_root()
            label = kmeans.predict([cas_a_comparar])[0]
            labels.append(label)

            # Seleccionar el subarbre adequat segons la predicció de KMeans.
            if label == 0:
                node_actual = node_actual.get_left()
            else:
                node_actual = node_actual.get_right()

        return node_actual.get_root(), labels
 
    def afegir_cas(self, nou_cas, ruta):
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

        # Obtenir els casos del node més similar i afegir el nou cas.
        casos_actuals = [node_actual.get_root(), nou_cas]

        # Crear un nou KMeans amb tots els casos.
        kmeans = KMeans(n_clusters=2, random_state=0, n_init='auto')
        kmeans.fit(casos_actuals)
        
        kmeans.labels_[0]
        # Dividir els casos segons les etiquetes del clustering.
        for i in range(2):
            if kmeans.labels_[i] == 0:
                cluster1 = [casos_actuals[i]]
            else:
                cluster2 = [casos_actuals[i]]
        
        # Crear els nous subarbres.
        subarbre1 = BinTree()
        subarbre2 = BinTree()
        subarbre1.creacio(cluster1)
        subarbre2.creacio(cluster2)

        # Actualitzar el node actual amb el nou cluster i subarbres.
        node_actual.set_root(kmeans)
        node_actual.set_left(subarbre1)
        node_actual.set_right(subarbre2)


# data = np.array([[2, 3],
#                  [3, 3],
#                  [3, 4],
#                  [6, 5],
#                  [6, 4],
#                  [7, 5],
#                  [8, 7],
#                  [8, 8],
#                  [9, 6],
#                  [9, 9]])

# arbre = BinTree(data)
# arbre.creacio(data)
# print(arbre.get_left())
# print(arbre.get_right())



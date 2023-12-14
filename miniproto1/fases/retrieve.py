"""
RETRIEVE CYCLE PART 
"""
from miniproto1.cases.index import Indexacio
from miniproto1.cases.case import Cas
from typing import Tuple, List
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

def find_leaf(indexacio: Indexacio, cas: Cas) -> Tuple[Cas, List]:
    node_actual = indexacio
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

def collect_cases(node):
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
        for case in node.get_root():
            case.cops_us +=1

        return [case for case in node.get_root()]

    # if node.leaf():
    #     cas=[]
    #     for case in node.get_root():
    #         case.cops_us +=1
    #         cas.append(case)
    # return cas

    # # Caso recursivo: Recoger casos de los nodos hijos
    return collect_cases(node.get_left()) + collect_cases(node.get_right())

def navigate_to_sibling(indexacio: Indexacio, path):
    """
    Navega al nodo hermano basado en el camino proporcionado.
    """
    current = indexacio
    for step in path[:-1]:  # Ignorar el último paso, que es hacia el nodo actual
        current = current.get_left() if step == 0 else current.get_right()
    
    # Si el camino está vacío, no hay hermano al que navegar
    if not path:
        return None
    
    # Ir al nodo hermano
    sibling = current.get_right() if path[-1] == 0 else current.get_left()
    return sibling

def most_similar(indexacio: Indexacio, new_case, n) -> Tuple[List[Tuple[float, Cas]], List[int]]:
    """
    Encuentra los n casos más similares al new_case.
    """
    # Encuentra la hoja más cercana y el recorrido
    leaf, path = find_leaf(indexacio,new_case)

    originalpath = path.copy()

    # Recolecta casos de la hoja más cercana
    all_cases = collect_cases(leaf)

    # Si no hay suficientes casos, busca en los nodos hermanos
    while len(all_cases) <= n+3 and path:
        path.pop()  # Retroceder un nivel en el árbol

        if not path:  # Si hemos llegado a la raíz, terminar la búsqueda
            break

        node_to_explore = navigate_to_sibling(indexacio,path)
        sibling_cases = collect_cases(node_to_explore)
        all_cases.extend(sibling_cases)

    print(len(all_cases))
    # Calcular distancias y seleccionar los n más cercanos
    distances = [[euclidean(new_case.descripcio, case.descripcio), case] for case in all_cases]
    distances.sort(key=lambda x: x[0])
    closest_cases = distances[:n]

    print(len(distances)) # 9

    return closest_cases, originalpath


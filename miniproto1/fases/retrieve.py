"""
RETRIEVE CYCLE PART 
"""
from miniproto1.cases.index import Indexacio
from miniproto1.cases.case import Cas
from typing import Tuple, List
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

def collect_cases(node:Indexacio, new_case:Cas, cases:List[Cas], n:int):
    if node.leaf():
        return cases + node.get_root()
    else:
        kmeans = node.get_root()
        label = kmeans.predict([new_case.descripcio])[0]
        if label == 0:
            cases = collect_cases(node.get_left(), new_case, cases, n)
            if len(cases) >= n:
                return cases
            else:
                cases = collect_cases(node.get_right(), new_case, cases, n)
                return cases
        else:
            cases = collect_cases(node.get_right(), new_case, cases, n)
            if len(cases) >= n:
                return cases
            else:
                cases = collect_cases(node.get_left(), new_case, cases, n)
                return cases

def most_similar(indexacio: Indexacio, new_case:Cas) -> Tuple[List[Tuple[float, Cas]], List[int]]:
    n = indexacio.casesxleaf

    leaf, path = find_leaf(indexacio,new_case)
    originalpath = path.copy()
    cases = leaf.get_root()

    if len(cases) < n:
        last_label = path.pop()
        node_actual = indexacio
        for label in path:
            node_actual = node_actual.get_left() if label == 0 else node_actual.get_right()
        neighbor = node_actual.get_left() if last_label == 1 else node_actual.get_right()
        
        cases = collect_cases(neighbor, new_case, cases, n)
    
    distances = [[euclidean(new_case.descripcio, case.descripcio), case] for case in cases]
    distances.sort(key=lambda x: x[0])
    most_n_similars = distances[:n]

    return most_n_similars, originalpath
       

def collect_cases2(node, new_case, cases, n):
    """
    Collect cases from the tree, keeping track of the path taken to reach each case.
    Each case is associated with its unique path.
    """
    """
    Collect cases from the tree. This function remains as in the original implementation.
    """
    if node.leaf():
        return cases + node.get_root()
    else:
        kmeans = node.get_root()
        label = kmeans.predict([new_case.descripcio])[0]
        if label == 0:
            cases = collect_cases2(node.get_left(), new_case, cases, n)
            if len(cases) >= n:
                return cases
            else:
                return collect_cases2(node.get_right(), new_case, cases, n)
        else:
            cases = collect_cases2(node.get_right(), new_case, cases, n)
            if len(cases) >= n:
                return cases
            else:
                return collect_cases2(node.get_left(), new_case, cases, n)



def most_similar2(indexacio, new_case):
    """
    Find the most similar cases to a new case, and return them along with the path taken to find them.
    """
    n = indexacio.casesxleaf

    leaf, path = find_leaf(indexacio, new_case)
    originalpath = path.copy()
    cases = leaf.get_root()

    if len(cases) < n:
        last_label = path.pop()
        node_actual = indexacio
        for label in path:
            node_actual = node_actual.get_left() if label == 0 else node_actual.get_right()
        neighbor = node_actual.get_left() if last_label == 1 else node_actual.get_right()

        cases = collect_cases2(neighbor, new_case, cases, n)

    # Calculate distances and associate each case with the original path
    distances = [[euclidean(new_case.descripcio, case.descripcio),
                  case, originalpath] for case in cases]
    distances.sort(key=lambda x: x[0])
    most_n_similars_with_paths = distances[:n]

    return most_n_similars_with_paths, originalpath




#############################################################################




















'''def most_similar_original_Artur(indexacio, new_case, n):
    """
    Encuentra los n casos más similares al new_case.
    """
    # Encuentra la hoja más cercana y el recorrido
    leaf_node, path = find_leaf(indexacio, new_case)
    originalpath = path.copy()

    # Recolecta casos de la hoja más cercana
    all_cases = collect_cases_original(indexacio, leaf_node)

    # Si no hay suficientes casos, busca en los nodos hermanos
    pila = []

    while len(all_cases) < n and path:
          # Retroceder un nivel en el árbol
        node_to_explore = navigate_to_sibling_original(indexacio, path)

        if node_to_explore.leaf():
            sibling_cases = collect_cases_original(indexacio, node_to_explore)
        
        else:
            node_to_explore.get_root()
         
        all_cases.extend(sibling_cases)

        path.pop()

    # Calcular distancias y seleccionar los n más cercanos
    distances = [(euclidean(new_case.descripcio, case.descripcio), case) for case in all_cases]
    distances.sort(key=lambda x: x[0])
    closest_cases = distances[:n]

    return closest_cases, originalpath'''
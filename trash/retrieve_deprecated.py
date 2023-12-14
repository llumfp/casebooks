def collect_cases_1(node):
    print('Entro a Collect Cases')
    """
    Recolecta todos los casos de un nodo y sus descendientes.
    """
    # Verificar si el nodo es None antes de intentar acceder a sus atributos
    if node is None:
        print('Node is None')
        return []

    # Si el nodo actual contiene un modelo KMeans, no recoger casos de este nodo
    if isinstance(node.get_root(), KMeans):
        print('Estoy en un nodo KMeans')
        return []

    # Caso base: Si el nodo es una hoja, devolver los casos en este nodo
    if node.leaf():
        print('Estoy en una Hoja')
        print(f'Tengo {len(node.get_root())} casos')
        return [case for case in node.get_root()]

    # Caso recursivo: Recoger casos de los nodos hijos
    return collect_cases(node.get_left()) + collect_cases(node.get_right())

def navigate_to_sibling(indexacio: Indexacio, path):
    print('Entro a Navigate to Sibling')
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
    print('PRIMERA PARTE')
    # Encuentra la hoja más cercana y el recorrido
    leaf, path = find_leaf(indexacio,new_case)

    originalpath = path.copy()

    # Recolecta casos de la hoja más cercana
    all_cases = collect_cases(leaf)

    print('SEGUNDA PARTE')
    # Si no hay suficientes casos, busca en los nodos hermanos
    while len(all_cases) < n and path:
        path.pop()  # Retroceder un nivel en el árbol

        if not path:  # Si hemos llegado a la raíz, terminar la búsqueda
            print('He llegado a la raíz')
            break
        
        print(f'Actualmente all_cases tiene {len(all_cases)} casos')
        node_to_explore = navigate_to_sibling(indexacio,path)
        sibling_cases = collect_cases(node_to_explore)
        print(f'Sibling cases tiene {len(sibling_cases)} casos')
        all_cases.extend(sibling_cases)
        print(f'Modificando all_cases a tener {len(all_cases)} casos.')

    # Calcular distancias y seleccionar los n más cercanos
    distances = [[euclidean(new_case.descripcio, case.descripcio), case] for case in all_cases]
    distances.sort(key=lambda x: x[0])
    closest_cases = distances[:n+1]

    print(len(distances)) # 9

    return closest_cases, originalpath
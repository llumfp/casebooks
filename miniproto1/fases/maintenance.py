"""
Funció: Incorpora la nova experiència (cas d'ús actual) a la base de dades per a futurs usos.

Components: Mecanismes per a l'actualització de la base de dades amb nous casos.
"""
import random
from miniproto1.cases import Cas, Indexacio
from miniproto1.fases import *
import random
import timeit

def generate_new_case():
    # Generar los primeros 10 valores: enteros únicos del 1 al 10
    first_ten = random.sample(range(1, 11), 10)
    
    # Generar el undécimo valor: entero en el rango de 100 a 400
    eleventh_value = random.randint(100, 400)
    
    # Generar el duodécimo valor: entero en el rango de 1 a 200
    twelfth_value = random.randint(1, 200)
    
    # Generar el decimotercer valor: decimal en el rango de 1 a 5
    thirteenth_value = random.uniform(1, 5)
    
    # Crear el new_case como una cadena
    new_case = ','.join(map(str, first_ten + [eleventh_value, twelfth_value, thirteenth_value]))
    return new_case


def calcular_temps(indexacio: Indexacio):
    num_cases = 200  # Número de casos de prueba a generar
    execution_times = []

    for _ in range(num_cases):
        new_case = generate_new_case()

        # Medir el tiempo de ejecución de most_similar para este new_case
        time_taken = timeit.timeit(
            lambda: most_similar(indexacio, new_case), number=1)
        execution_times.append(time_taken)

    media_tiempo = sum(execution_times) / len(execution_times)
    return media_tiempo


def find_high_utility_cases(bin_tree):
    def dfs(node):
        llindar_utilitat = 0.5
        # Si el árbol está vacío, no hacer nada
        if node.empty():
            return []

        # Si es un nodo hoja, procesar los casos
        if node.leaf():
            return [cas for cas in node.get_root() if cas.UM > llindar_utilitat]

        # Si no es un nodo hoja, continuar con el recorrido
        return dfs(node.get_left()) + dfs(node.get_right())

    # Iniciar el recorrido desde la raíz del árbol
    return dfs(bin_tree)

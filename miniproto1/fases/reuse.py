"""
Funció: Adapta les solucions dels casos recuperats a la nova situació.

Components: Algoritmes per ajustar les recomanacions basades en els casos recuperats.
"""

from miniproto1.cases.index import Indexacio
from miniproto1.cases.case import Cas
from typing import Tuple, List
from scipy.spatial.distance import euclidean


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


"""
Funció: Adapta les solucions dels casos recuperats a la nova situació.

Components: Algoritmes per ajustar les recomanacions basades en els casos recuperats.
"""

from collections import defaultdict
from miniproto1.cases.index import Indexacio
from miniproto1.cases.case import Cas
from typing import Tuple, List
from scipy.spatial.distance import euclidean

def calcular_valor_confianza(casos_similares: List[Tuple[float, 'Cas']], new_case: 'Cas'):
    """

    A partir d'una llista de casos similars i un nou cas, retorna un diccionari amb la informació dels 3 llibres a recomanar
    -> {id_llibre: [valoracions_predita,[casos_similar_que_contenen_el_llibre]]}

    """

    valor_confianza_libros = defaultdict(
        lambda: [0, 0, []])  # Utiliza defaultdict

    for distancia, caso in casos_similares:
        similitud = 1 / distancia if distancia != 0 else 1
        for index, libro in enumerate(caso.solucio):
            aval = caso.avaluacio[index]
            if aval != 0:
                # Calculado una sola vez
                aval_escalado = -2.5 + ((aval - 1) * 1.25)
                valor = aval_escalado * similitud
                valor_confianza_libros[libro][0] += valor
                valor_confianza_libros[libro][1] += similitud
                valor_confianza_libros[libro][2].append(caso)
    print(valor_confianza_libros)
    # Conversión y Ordenación en un paso
    diccionario_ordenado = sorted(
        ((id_llibre, [1 + ((valor / (simil+0.05) - (-2.5)) * 0.8), cases])
         for id_llibre, (valor, simil, cases) in valor_confianza_libros.items()),
        key=lambda item: item[1][0], reverse=True
    )
    
    tres_primers = dict(diccionario_ordenado[:3])
    new_case.solucio = list(tres_primers.keys())

    return tres_primers

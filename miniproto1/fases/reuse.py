"""
Funció: Adapta les solucions dels casos recuperats a la nova situació.

Components: Algoritmes per ajustar les recomanacions basades en els casos recuperats.
"""

from miniproto1.cases.index import Indexacio
from miniproto1.cases.case import Cas
from typing import Tuple, List
from scipy.spatial.distance import euclidean


def calcular_valor_confianza(casos_similares: List[Tuple[float, 'Cas']], new_case: 'Cas'):
    valor_confianza_libros = {}

    for distancia, caso in casos_similares:
        if caso.solucio and caso.avaluacio:
            for index, libro in enumerate(caso.solucio):
                if libro not in valor_confianza_libros:
                    valor_confianza_libros[libro] = [0, 0, []]

                if distancia == 0:
                    continue

                similitud = 1 / distancia

                # Escalar avaluacio de [1, 5] a [-2.5, 2.5]
                avaluacio_escalada = -2.5 + ((caso.avaluacio[index] - 1) * (2.5 - (-2.5)) / (5 - 1))
                
                valor_confianza_libros[libro][0] += avaluacio_escalada * similitud
                valor_confianza_libros[libro][1] += similitud
                valor_confianza_libros[libro][2].append(caso)

    resultado = {libro: (valores[0] / valores[1] if valores[1] != 0 else 0, valores[2]) for libro, valores in valor_confianza_libros.items()}
    resultado_ordenado = sorted(resultado.items(), key=lambda x: x[1][0], reverse=True)[:3]


    listas_casos_utilitzats = [[] for _ in range(3)]
    puntuaciones_confianza = []
    for i, (libro, (confianza, casos)) in enumerate(resultado_ordenado):
        new_case.solucio.append(libro)
        
        # Re-escalar confianza de [-2.5, 2.5] a [1, 5]
        confianza_reescalada = 1 + ((confianza - (-2.5)) * (5 - 1) / (2.5 - (-2.5)))
        puntuaciones_confianza.append(confianza_reescalada)

        listas_casos_utilitzats[i] = casos



    print("ara el que m'interesa")
    print(resultado)
    
    print(listas_casos_utilitzats)
    return listas_casos_utilitzats, puntuaciones_confianza


def calcular_valor_confianz2(casos_similares: List[Tuple[float, 'Cas']], new_case: 'Cas') -> {id_llibre: [valoracions,[casos]]} :
    """
    
    """
    valor_confianza_libros = {}  #{id llibre: [valor, dis,[casos]]}

    for distancia, caso in casos_similares:
        for index, libro in enumerate(caso.solucio):
            aval = caso.avaluacio[index]
            if aval != 0:
                # Escalar avaluacio de [1, 5] a [-2.5, 2.5]
                aval = -2.5 + ((aval- 1) * (2.5 - (-2.5)) / (5 - 1))
                similitud = 1/distancia if distancia != 0 else 1
                if libro not in valor_confianza_libros:
                    valor_confianza_libros[libro] = [aval*similitud, similitud, [caso]]
                else:
                    valor_confianza_libros[libro][0] += aval*similitud
                    valor_confianza_libros[libro][1] += similitud
                    valor_confianza_libros[libro][2].append(caso)

    # {id llibre: [valoracions,[casos]]}
    
    dicc_final = {id_llibre:[valor/simil,cases] for id_llibre, (valor,simil,cases) in valor_confianza_libros.items()}
    resultado_ordenado = sorted(dicc_final.items(), key=lambda x: x[1][0], reverse=True)[:3]

    for valor





















            # Escalar avaluacio de [1, 5] a [-2.5, 2.5]
            avaluacio_escalada = -2.5 + ((caso.avaluacio[index] - 1) * (2.5 - (-2.5)) / (5 - 1))
            
            valor_confianza_libros[libro][0] += avaluacio_escalada * similitud
            valor_confianza_libros[libro][1] += similitud
            valor_confianza_libros[libro][2].append(caso)

    resultado = {libro: (valores[0] / valores[1] if valores[1] != 0 else 0, valores[2]) for libro, valores in valor_confianza_libros.items()}
    resultado_ordenado = sorted(resultado.items(), key=lambda x: x[1][0], reverse=True)[:3]


    listas_casos_utilitzats = [[] for _ in range(3)]
    puntuaciones_confianza = []
    for i, (libro, (confianza, casos)) in enumerate(resultado_ordenado):
        new_case.solucio.append(libro)
        
        # Re-escalar confianza de [-2.5, 2.5] a [1, 5]
        confianza_reescalada = 1 + ((confianza - (-2.5)) * (5 - 1) / (2.5 - (-2.5)))
        puntuaciones_confianza.append(confianza_reescalada)

        listas_casos_utilitzats[i] = casos



    print("ara el que m'interesa")
    print(resultado)
    
    print(listas_casos_utilitzats)
    return listas_casos_utilitzats, puntuaciones_confianza

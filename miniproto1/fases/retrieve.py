"""
Funció: Busca a la base de dades els casos que s'assemblen més a la consulta de l'usuari.

Components: Conexió a la base de dades, algoritmes de cerca, càlcul de similitud.

Tenim: cas més similar i problema del nou cas
Hem de: adaptar la solució del cas similar per al nostre nou cas
Com? quisap


"""
from miniproto1.cases import *
import statistics



def adaptacio_nulla(new:Cas) -> None:
    cas_similar = arbre.most_similar(new)
    sol_similar = cas_similar.solucio
    new.solucio = sol_similar
    new.derivacio = cas_similar


def adaptacio_ponderada(new:Cas) -> None:

    
    cas_similar = arbre.most_n_similars(new, 3) #3 mes similars

    cas_similar.solucio

    for i in range(3):      
        statistics.mode([cas_similar[i].solucio[i],cas_similar[i].solucio[i],cas_similar[i].solucio[i]])
        

    
    

    sol_similar = cas_similar.solucio
    new.solucio = sol_similar
    new.derivacio = cas_similar


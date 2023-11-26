"""
Funció: Busca a la base de dades els casos que s'assemblen més a la consulta de l'usuari.

Components: Conexió a la base de dades, algoritmes de cerca, càlcul de similitud.

Tenim: cas més similar i problema del nou cas
Hem de: adaptar la solució del cas similar per al nostre nou cas
Com? quisap


"""
from miniproto1.cases import *
from collections import Counter

def adaptacio_nulla(new:Cas) -> None:
    cas_similar = arbre.most_similar(new)
    sol_similar = cas_similar.solucio
    new.solucio = sol_similar
    new.derivacio = cas_similar


def adaptacio_ponderada(new:Cas) -> None:
    cas_similar = arbre.most_n_similars(new, 3) #3 mes similars
    books = Counter([book for case in cas_similar for book in case.solution])
    new.solucio = [m[0] for m in books.most_common(3)]
    new.derivacio = cas_similar

def un_paper_mes(new:Cas) -> None:
    pass


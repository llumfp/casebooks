from typing import Any, Tuple
from miniproto1.ontology import Book
from numpy import ndarray

class Cas:
    def __init__(
        self,
        id: str,
        descripcio: ndarray[Any], # El nostre problema ja preprocessat
        derivacio: None,
        solucio: Tuple[Book,Book,Book] = None,
        avaluacio: None = None,
        utilitat: None = None
    ) -> None:
        self.id = id
        self.descripcio:dict = descripcio
        self.derivacio:list = derivacio
        self.solucio:list = solucio # llista de 3 llibres recomanats
        self.avaluacio:int = avaluacio # num del 1-5
        self.mesura_utilitat:bool = utilitat # mirar els altres casos que tenim i valorar si val la pena
    
    def __repr__(self) -> str:
        return f"Cas(id={self.id}, descripcio={self.descripcio})"
    
    def validate(self, casos): 
        # Òscar: potser seria millor això posar-ho al RecommenderSystem, 
        # llavors la funció seria def validate(self, cas:Cas) i ja 
        # tindriem accés a la base de casos
        '''
        mirar tots els casos que tenim a la base de casos
        - Si hi ha un cas molt similar amb mateix resultat no guardem
        - Si el self.avaluacio es molt intermedi (2.5) no ens està aportant 
            informació útil sobre si esta bé o no
        '''

    def obtenir_solucio(self):
        assert self.derivacio != []
        #Quan ja es tenen els casos similars, generar la resposta
        pass
    
    def evaluate(self):
        assert self.solucio != []
        '''
        un cop tenim la solució, preguntar a l'usuari, qunant de bona ha sigut la recomanació
        '''
        pass
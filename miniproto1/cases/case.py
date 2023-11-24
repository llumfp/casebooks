from typing import Any, List
from sklearn.preprocessing import MinMaxScaler
from numpy import ndarray
from collections import namedtuple
import random
import numpy as np

ValType = namedtuple('ValType', ['value', 'type'])

orders = {
    'time':['poco','normal','mucho'],
    ...:...
}

categories = {
    'genre':['Ficcion','No Ficcion'],
    ...:...
}

# Define the Problem class
class Problem:

    '''
    Classe Abstracta de Lector i altres components del problema
    '''
    def __init__(self, age: int, time: str, genre: str):
        self.age = ValType(age,'integer')
        self.time = ValType(time,'discrete') # Categòriques amb ordre
        self.genre = ValType(genre,'categoric') # Categòriques sense ordre

    def __repr__(self):
        return f"Problem(age={self.age}, time='{self.time}', genre='{self.genre}')"
    
    def encode_problem(self) -> List[int]:
        '''
        Function to encode categorical data to numerical values
        '''
        encoded = []

        for variable,v in self.__dict__.items():
            if v.type == 'discrete':
                for idx,value in enumerate(orders[variable]):
                    if value == v.value:
                        encoded.append(idx)
            elif v.type == 'categoric':
                for category in categories[variable]:
                    encoded.append(1) if category == v.value else encoded.append(0)
            else:
                encoded.append(v.value)
        
        return encoded

def scale_features(problems: List["Problem"]) -> np.ndarray:
    '''
    Function to scale features between 0 and 1
    '''
    features = np.array([problem.encode_problem() for problem in problems])

    scaler = MinMaxScaler()
    scaled_features = scaler.fit_transform(features)

    return scaled_features


class Cas:
    def __init__(
        self,
        id: str,
        descripcio: ndarray[Any], # El nostre problema ja preprocessat
        derivacio: Any = [],
        solucio: None = None,
        avaluacio: None = None,
        utilitat: None = None
    ) -> None:
        self.id = id
        self.descripcio:dict = descripcio
        self.derivacio:list = derivacio
        self.solucio:list = solucio #llista de 3 llibres recomanats
        self.avaluacio:int = avaluacio #num del 1-5
        self.mesura_utilitat:bool = utilitat #mirar els altres casos que tenim i valorar si val la pena
    
    def __repr__(self) -> str:
        return f"Cas(id={self.id}, problem={self.descripcio})"
    
    def validate(self, casos):
        '''
        mirar tots els casos que tenim a la base de dades
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
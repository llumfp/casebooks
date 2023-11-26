from typing import Any, List
from sklearn.preprocessing import MinMaxScaler
from numpy import ndarray
from collections import namedtuple, Counter
import random
import numpy as np

from miniproto1 import *

ValType = namedtuple('ValType', ['value', 'type'])

discrete = {
    'public':publics,
    'cover':covers,
    'length':lengths
}

categories = {
    'genre':generes,
    'subgenre':subgenres,
    'goal': goals,
    'theme' : themes
}

def encode_discrete(v,variable:str,encoded:List):
    for idx,value in enumerate(discrete[variable]):
        if value == v:
            encoded.append(idx)
    return encoded

def encode_categoric(v,variable:str,encoded:List):
    for category in categories[variable]:
        encoded.append(1) if category == v else encoded.append(0)
    return encoded

# Define the Problem class
class Problem:

    '''
    Classe Abstracta de Lector i altres components del problema
    '''
    def __init__(
        self, age: int, genre: str, subgenre: str, cover: str, bestseller: bool,
        goal: str, illustrated: bool, hab_lectura: bool, length:str, theme: str, trigger_warnings: list
    ) -> None:
        self.public = ValType(age, 'discrete')
        # self.available = ValType(available, 'discrete') # Categoriques amb ordre
        self.genre = ValType(genre, 'categoric') # Categoriques sense ordre
        self.subgenre = ValType(subgenre, 'categoric')
        self.cover = ValType(cover, 'discrete')
        self.bestseller = ValType(bestseller, 'boolean')
        self.goal = ValType(goal, 'categoric')
        self.illustrated = ValType(illustrated, 'boolean')
        self.hab_lectura = ValType(hab_lectura, 'boolean')
        self.length = ValType(length, 'discrete')
        # self.language = ValType(language, 'categoric')
        self.theme = ValType(theme, 'categoric')
        self.trigger_warnings = ValType(trigger_warnings,'trigger_w')
        # self.read = ValType(read,'books')
        # self.fav_author= ValType(fav_author,'author')
        
        self.encoded = []        

    def __repr__(self):
        return f"Problem(age={self.age}, time='{self.time}', genre='{self.genre}')"
    
    def encode_easy(self) -> None:
        '''
        Function to encode categorical data to numerical values
        '''
        for variable,v in self.__dict__.items():
            if variable != 'encoded' and v.value != None:
                if v.type == 'discrete':
                    self.encoded = encode_discrete(v.value, variable, self.encoded)
                elif v.type == 'categoric':
                    self.encoded = encode_categoric(v.value, variable, self.encoded)
                elif v.type == 'boolean':
                    self.encoded.append(1) if v.value else self.encoded.append(0)
                else:
                    self.encoded.append(v.value)
            else:
                continue

    def encode_hard(self) -> None:
        for variable,v in self.__dict__.items():
            if v.value != None:
                if v.type == 'trigger_w':
                    trig_list = [1 if tr in v.value else 0 for tr in trigger_w]
                    self.encoded += trig_list
            # if v.type == 'books':
            #     d = {g:0 for g in generes}
            #     count = 0
            #     for book in v.value:
            #         d[book.genre] += 1
            #         count += 1
            #     l = [d[g]/count for g in generes]
            #     for percentage in l:
            #         self.encoded.append(percentage)
            # elif v.type == 'author':
            #     self.encoded.append(1) if v.value.isactual else self.encoded.append(0)
            #     self.encoded = encode_discrete(v.value.public, variable, self.encoded)
            #     self.encoded = encode_categoric(v.value.genre, variable, self.encoded)
            #     self.encoded.append(1) if v.value.famous else self.encoded.append(0)
            
            else:
                continue

def scale_features(problems: List["Problem"]) -> np.ndarray:
    '''
    Function to scale features between 0 and 1
    '''
    features = np.array([problem.encoded for problem in problems])

    scaler = MinMaxScaler()
    scaled_features = scaler.fit_transform(features)

    for s, p in zip(scaled_features, problems):
        p.encoded = list(s)

def preprocess(problems:List[Problem]):
    for p in problems:
        p.encode_easy()
    scale_features(problems)
    for p in problems:
        p.encode_hard()



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
        return f"Cas(id={self.id}, descripcio={self.descripcio})"
    
    def validate(self, casos):
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
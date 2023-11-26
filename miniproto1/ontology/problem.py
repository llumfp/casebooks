from typing import List
from sklearn.preprocessing import MinMaxScaler
from collections import namedtuple
import numpy as np

from miniproto1.constants import *

ValType = namedtuple('ValType', ['value', 'type'])

discrete = {
    'public':publics,
    'cover':covers,
    'length':lengths
}

categories = {
    'genre':genres,
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

class Problem:

    '''
    Classe Abstracta de Lector i altres components del problema
    '''
    def __init__(
        self, public: str, genre: str, subgenre: str, cover: str, bestseller: bool,
        goal: str, illustrated: bool, hab_lectura: bool, length:str, theme: str, trigger_warnings: list
    ) -> None:
        self.public = ValType(public, 'discrete')
        self.genre = ValType(genre, 'categoric') 
        self.subgenre = ValType(subgenre, 'categoric')
        self.cover = ValType(cover, 'discrete')
        self.bestseller = ValType(bestseller, 'boolean')
        self.goal = ValType(goal, 'categoric')
        self.illustrated = ValType(illustrated, 'boolean')
        self.hab_lectura = ValType(hab_lectura, 'boolean')
        self.length = ValType(length, 'discrete')
        self.theme = ValType(theme, 'categoric')
        self.trigger_warnings = ValType(trigger_warnings,'trigger_w')
        
        self.encoded = []        

    def __repr__(self):
        return f"Problem(public={self.public}, genre='{self.genre}', cover='{self.cover}')"
    
    def encode_easy(self) -> None:
        '''
        Function to encode categorical data to numerical values
        '''
        for variable,v in self.__dict__.items():
            if variable != 'encoded':
                
                if v.type == 'discrete':
                    if v.value != None:
                        self.encoded = encode_discrete(v.value, variable, self.encoded)
                    else:
                        #TODO: Tractament de valors nuls
                        pass

                elif v.type == 'categoric':
                    if v.value != None:
                        self.encoded = encode_categoric(v.value, variable, self.encoded)
                    else:
                        #TODO: Tractament de valors nuls
                        pass

                elif v.type == 'boolean':
                    if v.value != None:
                        self.encoded.append(1) if v.value else self.encoded.append(0)
                    else:
                        #TODO: Tractament de valors nuls
                        pass

                elif v.type == 'integer':
                    if v.value != None:
                        self.encoded.append(v.value)
                    else:
                        #TODO: Tractament de valors nuls
                        pass

    def encode_hard(self) -> None:
        v = self.trigger_warnings
        if v.value != None:
            trig_list = [1 if tr in v.value else 0 for tr in trigger_w]
            self.encoded += trig_list
        else:
            #TODO: Tractament de valors nuls
            pass


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

    return [p.encoded for p in problems]
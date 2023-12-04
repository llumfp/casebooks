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
    Classe Abstracta de Lector i altres components del problema:
    - user_id : cadena de números per identificar l'usuari
    - fantasy : de tots els llibres que ha llegit, el percentatge que són de fantasia
    - fiction : de tots els llibres que ha llegit, el percentatge que són de ficció
    - mystery : de tots els llibres que ha llegit, el percentatge que són de misteri
    - poetry : de tots els llibres que ha llegit, el percentatge que són de poesia
    - history : de tots els llibres que ha llegit, el percentatge que són de historia
    - romance : de tots els llibres que ha llegit, el percentatge que són romantics
    - nonfiction : de tots els llibres que ha llegit, el percentatge que no son de ficcio
    - children : de tots els llibres que ha llegit, el percentatge que són de nens
    - youngadult : de tots els llibres que ha llegit, el percentatge que són de adolescents
    - comics : de tots els llibres que ha llegit, el percentatge que són de comics
    - mean_cover : format de llibre que ha llegit més
    - mean_length : mitjana de la longitud de tots els llibres que ha llibre
    - num_reads : quantitat de llibres llegits
    - avg_rating : mitjana de la puntuació que ha posat als llibres llegits
    - review_prop : proporció de comentaris ha escrit dels llibres que ha llegit

    '''
    def __init__(
        self, 
        fantasy:int, fiction:int, mystery:int, poetry: int, history: int, romance: int,
        nonfiction: int, children: int, youngadult: int, comics: int, mean_cover: str, 
        mean_length: int, count_reads: int, avg_rating: int, review_prop: int) -> None:
        
        
        self.genre = genre, ''
        self.mean_cover = ValType(mean_cover, '')
        self.mean_length = ValType(mean_length, '')
        self.count_reads = ValType(count_reads, '')
        self.avg_rating =  ValType(avg_rating, '')
        self.review_prop = ValType(review_prop, '')
        
        self.encoded = []        

    def __repr__(self):
        return f"Problem(id={self.id_usuari}, genre='{self.genre}', cover='{self.cover}')"
    
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
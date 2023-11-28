from typing import List, Tuple

class Book:

    def __init__(
            self,
            title:str,
            isactual:bool,
            length:str,
            public:bool,
            cover:str,
            genre:str,
            #author:'Author',
            rating:float,
            subgenre:str = None,
            goal:str = "",
            illustrated = 'FALSE',
            theme:str = "",
            bestseller:bool = 'FALSE',
            triggerw:List = None,
        ) -> None:

        # Features
        self.title = title # Título del libro
        self.isactual = isactual # Actual or not
        self.length = length # Longitud del libro (corto, mediano, largo, muy_largo)
        self.public = public # Público al cual va destinado
        self.cover = cover # Bolsillo, blanda, dura
        self.theme = theme # Temática (lista de temáticas)
        self.goal = goal # Objetivo (entretenimiento, aprendizaje)
        self.illustrated = illustrated # Contiene o no ilustraciones.
        self.bestseller = bestseller # Es o no un bestseller.
        #self.author = author # Autor del libro
        self.triggerw = triggerw # Contiene todos los trigger warnings de este libro. 
        self.genre = genre # Géneros.
        self.subgenre = subgenre # Subgénero.
        self.rating = rating # Valoración media.
        self.punctuation = 0
        
        # Inici de característiques extres !! que no farem avui
        self.saga:str = None # Saga a la que pertenece.
        self.language:str = None # Lengua inicial del libro.
        self.difficulty:bool = None # Dificultad del libro.

    def __getattr__(self, key):
        try:
            return self.__dict[key]
        except:
            raise KeyError()
            
    def __repr__(self) -> str:
        return f'Book({self.title})' 
    
    def __eq__(self, other: object) -> bool:
        return self.dict['title'] == other.dict['title']
    
class Author:
    def __init__(
            self,
            name:str,
            isactual:bool,
            public:str,
            genre:str = None,
            famous:bool = False
        ) -> None:
        self.name = name
        self.isactual = isactual
        self.public = public
        self.genre = genre
        self.famous = famous
        self.books:List['Book'] = []

    def __repr__(self) -> str:
        return f'Author({self.name})'
    
    def __eq__(self, other: 'Author') -> bool: # Similar
        return self.isactual == other.isactual and self.genre == other.genre

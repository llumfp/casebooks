from book import Book
from typing import List

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

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
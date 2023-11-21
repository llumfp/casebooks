class Cas:
    def __init__(self, id:str, descripcio:dict, derivacio = [], solucio = None, avaluacio = None, utilitat = None):
        self.id = id
        self.derivacio:list = derivacio
        self.descripcio:dict = descripcio
        self.diagnostic = ... #preguntar ramon, perque per tenir diagnostic hauriem de fer 'abstraccio'
        self.solucio:list = solucio #llista de 3 llibres recomanats
        self.avaluacio:int = avaluacio #num del 1-5
        self.mesura_utilitat:bool = utilitat #mirar els altres casos que tenim i valorar si val la pena
    
    
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
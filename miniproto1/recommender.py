from miniproto1.fases import *
from miniproto1.cases import *
from typing import Set

class RecommenderSystem:
    def __init__(
            self, 
            maxcasesxleaf:int = 5,
            casebase:pd.DataFrame=None,
            indexacio:str=None
        ) -> None:
        """"Per a que funcioni, és necessari tenir el casebase o la indexació"""
        if not indexacio:
            print(casebase.head())
            self.casebase = redundant_clustering(createDB(casebase))
            self.maxcasesxleaf = maxcasesxleaf
            self.indexacio = Indexacio(casesbase=self.casebase, casesxleaf=self.maxcasesxleaf)

            print("he acabat de crear el arbre")
        else:
            self.indexacio = Indexacio.load(indexacio)

    def guardar(self, nom):
        self.indexacio.save(nom)



    def retrieve(self, newp:Problem) -> Set[Cas]:
        newp = Cas(id=len(self.casebase),descripcio=scale_features([newp])[0])
        return most_similar(self.indexacio, newp)

    def reuse(self, ):
        pass


    def revise(self):
        pass


    def retain(self):
        pass
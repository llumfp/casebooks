from miniproto1.fases import *
from miniproto1.cases import *
from typing import Set

class RecommenderSystem:
    def __init__(
            self, 
            casebase:pd.DataFrame,
            maxcasesxleaf:int = 5,
        ) -> None:
        print(casebase.head())
        self.casebase = redundant_clustering(createDB(casebase))
        self.maxcasesxleaf = maxcasesxleaf
        self.indexacio = Indexacio(casesbase=self.casebase, casesxleaf=self.maxcasesxleaf)

    def retrieve(self, newp:Problem) -> Set[Cas]:
        newp = Cas(id=len(self.casebase),descripcio=scale_features([newp])[0])
        return most_similar(self.indexacio, newp)

    def reuse(self):
        pass


    def revise(self):
        pass


    def retain(self):
        pass
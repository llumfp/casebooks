from miniproto1.fases import *
from miniproto1.cases import *
from typing import Set
import pickle

class RecommenderSystem:
    def __init__(
            self, 
            maxcasesxleaf:int = 5,
            casebase:pd.DataFrame=None
        ) -> None:
        db, self.scaler = createDB(casebase)
        self.casebase = db #redundant_clustering(db)
        self.indexacio = Indexacio(casesbase=self.casebase, casesxleaf=maxcasesxleaf)

    def save(self, nombre_archivo_sin_extension):
        nombre_archivo_completo = f"{nombre_archivo_sin_extension}.pkl"
        with open(nombre_archivo_completo, 'wb') as archivo:
            pickle.dump(self, archivo)

    @classmethod
    def load(cls, path):
        with open(path, 'rb') as archivo:
            instancia = pickle.load(archivo)
        return instancia

    def retrieve(self, newp:Problem) -> List[Tuple[float, Cas, List[int]]]:
        newcase = Cas(id=(len(self.indexacio)),descripcio=self.scaler.transform([newp.array])[0])
        return most_similar(self.indexacio, newcase)
    
    def reuse(self, casos_sim, newc):
        result = confianza(casos_sim, newc)
        return result

    def revise(self, cas, casos, diccion, metode:bool = True):
        if metode:
            user_evaluation(cas)  # Forma manual
        else:
            predict_evaluation(cas) # Usant predictiu
        recompte_valors_utilitzats(cas, casos, diccion)
        calcAE(self.indexacio,cas,diccion)

    def retain(self, cas, cas_dist:List[Tuple[float, Cas]], list_path:List[int]):
        '''
        Per una banda necesitem "Tuple[List[Tuple[float, Cas]" per "redundant_optim", 
        pero per l'altre banda "add" necesita el path que realmet esta calula en 
        "List[Tuple[float, Cas, path]]"
        '''
        # CALCUL DE REDUNDANCIA
        if redundant_cas(cas, cas_dist):
            print("Cas redundant")
        else:
            print("Cas no redundant i s'ha indexat")
            self.indexacio.add(cas,list_path)

    def maintenance(self, T = 999, E = 999):
        '''
        T -> timesteps
        E -> spacesteps
        '''
        if calcular_temps(self.indexacio) >= T or self.indexacio.space >= E:
            refer_base(self.indexacio)

def createRS(from_model:bool, path:str = None, maxcasesxleaf:int = 10, casebase:pd.DataFrame = None):
    if from_model:
        rs = RecommenderSystem.load(path)
    else:
        try:
            casebase.drop('Unnamed: 0',axis=1,inplace=True)
        except:
            pass
        rs = RecommenderSystem(maxcasesxleaf=maxcasesxleaf,casebase=casebase)
    return rs

from miniproto1.fases import *
from miniproto1.cases import *
from typing import Set
import pickle

class RecommenderSystem:
    def __init__(
            self, 
            maxcasesxleaf:int = 5,
            casebase:pd.DataFrame=None,
            
            #Experimentacio redundant
            distance_threshold: float = 2.0,
            # Calcular Eval
            n_correct: int = 0, #numero de prediccions correctes
            n_predictons: int = 0, #numero de casos evaluats

            #Calcualr com de real es la prediccio
            AE:int = 0, # Sumatorio de las diferencias absolutas entre las puntuaciones predichas y las reales para todos los libros y todos los usuarios
            num_casos_valorats: int=0, # Numero de casos valorats

        ) -> None:
        
        db, self.scaler = createDB(casebase)
        self.casebase = redundant_clustering(db, distance_threshold)
        self.indexacio = Indexacio(casesbase=db, casesxleaf=maxcasesxleaf)
        
        # Eval
        self.n_correct: n_correct
        self.n_predictons: n_predictons
        

        
        self.AE = AE
        self.num_casos_valorats = num_casos_valorats

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
        newcase = Cas(id=self.indexacio.ultim_id,descripcio=self.scaler.transform([newp.array])[0])
        return most_similar(self.indexacio, newcase)
    
    def reuse(self, casos_sim, newc):
        result = confianza(casos_sim, newc)
        return result

    def revise(self, cas, casos, diccion, metode:bool = True):
        if metode:
            user_evaluation(cas, self)  # Forma manual
        else:
            predict_evaluation(cas) # Usant predictiu
        recompte_valors_utilitzats(cas, casos, diccion)
        calcAE(cas,diccion,self)

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

    def maintenance(self, T = 0.1, E = 999):
        '''
        T -> timesteps
        E -> spacesteps
        '''
        if calcular_temps(self) >= T or self.indexacio.space >= E:
            self.indexacio.refer_base()

    @property
    def evaluation(self):
        return (self.n_correct/self.n_predictons)*2 if self.n_predictons != 0 else 0

    @property
    def NMAE(self):
        return (self.AE/self.num_casos_valorats)/(self.r_max - self.r_min)


def createRS(from_model:bool, path:str = None, maxcasesxleaf:int = 10, dist_threshold:float = 2.0, casebase:pd.DataFrame = None):
    if from_model:
        rs = RecommenderSystem.load(path)
    else:
        try:
            casebase.drop('Unnamed: 0',axis=1,inplace=True)
        except:
            pass
        rs = RecommenderSystem(maxcasesxleaf=maxcasesxleaf,casebase=casebase, distance_threshold=dist_threshold)
    return rs


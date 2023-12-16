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
    
    def reuse(self, casos, newp):
        casos_utilitzats, puntuacions = calcular_valor_confianza(casos, newp)
        return casos_utilitzats, puntuacions

    def revise(self, cas, metode:bool = True):
        if metode:
            assign(cas) # Forma manual
        else:
            automatic(cas) # Usant predictiu

    # def retain(self, Cas, cas_dist:  List[Tuple[float, Cas]], list_path: List[path]):
    #     '''
    #     Per una banda necesitem "Tuple[List[Tuple[float, Cas]" per "redundant_optim", pero per l'altre banda "delete" necesita el path que realmet esta calula en " List[Tuple[float, Cas, path]]"

    #     E
    #     '''
    #     # CALCUL DE REDUNDANCIA
    #     if redundant_optim(Cas, cas_dist):
    #         print("Cas redundant")

    #     else:
    #         print("Cas no redundant")
    #         # CALCUL Utilitat Normalitzada
    #         recompte_valors_utilitxats(cas, casos_similares, listas_casos_utilitzats)
    #         actualitzar_Utilitat_normalitzada_casos(llista_casos_similars)

    #         for cas in casos_similares:
    #             if cas.UM < threshold:
    #                 print(f"S'ha eliminat: {cas}")
    #                 self.indexacio.delete(cas, path)


    # def evaluation(self, cas, puntuaciones_confianza):
    #     realness(self.indexacio, Cas, puntuaciones_confianza)
    #     return actualixar_NMAE(self.indexacio)


def createRS(from_model, path:str = None, maxcasesxleaf:int = 10, casebase:pd.DataFrame = None):
    if from_model:
        rs = RecommenderSystem.load(path)
    else:
        try:
            casebase.drop('Unnamed: 0',axis=1,inplace=True)
        except:
            pass
        rs = RecommenderSystem(maxcasesxleaf=maxcasesxleaf,casebase=casebase)
    return rs

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
            self.indexacio = Indexacio(casesbase=self.casebase, casesxleaf=maxcasesxleaf)

            print("he acabat de crear el arbre")
        else:
            self.indexacio = Indexacio.load(indexacio)

    def guardar(self, nom):
        self.indexacio.save(nom)


    def retrieve(self, newp:Problem) -> Set[Cas]:
        newp = Cas(id=(len(self.indexacio)),descripcio=scale_features([newp])[0])
        return most_similar2(self.indexacio, newp)
    
    def reuse(self, casos_para_confianza, newp):
        listas_casos_utilitzats, puntuaciones_confianza= calcular_valor_confianza(casos_para_confianza, newp)
        return listas_casos_utilitzats, puntuaciones_confianza


    def revise(self, cas, valoracio1:int=None, valoracio2:int=None, valoracio3:int=None, Metode: Bool= True):
        if Metode:
            assingar_valoracions_a_ma(cas, valoracio1=None, valoracio2=None, valoracio3=None)

        else:
            automatic(cas)

    def retain(self, Cas, most_similars1:  List[Tuple[float, Cas, path]], most_similars2: Tuple[List[Tuple[float, Cas]]]):
        # CALCUL DE REBUNDANCIA
        if redundant_optim(Cas, most_similars2):
            print("Cas rebundant")

        else:
            print("Cas no rebundant")
            # CALCUL Utilitat Normalitzada
            recompte_valors_utilitxats(cas, casos_similares, listas_casos_utilitzats)
            actualitzar_Utilitat_normalitzada_casos(llista_casos_similars)

            for cas in casos_similares:
                if cas.UM < threshold:
                    print(f"S'ha eliminat: {cas}")
                    self.indexacio.delete(cas, path)


    def evaluation(self, cas, puntuaciones_confianza):
        calcul__Sum_Dif_Abs__num_casos_valorats(self.indexacio, Cas, puntuaciones_confianza)
        return actualixar_NMAE(self.indexacio)

git add -A
        pass
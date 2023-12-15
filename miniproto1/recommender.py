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
        if not indexacio:
            print(casebase.head())
            self.casebase = redundant_clustering(createDB(casebase))
            self.indexacio = Indexacio(casesbase=self.casebase, casesxleaf=maxcasesxleaf)
        else:
            self.indexacio = Indexacio.load(indexacio)

    def save_indexation(self, nom):
        self.indexacio.save(nom)

    def retrieve(self, newp:Problem) -> Set[Cas]:
        newp = Cas(id=(len(self.indexacio)),descripcio=scale_features([newp])[0])
        return most_similar(self.indexacio, newp)
    
    def reuse(self, casos, newp):
        casos_utilitzats, puntuacions = calcular_valor_confianza(casos, newp)
        return casos_utilitzats, puntuacions

    def revise(self, cas, metode:bool = True, *args):
        if metode:
            assingar_valoracions_a_ma(cas, args)
        else:
            automatic(cas)

    def retain(self, Cas, most_similars1:  List[Tuple[float, Cas, path]], most_similars2: Tuple[List[Tuple[float, Cas]]]):
        # CALCUL DE REBUNDANCIA
        if redundant_optim(Cas, most_similars2):
            print("Cas redundant")

        else:
            print("Cas no redundant")
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

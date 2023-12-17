from miniproto1.fases import *
from miniproto1.cases import *
from recommender import *
import pandas as pd

def exp_redundancia_inicial(dist_threshold):
    num_cases = 1000
    df_problemes = pd.read_csv('problems40000.csv')
    rs = createRS(from_model= False, casebase=df_problemes, maxcasesxleaf=10, dist_threshold = dist_threshold)

    avaluacio, qualitat = [], []

    for _ in range(num_cases):
        newp_str = generate_new_problem()
        newp = eval(newp_str)
        newcas = Cas(id=(rs.indexacio.ultim_id),descripcio=rs.scaler.transform([newp.array])[0])    
        
        most_similar_cases = rs.retrieve(newp) # Retrieve

        distancies, casos, paths = zip(*most_similar_cases) # Reuse
        cas_dists = list(zip(distancies, casos))
        dicc_most_sim = rs.reuse(cas_dists, newcas)

        rs.revise(newcas, casos, dicc_most_sim, False) # Revise

        rs.retain(newcas, cas_dists,paths[0]) # Retain

        avaluacio.append(rs.evaluation())
        qualitat.append(rs.NMAE())

"""
Per a cada valor de threshold, es genera un problema, i s'afegeixen 1000 casos nous.
Per a cada cas nou es mira:
- Accurcy del model rs.nmae(self)
- Avauluació -> rs.evaluation(self)
Finalment, es mira per a cada valor de thresholds quins són els millors resultats.
La maxcases leaf esta fixada a 10.
"""

def exp_redundancia_newcase():
    pass


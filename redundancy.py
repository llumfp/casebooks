from miniproto1 import *
import pandas as pd
import matplotlib.pyplot as plt
import itertools
from time import time
from datetime import timedelta

def exp_retain(casesxfulla):
    num_cases = 30
    df_problemes = pd.read_csv('./data/problems4000_not_0_0_0.csv')
    init_time = time()
    rs = createRS(from_model= False, casebase=df_problemes, maxcasesxleaf=casesxfulla)
    t_creacio = timedelta(seconds=(time() - init_time))
    avaluacio, qualitat, t_noucas = [], [], []

    for _ in range(num_cases):
        init_time = time()
        newp_str = generate_new_problem()
        newp = eval(newp_str)
        newcas = Cas(id=(rs.indexacio.ultim_id),descripcio=rs.scaler.transform([newp.array])[0])    
        
        most_similar_cases = rs.retrieve(newp) # Retrieve

        distancies, casos, paths = zip(*most_similar_cases) # Reuse
        cas_dists = list(zip(distancies, casos))
        dicc_most_sim = rs.reuse(cas_dists, newcas)

        rs.revise(newcas, casos, dicc_most_sim, False) # Revise

        r = rs.retain(newcas, cas_dists, paths[0]) # Retain
        t_noucas.append(timedelta(seconds=(time() - init_time)))

        avaluacio.append(rs.evaluation)
        qualitat.append(rs.NMAE)

    return t_creacio, avaluacio, qualitat, t_noucas

def plot_data(data, title, thresholds):
    for i, sublist in enumerate(data):
        plt.plot(sublist, label=f'{thresholds[i]} casos per fulla')

    plt.title(title)
    plt.xlabel('Índex de cas')
    plt.ylabel('Valor')
    plt.legend()
    plt.savefig(f'./images/{title}')
    plt.show()
    plt.close()


num_casos = [i for i in range(3,22,2)] 
avaluacions, nmaes, t_inici, t_afegir = [], [], [], []

for casos in num_casos:
    t_creacio, aval, qual, temps = exp_retain(casos)
    t_inici.append(t_creacio)
    avaluacions.append(aval)
    nmaes.append(qual)
    t_afegir.append(temps)


plot_data(avaluacions, 'Avaluacions per a diferents valors de casesxleaf', num_casos)
plot_data(nmaes, 'Resultats de NMAE per a diferents valors de casesxleaf', num_casos)


# Etiquetas para las barras (opcional)

# # Crear el gráfico de barras
# plt.bar(range(len(rates)), rates, tick_label=[str(l) for l in num_casos])
# plt.xlabel('Tasas')
# plt.ylabel('Valores')
# plt.title('Gráfico de Barras para Tasas')

# # Mostrar el gráfico
# plt.savefig('./images/Redundancy_rates_2')
# plt.show()
# plt.close()

#############################
# CONCLUSIÓ: T = 2
#############################


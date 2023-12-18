from miniproto1 import *
import pandas as pd
import matplotlib.pyplot as plt
from time import time

def exp_retain(threshold):
    num_cases = 30
    df_problemes = pd.read_csv('./data/problems8000.csv')
    rs = createRS(from_model= False, casebase=df_problemes)

    avaluacio, qualitat = [], []
    redundants = 0

    for _ in range(num_cases):
        newp_str = generate_new_problem()
        newp = eval(newp_str)
        newcas = Cas(id=(rs.indexacio.ultim_id),descripcio=rs.scaler.transform([newp.array])[0])    
        
        most_similar_cases = rs.retrieve(newp) # Retrieve

        distancies, casos, paths = zip(*most_similar_cases) # Reuse
        cas_dists = list(zip(distancies, casos))
        dicc_most_sim = rs.reuse(cas_dists, newcas)

        rs.revise(newcas, casos, dicc_most_sim, False) # Revise

        r = rs.retain(newcas, cas_dists, paths[0], threshold) # Retain
        redundants += 1 if r else 0

        avaluacio.append(rs.evaluation)
        qualitat.append(rs.NMAE)

    redundancy_rate = redundants/num_cases
    return avaluacio, qualitat, redundancy_rate

def plot_data(data, title, thresholds):
    for i, sublist in enumerate(data):
        plt.plot(sublist, label=f'Threshold {thresholds[i]}')

    plt.title(title)
    plt.xlabel('Índex de cas')
    plt.ylabel('Valor')
    plt.legend()
    plt.savefig(f'./images/{title}')
    plt.show()
    plt.close()


distance_thresholds = [0]+[round(i*0.5,1) for i in range(1,9)]
avaluacions, nmaes, rrate = [], [], []

for threshold in distance_thresholds:
    aval, qual, r = exp_retain(threshold)
    avaluacions.append(aval)
    nmaes.append(qual)
    rrate.append(r)

plot_data(avaluacions, 'Avaluacions per a diferents valors de Thresholds', distance_thresholds)
plot_data(nmaes, 'Resultats de NMAE per a diferents valors de Thresholds', distance_thresholds)


rates = rrate
# Etiquetas para las barras (opcional)

# Crear el gráfico de barras
plt.bar(range(len(rates)), rates, tick_label=[str(l) for l in distance_thresholds])
plt.xlabel('Tasas')
plt.ylabel('Valores')
plt.title('Gráfico de Barras para Tasas')

# Mostrar el gráfico
plt.savefig('./images/Redundancy_rates_2')
plt.show()
plt.close()

#############################
# CONCLUSIÓ: quants més casos per fulla millor (hem provat fins a 21)
#############################
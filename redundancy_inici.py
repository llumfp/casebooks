from CBR import *
import pandas as pd
import matplotlib.pyplot as plt
from time import time
import itertools

def exp_retain(parametres):
    num_cases = 30
    df_problemes = pd.read_csv('./data/problems8000.csv')
    init_time = time()
    rs = createRS(from_model= False, casebase=df_problemes, params=parametres)
    t_creacio = float(time() - init_time)

    avaluacio, qualitat, t_noucas = [], [], []
    redundants = 0

    for _ in range(num_cases): 
        init_time = time()
        newp_str = generate_new_problem()
        newp = eval(newp_str)  
        
        most_similar_cases, newcas = rs.retrieve(newp) # Retrieve

        distancies, casos, paths = zip(*most_similar_cases) # Reuse
        cas_dists = list(zip(distancies, casos))
        dicc_most_sim = rs.reuse(cas_dists, newcas)

        rs.revise(newcas, casos, dicc_most_sim, False) # Revise

        r = rs.retain(newcas, cas_dists, paths[0]) # Retain
        t_noucas.append(float(time() - init_time))
        redundants += 1 if r==1 else 0

        avaluacio.append(rs.evaluation)
        qualitat.append(rs.NMAE)

    redundancy_rate = redundants/num_cases
    return t_creacio, avaluacio, qualitat, t_noucas, redundancy_rate

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

avaluacions, nmaes, t_inici, t_afegir, rrate = [], [], [], [], []
common_books = [2,6]
common_recom = [2,3]
common_rating = [0.2,0.6]
min_distance = [0.2, 0.3]

combinacions = list(itertools.product(common_books, common_recom, common_rating, min_distance))

for parametres in combinacions:
    t_creacio, aval, qual, temps, r = exp_retain(parametres)
    t_inici.append(t_creacio)
    avaluacions.append(aval)
    nmaes.append(qual)
    t_afegir.append(temps)
    rrate.append(r)

plot_data(avaluacions, 'Avaluacions per a diferents valors de casesxleaf', parametres)
plot_data(nmaes, 'Resultats de NMAE per a diferents valors de casesxleaf', parametres)
plot_data(t_afegir, 'Temps en afegir un nou cas per a diferents valors de casesxleaf', parametres)


# Crear el gráfico de barras
plt.bar(range(len(rrate)), rrate, tick_label=[str(l) for l in parametres])
plt.xlabel('Tasas')
plt.ylabel('Valores')
plt.title('Gráfico de Barras para Tasas')

# Mostrar el gráfico
plt.savefig('./images/Redundancy_rates_2')
plt.show()
plt.close()

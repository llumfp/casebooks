from miniproto1 import *
import pandas as pd
import matplotlib.pyplot as plt
from time import time

def exp_retain(casesxfulla):
    num_cases = 10
    df_problemes = pd.read_csv('./data/problems4000_not_0_0_0.csv')
    init_time = time()
    rs = createRS(from_model= False, casebase=df_problemes, maxcasesxleaf=casesxfulla)
    t_creacio = float(time() - init_time)
    avaluacio, qualitat, t_noucas = [], [], []
    redundants = 0

    for _ in range(num_cases):
        print('ja')
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

def plot_data(data, title, cases):
    for i, sublist in enumerate(data):
        plt.plot(sublist, label=f'{cases[i]} casos per fulla')

    plt.title(title)
    plt.xlabel('Índex de cas')
    plt.ylabel('Valor')
    plt.legend()
    plt.savefig(f'./images/{title}')
    plt.show()
    plt.close()


num_casos = [i for i in range(3,50,2)] 
avaluacions, nmaes, t_inici, t_afegir, rrate = [], [], [], [], []

for casos in num_casos:
    t_creacio, aval, qual, temps, r = exp_retain(casos)
    t_inici.append(t_creacio)
    avaluacions.append(aval)
    nmaes.append(qual)
    t_afegir.append(temps)
    rrate.append(r)


plot_data(avaluacions, 'Avaluacions per a diferents valors de casesxleaf', num_casos)
plot_data(nmaes, 'Resultats de NMAE per a diferents valors de casesxleaf', num_casos)
plot_data(t_afegir, 'Temps en afegir un nou cas per a diferents valors de casesxleaf', num_casos)


# GRÀFIC DEL RATE
plt.bar(range(len(rrate)), rrate, tick_label=[str(l) for l in num_casos])
plt.xlabel('Percentatge de redundants')
plt.ylabel('Num de casos')
plt.title('Gràfico de Barres per a la redundància')

# Mostrar el gráfico
plt.savefig('./images/Casesxleaf_redundancy')
plt.show()
plt.close()


# GRÀFIC DEL RATE
plt.bar(range(len(t_inici)), t_inici, tick_label=[str(l) for l in num_casos])
plt.xlabel('Percentatge de redundants')
plt.ylabel('Num de casos')
plt.title('Gàfic de Barres per al temps')

# Mostrar el gráfico
plt.savefig('./images/Casesxleaf_time')
plt.show()
plt.close()


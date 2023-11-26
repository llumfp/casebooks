"""
Funció: Punt d'entrada del programa. Gestiona la interacció amb l'usuari i coordina els altres mòduls.

Contingut: Inicialització, menú d'usuari, crides a altres mòduls.
"""

from miniproto1 import *
from ejecutador import *
import sys

cas1 = Problem(
    public='baby', 
    genre='Fantasy', 
    subgenre='Dark_Fantasy', 
    cover='soft', 
    bestseller=True,
    goal='Entretainment', 
    illustrated=False, 
    hab_lectura=True, 
    length='medium', 
    theme='Sports', 
    trigger_warnings=['1','2','3']
)
cas2 = Problem(
    public='teen', 
    genre='Horror', 
    subgenre='Psychological_Horror', 
    cover='hard', 
    bestseller=True,
    goal='Learning', 
    illustrated=True, 
    hab_lectura=True, 
    length='short', 
    theme='Daily_life', 
    trigger_warnings=['4','5','6']
)
cas3 = Problem(
    public='adult', 
    genre='Historical', 
    subgenre='Realistic', 
    cover='pocket', 
    bestseller=False,
    goal='Learning', 
    illustrated=True, 
    hab_lectura=False, 
    length='very_long', 
    theme='Daily_life', 
    trigger_warnings=['7','8','9']
)


lectors, problemes = generar_libros_aleatorios(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))

for i,l in enumerate(lectors):
    with open(f'instancia_lector.clp','w') as f:
        f.write('(definstances instances')
        f.write(l)
        f.write(') \n \n \n')
    run_clips_with_commands('jp_comandes1.txt', f'llibre_recomanat_{i}.txt')
print(problemes)
    
        
# a = preprocess(problemes)

# for c in a:
#     print(c,end='\n\n')
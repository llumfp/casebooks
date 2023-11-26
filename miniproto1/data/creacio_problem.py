from miniproto1 import *
import numpy as np
import random
import sys

def instancia_baby(goal,illustrated,theme):
    instancia = f"""
    ([lector] of Lector
        (public "baby")
        (goal "{goal}")
        (hab_lectura "Neutral")
        (illustrated {illustrated})
        (theme "{theme}")
    )"""

    problema = Problem('baby', None, None, 'hard', None, goal, illustrated, 'Neutral', 'short', theme, None)
    
    return instancia, problema

#(public: str, genre: str, subgenre: str, cover: str, bestseller: bool, goal: str, illustrated: bool, hab_lectura: bool, length: str, theme: str, trigger_warnings: list) -> None

def instancia_children(illustrated, theme, time_read):
    instancia = f"""
    ([lector] of Lector
        (public "children")
        (hab_lectura "Neutral")
        (illustrated {illustrated})
        (theme "{theme}")
        (time_read "{time_read}")
    )"""
    
    problema = Problem('children', None, None, 'hard', None, None, illustrated, 'Neutral', time_read, theme, None)
    return instancia, problema

#No és segur, fa falta revisar com emmagatzemam es trigger_warnings
def instancia_teenager(main_genre, bestseller, cover, time_read, triggerw):
    instancia = f"""
    ([lector] of Lector
        (public "teenager")
        (main_genre [{main_genre}])
        (bestseller {bestseller})
        (cover "{cover}")
        (hab_lectura "Neutral")
        (time_read "{time_read}")"""
    
    if triggerw != []:
        triggers = ""
        for tr in triggerw:
            triggers += f"{tr} "
        af = f"""        
        (triggerw {triggers})
        )"""
    else:
        af = f"""
        )"""
    instancia += af

    problema = Problem('teenager', main_genre, None, cover, bestseller, None, None, 'Neutral', time_read, None, triggerw)
    return instancia, problema


def instancia_adult(main_genre, has_subgenre, actual, famous, bestseller, cover, time_read, triggerw):
    instancia = f"""
    ([lector] of Lector
        (public "adult")
        (main_genre [{main_genre}])
        (has_subgenre [{has_subgenre}])
        (actual {actual})
        (famous {famous})
        (bestseller {bestseller})
        (cover "{cover}")
        (hab_lectura "Neutral")
        (time_read "{time_read}")"""
    
    if triggerw != []:
        triggers = ""
        for tr in triggerw:
            triggers += f"{tr} "
        af = f"""        
        (triggerw {triggers})
        )"""
    else:
        af = f"""
        )"""
    instancia += af

    problema = Problem('adult', main_genre, has_subgenre, cover , bestseller , None, None, 'Neutral', time_read, None, triggerw)
    return instancia, problema


def generar_baby(num_libros):
    libros, problemas = [], []
    
    for _ in range(num_libros):
        goal = random.choice(goals)
        illustrated = random.choice(['FALSE', 'TRUE'])
        theme = random.choice(themes)
        libro, problema = instancia_baby(goal, illustrated, theme)
        libros.append(libro)
        problemas.append(problema)

    return libros, problemas

def generar_children(num_libros):
    libros, problemas = [], []
    
    for _ in range(num_libros):
        illustrated = random.choice(['FALSE', 'TRUE'])
        theme = random.choice(themes)
        time_read = random.choice(lengths)
        libro, problema = instancia_children(illustrated, theme, time_read)
        libros.append(libro)
        problemas.append(problema)

    return libros, problemas

def generar_teenager(num_libros):
    libros, problemas = [], []
    for _ in range(num_libros):
        main_genre = random.choice(genres_teen)
        bestseller = random.choice(['FALSE', 'TRUE'])
        cover = random.choice(covers)
        time_read = random.choice(lengths)
        prob_tw = genre_teen_trigg_prob[main_genre]
        if prob_tw != 0:
            tw = np.random.choice(['TRUE', 'FALSE'])
        else:
            tw = 'FALSE'
        if tw == 'TRUE':
            triggers = random.sample(trigger_warnings[main_genre], random.randint(1,len(trigger_warnings[main_genre])-1))
            
        else: 
            triggers = []
        libro, problema = instancia_teenager(main_genre, bestseller, cover, time_read,triggers)
        libros.append(libro)
        problemas.append(problema)

    return libros, problemas

def generar_adult(num_libros):
    libros, problemas = [], []
    for _ in range(num_libros):
        main_genre = random.choice(genres)
        has_subgenre = random.choice(list(genrestree[main_genre]))
        bestseller = random.choice(['FALSE', 'TRUE'])
        famous = 'TRUE' if bestseller == 'TRUE' else random.choice(['FALSE', 'TRUE'])
        actual = random.choice(['FALSE', 'TRUE'])
        cover = random.choice(covers)
        time_read = random.choice(lengths)
        prob_tw = subgenre_trigger_warning_probabilities[main_genre][has_subgenre]
        tw = np.random.choice(['TRUE', 'FALSE'], p = [prob_tw, 1-prob_tw])
        if tw == 'TRUE':
            trigger_warning = random.sample(trigger_warnings[main_genre], random.randint(1,len(trigger_warnings[main_genre])-1))

        else: 
            trigger_warning = ""
        libro, problema = instancia_adult(main_genre, has_subgenre, actual, famous, bestseller, cover, time_read, trigger_warning)
        libros.append(libro)
        problemas.append(problema)

    return libros, problemas

def generar_libros_aleatorios(num_baby, num_children, num_teenager, num_adult):
    libros_baby, problemas_baby = generar_baby(num_baby)
    libros_children, problemas_children = generar_children(num_children)
    libros_teenager, problemas_teenager = generar_teenager(num_teenager)
    libros_adult, problemas_adult = generar_adult(num_adult)
    
    libros = libros_baby + libros_children + libros_teenager + libros_adult
    problemas = problemas_baby + problemas_children + problemas_teenager + problemas_adult
    
    return libros, problemas
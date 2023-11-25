import random
import requests
import re
import numpy as np
import pandas as pd
from typing import List, Tuple
import unicodedata

tematiques = ['Sports','Music','Daily_life','Adventures','Magic','Culture']
goals = ['Learning','Entretainment']

names_by_subgenre = {
    'Classic_Romance' : ["El susurro del corazón", "El baile de los sentimientos", "El destello de tus ojos", "Entre sueños y promesas", "El suspiro del amor", "El latido eterno", "Bajo el cielo estrellado", "El perfume de la pasión", "La melodía del amor perdido", "El abrazo del destino", "Entre ruinas y rosas", "El eco del amor", "Las sombras del pasado", "El susurro del viento", "El beso robado", "El jardín de los suspiros", "El secreto del corazón", "El hechizo de tus labios", "La promesa eterna", "Bajo el manto de la luna", "El susurro de tus palabras", "El baúl de los recuerdos", "El refugio de los enamorados"],
    'Erotic' : ["Seducción en la penumbra", "El perfume del deseo", "Secretos entre sábanas", "Bajo el hechizo del placer", "Noches de pasión prohibida", "El fuego de la tentación", "Despertar de los sentidos", "Entre susurros y gemidos", "La danza de la lujuria", "Amor en tiempos eróticos", "El juego del deseo", "Bajo la piel del deseo", "Noches de éxtasis", "El arte del placer", "Destino ardiente", "Labios prohibidos", "El abrazo del deseo", "Bajo la sombra del pecado", "El instante eterno", "Pasión adictiva", "El susurro del amor", "Entre llamas y suspiros", "El vértigo del placer"],
    'Historical_Romance' : ["Susurros del pasado", "La promesa olvidada", "El amor entre los siglos", "El jardín de los enamorados", "Bajo el cielo eterno", "El suspiro del caballero", "El destino de dos corazones", "La dama y el pirata", "El encanto de la condesa", "La pasión prohibida", "El secreto del castillo", "El beso del caballero", "El susurro de la marquesa", "La promesa del duque", "El encuentro en la mansión", "El amor en tiempos de guerra", "El suspiro de la princesa", "El corazón del corsario", "La venganza del conde", "El baile de los amantes", "El encuentro en el bosque", "La pasión de la doncella", "El amor en la corte"],
    'Realistic' : ["El susurro de la historia", "El eco de los tiempos", "La memoria de los siglos", "El legado de los ancestros", "La sombra del pasado", "El suspiro de la nostalgia", "El latido de la historia", "El lienzo de la vida", "El retrato de una era", "El reflejo de los recuerdos", "El tesoro olvidado", "La melodía del tiempo", "El susurro de los antepasados", "La huella de los años", "El susurro del destino", "La mirada del pasado", "El eco de los acontecimientos", "El legado de una época", "El suspiro de la historia", "La memoria de la humanidad", "El latido de la memoria", "El retrato de una generación", "El reflejo de la vida pasada", "El tesoro de la historia", "La melodía de los siglos", "El susurro de los ancestros", "La huella del tiempo", "El susurro del legado", "La mirada de la historia", "El eco de los momentos", "El legado de una era", "El suspiro del pasado", "La memoria de los hombres", "El latido de la nostalgia", "El retrato de una época", "El reflejo de los recuerdos", "El tesoro olvidado", "La melodía del pasado", "El susurro de los antepasados", "La huella de los años", "El susurro del destino", "La mirada del pasado", "El eco de los acontecimientos", "El legado de una época", "El suspiro de la historia", "La memoria de la humanidad", "El latido de la memoria", "El retrato de una generación", "El reflejo de la vida pasada", "El tesoro de la historia", "La melodía de los siglos", "El susurro de los ancestros", "La huella del tiempo", "El susurro del legado", "La mirada de la historia", "El eco de los momentos", "El legado de una era", "El suspiro del pasado", "La memoria de los hombres", "El latido de la nostalgia", "El retrato de una época", "El reflejo de los recuerdos", "El tesoro olvidado", "La melodía del pasado", "El susurro de los antepasados", "La huella de los años", "El susurro del destino", "La mirada del pasado", "El eco de los acontecimientos", "El legado de una época", "El suspiro de la historia", "La memoria de la humanidad", "El latido de la memoria", "El retrato de una generación", "El reflejo de la vida pasada", "El tesoro de la historia", "La melodía de los siglos", "El susurro de los ancestros", "La huella del tiempo", "El susurro del legado", "La mirada de la historia", "El eco de los momentos", "El legado de una era", "El suspiro del pasado", "La memoria de los hombres", "El latido de la nostalgia", "El retrato de una época", "El reflejo de los recuerdos", "El tesoro olvidado", "La melodía del pasado", "El susurro de los antepasados", "La huella de los años", "El susurro del destino", "La mirada del pasado", "El eco de los acontecimientos", "El legado de una época", "El suspiro de la historia", "La memoria de la humanidad", "El latido de la memoria", "El retrato de una generación", "El reflejo de la vida pasada", "El tesoro de la historia", "La melodía de los siglos", "El susurro de los ancestros", "La huella del tiempo", "El susurro del legado", "La mirada de la historia", "El eco de los momentos", "El legado de una era", "El suspiro del pasado", "La memoria de los hombres", "El latido de la nostalgia", "El retrato de una época", "El reflejo de los recuerdos", "El tesoro olvidado", "La melodía del pasado", "El susurro de los antepasados", "La huella de los años", "El susurro del destino", "La mirada del pasado", "El eco de los acontecimientos", "El legado de una época", "El suspiro de la historia", "La memoria de la humanidad", "El latido de la memoria", "El retrato de una generación", "El reflejo de la vida pasada", "El tesoro de la historia", "La melodía de los siglos", "El susurro de los ancestros", "La huella del tiempo", "El susurro del legado", "La mirada de la historia", "El eco de los momentos", "El legado de una era", "El suspiro del pasado", "La memoria de los hombres", "El latido de la nostalgia", "El retrato de una época", "El reflejo de los recuerdos", "El tesoro olvidado", "La melodía del pasado", "El susurro de los antepasados", "La huella de los años", "El susurro del destino", "La mirada del pasado", "El eco de los acontecimientos", "El legado de una época", "El suspiro de la historia", "La memoria de la humanidad", "El latido de la memoria", "El retrato de una generación", "El reflejo de la vida pasada", "El tesoro de la historia", "La melodía de los siglos", "El susurro de los ancestros", "La huella del tiempo", "El susurro del legado", "La mirada de la historia", "El eco de los momentos", "El legado de una era", "El suspiro del pasado", "La memoria de los hombres", "El latido de la nostalgia", "El retrato de una época", "El reflejo de los recuerdos", "El tesoro olvidado", "La melodía del pasado", "El susurro de los antepasados", "La huella de los años", "El susurro del destino", "La mirada del pasado", "El eco de los acontecimientos", "El legado de una época", "El suspiro de la historia", "La memoria de la humanidad", "El latido de la memoria", "El retrato de una generación", "El reflejo de la vida pasada", "El tesoro de la historia", "La melodía de los siglos", "El susurro de los ancestros", "La huella del tiempo", "El susurro del legado", "La mirada de la historia", "El eco de los momentos", "El legado de una era", "El suspiro del pasado", "La memoria de los hombres", "El latido de la nostalgia", "El retrato de una época", "El reflejo de los recuerdos", "El tesoro olvidado", "La melodía del pasado", "El susurro de los antepasados", "La huella de los años", "El susurro del destino", "La mirada del pasado", "El eco de los acontecimientos", "El legado de una época", "El suspiro de la historia", "La memoria de la humanidad", "El latido de la memoria", "El retrato de una generación", "El reflejo de la vida pasada", "El tesoro de la historia", "La melodía de los siglos", "El susurro de los ancestros", "La huella del tiempo", "El susurro del legado", "La mirada de la historia", "El eco de los momentos"],
    'Fiction_History' : ["La sombra del pasado", "Los secretos enterrados", "El susurro de la historia", "El eco de los ancestros", "El legado perdido", "El laberinto del tiempo", "La promesa olvidada", "El destino de los valientes", "El amanecer de la revolución", "El vuelo de las águilas", "La fuerza de la resistencia", "Los hilos del destino", "El amargo sabor de la guerra", "La melodía de la libertad", "El último suspiro", "El despertar de la civilización", "La caída de un imperio", "La esperanza en ruinas", "El secreto de la realeza", "La pasión prohibida", "El rastro de la traición", "La lucha por la igualdad", "El susurro de los dioses", "La búsqueda del tesoro perdido", "El destino de los elegidos", "El legado de los antepasados", "La danza de la revolución", "La balada de los valientes", "El misterio de la historia", "La guerra en las sombras", "El despertar de la esperanza", "El renacimiento de una nación", "El grito de la libertad", "El último acto", "La caída de una dinastía", "El amor en tiempos de guerra", "La conspiración del poder", "La senda de la venganza", "El rugido del león", "El destino de los desterrados", "La llama de la rebelión", "La melodía del pasado", "El último testamento", "La sombra del imperio", "El misterio de la realeza", "La promesa incumplida", "La fuerza de la esperanza", "El despertar de la conciencia", "El legado oculto", "La batalla por la libertad", "El último aliento", "La caída de una era", "El secreto del trono", "La pasión en tiempos oscuros", "El rastro de la ambición", "La lucha por los derechos", "El susurro de los antiguos", "La búsqueda de la reliquia perdida", "El destino de los olvidados", "El legado de los mártires", "La danza de la revuelta", "La balada de los caídos", "El enigma de la historia", "La guerra en la penumbra", "El despertar de la esperanza", "El renacer de una civilización", "El grito de la emancipación", "El último capítulo", "La caída de un linaje", "El amor en épocas turbulentas", "La conspiración del poder", "La senda de la venganza", "El rugido del tigre", "El destino de los desterrados", "La llama de la rebelión", "La melodía del pasado", "El último legado", "La sombra del reino", "El misterio de la monarquía", "La promesa incumplida", "La fuerza de la fe", "El despertar de la conciencia", "El legado escondido", "La batalla por la independencia", "El último respiro", "La caída de una época", "El secreto del poder", "La pasión en tiempos de adversidad", "El rastro de la codicia", "La lucha por la justicia", "El susurro de los dioses antiguos", "La búsqueda del objeto perdido", "El destino de los abandonados", "El legado de los mártires", "La danza de la insurrección", "La balada de los héroes caídos", "El enigma de la historia", "La guerra en las tinieblas", "El despertar de la esperanza", "El renacimiento de una sociedad", "El grito de la liberación", "El último acto", "La caída de una dinastía", "El amor en tiempos de conflicto", "La conspiración del poder", "La senda de la venganza", "El rugido del león", "El destino de los desterrados", "La llama de la revolución", "La melodía del pasado", "El último testamento", "La sombra del imperio", "El misterio de la realeza", "La promesa incumplida", "La fuerza de la esperanza", "El despertar de la conciencia", "El legado oculto", "La batalla por la libertad", "El último aliento", "La caída de una era", "El secreto del trono", "La pasión en tiempos oscuros", "El rastro de la ambición", "La lucha por los derechos", "El susurro de los antiguos", "La búsqueda de la reliquia perdida", "El destino de los olvidados", "El legado de los mártires", "La danza de la revuelta", "La balada de los caídos", "El enigma de la historia", "La guerra en la penumbra", "El despertar de la esperanza", "El renacer de una civilización", "El grito de la emancipación", "El último capítulo", "La caída de un linaje", "El amor en épocas turbulentas", "La conspiración del poder", "La senda de la venganza", "El rugido del tigre", "El destino de los desterrados", "La llama de la rebelión", "La melodía del pasado", "El último legado", "La sombra del reino", "El misterio de la monarquía", "La promesa incumplida", "La fuerza de la fe", "El despertar de la conciencia", "El legado escondido", "La batalla por la independencia", "El último respiro", "La caída de una época", "El secreto del poder", "La pasión en tiempos de adversidad", "El rastro de la codicia", "La lucha por la justicia", "El susurro de los dioses antiguos", "La búsqueda del objeto perdido", "El destino de los abandonados", "El legado de los mártires", "La danza de la insurrección", "La balada de los héroes caídos", "El enigma de la historia", "La guerra en las tinieblas", "El despertar de la esperanza", "El renacimiento de una sociedad", "El grito de la liberación"],
    'Police' : ["La sombra del detective", "El enigma de la calle desierta", "El secreto detrás del crimen", "La noche del misterio sin resolver", "El caso del inspector perdido", "El laberinto de las pistas ocultas", "El silencio de la víctima", "El puzzle del asesinato perfecto", "El detective y la sombra del pasado", "El misterio de la habitación cerrada", "El enigma de la carta anónima", "La traición del alguacil", "El caso del testigo desaparecido", "La conspiración del juez corrupto", "El secreto del informante anónimo", "La red de engaños policiales", "El misterio de la casa abandonada", "El enigma del reloj sin agujas", "El caso del detective sin nombre", "La trampa del inspector infiltrado", "El secreto de la víctima silenciosa", "La sombra del crimen perfecto", "El laberinto de los sospechosos", "El misterio de la marca de sangre", "El enigma del testigo misterioso", "La traición del detective leal", "El caso del asesinato sin motivo", "El secreto del jurado manipulado", "La red de conspiraciones policiales", "El misterio de la mansión embrujada", "El enigma del cadáver sin identidad", "La trampa del detective enmascarado", "El secreto de la víctima olvidada", "La sombra del crimen insoluble", "El laberinto de las pruebas falsas", "El misterio de la marca de fuego", "El enigma de la coartada perfecta", "El caso del detective sin rostro", "La traición del inspector corrupto", "El secreto del testigo amenazado", "La red de mentiras policiales", "El misterio de la casa encantada", "El enigma del asesinato sin rastro", "La trampa del detective traicionado", "El secreto de la víctima desconocida"],
    'Thriller_Mystery' : ["El enigma de la sombra nocturna", "La trampa del laberinto mortal", "El susurro de los secretos ocultos", "El misterio de la habitación cerrada", "La oscuridad tras la sonrisa", "El juego del destino incierto", "La sombra del pasado eterno", "El enigma de la noche eterna", "El laberinto de las mentiras", "El secreto bajo la luna de sangre", "El susurro de la muerte silenciosa", "El misterio de la mente perturbada", "La oscuridad tras el espejo roto", "El juego del destino implacable", "La sombra del pasado olvidado", "El enigma de los suspiros perdidos", "La trampa del laberinto infernal", "El secreto bajo la piel pálida", "El susurro de la noche eterna", "El misterio de la habitación vacía", "La oscuridad tras la sonrisa falsa", "El juego del destino traicionero", "La sombra del pasado oscuro", "El enigma de los secretos prohibidos", "La trampa del laberinto siniestro", "El secreto bajo la máscara de porcelana", "El susurro de la muerte acechante", "El misterio de la mente atormentada", "La oscuridad tras el espejo maldito", "El juego del destino implacable", "La sombra del pasado olvidado", "El enigma de los suspiros perdidos", "La trampa del laberinto infernal", "El secreto bajo la piel pálida", "El susurro de la noche eterna", "El misterio de la habitación vacía", "La oscuridad tras la sonrisa falsa", "El juego del destino traicionero", "La sombra del pasado oscuro", "El enigma de los secretos prohibidos", "La trampa del laberinto siniestro", "El secreto bajo la máscara de porcelana", "El susurro de la muerte acechante", "El misterio de la mente atormentada", "La oscuridad tras el espejo maldito"],
    'Paranormal_Mystery' : ["Sombras en la oscuridad", "El misterio de la casa embrujada", "El enigma de la noche eterna", "El secreto de la tumba olvidada", "La puerta hacia lo desconocido", "El susurro de los espíritus", "El fantasma de la mansión abandonada", "El laberinto de los sueños perdidos", "La sombra que acecha en la penumbra", "El misterio de la mirada perdida", "El secreto del espejo encantado", "La criatura de la oscuridad", "El enigma de la llave ancestral", "El espíritu que vaga sin descanso", "Los secretos ocultos del viejo cementerio", "El misterio de la casa encantada", "El susurro de los muertos", "La sombra del monstruo invisible", "El enigma de la noche eterna", "La puerta hacia lo desconocido", "El susurro de los espíritus", "El fantasma de la mansión abandonada", "El laberinto de los sueños perdidos", "La sombra que acecha en la penumbra", "El misterio de la mirada perdida", "El secreto del espejo encantado", "La criatura de la oscuridad", "El enigma de la llave ancestral", "El espíritu que vaga sin descanso", "Los secretos ocultos del viejo cementerio", "El misterio de la casa encantada", "El susurro de los muertos", "La sombra del monstruo invisible", "El enigma de la noche eterna", "La puerta hacia lo desconocido", "El susurro de los espíritus", "El fantasma de la mansión abandonada", "El laberinto de los sueños perdidos", "La sombra que acecha en la penumbra", "El misterio de la mirada perdida", "El secreto del espejo encantado", "La criatura de la oscuridad", "El enigma de la llave ancestral", "El espíritu que vaga sin descanso", "Los secretos ocultos del viejo cementerio"],
    'High_Fantasy' : ["El Reino de las Sombras Perdidas", "El Susurro de los Dragones", "El Oráculo de los Sueños Olvidados", "La Espada de la Eternidad", "El Laberinto de las Almas Errantes", "La Canción de los Elementos", "El Destino de los Portales", "El Enigma de la Luna Mágica", "El Legado de los Guardianes", "La Profecía de los Héroes", "Las Crónicas del Reino de Cristal", "El Misterio de la Piedra Encantada", "La Senda de los Secretos Prohibidos", "El Velo de los Dioses Antiguos", "La Guerra de las Razas Míticas", "El Despertar de los Seres de Luz", "El Laberinto de los Sueños Perdidos", "La Batalla de los Reinos Olvidados", "La Llave del Portal Dimensional", "El Último Suspiro del Inmortal", "La Profecía de los Siete Reinos", "El Legado de los Elementales", "El Secreto de los Guardianes Celestiales", "La Espada del Destino", "El Misterio de la Isla Prohibida"],
    'Dark_Fantasy' : ["El Reino de las Sombras", "El Susurro de los Demonios", "El Laberinto de la Oscuridad", "El Velo de la Pesadilla", "La Danza de los Espectros", "El Legado de la Muerte", "El Resplandor de la Luna Negra", "La Sombra del Caos", "El Jardín de las Almas Perdidas", "El Canto de los Condenados", "El Espejo de la Locura", "La Profecía de la Tormenta", "El Origen de los Vampiros", "La Ciudad de los Susurros", "El Último Suspiro", "El Manto de las Tinieblas", "La Marca del Destino", "La Corona de los Pesares", "El Laberinto de las Pesadillas", "El Legado de las Criaturas", "La Senda de los Sacrificios", "El Bosque de los Lamentos", "El Eco de la Oscuridad", "La Canción de los Condenados", "El Rostro del Miedo", "La Cosecha de las Almas"],
    'Urban_Fantasy' : ["El Sueño de las Sombras", "El Laberinto de los Sueños", "La Ciudad de los Mil Reflejos", "El Portal de los Destinos", "El Reino de los Susurros", "Las Calles del Olvido", "La Torre de los Secretos", "El Bosque de los Susurros", "El Laberinto de los Recuerdos", "La Ciudad de los Sueños Perdidos", "El Portal de las Pesadillas", "El Reino de los Espejos", "Las Calles del Silencio", "La Torre de los Misterios", "El Bosque de las Sombras", "La Ciudad de los Deseos Prohibidos", "El Portal de las Ilusiones", "El Reino de los Encantamientos", "Las Calles del Despertar", "La Torre de los Enigmas", "El Bosque de los Encuentros", "La Ciudad de los Sueños", "El Portal de las Maravillas", "El Reino de los Secretos Olvidados", "Las Calles del Misterio", "La Torre de los Sueños"],
    'Space_Opera' : ["El Origen de las Estrellas",  "El Canto de las Galaxias",  "El Viaje de los Astronautas",  "El Destino de los Planetas",  "La Danza de los Cometas",  "El Sueño de los Exploradores",  "La Guerra de las Constelaciones",  "El Misterio del Agujero Negro",  "La Rebelión de los Androides",  "El Secreto de la Nave Espacial",  "La Profecía del Universo",  "El Legado de los Extraterrestres",  "El Laberinto de los Planetas",  "La Alianza de las Razas",  "El Enigma de la Nebulosa",  "La Odisea de los Cosmonautas",  "El Exilio de los Humanos",  "La Batalla por la Galaxia"],
    'Cyberpunk' : ["Sueños Enredados en el Ciberespacio", "Ciudad de Neones y Circuitos", "El Reloj de los Hackers", "El Laberinto de la Realidad Virtual", "El Oráculo de los Algoritmos", "El Último Bit de Libertad", "La Rebelión de los Cyborgs", "La Cibernética de los Sentimientos", "Los Susurros del Código Fuente", "La Ciudad de los Drones", "El Espejo Digital del Futuro", "El Vuelo de los Datos Perdidos", "El Lenguaje de las Máquinas", "El Cerebro Cibernético", "El Amanecer de la Inteligencia Artificial", "El Resplandor de los Hologramas", "La Conexión de las Almas Digitales", "La Guerra de los Megacorporaciones"],
    'Postapocalyptic_Dystopia' : ["El último eco", "Despertar en el abismo", "La ciudad en ruinas", "Máquinas de cenizas", "El ocaso de la humanidad", "El laberinto de la desolación", "El renacer de la oscuridad", "El susurro del fin", "El legado de la devastación", "El silencio de la civilización", "El camino hacia la nada", "El amanecer sombrío", "El destino en llamas", "Las sombras del mañana", "La era de la desesperación", "La rebelión en ruinas", "El olvido de la humanidad", "La última esperanza"],
    'Technological' : ["El Código de las Máquinas", "La Era de los Ciberpunks", "El Laberinto de la Inteligencia Artificial", "La Última Frontera Tecnológica", "El Horizonte de los Androides", "La Conexión del Futuro", "El Legado de los Cyborgs", "La Rebelión de las Máquinas", "El Oráculo de los Datos", "El Viaje a la Realidad Virtual", "La Ciudad de los Algoritmos", "La Guerra de los Hackers", "El Amanecer de la Realidad Aumentada", "La Red de los Sueños", "El Exilio de los Humanos", "La Revolución de los Nanobots", "El Laberinto de la Realidad Virtual", "La Era de los Drones"],
    'Thriller_Horror' : ["El susurro en la oscuridad", "El juego de la muerte", "El eco del terror", "La sombra del miedo", "El laberinto de las pesadillas", "La trampa mortal", "El secreto del abismo", "El último aliento", "La noche sin fin", "El pacto siniestro", "La casa de los susurros"],
    'Paranormal_Horror' : ["El susurro del más allá", "El misterio de las sombras eternas", "El portal de los espíritus perdidos", "La oscuridad que acecha", "El eco de los lamentos", "El secreto en la mansión embrujada", "El espectro en la noche", "El enigma de la casa abandonada", "El suspenso del más allá", "La sombra del terror", "El despertar de los muertos"],
    'Psychological_Horror' : ["La sombra en la mente", "El eco de la locura", "El laberinto de la psique", "El susurro de la oscuridad", "El reflejo siniestro", "La trampa de la cordura", "El secreto de la mente fracturada", "La pesadilla en el espejo", "El abismo de la conciencia", "El enigma de la mente retorcida", "El vértigo de la obsesión"],
    'Historical_Romance_Contemporany' : ["Susurros en el tiempo", "El suspiro del pasado", "Bajo el cielo de seda", "El latido de las estrellas", "El eco de los recuerdos", "El destino tejido en hilos", "La melodía de los corazones", "El fuego de la pasión", "El amanecer de los sueños", "El susurro de los secretos", "El encanto de lo prohibido", "Las lágrimas del ayer", "La promesa del atardecer", "El baile de las emociones", "El perfume del amor", "La sombra del pasado", "El abrazo de la nostalgia", "El reflejo de la esperanza", "El susurro de la guerra", "El latido del deseo", "El beso de la traición", "La promesa en la distancia", "La melodía del corazón", "El eco de los sueños", "El amanecer de los amantes", "El susurro del destino", "El encanto de la intriga", "El fuego de la venganza", "El latido de la libertad", "El suspiro de la pasión", "El baile de las sombras", "El perfume de la tentación", "La promesa del recuerdo", "La melodía de los amantes", "El eco de la esperanza", "El beso del perdón", "La sombra del deseo", "El abrazo del olvido", "El reflejo de la melancolía", "El susurro de la redención", "El latido de la guerra", "El encanto de lo inesperado", "El fuego de la esperanza", "El amanecer de la pasión", "El susurro de la traición", "El beso del destino", "La promesa del amor eterno", "La melodía de la nostalgia", "El eco de los secretos", "El perfume de la seducción", "La sombra del misterio", "El abrazo del deseo", "El reflejo de la soledad", "El susurro de la tentación", "El latido de la venganza", "El beso de la libertad", "El encanto de la pasión prohibida", "El fuego de la intriga", "El amanecer de los recuerdos", "El susurro de la ilusión", "El baile de los corazones rotos", "La promesa de la eternidad", "La melodía del deseo", "El eco de la esperanza perdida", "El beso de la melancolía", "La sombra del olvido", "El abrazo del destino", "El reflejo de la tentación", "El susurro de la guerra interior", "El latido de la redención", "El encanto de la pasión perdida", "El fuego de la traición", "El amanecer de la esperanza", "El susurro de la venganza", "El beso de la intriga", "La promesa del pasado", "La melodía de los sueños rotos", "El eco de la soledad", "El perfume de la pasión", "La sombra del desamor", "El abrazo del recuerdo", "El reflejo de la tristeza", "El susurro de la redención", "El latido del destino", "El encanto de lo inalcanzable", "El fuego de la ilusión", "El amanecer de los secretos", "El susurro de la esperanza", "El beso de la traición", "La promesa de la libertad", "La melodía de la melancolía", "El eco de los sueños perdidos", "El perfume del deseo", "La sombra del misterio", "El abrazo del corazón herido", "El reflejo del amor", "El susurro de la tentación prohibida", "El latido de la venganza", "El encanto del olvido", "El fuego de la pasión eterna", "El amanecer de la traición", "El susurro de la promesa rota", "El beso de la esperanza perdida", "La melodía del destino", "El eco de la intriga", "El perfume del pasado", "La sombra del deseo prohibido", "El abrazo de la soledad", "El reflejo del desamor", "El susurro del recuerdo", "El latido de la tristeza", "El encanto de la redención", "El fuego de la pasión desenfrenada", "El amanecer de la ilusión", "El susurro de los secretos ocultos", "El beso de la tentación", "La promesa de la venganza", "La melodía de la libertad", "El eco de la pasión prohibida", "El perfume de la intriga", "La sombra del pasado olvidado", "El abrazo del destino perdido", "El reflejo de la soledad eterna", "El susurro del amor perdido", "El latido de la traición", "El encanto de la esperanza rota", "El fuego de la melancolía", "El amanecer de la pasión prohibida", "El susurro del deseo oculto", "El beso de la redención", "La promesa del corazón herido", "La melodía del amor eterno", "El eco de la traición", "El perfume de la esperanza perdida", "La sombra de los secretos ocultos", "El abrazo de la tentación prohibida", "El reflejo de la venganza", "El susurro de la pasión desenfrenada", "El latido de la ilusión", "El encanto del pasado olvidado", "El fuego del destino perdido", "El amanecer de la soledad eterna", "El susurro del amor prohibido", "El beso del deseo oculto", "La promesa de la redención", "La melodía del destino perdido", "El eco de la soledad eterna", "El perfume del amor perdido", "La sombra de la traición", "El abrazo de la esperanza rota", "El reflejo de la melancolía", "El susurro de la pasión prohibida", "El latido del deseo oculto", "El encanto de la redención", "El fuego del corazón herido", "El amanecer del amor eterno", "El susurro de la traición", "El beso de la esperanza perdida", "La promesa del pasado olvidado", "La melodía del destino perdido", "El eco de la soledad eterna", "El perfume del amor prohibido", "La sombra del deseo oculto", "El abrazo de la redención", "El reflejo del corazón herido", "El susurro de la pasión desenfrenada", "El latido de la ilusión", "El encanto del destino perdido", "El fuego de la soledad eterna", "El amanecer del amor prohibido", "El susurro del deseo oculto", "El beso de la redención", "La promesa del corazón herido", "La melodía del amor eterno", "El eco de la traición", "El perfume de la esperanza perdida", "La sombra de los secretos ocultos", "El abrazo de la tentación prohibida", "El reflejo de la venganza", "El susurro de la pasión desenfrenada", "El latido de la ilusión", "El encanto del pasado olvidado", "El fuego del destino perdido", "El amanecer de la soledad eterna", "El susurro del amor prohibido", "El beso del deseo oculto", "La promesa de la redención", "La melodía del destino perdido", "El eco de la soledad eterna", "El perfume del amor perdido", "La sombra de la traición", "El abrazo de la esperanza rota", "El reflejo de la melancolía", "El susurro de la pasión prohibida", "El latido del deseo oculto", "El encanto de la redención", "El fuego del corazón herido", "El amanecer del amor eterno", "El susurro de la traición", "El beso de la esperanza perdida", "La promesa del pasado olvidado", "La melodía del destino perdido", "El eco de la soledad eterna", "El perfume del amor prohibido", "La sombra del deseo oculto", "El abrazo de la redención", "El reflejo del corazón herido"],
    'Realistic_Fiction' : ["Miradas de Cristal", "El eco de los silencios", "Entre sombras y verdades", "El latido del tiempo", "Reflejos de una vida", "El susurro de los recuerdos", "El rompecabezas del destino", "La danza de los sueños", "El refugio de los corazones rotos", "A través de tus ojos", "El laberinto de los secretos", "Las palabras que nunca dijimos", "El peso de las decisiones", "Caminos entrelazados", "El eco de la soledad", "El suspiro del viento", "Los hilos invisibles", "La melodía de los sueños", "Bajo el cielo estrellado", "El arte de ser imperfecto", "La fragilidad del alma", "El abismo de la memoria", "El faro en la tormenta", "La huella de los sueños", "El último aliento", "El rastro de las lágrimas", "Los secretos del pasado", "El despertar de la esperanza", "La sombra del olvido", "El susurro del destino", "El puente entre dos mundos", "La tristeza de las palabras", "El suspiro de la vida", "El eco de los sueños", "El susurro del pasado", "La melodía de la tristeza", "Las huellas del corazón", "El reflejo de la ausencia", "El susurro de la noche", "Los hilos del destino", "El peso de los recuerdos", "El baile de las emociones", "El eco de la melancolía", "La esencia de la vida", "El refugio de los sueños", "La promesa olvidada", "El eco de la esperanza", "El laberinto de los sueños", "Las piezas del rompecabezas", "El eco de la pasión", "Las sombras del corazón", "La melodía de la oscuridad", "El susurro del corazón", "El eco del amor", "El abismo de los secretos", "La eternidad en un suspiro", "La fragilidad de la felicidad", "El eco de la nostalgia", "El refugio de la soledad", "La melodía de la vida", "El eco del silencio", "El susurro del perdón", "El eco de la libertad", "El rastro de la felicidad", "El baile de los recuerdos", "El eco de la soledad", "El susurro del alma", "El laberinto de los secretos", "La melodía del tiempo", "El eco de la tristeza", "La sombra del destino", "El susurro del amor", "El eco de la ausencia", "Los hilos del pasado", "El peso del olvido", "El refugio de la esperanza", "La promesa olvidada", "El eco de la pasión", "El laberinto de los sueños", "Las piezas del rompecabezas", "El eco de la vida", "La melodía de la oscuridad", "El susurro del corazón", "El eco del amor", "La tristeza de los recuerdos", "El abismo de los secretos", "La eternidad en un suspiro", "La fragilidad de la felicidad", "El eco de la nostalgia", "El refugio de la soledad", "La melodía de la vida", "El eco del silencio", "El susurro del perdón", "El eco de la libertad", "El rastro de la felicidad", "El baile de los recuerdos", "El eco de la soledad", "El susurro del alma", "El laberinto de los secretos", "La melodía del tiempo", "El eco de la tristeza", "La sombra del destino", "El susurro del amor", "El eco de la ausencia", "Los hilos del pasado", "El peso del olvido", "El refugio de la esperanza", "La promesa olvidada", "El eco de la pasión", "El laberinto de los sueños", "Las piezas del rompecabezas", "El eco de la vida", "La melodía de la oscuridad", "El susurro del corazón", "El eco del amor", "La tristeza de los recuerdos", "El abismo de los secretos", "La eternidad en un suspiro", "La fragilidad de la felicidad", "El eco de la nostalgia", "El refugio de la soledad", "La melodía de la vida", "El eco del silencio", "El susurro del perdón", "El eco de la libertad", "El rastro de la felicidad", "El baile de los recuerdos", "El eco de la soledad", "El susurro del alma", "El laberinto de los secretos", "La melodía del tiempo", "El eco de la tristeza", "La sombra del destino", "El susurro del amor", "El eco de la ausencia", "Los hilos del pasado", "El peso del olvido", "El refugio de la esperanza", "La promesa olvidada", "El eco de la pasión", "El laberinto de los sueños", "Las piezas del rompecabezas", "El eco de la vida", "La melodía de la oscuridad", "El susurro del corazón", "El eco del amor"],
    'Real_Dystopia' : ["Fragmentos del Caos", "El último aliento", "Sueños rotos", "La ciudad olvidada", "Amanecer de cenizas", "El eco del silencio", "El laberinto de sombras", "El fin del mundo en tus ojos", "Máscaras de acero", "La rebelión de los susurros", "El jardín de cristal", "La ciudad de los suspiros", "El tiempo detenido", "La oscuridad eterna", "Las cenizas del paraíso", "El espejo quebrado", "El eco del vacío", "El invierno perpetuo", "La tormenta inmortal", "El abismo de la mente", "El último suspiro", "El reloj sin tiempo", "La sombra del olvido", "El lamento de las estrellas", "Las ruinas del éxodo", "El río de las almas perdidas", "La mirada del abismo", "El despertar del caos", "El susurro de la desolación", "El corazón de la oscuridad", "El eco de la destrucción", "La ciudad en ruinas", "El laberinto de los sueños rotos", "El último aliento del sol", "El reflejo perdido", "La melodía del silencio", "El fin de los días", "El susurro del tiempo", "El grito de la nada", "La ciudad de los espejos rotos", "El jardín de las sombras", "El eco de la locura", "La oscuridad que nos rodea", "El abismo de la esperanza", "El último susurro del viento", "El reloj sin fin", "El eco de la soledad", "La tormenta eterna", "El laberinto de la realidad", "El lamento de los caídos", "Las ruinas del olvido", "El río de los sueños perdidos", "La mirada del vacío", "El despertar de la destrucción", "El susurro de la desesperanza", "El corazón de las sombras", "El eco de la muerte", "La ciudad en llamas", "El laberinto de los suspiros", "El último aliento del tiempo", "El reflejo olvidado", "La melodía de la oscuridad", "El fin de todo", "El susurro de la eternidad", "El grito del vacío", "La ciudad de los espejos rotos", "El jardín de las pesadillas", "El eco de la locura", "La oscuridad que nos consume", "El abismo del olvido", "El último susurro del silencio", "El reloj sin fin", "El eco de la tristeza", "La tormenta interminable", "El laberinto de la fantasía", "El lamento de los olvidados", "Las ruinas del recuerdo", "El río de los deseos perdidos", "La mirada de la nada", "El despertar de la devastación", "El susurro de la desolación", "El corazón de la penumbra", "El eco de la muerte eterna", "La ciudad en ruinas", "El laberinto de los susurros", "El último aliento de la eternidad", "El reflejo perdido en el tiempo", "La melodía de la oscuridad eterna", "El fin de la existencia", "El susurro del infinito", "El grito del olvido", "La ciudad de los espejos rotos", "El jardín de las almas perdidas", "El eco de la locura", "La oscuridad que nos consume", "El abismo del recuerdo", "El último susurro del olvido", "El reloj sin fin", "El eco de la soledad eterna", "La tormenta sin fin", "El laberinto de la imaginación", "El lamento de los desolados", "Las ruinas del pasado", "El río de los recuerdos perdidos", "La mirada del vacío eterno", "El despertar de la destrucción total", "El susurro de la desesperación", "El corazón de la oscuridad infinita", "El eco de la muerte etérea", "La ciudad en cenizas", "El laberinto de los secretos", "El último aliento de la eternidad perdida", "El reflejo olvidado en el abismo", "La melodía de la oscuridad eterna", "El fin del universo", "El susurro del infinito oscuro", "El grito del olvido eterno", "La ciudad de las almas rotas", "El jardín de las pesadillas eternas", "El eco de la locura eterna", "La oscuridad que nos devora", "El abismo del recuerdo perdido", "El último susurro del olvido eterno", "El reloj sin fin", "El eco de la soledad infinita", "La tormenta sin fin", "El laberinto de la imaginación perdida", "El lamento de los desolados eternos", "Las ruinas del pasado olvidado", "El río de los recuerdos perdidos", "La mirada del vacío eterno", "El despertar de la destrucción total", "El susurro de la desesperación eterna", "El corazón de la oscuridad infinita", "El eco de la muerte etérea", "La ciudad en cenizas eternas", "El laberinto de los secretos olvidados", "El último aliento de la eternidad perdida", "El reflejo olvidado en el abismo del tiempo", "La melodía de la oscuridad eterna", "El fin del cosmos", "El susurro del infinito oscuro", "El grito del olvido eterno", "La ciudad de las almas rotas eternamente", "El jardín de las pesadillas eternas", "El eco de la locura eterna", "La oscuridad que nos devora eternamente", "El abismo del recuerdo perdido", "El último susurro del olvido eterno", "El reloj sin fin", "El eco de la soledad infinita", "La tormenta sin fin", "El laberinto de la imaginación perdida", "El lamento de los desolados eternos", "Las ruinas del pasado olvidado", "El río de los recuerdos perdidos eternamente", "La mirada del vacío eterno", "El despertar de la destrucción total", "El susurro de la desesperación eterna", "El corazón de la oscuridad infinita", "El eco de la muerte etérea"]
}

teenager_names = {
    'Fantasy':[
    "Cantos de Drakonia",
    "Crepúsculo Astral en Meridia",
    "Sombras de Aetherium",
    "Hechizos de Quimera Invertida",
    "Místicos Arcanos de Silmar",
    "Destellos de Vortex Sempiterno",
    "Susurros de Titanio Encantado",
    "Versos de Cristal Oscuro",
    "Sabiduría de los Cronófagos",
    "Soledad del Pegaso Herido"
],
    'Adventure':[
    "Travesía por Dunas Carmesí",
    "Huracanes del Desierto Escondido",
    "Expedición al Valle Intransitable",
    "Navegantes del Río Inverso",
    "Ascenso a la Montaña Resplandeciente",
    "Caminos en la Selva de Zafiro",
    "Rincones Ocultos de Atlántida",
    "Vuelo sobre el Cañón Profundo",
    "Descubrimiento del Oasis Espejismo",
    "Salto entre Islas Flotantes"
],
    'Romance':[
    "Besos bajo Luna de Amatista",
    "Suspiros en el Crepúsculo de Coral",
    "Amor en los Campos de Lavanda",
    "Encantos del Lago de las Perlas",
    "Corazones entre Ruinas Silenciosas",
    "Pasión en el Palacio de Nácar",
    "Serenata de Estrellas Fugaces",
    "Romance a Orillas del Río de Plata",
    "Brisa de Amor en la Costa Esmeralda",
    "Destinos Entrelazados en la Torre Iridescente"
],
    'Mystery':[
    "Sombras sobre la Mansión de Obsidiana",
    "Susurros en la Biblioteca Abandonada",
    "Ecos de un Pasado Oscuro",
    "El Reloj que Tocó Medianoche",
    "Secreto en el Jardín de los Suspiros",
    "Intriga en el Callejón sin Salida",
    "Enigma de la Habitación Sellada",
    "Retrato de una Dama Desvanecida",
    "Codex de las Puertas Entrelazadas",
    "Espejo de las Almas Perdidas"
],
    'Dystopia':[
    "Desierto de Acero y Neón",
    "Laberinto de Pantallas Silenciosas",
    "Refugio en la Ciudad de Cenizas",
    "Anarquía en el Enclave de Cristal",
    "Rebelión en la Metrópolis de Hielo",
    "Exilio en la Isla Tecnológica",
    "Rincones Oscuros de Utopía",
    "Retorno a la Zona Contaminada",
    "El Último Bosque bajo el Dome",
    "Coloso de las Tierras Yermas"
],
    'Social':[
    "Voces de la Barriada Olvidada",
    "Historias desde el Tren Subterráneo",
    "Silencio en la Plaza de Oro",
    "Luchas en la Escuela de Espejos",
    "Resistencia en el Parque de los Sueños",
    "Vidas Paralelas en la Torre de Babel",
    "Sociedad del Mosaico Roto",
    "Revolución en la Fábrica de Ideas",
    "Diario de un Vendedor de Sonrisas",
    "Mujeres en la Ciudad Invisible"
],
}

children_names = {
    'Sports':[
    "Carrera por el Valle Saltarín",
    "Fútbol en la Ciudad Regordeta",
    "Natación en la Laguna Risueña",
    "Baloncesto entre Nubes Algodonosas",
    "Béisbol en el Campo Arcoíris",
    "Patinaje sobre el Lago de Miel",
    "Golf en el Bosque Susurrante",
    "Acrobacias en la Plaza Giratoria",
    "Rugby con los Monstruos Amistosos",
    "Tenis en la Isla Deslumbrante"
],
    'Music':[
    "Melodías desde el Monte Cantarín",
    "Ritmos del Desierto Colorido",
    "Canción del Océano Sonriente",
    "Sinfonía de la Selva Luminosa",
    "Rock en el Volcán Vibrante",
    "Jazz en la Noche Estrellada",
    "Rap en la Calle del Murmullo",
    "Pop entre los Árboles Bailarines",
    "Blues en la Cueva Misteriosa",
    "Reggae en la Playa Chispeante"
],
    'Daily_life':[
    "Día de Mercado en Pueblo Feliz",
    "Recreo en la Escuela del Sol",
    "Cumpleaños en la Casa Revoloteante",
    "Paseo por el Parque Chisporroteante",
    "Desayuno en la Cocina Mágica",
    "Siesta en la Habitación Nubosa",
    "Juegos en el Jardín Secretito",
    "Estudio en la Biblioteca Voladora",
    "Cena en el Comedor Girasol",
    "Noche en la Terraza Encantada"
],
    'Adventures':[
    "Exploración del Bosque Risueño",
    "Viaje al Planeta Juguete",
    "Safari por el Zoo Fabuloso",
    "Expedición al Reino Escondido",
    "Aventura en la Ciudad de Dulces",
    "Odisea en el Mar de Burbujas",
    "Periplo por la Isla Piruleta",
    "Vuelo en el Globo Sorridente",
    "Travesía de la Montaña Saltarina",
    "Ruta por el Valle de los Dibujos"
],
    'Culture':[
    "Fiesta en la Aldea Arcoíris",
    "Tradiciones del Pueblo Caramelo",
    "Mitología de la Ciudad Sonámbula",
    "Leyendas del Barrio Aventura",
    "Costumbres del Valle Encantado",
    "Folklore de la Isla Riente",
    "Cuentos del País Mosaico",
    "Celebraciones del Desierto Florido",
    "Historias de la Región Cascabel",
    "Rituales de la Montaña Cantora"
],
    'Magic':[
    "Brujería en la Escuela Chispeante",
    "Hechizos del Jardín Susurrante",
    "Encantos de la Luna Cascarón",
    "Pócimas en la Cocina Chirriante",
    "Sortilegios del Bosque Titilante",
    "Conjuros en el Castillo Nuboso",
    "Magia en la Playa de las Estrellas",
    "Alquimia en la Cueva de Cristales",
    "Adivinación en la Torre Susurro",
    "Misterios en el Lago Resplandeciente"
]
}

baby_names = {
    'Sports':[
    "Saltitos y Carreritas",
    "Pelota Sonriente",
    "Burbujas Acuáticas Juguetonas",
    "Aros Coloreados en el Aire",
    "Estrellitas Patinadoras"
],
    'Music':[
    "Melodía de los Animalitos",
    "Canción de la Risa",
    "Tamborcito Feliz",
    "Pajaritos Cantarines",
    "Danza de las Mariposas"
],
    'Daily_life':[
    "Despertar con el Sol Brillante",
    "Hora de Comer: ¡Frutas y Risas!",
    "Jueguito de la Casa",
    "Noche de Luna y Estrellitas",
    "Baño de Burbujas Mágicas"
],
    'Adventures':[
    "Vuelo en Globo de Colores",
    "Día de Parque y Juegos",
    "La Casita en el Árbol",
    "Paseo en Trenecito Encantado",
    "Aventuras de Peluches"
],
    'Magic':[
    "Varita de Estrellitas",
    "El Espejo de las Risas",
    "El Jardín que Habla",
    "Nube Suavecita y Mágica",
    "El Sombrero que Canta"
], 
    'Culture':["Descubriendo el Mundo a Través de Colores",
                "Risas y Sonrisas de Todas las Culturas", 
                "Cuentos de la Abuela en el Mundo Entero", 
                "Bailando con los Sonidos del Mundo", 
                "Viaje Mágico por las Maravillas del Planeta"]
}

class Book:

    def __init__(
            self,
            title:str,
            isactual:bool,
            length:str,
            public:bool,
            cover:str,
            genre:str,
            author:'Author',
            rating:float,
            subgenre:str = None,
            goal:str = "",
            illustrated = 'FALSE',
            theme:str = "",
            bestseller:bool = 'FALSE',
            triggerw:List = None,

        ) -> None:

        # Features
        self.title = title # Título del libro
        self.isactual = isactual # Actual or not
        self.length = length # Longitud del libro (corto, mediano, largo, muy_largo)
        self.public = public # Público al cual va destinado
        self.cover = cover # Bolsillo, blanda, dura
        self.theme = theme # Temática (lista de temáticas)
        self.goal = goal # Objetivo (entretenimiento, aprendizaje)
        self.illustrated = illustrated # Contiene o no ilustraciones.
        self.bestseller = bestseller # Es o no un bestseller.
        self.author = author # Autor del libro
        self.triggerw = triggerw # Contiene todos los trigger warnings de este libro. 
        self.genre = genre # Géneros.
        self.subgenre = subgenre # Subgénero.
        self.rating = rating # Valoración media.
        self.punctuation = 0
        
        # Inici de característiques extres !! que no farem avui
        self.saga:str = None # Saga a la que pertenece.
        self.language:str = None # Lengua inicial del libro.
        self.difficulty:bool = None # Dificultad del libro.

    def __getattr__(self, key):
        try:
            return self.__dict[key]
        except:
            raise KeyError()
            
    def __repr__(self) -> str:
        return f'Book({self.title})' 
    
    def __eq__(self, other: object) -> bool:
        return self.dict['title'] == other.dict['title']
    
class Author:
    
    def __init__(
            self,
            name:str,
            isactual:bool,
            public:str,
            genre:str = None,
            famous:bool = False
        ) -> None:
        self.name = name
        self.isactual = isactual
        self.public = public
        self.genre = genre
        self.famous = famous
        self.books = []

    def __repr__(self) -> str:
        return f'Author({self.name})'
    
    def __eq__(self, other: 'Author') -> bool: # Similar
        return self.isactual == other.isactual and self.genre == other.genre


def isalphareal(cadena:str) -> bool:
    patron = re.compile('^[a-zA-Z]+$')
    return bool(patron.match(cadena))

def remove_accents_and_n(string):
    # Reemplazar ñ con n
    string = string.replace('ñ', 'n')
    string = string.replace('Ñ', 'N')
    
    # Eliminar acentos
    string = ''.join(
        (c for c in unicodedata.normalize('NFD', string) if unicodedata.category(c) != 'Mn')
    )
    
    return string

def createname() -> str:
    url = "https://randomuser.me/api/"
    try:
        r = True
        while r:
            response = requests.get(url)
            response.raise_for_status()  # Lanza un error si la solicitud no fue exitosa
            data = response.json()
            user = data['results'][0]
            if isalphareal(user['name']['first']) and isalphareal(user['name']['last']):
                name = user['name']['first'] + ' ' + user['name']['last']
                r = False
        return name
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")

def findauthors(
        authors, 
        public, 
        genre, 
        isactual
    ) -> List['Author']:
    subset = []
    for a in authors:
        if a.public == public and a.genre == genre and a.isactual == isactual:
            subset.append(a)
    return subset

def findauthorschildren(
        authors,
        public,
        isactual
    ):
    subset = []
    for a in authors:
        if a.public == public and a.isactual == isactual:
            subset.append(a)
    return subset

def generateData(
        public_probs:dict,
        adult_genres_probs:dict, # Clau: gènere, Valor: probabilitat
        adult_subgenres:dict, # Arbre de subgèneres d'adults invertit
        adol_genres_probs:dict,
        adult_names:dict,
        teenager_names:dict,
        children_names:dict,
        baby_names:dict,
        triggerw:dict,
        triggerw_probs_per_subgenre:dict, # Diccionari on la clau és el gènere i el valor és una llista de probabilitats.
                                      # Cada posició representa la probabilitat del triggerw X.
        genre_teen_trigg_prob:dict,
        num_authors = 100
    ) -> Tuple[pd.DataFrame]:
    num_authors = num_authors
    authors = []
    authors_object = []
    # Creem els autors
    for i in range(num_authors):
        print(f'Autor {i}')
        public = np.random.choice(list(public_probs.keys()),p=list(public_probs.values()))
        isactual = np.random.choice([True, False])
        name = createname()
        if public == 'adult':
            genre = np.random.choice(list(adult_genres_probs.keys()),p=list(adult_genres_probs.values()))
        elif public == 'teenager':
            genre = np.random.choice(list(adol_genres_probs.keys()),p=list(adol_genres_probs.values()))
        else:
            genre = None
        author = Author(name,isactual,public,genre)
        authors_object.append(author)

    print('--- Created Authors ---')

    books = []
    titles = []

    # Llibres d'adults
    for sg in list(adult_names.keys()):
        for title in adult_names[sg]:
            title = remove_accents_and_n(title)
            if title in titles:
                continue
            else:
                titles.append(title)
            name = title
            subgenre = sg
            genre = adult_subgenres[sg]
            isactual = np.random.choice(['FALSE', 'TRUE'])
            public = 'adult'
            author_options = findauthors(authors_object, public, genre, isactual)
            if author_options == []:
                author = Author(createname(),isactual,public,genre)
                authors_object.append(author)
            else:
                author = np.random.choice(author_options)
            cover = np.random.choice(['pocket', 'soft', 'hard'])
            length = np.random.choice(['short', 'medium', 'long', 'very_long'], p=[0.15,0.35,0.35,0.15])
            bestseller = np.random.choice(['TRUE', 'FALSE'],p=[0.05,0.95])
            if bestseller:
                if isinstance(author, Author):
                    author.famous = 'TRUE'
                else:
                    author['famous'] ='TRUE'
            rating = random.uniform(1,10)
            prob_tw = triggerw_probs_per_subgenre[genre][subgenre]
            tw = np.random.choice(['TRUE', 'FALSE'], p = [prob_tw, 1-prob_tw])
            if tw == 'TRUE':
                triggers = random.sample(triggerw[genre], random.randint(1,len(triggerw[genre])-1))
                trigger_warning = "{"
                for t in triggers:
                    trigger_warning += ' '
                    trigger_warning  += t
                trigger_warning += '}'
            else: 
                trigger_warning = ""
            book = Book(name, isactual, length, public, cover, genre, author, rating, subgenre=subgenre, bestseller=bestseller, triggerw=trigger_warning)
            books.append(book.__dict__)
            author.books.append(book)

    # Llibres de teenagers
    for genere in list(teenager_names.keys()):
        for title in teenager_names[genere]:
            title = remove_accents_and_n(title)
            if title in titles:
                continue
            else:
                titles.append(title)
            name = title
            genre = genere
            isactual = np.random.choice(['TRUE', 'FALSE'])
            public = 'teenager'
            author_options = findauthors(authors_object, public, genre, isactual)
            if author_options == []:
                author = Author(createname(),isactual,public,genre)
                authors_object.append(author)
            else:
                author = np.random.choice(author_options)
            cover = np.random.choice(['pocket', 'soft', 'hard'])
            length = np.random.choice(['short', 'medium', 'long', 'very_long'], p=[0.25,0.35,0.35,0.05]) # Canvi de probabilitats
            bestseller = np.random.choice(['TRUE', 'FALSE'],p=[0.05,0.95])
            if bestseller:
                if isinstance(author, Author):
                    author.famous = 'TRUE'
                else:
                    author['famous'] = 'TRUE'
            rating = random.uniform(1,10)
            prob_tw = genre_teen_trigg_prob[genre]
            tw = np.random.choice(['TRUE', 'FALSE'], p = [prob_tw, 1-prob_tw])
            if tw == 'TRUE':
                triggers = random.sample(triggerw[genre], random.randint(1,len(triggerw[genre])-1))
                trigger_warning = "{"
                for t in triggers:
                    trigger_warning += ' '
                    trigger_warning  += t
                trigger_warning += '}'
            else: 
                trigger_warning = ""
            book = Book(name, isactual, length, public, cover, genre, author, rating, subgenre=subgenre, bestseller=bestseller)
            books.append(book.__dict__)
            author.books.append(book)
    
    # Llibres de childrens
    for tematica in list(children_names.keys()):
        for title in children_names[tematica]:
            title = remove_accents_and_n(title)
            if title in titles:
                continue
            else:
                titles.append(title)
            name = title
            theme = tematica
            genre = None
            isactual = np.random.choice(['TRUE', 'FALSE'])
            public = 'children'
            author_options = findauthorschildren(authors_object, public, isactual)
            if author_options == []:
                author = Author(createname(),isactual,public)
                authors_object.append(author)
            else:
                author = np.random.choice(author_options)
            cover = 'hard'
            length = np.random.choice(['short', 'medium'], p=[0.6,0.4]) # Canvi de probabilitats
            bestseller = False
            if bestseller:
                if isinstance(author, Author):
                    author.famous = 'TRUE'
                else:
                    author['famous'] = 'TRUE'
            rating = random.uniform(1,10)
            illustrated = np.random.choice(['TRUE', 'FALSE'],p=[0.7,0.3])
            book = Book(name, isactual, length, public, cover, genre, author, rating, bestseller=bestseller, theme=theme, illustrated=illustrated)
            books.append(book.__dict__)
            author.books.append(book)

    # Llibres de babys
    for tematica in list(baby_names.keys()):
        for title in baby_names[tematica]:
            title = remove_accents_and_n(title)
            if title in titles:
                continue
            else:
                titles.append(title)
            name = title
            theme = tematica
            genre = None
            isactual = np.random.choice(['TRUE', 'FALSE'])
            public = 'baby'
            author_options = findauthorschildren(authors_object, public, isactual)
            if author_options == []:
                author = Author(createname(),isactual,public)
                authors_object.append(author)
            else:
                author = np.random.choice(author_options)
            cover = 'hard'
            length = 'short'
            bestseller = 'FALSE'
            if bestseller:
                if isinstance(author, Author):
                    author.famous = 'TRUE'
                else:
                    author['famous'] = 'TRUE'
            rating = random.uniform(1,10)
            illustrated = 'TRUE'
            goal = np.random.choice(goals)
            book = Book(name, isactual, length, public, cover, genre, author, rating, bestseller=bestseller, theme=theme, illustrated=illustrated, goal=goal)
            books.append(book.__dict__)
            author.books.append(book)

    for a in authors_object:
        if a.books != []:
            authors.append(a.__dict__)

    authorsdf = pd.DataFrame(authors)
    booksdf = pd.DataFrame(books)
    return booksdf, authorsdf

########################################
# Definitions


public_probs = {
        'baby':2.4/100,
        'children': 4.5/100,
        'teenager': 4.5/100,
        'adult': 88.6/100
    }
adult_genres_probs = {
    'Romance':0.07,
    'Historical':0.26,
    'Mystery':0.12,
    'Fantasy':0.08,
    'Sci-Fi':0.07,
    'Contemporany':0.37,
    'Horror':0.03,
}
adol_genres_probs = {
    'Fantasy':2/8,
    'Adventure':1/8,
    'Romance':2/8,
    'Mystery':1/8,
    'Dystopia':1/8,
    'Social':1/8,
}
generes = {
    "Fantasy": {"High_Fantasy", "Dark_Fantasy", "Urban_Fantasy"},
    "Romance": {"Classic_Romance", "Historical_Romance", "Erotic"},
    "Contemporary": {"Realistic_Fiction", "Historical_Romance_Contemporany", "Real_Dystopia"},
    "Mystery": {"Police", "Thriller_Mystery", "Paranormal_Mystery"},
    "Horror": {"Psychological_Horror", "Thriller_Horror", "Paranormal_Horror"},
    "Historical": {"Realistic", "Fiction_History"},
    "Science_Fiction": {"Space_Opera", "Cyberpunk", "Postapocalyptic_Dystopia", "Technological"}
}

generesinv = {}
for c,v in generes.items():
    for k in v:
        generesinv[k] = c

subgenre_trigger_warning_probabilities = {
    "Fantasy": {
        "High_Fantasy": 0,
        "Dark_Fantasy": 0,
        "Urban_Fantasy": 0
    },
    "Romance": {
        "Classic_Romance": 0.1, 
        "Historical_Romance": 0.3, 
        "Erotic": 0.7
    },
    "Contemporary": {
        "Realistic_Fiction": 0.3,
        "Historical_Romance_Contemporany": 0.3, 
        "Real_Dystopia": 0.4
    },
    "Mystery": {
        "Police": 0.5, 
        "Thriller_Mystery": 0.8, 
        "Paranormal_Mystery": 0.7 
    },
    "Horror": {
        "Psychological_Horror": 0.9, 
        "Thriller_Horror": 0.85, 
        "Paranormal_Horror": 0.8
    },
    "Historical": {
        "Realistic": 0,
        "Fiction_History": 0
    },
    "Science_Fiction": {
        "Space_Opera": 0,
        "Cyberpunk": 0.3,
        "Postapocalyptic_Dystopia": 0.4,
        "Technological": 0
    }
}

genre_teen_trigg_prob = {
'Romance': 0.4,
'Mystery': 0.2,
'Fantasy':0, 
'Adventure':0, 
'Dystopia':0, 
'Social':0
}


'''
Utilitzarem simbologia per a anomenar els trigger warnings:
'1' -> 'Abuse'
'2' ->  'Sexual assault'
'3' -> 'Nudity'
'4' -> 'Homophobia or Transphobia'
'5' -> 'Mental illness and ableism'
'6' -> 'Pornographic content'
'7' -> 'Self-harm or suicide'
'8' -> 'Eating disorders or fat phobia'
'9' -> 'Racism and racial slurs'
'10' -> 'Violence'
'11' -> 'Blood and gore'
'12' -> 'Kidnapping and abduction'
'13' -> 'Murder'
'14' -> 'Child abuse/pedophilia/incest'
'15' -> 'Animal cruelty'
'16' -> 'Torture'
'''






trigger_warnings = {
    "Fantasy": [],
    "Romance": [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6"
    ],
    "Contemporary": [
        "1",
        "5",
        "7",
        "8",
        "9",
        "2",
        "4"
    ],
    "Mystery": [
        "1",
        "10",
        "11",
        "12",
        "13",
        "14",
        "9",
        "5"
    ],
    "Horror": [
        "1",
        "10",
        "11",
        "14",
        "15",
        "5",
        "7",
        "16",
        "13",
        "2"
    ],
    "Historical": ["11","9"],
    "Science_Fiction": ["11","9"],
}


if __name__ == '__main__':
    books, authors = generateData(public_probs,adult_genres_probs,generesinv,adol_genres_probs,names_by_subgenre,teenager_names,children_names,baby_names,trigger_warnings,subgenre_trigger_warning_probabilities,genre_teen_trigg_prob,num_authors=400)
    authors.to_csv('./authors.csv')
    books.to_csv('./books.csv')

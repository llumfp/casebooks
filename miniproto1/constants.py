'''
Arxiu contenidor de les constants necessaries per al 
desenvolupament de la pràctica
'''

genrestree = {
    "Fantasy": {"High_Fantasy", "Dark_Fantasy", "Urban_Fantasy"},
    "Romance": {"Classic_Romance", "Historical_Romance", "Erotic"},
    "Contemporary": {"Realistic_Fiction", "Historical_Romance_Contemporany", "Real_Dystopia"},
    "Mystery": {"Police", "Thriller_Mystery", "Paranormal_Mystery"},
    "Horror": {"Psychological_Horror", "Thriller_Horror", "Paranormal_Horror"},
    "Historical": {"Realistic", "Fiction_History"},
    "Science_Fiction": {"Space_Opera", "Cyberpunk", "Postapocalyptic_Dystopia", "Technological"}
}

generes = ['Fantasy', 'Romance', 'Contemporary', 'Mystery', 'Horror', 'Historical', 'Science_Fiction'] 
subgenres = [s for g,sg in genrestree.items() for s in sg]

themes = ['Sports','Music','Daily_life','Adventures','Magic','Culture']
goals = ['Learning','Entretainment']
publics = ['baby','children','teen','adult']
covers = ['pocket', 'soft', 'hard']
lengths = ['short', 'medium', 'long', 'very_long']


trigger_w = [str(i+1) for i in range(17)]
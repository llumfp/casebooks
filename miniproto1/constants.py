'''
Arxiu contenidor de les constants necessaries per al 
desenvolupament de la pràctica
'''
generes_sub = {
    "Fantasy": {"High_Fantasy", "Dark_Fantasy", "Urban_Fantasy"},
    "Romance": {"Classic_Romance", "Historical_Romance", "Erotic"},
    "Contemporary": {"Realistic_Fiction", "Historical_Romance_Contemporany", "Real_Dystopia"},
    "Mystery": {"Police", "Thriller_Mystery", "Paranormal_Mystery"},
    "Horror": {"Psychological_Horror", "Thriller_Horror", "Paranormal_Horror"},
    "Historical": {"Realistic", "Fiction_History"},
    "Science_Fiction": {"Space_Opera", "Cyberpunk", "Postapocalyptic_Dystopia", "Technological"}
}

generes = list(generes_sub.keys())

trigger_w = [str(i+1) for i in range(17)]
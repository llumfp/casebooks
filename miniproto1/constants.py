genrestree = {
    "Fantasy": {"High_Fantasy", "Dark_Fantasy", "Urban_Fantasy"},
    "Romance": {"Classic_Romance", "Historical_Romance", "Erotic"},
    "Contemporary": {"Realistic_Fiction", "Historical_Romance_Contemporany", "Real_Dystopia"},
    "Mystery": {"Police", "Thriller_Mystery", "Paranormal_Mystery"},
    "Horror": {"Psychological_Horror", "Thriller_Horror", "Paranormal_Horror"},
    "Historical": {"Realistic", "Fiction_History"},
    "Science_Fiction": {"Space_Opera", "Cyberpunk", "Postapocalyptic_Dystopia", "Technological"}
}

genres = ['Fantasy', 'Romance', 'Contemporary', 'Mystery', 'Horror', 'Historical', 'Science_Fiction'] 
subgenres = [s for g,sg in genrestree.items() for s in sg]

genres_teen = ['Fantasy', 'Adventure', 'Mystery', 'Romance', 'Dystopia', 'Social']

themes = ['Sports','Music','Daily_life','Adventures','Magic','Culture']
goals = ['Learning','Entretainment']
publics = ['baby','children','teen','adult']
covers = ['pocket', 'soft', 'hard']
lengths = ['short', 'medium', 'long', 'very_long']


trigger_w = [i+1 for i in range(17)]

genre_teen_trigg_prob = {
'Romance': 0.4,
'Mystery': 0.2,
'Fantasy':0, 
'Adventure':0, 
'Dystopia':0, 
'Social':0
}

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
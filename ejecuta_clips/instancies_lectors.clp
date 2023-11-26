(definstances instances
    ([lector] of Lector
        (public "baby")
        (goal "Entretainment")
        (hab_lectura "Neutral")
        (illustrated TRUE)
        (theme "Adventures")
    )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "baby")
        (goal "Learning")
        (hab_lectura "Neutral")
        (illustrated FALSE)
        (theme "Sports")
    )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "children")
        (hab_lectura "Neutral")
        (illustrated TRUE)
        (theme "Magic")
        (time_read "long")
    )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "children")
        (hab_lectura "Neutral")
        (illustrated TRUE)
        (theme "Music")
        (time_read "short")
    )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "children")
        (hab_lectura "Neutral")
        (illustrated FALSE)
        (theme "Sports")
        (time_read "medium")
    )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "children")
        (hab_lectura "Neutral")
        (illustrated TRUE)
        (theme "Adventures")
        (time_read "short")
    )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "children")
        (hab_lectura "Neutral")
        (illustrated TRUE)
        (theme "Sports")
        (time_read "short")
    )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "teenager")
        (main_genre [Social])
        (bestseller FALSE)
        (cover "soft")
        (hab_lectura "Neutral")
        (time_read "very_long")
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "teenager")
        (main_genre [Romance])
        (bestseller TRUE)
        (cover "soft")
        (hab_lectura "Neutral")
        (time_read "very_long")        
        (triggerw 2 3 )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "teenager")
        (main_genre [Dystopia])
        (bestseller FALSE)
        (cover "hard")
        (hab_lectura "Neutral")
        (time_read "short")
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "teenager")
        (main_genre [Romance])
        (bestseller FALSE)
        (cover "hard")
        (hab_lectura "Neutral")
        (time_read "short")
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "teenager")
        (main_genre [Fantasy])
        (bestseller TRUE)
        (cover "soft")
        (hab_lectura "Neutral")
        (time_read "medium")
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "teenager")
        (main_genre [Mystery])
        (bestseller FALSE)
        (cover "pocket")
        (hab_lectura "Neutral")
        (time_read "medium")
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "teenager")
        (main_genre [Dystopia])
        (bestseller FALSE)
        (cover "soft")
        (hab_lectura "Neutral")
        (time_read "very_long")
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Romance])
        (has_subgenre [Erotic])
        (actual FALSE)
        (famous TRUE)
        (bestseller TRUE)
        (cover "pocket")
        (hab_lectura "Neutral")
        (time_read "short")        
        (triggerw 1 2 5 6 )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Romance])
        (has_subgenre [Erotic])
        (actual TRUE)
        (famous TRUE)
        (bestseller TRUE)
        (cover "soft")
        (hab_lectura "Neutral")
        (time_read "medium")        
        (triggerw 6 5 )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Fantasy])
        (has_subgenre [Urban_Fantasy])
        (actual TRUE)
        (famous TRUE)
        (bestseller FALSE)
        (cover "soft")
        (hab_lectura "Neutral")
        (time_read "long")        
        (triggerw )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Horror])
        (has_subgenre [Psychological_Horror])
        (actual FALSE)
        (famous TRUE)
        (bestseller FALSE)
        (cover "hard")
        (hab_lectura "Neutral")
        (time_read "very_long")        
        (triggerw 5 1 7 16 10 11 2 13 15 )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Horror])
        (has_subgenre [Psychological_Horror])
        (actual FALSE)
        (famous TRUE)
        (bestseller TRUE)
        (cover "hard")
        (hab_lectura "Neutral")
        (time_read "short")        
        (triggerw 7 10 )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Mystery])
        (has_subgenre [Police])
        (actual TRUE)
        (famous TRUE)
        (bestseller TRUE)
        (cover "soft")
        (hab_lectura "Neutral")
        (time_read "long")        
        (triggerw 9 1 5 10 11 )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Science_Fiction])
        (has_subgenre [Cyberpunk])
        (actual TRUE)
        (famous FALSE)
        (bestseller FALSE)
        (cover "soft")
        (hab_lectura "Neutral")
        (time_read "short")        
        (triggerw )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Horror])
        (has_subgenre [Thriller_Horror])
        (actual FALSE)
        (famous TRUE)
        (bestseller TRUE)
        (cover "soft")
        (hab_lectura "Neutral")
        (time_read "very_long")        
        (triggerw 5 11 13 14 1 )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Historical])
        (has_subgenre [Fiction_History])
        (actual FALSE)
        (famous TRUE)
        (bestseller TRUE)
        (cover "hard")
        (hab_lectura "Neutral")
        (time_read "short")        
        (triggerw )
        )) 
 
 

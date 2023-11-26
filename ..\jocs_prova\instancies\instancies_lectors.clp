(definstances instances
    ([lector] of Lector
        (public "baby")
        (goal "Entretainment")
        (hab_lectura "Neutral")
        (illustrated TRUE)
        (theme "Magic")
    )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "baby")
        (goal "Entretainment")
        (hab_lectura "Neutral")
        (illustrated FALSE)
        (theme "Magic")
    )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "children")
        (hab_lectura "Neutral")
        (illustrated TRUE)
        (theme "Magic")
        (time_read "very_long")
    )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "children")
        (hab_lectura "Neutral")
        (illustrated FALSE)
        (theme "Culture")
        (time_read "medium")
    )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "children")
        (hab_lectura "Neutral")
        (illustrated FALSE)
        (theme "Culture")
        (time_read "short")
    )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "children")
        (hab_lectura "Neutral")
        (illustrated TRUE)
        (theme "Adventures")
        (time_read "long")
    )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "children")
        (hab_lectura "Neutral")
        (illustrated FALSE)
        (theme "Sports")
        (time_read "very_long")
    )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "teenager")
        (main_genre [Adventure])
        (bestseller TRUE)
        (cover "soft")
        (hab_lectura "Neutral")
        (time_read "long")
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "teenager")
        (main_genre [Mystery])
        (bestseller TRUE)
        (cover "pocket")
        (hab_lectura "Neutral")
        (time_read "short")
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "teenager")
        (main_genre [Romance])
        (bestseller FALSE)
        (cover "pocket")
        (hab_lectura "Neutral")
        (time_read "medium")
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "teenager")
        (main_genre [Romance])
        (bestseller FALSE)
        (cover "pocket")
        (hab_lectura "Neutral")
        (time_read "short")        
        (triggerw 3 2 )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "teenager")
        (main_genre [Dystopia])
        (bestseller FALSE)
        (cover "soft")
        (hab_lectura "Neutral")
        (time_read "long")
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "teenager")
        (main_genre [Fantasy])
        (bestseller TRUE)
        (cover "pocket")
        (hab_lectura "Neutral")
        (time_read "long")
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "teenager")
        (main_genre [Dystopia])
        (bestseller TRUE)
        (cover "pocket")
        (hab_lectura "Neutral")
        (time_read "medium")
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Romance])
        (has_subgenre [Classic_Romance])
        (actual FALSE)
        (famous TRUE)
        (bestseller TRUE)
        (cover "pocket")
        (hab_lectura "Neutral")
        (time_read "short")        
        (triggerw )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Fantasy])
        (has_subgenre [High_Fantasy])
        (actual TRUE)
        (famous TRUE)
        (bestseller TRUE)
        (cover "soft")
        (hab_lectura "Neutral")
        (time_read "long")        
        (triggerw )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Historical])
        (has_subgenre [Fiction_History])
        (actual FALSE)
        (famous TRUE)
        (bestseller FALSE)
        (cover "hard")
        (hab_lectura "Neutral")
        (time_read "short")        
        (triggerw )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Contemporary])
        (has_subgenre [Real_Dystopia])
        (actual FALSE)
        (famous TRUE)
        (bestseller TRUE)
        (cover "soft")
        (hab_lectura "Neutral")
        (time_read "medium")        
        (triggerw   1 )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Horror])
        (has_subgenre [Thriller_Horror])
        (actual FALSE)
        (famous TRUE)
        (bestseller TRUE)
        (cover "pocket")
        (hab_lectura "Neutral")
        (time_read "long")        
        (triggerw   1 1   1 3   1 5   7   1 6   1   2 )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Contemporary])
        (has_subgenre [Real_Dystopia])
        (actual TRUE)
        (famous FALSE)
        (bestseller FALSE)
        (cover "hard")
        (hab_lectura "Neutral")
        (time_read "very_long")        
        (triggerw   4   8   5   7 )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Mystery])
        (has_subgenre [Police])
        (actual TRUE)
        (famous TRUE)
        (bestseller FALSE)
        (cover "hard")
        (hab_lectura "Neutral")
        (time_read "short")        
        (triggerw   1 4   5   1 0   9 )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Contemporary])
        (has_subgenre [Realistic_Fiction])
        (actual FALSE)
        (famous TRUE)
        (bestseller TRUE)
        (cover "soft")
        (hab_lectura "Neutral")
        (time_read "short")        
        (triggerw )
        )) 
 
 
(definstances instances
    ([lector] of Lector
        (public "adult")
        (main_genre [Romance])
        (has_subgenre [Classic_Romance])
        (actual FALSE)
        (famous TRUE)
        (bestseller TRUE)
        (cover "pocket")
        (hab_lectura "Neutral")
        (time_read "medium")        
        (triggerw )
        )) 
 
 

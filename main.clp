(defmodule MAIN (export ?ALL))

;;; ---------------------------------------------------------
;;; turtles/prote_GT_dos.clp
;;; Translated by owl2clips
;;; Translated to CLIPS from ontology turtles/prote_GT_dos.ttl
;;; :Date 20/10/2023 22:52:21

(defclass Ficcion
    (is-a USER)
    (role concrete)
    (pattern-match reactive)
)

(defclass Genero
    (is-a Ficcion)
    (role concrete)
    (pattern-match reactive)
    (slot name_genre
        (type STRING)
        (create-accessor read-write))
)

(defclass Subgenero
    (is-a Genero)
    (role concrete)
    (pattern-match reactive)
    (slot subgenre_of
        (type INSTANCE)
        (create-accessor read-write))
)

(defclass Persona
    (is-a USER)
    (role concrete)
    (pattern-match reactive)
)

(defclass Autor
    (is-a Persona)
    (role concrete)
    (pattern-match reactive)
    (multislot author_of
        (type INSTANCE)
        (create-accessor read-write))
    (slot main_genre
        (type INSTANCE)
        (create-accessor read-write))
    (slot actual
        (type SYMBOL)
        (create-accessor read-write))
    (slot famous
        (type SYMBOL)
        (create-accessor read-write))
    (slot name_author
        (type STRING)
        (create-accessor read-write))
    (slot public
        (type STRING)
        (create-accessor read-write))
)

(defclass Lector
    (is-a Persona)
    (role concrete)
    (pattern-match reactive)
    (slot fav_author
        (type INSTANCE)
        (create-accessor read-write))
    (slot has_subgenre
        (type INSTANCE)
        (create-accessor read-write))
    (slot main_genre
        (type INSTANCE)
        (create-accessor read-write))
    (slot actual
        (type SYMBOL)
        (create-accessor read-write))
    (slot bestseller
        (type SYMBOL)
        (create-accessor read-write))
    (slot cover
        (type STRING)
        (create-accessor read-write))
    (slot famous
        (type SYMBOL)
        (create-accessor read-write))
    (slot goal
        (type STRING)
        (create-accessor read-write))
    (slot hab_lectura
        (type SYMBOL)
        (create-accessor read-write))
    (slot illustrated
        (type SYMBOL)
        (create-accessor read-write))
    (slot language
        (type STRING)
        (create-accessor read-write))
    (slot public
        (type STRING)
        (create-accessor read-write))
    (slot saga
        (type STRING)
        (create-accessor read-write))
    (slot theme
        (type STRING)
        (create-accessor read-write))
    (slot time_read
        (type STRING)
        (create-accessor read-write))
    (multislot triggerw
        (type STRING)
        (create-accessor read-write))
)

(defclass Libro
    (is-a USER)
    (role concrete)
    (pattern-match reactive)
    (slot has_subgenre
        (type INSTANCE)
        (create-accessor read-write))
    (slot main_genre
        (type INSTANCE)
        (create-accessor read-write))
    (slot actual
        (type SYMBOL)
        (create-accessor read-write))
    (slot bestseller
        (type SYMBOL)
        (create-accessor read-write))
    (slot cover
        (type STRING)
        (create-accessor read-write))
    (slot difficulty
        (type STRING)
        (create-accessor read-write))
    (slot goal
        (type STRING)
        (create-accessor read-write))
    (slot illustrated
        (type SYMBOL)
        (create-accessor read-write))
    (slot language
        (type STRING)
        (create-accessor read-write))
    (slot length
        (type STRING)
        (create-accessor read-write))
    (slot public
        (type STRING)
        (create-accessor read-write))
    (slot punctuation
        (type INTEGER)
        (create-accessor read-write))
    (slot rating
        (type FLOAT)
        (create-accessor read-write))
    (slot saga
        (type STRING)
        (create-accessor read-write))
    (slot theme
        (type STRING)
        (create-accessor read-write))
    (slot title
        (type STRING)
        (create-accessor read-write))
    (multislot triggerw
        (type STRING)
        (create-accessor read-write))
)

(definstances instances
    ([Adventure] of Genero
         (name_genre  "Adventure")
    )

    ([Classic_Romance] of Subgenero
         (subgenre_of  [Romance])
         (name_genre  "Classic_Romance")
    )

    ([Contemporary] of Genero
         (name_genre  "Contemporary")
    )

    ([Cyberpunk] of Subgenero
         (subgenre_of  [Science_Fiction])
         (name_genre  "Cyberpunk")
    )

    ([Dark_Fantasy] of Subgenero
         (subgenre_of  [Fantasy])
         (name_genre  "Dark_Fantasy")
    )

    ([Dystopia] of Genero
         (name_genre  "Dystopia")
    )

    ([Erotic] of Subgenero
         (subgenre_of  [Romance])
         (name_genre  "Erotic")
    )

    ([Fantasy] of Genero
         (name_genre  "Fantasy")
    )

    ([Fiction_History] of Subgenero
         (subgenre_of  [Historical])
         (name_genre  "Fiction_History")
    )

    ([Global] of Genero
        (name_genre "Global")
    )

    ([High_Fantasy] of Subgenero
         (subgenre_of  [Fantasy])
         (name_genre  "High_Fantasy")
    )

    ([Historical] of Genero
         (name_genre  "Historical")
    )

    ([Historical_Romance] of Subgenero
         (subgenre_of  [Romance])
         (name_genre  "Historical_Romance")
    )

    ([Historical_Romance_Contemporary] of Subgenero
         (subgenre_of  [Contemporary])
         (name_genre  "Historical_Romance_Contemporary")
    )

    ([Horror] of Genero
         (name_genre  "Horror")
    )

    ([Mystery] of Genero
         (name_genre  "Mystery")
    )

    ([Paranormal_Horror] of Subgenero
         (subgenre_of  [Horror])
         (name_genre  "Paranormal_Horror")
    )

    ([Paranormal_Mystery] of Subgenero
         (subgenre_of  [Mystery])
         (name_genre  "Paranormal_Mystery")
    )

    ([Police] of Subgenero
         (subgenre_of  [Mystery])
         (name_genre  "Police")
    )

    ([Postapocalyptic_Dystopia] of Subgenero
         (subgenre_of  [Science_Fiction])
         (name_genre  "Postapocalyptic_Dystopia")
    )

    ([Psychological_Horror] of Subgenero
         (subgenre_of  [Horror])
         (name_genre  "Psychological_Horror")
    )

    ([Real_Dystopia] of Subgenero
         (subgenre_of  [Contemporary])
         (name_genre  "Real_Dystopia")
    )

    ([Realistic] of Subgenero
         (subgenre_of  [Historical])
         (name_genre  "Realistic")
    )

    ([Realistic_Fiction] of Subgenero
         (subgenre_of  [Contemporary])
         (name_genre  "Realistic_Fiction")
    )

    ([Romance] of Genero
         (name_genre  "Romance")
    )

    ([Science_Fiction] of Genero
         (name_genre  "Science_Fiction")
    )

    ([Social] of Genero
         (name_genre  "Social")
    )

    ([Space_Opera] of Subgenero
         (subgenre_of  [Science_Fiction])
         (name_genre  "Space_Opera")
    )

    ([Technological] of Subgenero
         (subgenre_of  [Science_Fiction])
         (name_genre  "Technological")
    )

    ([Thriller_Horror] of Subgenero
         (subgenre_of  [Horror])
         (name_genre  "Thriller_Horror")
    )

    ([Thriller_Mystery] of Subgenero
         (subgenre_of  [Mystery])
         (name_genre  "Thriller_Mystery")
    )

    ([Urban_Fantasy] of Subgenero
         (subgenre_of  [Fantasy])
         (name_genre  "Urban_Fantasy")
    )

)

;;****************
;;* DEFFUNCTIONS *
;;****************

(deffunction MAIN::ask-question (?question $?allowed-values)
   (print ?question)
   (bind ?answer (read))
   (while (not (member$ ?answer ?allowed-values)) do
      (print ?question)
      (bind ?answer (read)))
   (return (str-cat ?answer)))



(deffunction MAIN::yes-or-no-p (?question)
   (bind ?response (ask-question ?question yes no y n YES NO Yes No -))
   (if (eq ?response "-")
        then ?response
    else
    (if (or (eq ?response "Yes") (eq ?response "yes") (eq ?response "y") (eq ?response "YES"))
       then (return TRUE) 
       else (return FALSE))
       )
    )

(deffunction MAIN::multi-select-p (?question $?allowed-values)
    (bind ?invalid TRUE)
    (bind ?allowed-values (insert$ ?allowed-values (+ 1 (length$ ?allowed-values)) -)) 
    (while ?invalid do
        (print ?question)
        (bind ?input (readline))
        (bind ?answer (create$))
        (bind ?input-list (explode$ ?input))
        (bind ?invalid FALSE)

        (foreach ?item ?input-list
            (if (not (member$ ?item ?allowed-values))
                then
                (printout t ?item " no es una opcion valida." crlf)
                (bind ?invalid TRUE)
            ))
        (if (not ?invalid)
            then
            (bind ?answer (create$)
            (foreach ?item ?input-list
                (if (and(member$ ?item ?allowed-values)(neq ?item "-"))
                    then
                    (bind ?answer (insert$ ?answer (+ 1 (length$ ?answer)) ?item))
                )
            ))
        )
    )
    (return ?answer)
)

(deffunction MAIN::countInstances (?clase)
    (bind ?num-instances (length$ (find-all-instances ((?i ?clase)) TRUE)))
    (return ?num-instances)
)

;;*******************
;;* MoDUL PRINCIPAL *
;;*******************

(defrule MAIN::benvinguda
    (declare (salience 2))
    =>
    (printout t "
--------------------------------------------------
  _________   _________
 /          |/         |    Recomanador de Llibres
||          |          ||   
||          |          ||   Practica 1 - SBC
||          |          ||
||          |          ||   By:
|| ________ | ________ ||     Artur A A
||/         |/        |||     Llum F P
                             Paula G S
                             Oscar M S

--------------------------------------------------
                   BENVINGUT!

Li farem diverses preguntes i el nostre sistema
recomanador li oferira els llibres que mes s'adap-
ten a les seves preferencies.

--------------------------------------------------
    ")
)

(defrule MAIN::init
    (declare (salience 1))
    =>
    (focus INPUT)
)

(defrule MAIN::end
    =>
    (focus SOLUTION)
)


;;*******************
;;*   MODUL FINAL   *
;;*******************

(defmodule SOLUTION
    (import MAIN ?ALL)
)

(defrule SOLUTION::endMessage
    (declare (salience -1))
    =>
    (printout t "
Gracies per haver respost les preguntes!

Els llibres seleccionats son els seguents:
" crlf)
(focus PUNCTUATION)
)

(defrule SOLUTION::justifica 
    (declare (salience -2))
   =>
   (focus JUSTIFY)
)

;;*******************
;;*   MODUL JUSTIFY *
;;*******************

(defmodule JUSTIFY
    (import MAIN ?ALL)
)

(deffunction JUSTIFY::getRecommendationRange (?lectorType ?puntuacio)
    (if (eq ?lectorType "baby")
        then 
        (if (>= ?puntuacio 50)
            then (return "ideal")
            else (if (and (>= ?puntuacio 40) (< ?puntuacio 50))
                then (return "good")
                else (return "bad")))

    else if (eq ?lectorType "children")
        then
        (if (>= ?puntuacio 45)
            then (return "ideal")
            else (if (and (>= ?puntuacio 20) (< ?puntuacio 45))
                then (return "good")
                else (return "bad")))
    else if (eq ?lectorType "teen")
        then
        (if (>= ?puntuacio 55)
            then (return "ideal")
            else (if (and (>= ?puntuacio 20) (< ?puntuacio 55))
                then (return "good")
                else (return "bad")))
    else if (eq ?lectorType "adult")
        then
        (if (>= ?puntuacio 85)
            then (return "ideal")
            else (if (and (>= ?puntuacio 20) (< ?puntuacio 85))
                then (return "good")
                else (return "bad")))
    )
)

(deffunction JUSTIFY::printRecom (?type)
    (switch ?type
        (case "ideal" then (printout t "Que be! Aquest llibre es exactament el que estaves buscant:" crlf))
        (case "good" then (printout t "Aquest llibre pot ser una bona opcio:" crlf))
        (default (printout t "Hmm... Mira veure si t'agrada aquest:" crlf))
    )
)

(deffunction JUSTIFY::showProperties (?book ?lector)
    (printout t "--------------- LLIBRE ---------------"crlf)
    (bind ?recommendation (getRecommendationRange (send ?lector get-public) (send ?book get-punctuation)))
    (printRecom ?recommendation)
    (printout t "Title: " (send ?book get-title) " | Puntuacio: " (send ?book get-punctuation) crlf)
)

(deffunction JUSTIFY::compareBooks (?b1 ?b2)
    (bind ?rating1 (send ?b1 get-punctuation))
    (bind ?rating2 (send ?b2 get-punctuation))
    (if (and (numberp ?rating1) (numberp ?rating2))
        then
        (if (< ?rating1 ?rating2) then (return TRUE) else (return FALSE))
        else
        (printout t "Error de Comparacion entre Puntuaciones" crlf)
        (return FALSE)
    )
)

(deffunction JUSTIFY::bestbooks (?N)
    (bind ?libros (find-all-instances ((?l Libro)) TRUE))
    (bind ?sorted-libros (sort compareBooks ?libros))
    (bind ?count 0)
    (bind ?chosen_books (create$))
    (foreach ?book ?sorted-libros
        (if (< ?count ?N) then
            (bind ?count (+ ?count 1))
            (bind ?chosen_books (insert$ ?chosen_books (+ (length$ ?chosen_books) 1) ?book))

        )
    )
    return ?chosen_books
)

(deffunction JUSTIFY::tematica (?theme)
    (switch ?theme
        (case "Sports" then (printout t "Aquest llibre et portara al mon emocionant dels esports, perfecte per als petits atletes com tu." crlf) )
        (case "Music" then (printout t "Amb aquesta historia, els sons i melodies cobren vida, ideal per als petits musics amb un cor ple de ritme com tu." crlf) )
        (case "Daily_life" then (printout t "Aquest llibre reflecteix les petites aventures i descobertes de la vida quotidiana." crlf) )
        (case "Adventures" then (printout t "Amb aquest llibre, els petits llegiran sobre emocionants viatges i desafiaments, ideal per als nens amb un esperit aventurer com el teu." crlf) )
        (case "Culture" then (printout t "Aquest llibre ofereix un viatge per diferents cultures i tradicions, perfecte per als petits curiosos com tu." crlf) )
        (case "Magic" then (printout t "En aquesta historia, la magia i l'encantament son els protagonistes, ideal per als nens que volen somiadors i creatius com tu." crlf) )
    )
)

(deffunction JUSTIFY::genre (?name_genre)
    (switch ?name_genre
        (case "Contemporary" then (printout t "Aquest llibre reflecteix el mon actual i les seves complexitats, perfecte ja que vols un llibre contemporani" crlf) )
        (case "Historical" then (printout t "Amb aquest llibre seras transportat a epoques passades, perfecte per a aquells que volen reviure la historia." crlf))
        (case "Mystery" then (printout t "Amb aquest llibre estaras intrigat fins al final ja que ens has demanat un llibre de misteri"crlf) )
        (case "Fantasy" then (printout t "Aquest llibre et portara a mons magics i terres desconegudes, ideal per a tu, un somiador apassionat per la fantasia."crlf) )
        (case "Romance" then (printout t "Aquest es un llibre romantic perque puguis viure un gran amor." crlf) )
        (case "Science_Fiction" then (printout t "Aquest es un llibre et permetra explorar els limits del possible i l'imaginable ja que volies ciencia ficcio." crlf) )
        (case "Horror" then (printout t "Prepara't per sentir la pell de gallina amb aquesta historia d'horror que et mantindra en vela tota la nit. Volies Terror? Doncs el tindras!" crlf) )
        (case "Adventure" then (printout t "Amb aquest llibre, viuras emocionants aventures i descobertes, perfecte per a aquells amb un esperit intrepid com tu." crlf) )
        (case "Dystopia" then (printout t "Aquest llibre et mostrara un futur sombri i pertorbador, veient realitats futures en un mon distopic, tal i com has demanat." crlf) )
        (case "Social" then (printout t "Aquest es un llibre esta ambientat en un entorn del dia a dia i reflexe alguns temes socials tal i com has demanat." crlf) )
    )
)


(defrule JUSTIFY::justify
    ?lector <- (object (is-a Lector)
                    (actual ?isactual)
                    (bestseller ?isbestseller)
                    (cover ?coverType)
                    (goal ?mainGoal)
                    (illustrated ?isIllustrated)
                    (time_read ?timeread)
                    (theme ?mainTheme)
                    (public ?public)
                    (main_genre ?genereMain)
                    (has_subgenre ?subgenere))
    =>
    (bind ?llibres_finals (bestbooks 3))
    (foreach ?book ?llibres_finals
        (showProperties ?book ?lector)
        ;actual
        (if (and (neq ?isactual nil)(eq ?isactual (send ?book get-actual))) 
            then (if (eq ?isactual TRUE) then (printout t "Aquest llibre es actual tal i com has demanat." crlf)
                    else (printout t "Aquest llibre ha estat escrit per un gran autor classic, tal i com has demanat." crlf) )
        )
        ;bestseller
        (if (and (neq ?isbestseller nil)(eq ?isbestseller (send ?book get-bestseller))) 
            then (if (eq ?isbestseller TRUE) then (printout t "Aquest llibre es un bestseller tal i com has demanat." crlf))
        )
        ;cover
        (if (and (and (neq ?coverType "")(eq ?coverType (send ?book get-cover))) (and (neq ?public "child")(neq ?public "baby"))) 
            then (switch ?coverType 
                    (case "hard" then (printout t "Hem trobat un llibre de tapa dura tal i com volies." crlf))
                    (case "soft" then (printout t "Hem trobat un llibre amb tapa fina tal i com volies." crlf))
                    (default (printout t "Hem trobat un llibre de butxaca perque el puguis portar a qualsevol lloc! Tal com volies." crlf))
                 )
        )
        ;goal
        (if (and (neq ?mainGoal "")(eq ?mainGoal (send ?book get-goal)) )
            then (if (eq ?mainGoal "Entretainment") then (printout t "Segur que amb aquest llibre passes una bona estona entretenint-te amb la lectura!" crlf)
                  else (printout t "Segur que si llegeixes aquest llibre aprens moltes coses interessants!" crlf))
        )
        ;illustrated
        (if (and (neq ?isIllustrated nil)(and (eq ?isIllustrated (send ?book get-illustrated))(eq ?public "children")))
            then (if (eq ?isbestseller TRUE) then (printout t "Aquest llibre conte dibuixos i ilustracions, tal i com has demanat." crlf)
                    else (printout t "Aquest llibre no conte dibuixos, nomes text, tal i com has demanat." crlf) )
        )
        ;theme
        (if (and (neq ?mainTheme "")(eq ?mainTheme (send ?book get-theme)) )
            then (tematica ?mainTheme)
        )
        ;genre
        (bind ?g (send ?book get-main_genre))
        (if (neq ?genereMain [nil])
            then
            (bind ?g_name (send ?g get-name_genre))
            (bind ?gen_name (send ?genereMain get-name_genre))
            (if (eq ?g_name ?gen_name)
                then (genre ?g_name) 
            )
        )
        ;subgenre
        (bind ?s (send ?book get-has_subgenre))
        (if (neq ?subgenere [nil])
        then
            (bind ?s_name (send ?s get-name_genre))
            (bind ?sub_name (send ?subgenere get-name_genre))

            (if (eq ?s_name ?sub_name)
                then (printout t "Com havies demanat, el llibre es del subgenere " ?s_name crlf)
            )
        )
        
        (printout t crlf)
    )
)


;;***********************
;;* MODUL PUNCTUATION   *
;;***********************
; Calcula les puntuacions de cada llibre

(defmodule PUNCTUATION
    (import MAIN ?ALL) 
)

(defrule PUNCTUATION::theme_punctuation
    ?lector <- (object (is-a Lector)(theme ?t&~""))
    =>
    (bind ?llibres (find-all-instances ((?l Libro)) (eq ?l:theme ?t)))
    (progn$ (?l ?llibres) 
    (bind ?p (send ?l get-punctuation))
    (bind ?p (+ ?p 10))
    (send ?l put-punctuation ?p))  
)

(defrule PUNCTUATION::goal_punctuation
    ?lector <- (object (is-a Lector)(goal ?g&~""))
    =>
    (bind ?llibres (find-all-instances ((?l Libro)) (eq ?l:goal ?g))) 
    (progn$ (?l ?llibres) 
    (bind ?p (send ?l get-punctuation))
    (bind ?p (+ ?p 10))
    (send ?l put-punctuation ?p))
)

(defrule PUNCTUATION::ilustrated_punctuation
    ?lector <- (object (is-a Lector)(illustrated ?i&~nil))
    =>
    (bind ?llibres (find-all-instances ((?l Libro)) (eq ?l:illustrated ?i) ))
    (progn$ (?l ?llibres) 
    (bind ?p (send ?l get-punctuation))
    (bind ?p (+ ?p 10))
    (send ?l put-punctuation ?p))  
)

(defrule PUNCTUATION::length_punctuation
    ?lector <- (object (is-a Lector)(time_read ?tr&~""))
    =>
    (bind ?llibres (find-all-instances ((?l Libro)) (eq ?l:length ?tr)))  
    (progn$ (?l ?llibres) 
    (bind ?p (send ?l get-punctuation))
    (bind ?p (+ ?p 10))
    (send ?l put-punctuation ?p))  
)

(defrule PUNCTUATION::cover_punctuation
    ?lector <- (object (is-a Lector)(cover ?c&~""))
    =>
    (bind ?llibres (find-all-instances ((?l Libro)) (eq ?l:cover ?c)))
    (progn$ (?l ?llibres) 
    (bind ?p (send ?l get-punctuation))
    (bind ?p (+ ?p 10))
    (send ?l put-punctuation ?p))  
)

(defrule PUNCTUATION::generes_punctuation
    ?lector <- (object (is-a Lector)(main_genre ?m&~[nil]))
    (test (neq ?m [Global]))
    =>
    (bind ?llibres (find-all-instances ((?l Libro)) (eq ?l:main_genre ?m)))  
    (progn$ (?l ?llibres) 
    (bind ?p (send ?l get-punctuation))
    (bind ?p (+ ?p 10))
    (send ?l put-punctuation ?p))  
)

(defrule PUNCTUATION::bestseller_punctuation
    ?lector <- (object (is-a Lector)(bestseller ?m&~nil))
    =>
    (bind ?llibres (find-all-instances ((?l Libro)) (eq ?l:bestseller ?m)))  

    (progn$ (?l ?llibres) 
    (bind ?p (send ?l get-punctuation))
    (bind ?p (+ ?p 10))
    (send ?l put-punctuation ?p))  
)

(defrule PUNCTUATION::famous_punctuation
    ?lector <- (object (is-a Lector)(public ?public)(famous ?f&~nil))
    =>
    (bind ?autors (find-all-instances ((?a Autor)) (and (eq ?a:famous ?f) (eq ?a:public ?public))))
    (progn$ (?a ?autors)
        (bind ?books (send ?a get-author_of))
        (progn$ (?llibre ?books)
            (bind ?p (send ?llibre get-punctuation))
            (bind ?p (+ ?p 10))
            (send ?llibre put-punctuation ?p))
    )        
)

(defrule PUNCTUATION::actual_punctuation
    ?lector <- (object (is-a Lector)(actual ?act&~nil))
    =>
    (bind ?llibres (find-all-instances ((?l Libro)) (eq ?l:actual ?act)))  
    (progn$ (?l ?llibres) 
    (bind ?p (send ?l get-punctuation))
    (bind ?p (+ ?p 10))
    (send ?l put-punctuation ?p))  
)

(defrule PUNCTUATION::subgenre_punctuation
    ?lector <- (object (is-a Lector)(has_subgenre ?sg&~[nil]))
    =>
    (bind ?llibres (find-all-instances ((?l Libro)) (eq ?l:has_subgenre ?sg)))  
    (progn$ (?l ?llibres) 
    (bind ?p (send ?l get-punctuation))
    (bind ?p (+ ?p 10))
    (send ?l put-punctuation ?p))  
)


;;*******************
;;*   MODUL INPUT   *
;;*******************

(defmodule INPUT
    (import MAIN ?ALL)
    (export deffunction basicQ basicQskip)
)

(deffunction INPUT::basicQ (?question ?options)
    (bind ?response (ask-question ?question ?options))
    (return ?response)
)

(deffunction INPUT::basicQskip (?question ?options)
    (bind ?options (insert$ ?options (+ (length$ ?options) 1) -))
    (bind ?response (ask-question ?question ?options))
    (return ?response)
)

(defrule INPUT::basicInput
    (declare (salience 1))
    =>
    (focus BASE)
)

(defrule INPUT::cridaPublic
    ?lector <- (object (is-a Lector) (public ?p&~""))
    =>
    (switch ?p
        (case "baby" then (focus BABY))
        (case "children" then (focus CHILD))
        (case "teenager" then (focus TEEN))
        (default (focus ADULT))
    )
)

;;*******************
;;*   MODUL  BASE   *
;;*******************
; Modul per a les preguntes basiques

(defmodule BASE
    (import MAIN ?ALL)
    (import INPUT ?ALL)
)

(defrule BASE::askPublic 
    (declare (salience 1))
    ?lector <- (object (is-a Lector) (public ""))
    =>
    (bind ?options baby children teenager adult)
    (bind ?public (basicQ "
A quin grup d'edat pertanys? 
    Si tens entre 4 i 6 anys tria l'opcio 'baby'
    Si tens entre 7 i 14 anys tria l'opcio 'children'
    Si tens entre 15 i 18 anys tria l'opcio 'teenager'
    Si tens mes de 18 anys tria l'opcio 'adult'

>>> " ?options))
    (send ?lector put-public ?public)
    (printout t "
Perfecte! Anem a per la proxima pregunta:" crlf)
)

(defrule BASE::askHabit
    ?lector <- (object (is-a Lector) (hab_lectura nil))
    =>
    (bind ?hab_lectura (yes-or-no-p "
Tens habit de lectura? Es a dir, acostumes a llegir en els teus temps lliures, quan vas de viatge... de manera coninuada?
    Respon 'Yes' o 'No'.

>>> "))
    (send ?lector put-hab_lectura ?hab_lectura)
    (if (eq ?hab_lectura TRUE) then
    (printout t "
Ens encanta que siguis un aficionat a la lectura!" crlf)
    else (printout t "
Segur que el llibres que et recomanem t'enganxaran a la lectura!"))
    (focus ACT)
)

;;*******************
;;* MODUL   BABYS   *
;;*******************

(defmodule BABY 
    (import MAIN ?ALL)
    (import INPUT deffunction basicQ basicQskip)
)

(defrule BABY::atributs
   ?lector <- (object (is-a Lector))  
    =>
    (send ?lector put-illustrated TRUE)
    (send ?lector put-cover "hard")
    (send ?lector put-time_read "short"))

(defrule BABY::tematica 
    (declare (salience 2))
    ?lector <- (object (is-a Lector) (theme ""))
    =>
    (bind ?options Sports Music Adventures Culture Magic Daily_life)
    (bind ?theme (basicQskip "
De quina tematica t'agradaria que fos el llibre? 
    Si t'agradaria que el teu llibre fos relacionat amb els esports tria l'opcio 'Sports'
    Si t'agradaria que el teu llibre fos relacionat amb les cancons i la musica tria l'opcio 'Music'
    Si t'agradaria que el teu llibre expliques histories emocionants tria l'opcio 'Adventures'
    Si t'agradaria que el teu llibre fos relacionat amb com es el mon tria l'opcio 'Culture'
    Si t'agradaria que el teu llibre fos relacionat amb la magia tria l'opcio 'Magic'
    Si t'agradaria que el teu llibre expliques fets del dia a dia tria l'opcio 'Daily_life'

Si vols saltar-te aquesta pregunta, escriu '-'.

>>> " ?options))
    (if (eq ?theme "-")
        then 
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Tingues en compte que quantes mes preguntes responguis mes afinarem en la recomanacio
                        " crlf)
    else
        (send ?lector put-theme ?theme)
        (printout t "
Tema assignat correctament, tens molt bon gust!" crlf)
    )

)

(defrule BABY::goal 
    (declare (salience 1))
    ?lector <- (object (is-a Lector) (goal "")) 
    =>
    (bind ?options Learning Entretainment)
    (bind ?goal (basicQskip "
Quina es la finalitat d'aquest llibre? 
    Si vols el llibre per aprendre sobre qualsevol tematica tria l'opcio 'Learning'
    Si vols el llibre per passar una bona estona tria l'opcio 'Entretainment'
Si vols saltar-te aquesta pregunta, escriu '-'.

>>> " ?options))
    (if (eq ?goal "-") then
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Tingues en compte que quantes mes preguntes responguis mes afinarem en la recomanacio
" crlf)
    else
        (send ?lector put-goal ?goal)
        (printout t "
Tindrem en compte la finalitat que busques!" crlf)
    )
)

;;*******************
;;* MODUL   CHILD   *
;;*******************
(defmodule CHILD 
    (import MAIN ?ALL)
    (import INPUT deffunction basicQ basicQskip)
)

(defrule CHILD::atributs
   ?lector <- (object (is-a Lector))  
    =>
    (send ?lector put-cover "hard"))


(defrule CHILD::tema_preferit
    (declare (salience 2))
    ?lector <- (object (is-a Lector) (theme ""))
    => 
    (bind ?options Sports Music Daily_life Adventures Culture Magic Sport)
    (bind ?theme (basicQskip "
Quines son les teves aficions? 
    Si t'agrada l'esport i les activitats fisiques, selecciona 'Sports'.
    Si ets un amant de la musica i els concerts, selecciona 'Music'.
    Si prefereixes les histories sobre la vida quotidiana, selecciona 'Daily_life'.
    Si t'agrada explorar i viure aventures, selecciona 'Adventures'.
    Si t'estimes la cultura i l'art, selecciona 'Culture'.
    Si t'agrada la magia i el mon del fantastic, selecciona 'Magic'.
Si vols saltar-te aquesta pregunta, escriu '-'.

>>> " ?options))

    (if (eq ?theme "-")
        then 
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Tingues en compte que quantes mes preguntes responguis mes afinarem en la recomanacio
" crlf)
    else
        (send ?lector put-theme ?theme)
        (printout t "
Molt bon tema! Tenim llibres molt interessants d'aquesta categoria" crlf)
   
    )
)

(defrule CHILD::llibre_illustrat
    (declare (salience 1))
    ?lector <- (object (is-a Lector) (illustrated nil))
    =>
    (bind ?illustrated (yes-or-no-p "
Busques un llibre amb illustracions?
    Respon 'Yes' si desitges un llibre amb illustracions, o 'No' si prefereixes un llibre sense illustracions.
Si vols saltar-te aquesta pregunta, escriu '-'.

>>> "))

    (if (eq ?illustrated "-")
        then 
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Tingues en compte que quantes mes preguntes responguis mes afinarem en la recomanacio
" crlf)
    else
        (send ?lector put-illustrated ?illustrated)
        (if (eq ?illustrated TRUE) then (printout t "
Perfecte! Tenim llibres amb ilustracions molt boniques." crlf crlf)
            else (printout t "
Llibres sense ilustracions! Es nota que comences a ferte gran..." crlf crlf))
    )
)

(defrule CHILD::longitud
    ?lector <- (object (is-a Lector) (time_read ""))
    => 
    (bind ?options short medium)
    (bind ?time_read (basicQskip "
Quant temps tens per llegir? 
    Si disposes de poc temps i desitges llibres curts, selecciona 'short'.
    Si tens bastant temps per llegir, selecciona 'medium'.
Si vols saltar-te aquesta pregunta, escriu '-'.

>>> " ?options))
    (if (eq ?time_read "-")
        then 
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Tingues en compte que quantes mes preguntes responguis mes afinarem en la recomanacio
" crlf)
    else 
        (send ?lector put-time_read ?time_read)
        (printout t "
Perfecte!" crlf)
    )
)


;;*******************
;;*  MODUL  TEEN    *
;;*******************

(defmodule TEEN 
    (import MAIN ?ALL)
    (import INPUT deffunction basicQ basicQskip)
)

(defrule TEEN::atributs
   ?lector <- (object (is-a Lector))  
    =>
    (send ?lector put-illustrated FALSE))

(defrule TEEN::genere_teen
    (declare (salience 3))
    ?lector <- (object (is-a Lector) (main_genre [nil]))
    => 
    (bind ?options Fantasy Adventure Romance Mystery Dystopia Social)
    (bind ?genre (basicQskip "
Quin genere de llibre estas buscant? 
    Si t'agradaria que el teu llibre fos d'aventures 'Adventure'
    Si t'agradaria que el teu llibre fos  de magia i fantasia tria l'opcio 'Fantasy'
    Si t'agradaria que el teu llibre fos sobre una historia d'amor tria l'opcio 'Romance'
    Si t'agradaria que el teu llibre fos sobre un misteri a resoldre tria l'opcio 'Mystery'
    Si t'agradaria que el teu llibre fos sobre un mon que ha canviat a una situacio nova i distopica tria l'opcio 'Dystopia'
    Si t'agradaria que el teu llibre expliques fets del dia a dia amb temes socials tria l'opcio 'Social'
Si vols saltar-te aquesta pregunta, escriu '-'.

>>> " ?options))
    (if (eq ?genre "-") 
        then
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Tingues en compte que quantes mes preguntes responguis mes afinarem en la recomanacio
" crlf)
    else
        (bind ?genrei (find-instance 
                                ((?g Genero)) 
                                (eq (send ?g get-name_genre) ?genre)
                              )) 
        (send ?lector put-main_genre ?genrei)
        (printout t "
Tindrem molt en compte el genere per triar els millors llibres per tu." crlf)
        (if (or (eq ?genre "Romance")
            (eq ?genre "Mystery"))
            then
            (focus TRIGGER_W))
    )
)


(defrule TEEN::tipus_de_coberta
    (declare (salience 2))
    ?lector <- (object (is-a Lector) (cover ""))
    => 
    (bind ?options hard soft pocket)
    (bind ?cover (basicQskip "
Quin tipus de coberta prefereixes? 
    Si prefereixes llibres amb tapa dura, selecciona 'hard'.
    Si prefereixes llibres amb tapa blanda, selecciona 'soft'.
    Si prefereixes l'edicio de butxaca, selecciona 'pocket'.
Si vols saltar-te aquesta pregunta, escriu '-'.

>>> " ?options))
    (if (eq ?cover "-") 
        then
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Tingues en compte que quantes mes preguntes responguis mes afinarem en la recomanacio
" crlf)
    else
        (send ?lector put-cover ?cover)
        (printout t "
Anem a buscar els llibres amb aquest tipus de coberta..." crlf)
    )
)


(defrule TEEN::llibre_trendy
    (declare (salience 1))
    ?lector <- (object (is-a Lector) (bestseller nil))
    =>
    (bind ?bestseller (yes-or-no-p "
... de mentres, t'agraden els llibres que actualment son tendencia o estan de moda?
    Respon 'Yes' o 'No'.
Si vols saltar-te aquesta pregunta, escriu '-'.

>>> "))
    (if (eq ?bestseller "-") 
        then
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Tingues en compte que quantes mes preguntes responguis mes afinarem en la recomanacio
" crlf)
    else
        (send ?lector put-bestseller ?bestseller)
        (if (eq ?bestseller TRUE) then (printout t "
Ens encanta que segueixis les tendencies!" crlf)
        else (printout t "
Tens molta personalitat, ens agrada!" crlf))
    )
)


(defrule TEEN::longitud
    ?lector <- (object (is-a Lector) (time_read ""))
    => 
    (bind ?options short medium long very_long)
    (bind ?time_read (basicQskip "
Quant temps tens per llegir? 
    Si disposes de poc temps i desitges llibres curts, selecciona 'short'.
    Si tens un temps moderat per llegir i busques llibres de longitud mitjana, selecciona 'medium'.
    Si tens prou de temps i vols llibres llargs, selecciona 'long'.
    Si tens molt de temps i busques llibres molt llargs, selecciona 'very_long'.
Si vols saltar-te aquesta pregunta, escriu '-'.

>>> " ?options))
    (if (eq ?time_read "-") 
        then
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Tingues en compte que quantes mes preguntes responguis mes afinarem en la recomanacio
" crlf)
    else
        (send ?lector put-time_read ?time_read)
        (printout t "
Perfecte!" crlf)
    )
)
;;*******************
;;* MoDUL   ADULT   *
;;*******************

(defmodule ADULT 
    (import MAIN ?ALL)
    (import INPUT deffunction basicQ basicQskip)
)


(defrule ADULT::atributs
   ?lector <- (object (is-a Lector))  
    =>
    (send ?lector put-illustrated FALSE))


(defrule ADULT::temps_de_lectura
    (declare (salience 7))
    ?lector <- (object (is-a Lector) (time_read ""))
    => 
    (bind ?options short medium long very_long)
    (bind ?time_read (basicQskip "
Quin temps tens per llegir? 
    Si disposes de poc temps i desitges llibres curts, selecciona 'short'.
    Si tens un temps moderat per llegir i busques llibres de longitud mitjana, selecciona 'medium'.
    Si tens prou de temps i vols llibres llargs, selecciona 'long'.
    Si tens molt de temps i busques llibres molt llargs, selecciona 'very_long'.
Si vols saltar-te aquesta pregunta, escriu '-'.

>>> " ?options))
    (if (eq ?time_read "-") 
        then
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Tingues en compte que quantes mes preguntes responguis mes afinarem en la recomanacio
" crlf)
    else
        (send ?lector put-time_read ?time_read)
        (printout t "
Anem a buscar els llibres d'aquesta mida..." crlf)
    )
)

(defrule ADULT::askFamous
    (declare (salience 6))
    ?lector <- (object (is-a Lector) (famous nil))
    =>
    (bind ?famous (yes-or-no-p "
... mentrestant, busques un llibre de algun autor considerat famos?
    Respon 'Yes' o 'No'.
Si vols saltar-te aquesta pregunta, escriu '-'.

>>> "))
    (if (eq ?famous "-")
        then
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Tingues en compte que quantes mes preguntes responguis mes afinarem en la recomanacio
" crlf)
    else
        (send ?lector put-famous ?famous)
        (if (eq ?famous TRUE) then (printout t "
Que be! Tenim molts llibres d'autors famosos." crlf)
            else (printout t "Bona eleccio, que els autors siguin desconeguts no treu que les seves obres siguin bones. " crlf))
    )
)




(defrule ADULT::interes_bestseller
    (declare (salience 5))
    ?lector <- (object (is-a Lector) (famous ?f) (bestseller nil))
    (test (or (eq ?f TRUE) (eq ?f nil)))
    =>
        (bind ?bestseller (yes-or-no-p "
T'interessa llegir best sellers?
    Respon 'Yes' si t'interessen, 'No' si no t'interessen.
Si vols saltar-te aquesta pregunta, escriu '-'.

>>> "))
    (if (eq ?bestseller "-")
        then
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Tingues en compte que quantes mes preguntes responguis mes afinarem en la recomanacio
" crlf)
    else
        (send ?lector put-bestseller ?bestseller)
        (if (eq ?bestseller TRUE) then (printout t "
Doncs a recomanarte Bestsellers!" crlf)
            else (printout t "
Que curios! Vols descobrir la cara poc coneguda dels autors famosos..." crlf))
    )
)


(defrule ADULT::tipus_de_coberta
    (declare (salience 4))
    ?lector <- (object (is-a Lector) (cover ""))
    => 
    (bind ?options hard soft pocket)
    (bind ?cover (basicQskip "
Quin tipus de coberta prefereixes? 
    Si prefereixes llibres amb tapa dura, selecciona 'hard'.
    Si prefereixes llibres amb tapa blanda, selecciona 'soft'.
    Si prefereixes l'edicio de butxaca, selecciona 'pocket'.
Si vols saltar-te aquesta pregunta, escriu '-'.

>>> " ?options))
    (if (eq ?cover "-")
        then
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Tingues en compte que quantes mes preguntes responguis mes afinarem en la recomanacio
" crlf)
    else
        (send ?lector put-cover ?cover)
        (printout t "
Prenem nota! Buscarem llibres amb aquest tipus de coberta." crlf)
    )
)

(defrule ADULT::preferencia_novela
    (declare (salience 3))
    ?lector <- (object (is-a Lector) (actual nil))
    =>
    (bind ?actual (yes-or-no-p "
T'agraden les novelles actuals? O prefereixes les classiques?
    Respon 'Yes' si prefereixes les actuals, 'No' si prefereixes les classiques.
Si vols saltar-te aquesta pregunta, escriu '-'.

>>> "))
    (send ?lector put-actual ?actual)
    (if (eq ?actual TRUE) then (printout t "
D'acord, anem a veure quins son els ultims llibres que ens han arribat." crlf)
            else (printout t "Llegir un classic sempre es una bona experiencia. " crlf))
)

(defrule ADULT::genere_adult
    (declare (salience 2))
    ?lector <- (object (is-a Lector) (main_genre [nil]))
    => 
    (bind ?options Contemporary Historical Mystery Fantasy Romance Science_Fiction Horror)
    (bind ?main_genre (basicQskip "
Quin genere de llibre estas buscant? 
    Si t'agradaria llegir una obra contemporania, selecciona 'Contemporary'.
    Si t'interessen les noveles ambientades en fets historics, selecciona 'Historical'.
    Si vols resoldre un misteri mentre llegeixes, selecciona 'Mystery'.
    Si t'agrada la magia i les terres fantastiques, selecciona 'Fantasy'.
    Si busques una historia d'amor, selecciona 'Romance'.
    Si t'agrada explorar futurs i tecnologies imaginaries, selecciona 'Science_Fiction'.
    Si t'agrada passar por mentre llegeixes, selecciona 'Horror'.
Si vols saltar-te aquesta pregunta, escriu '-'.

>>> " ?options))
    (if (eq ?main_genre "-")
        then
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Tingues en compte que quantes mes preguntes responguis mes afinarem en la recomanacio
" crlf)
        (send ?lector put-main_genre [Global])
    else
        (bind ?genrei (find-instance
                            ((?g Genero))
                            (eq (send ?g get-name_genre) ?main_genre) 
                          )) 
        (send ?lector put-main_genre ?genrei)
        (printout t "
Tindrem molt en compte el genere que has triat" crlf)

    )
)

(defrule ADULT::activaTriggerW
    (declare (salience 2))
    ?lector <- (object (is-a Lector)(main_genre ?g&~[nil]))
    (test (or (eq ?g [Global])
              (eq ?g [Contemporary])
              (eq ?g [Mystery])
              (eq ?g [Romance])
              (eq ?g [Horror])
              (eq ?g [Science_Fiction])
    ))
    =>
    (focus TRIGGER_W)
)




(deffunction ADULT::subg-disp (?genre_name)
    (bind ?subgenres_chosen (create$))
    
    (bind ?subgenres (find-all-instances ((?s Subgenero)) TRUE))
    
    (foreach ?s ?subgenres
        (bind ?sname (send ?s get-name_genre))
        (bind ?g (send ?s get-subgenre_of))
        (bind ?gname (send ?g get-name_genre))
        
        (if (eq ?gname ?genre_name) 
            then 
                (bind ?sname (sym-cat ?sname))
                (printout t "  " ?sname crlf)
                ; Añadir el subgenero a la lista de subgeneros elegidos usando insert$ de manera correcta
                (bind ?subgenres_chosen (insert$ ?subgenres_chosen (+ (length$ ?subgenres_chosen) 1) ?sname))
        )
    )
    
    (return ?subgenres_chosen)
)


(defrule ADULT::subgenere
    (declare (salience 1))
    ?lector <- (object (is-a Lector) 
                      (main_genre ?main_genre&~[nil]))
    (test (neq ?main_genre [Global]))
    =>
    (bind ?genre_name (send ?main_genre get-name_genre))
    (printout t "
    Quin subgenere t'agradaria? Pel genere escollit (" ?genre_name ") tens les opcions que es mostren a continuacio:" crlf crlf)
    (bind ?subgeneres (subg-disp ?genre_name))

    (bind ?sub_genre (basicQskip "
>>> " ?subgeneres))
    (bind ?sub_genre (str-cat ?sub_genre))

    (if (eq ?sub_genre "-")
        then
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Tingues en compte que quantes mes preguntes responguis mes afinarem en la recomanacio
" crlf)
    else
        (bind ?sub_genrei (find-instance
                                ((?g Subgenero))
                                (eq (send ?g get-name_genre) ?sub_genre) 
                            ))
        (send ?lector put-has_subgenre ?sub_genrei)
        (bind ?subgenere_elegit (send ?lector get-has_subgenre))
        (printout t "
Amb la informacio del subgenere que ens has dit podrem afinar molt millor en el resutats." crlf)

    )

)



; ;;**************************
; ;;*  MODUL  TRIGGER WARNING*
; ;;**************************
; ;Realitza accions sobre els atributs

 (defmodule TRIGGER_W 
     (import MAIN ?ALL)
     (import INPUT deffunction basicQ basicQskip)

 )

(defrule TRIGGER_W::trigger_avoid
    (declare (salience 5))
    ?lector <- (object (is-a Lector) (triggerw ""))
    =>
    (bind ?options 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16)
    (bind ?triggers (multi-select-p "
Quins trigger warnings t'agradaria evitar? 
    Escriu '1' per evitar continguts amb abusos.
    Escriu '2' per evitar l'assetjament sexual.
    Escriu '3' per evitar continguts amb cosos nuus.
    Escriu '4' per evitar l'homofobia o la transfobia.
    Escriu '5' per evitar malalties mentals o discriminacio contra persones amb discapacitats.
    Escriu '6' per evitar el contingut pornografic.
    Escriu '7' per evitar l'autolesio o el suicidi.
    Escriu '8' per evitar trastorns alimentaris o fobia a la obesitat.
    Escriu '9' per evitar el racisme i les ofenses racials.
    Escriu '10' per evitar la violencia.
    Escriu '11' per evitar la sang i la violencia grafica.
    Escriu '12' per evitar el segrest i l'abduccio.
    Escriu '13' per evitar l'assassinat.
    Escriu '14' per evitar l'abus infantil, la pedofilia i l'incest.
    Escriu '15' per evitar la crueltat cap als animals.
    Escriu '16' per evitar la tortura.

Escriu tots els trigger warnings que vols evitar, separats per un espai. Si no vols evitar-ne cap, escriu '-'.

>>> " ?options))
    (if (eq ?triggers "-")
        then
        (printout t "
Has decidit saltar-te aquesta pregunta! 
Anotarem que no vols evitar cap tema delicat.
" crlf)
    else
        (send ?lector put-triggerw ?triggers)
        (printout t "
Gracies per avisarnos! Evitarem els llibres que continguin aquests temes delicats." crlf)
    )
)


(defrule TRIGGER_W::podaTriggers
    (declare (salience 4))
    ?lector <- (object  (is-a Lector) 
                        (public ?p))
    =>
    (countInstances Libro)
    (printout t "
De fet, acabem de fer una poda per eliminar de la llista aquells llibres que contenen els Trigger Warnings que has demanat evitar." crlf)
    (bind ?llibres (find-all-instances ((?l Libro)) (eq ?l:public ?p)))
    (bind ?trig (send ?lector get-triggerw))
    (progn$ (?l ?llibres)   
        (bind ?tw (send ?l get-triggerw)) 
        (bind ?comptador FALSE)
        (progn$ (?t ?tw)
            (if (member$ ?t ?trig) then
                (bind ?comptador TRUE)))
        (if (eq ?comptador TRUE) then (send ?l delete))
       )
    (countInstances Libro)
)



;;*******************
;;* MODUL ACTUADORS *
;;*******************

(defmodule ACT 
    (import MAIN ?ALL)
)

(deffunction ACT::updateP (?public ?lector)
    (switch ?public
        (case "baby" then (send ?lector put-public "children"))
        (case "children" then (send ?lector put-public "teenager"))
        (case "teenager" then (send ?lector put-public "adult"))
    )
    (send ?lector put-hab_lectura "Neutral")
)

(defrule ACT::inici
(declare (salience 2))
=>
)

(defrule ACT::updatePublic
    (declare (salience 1))
    ?lector <- (object (is-a Lector)
                       (public ?p&~"adult"&~"")
                       (hab_lectura ?h)) ;Que hi hagi algo introduit
                                         ;Que tingui molt habit de lectura
    (test (eq ?h TRUE))                 ;Que no sigui adult, ja que llavors no s'actualitza
    =>
    (updateP ?p ?lector)
    (printout t crlf)
)

(defrule ACT::podaPublic
    ?lector <- (object  (is-a Lector) 
                        (public ?p))
    =>
    (printout t "
Eliminarem els llibres de la llista que no son de la teva edat.
Abans de la poda hi ha " (countInstances Libro) " instancies de llibres." crlf)
    (do-for-all-instances 
        ((?l Libro))
        (neq ?l:public ?p)
        (send ?l delete)
        )
    (printout t "Despres de la poda han quedat " (countInstances Libro) " instancies de llibres.
Ara anem amb preguntes una mica mes especifiques:" crlf)
    
)



;;*******************
;;* MoDUL PRINCIPAL *
;;*******************

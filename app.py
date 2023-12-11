import streamlit as st
from miniproto1.constants import *

# Título de la aplicación
st.title("Recomanador de llibres CBR")

# Inicia un formulario
with st.form("Introdueix el teu perfil"):
    # Campo de texto
    name = st.text_input("Introdueix el teu nom")
    age = st.number_input("Quina és la teva edat", min_value=0, max_value=100)

    if age > 17:
        generes = genres
    elif age > 14:
        generes = genres_teen
    else:
        generes = []
    if generes:
        genere = st.selectbox("Elegeix el teu gènere preferit", generes)

    llibres = st.multiselect("Elegeix els llibres que has llegit i que més t'han agradat", book_titles)

    user_id = st.text_input("Introdueix el teu identificador d'usuari. Deixa-ho en blanc si ets un nou usuari")
    nou_perfil = st.checkbox("Sóc un nou perfil",False)

    # Botón de envío
    enviado = st.form_submit_button("Enviar")
# Acciones a realizar si se envía el formulario
if enviado:
    st.write("Nom:", name)
    st.write("Edat:", age)
    st.write("Gènere preferit:", genere)
    st.write("Llibres preferits:", llibres)
    st.write("User ID:",user_id)
#    """user_id,num_leidos,mean_rating,prop_reviwed,read_books"""
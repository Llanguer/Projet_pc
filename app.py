import streamlit  as st
import pandas as pd
from pathlib import Path




# Logo Site
logoright, logomid, logoleft = st.columns([0.5,2,0.5])

imgpc_reco = Path(__file__).parent / "assets" / "logo_pngv2.png"
logomid.image(imgpc_reco)



st.title("Trouve le PC adapté à tes besoins")

st.text("""Vous cherchez un ordinateur, mais vous ne savez pas lequel choisir ? \nNe perdez plus de temps à comparer des centaines de modèles !""")

st.subheader("",divider='red')
st.subheader("PC Advisor, vous aide à trouver le PC idéal, parfaitement adapté à votre usage et à votre budget.", divider= 'red')

st.subheader("Comment ça marche ?")
st.write("""Dites-nous ce dont vous avez besoin:
\nBureautique simple, gaming, montage vidéo, design 3D ou usage professionnel : précisez votre utilisation principale.

Recevez nos recommandations personnalisées :
En quelques secondes, notre algorithme analyse les performances processeur, carte graphique, mémoire et stockage pour vous proposer les modèles les plus adaptés.""")

st.divider()
right,mid, left = st.columns([4.5,1,4.5])

with right:
    st.write('Décrivez votre usage et vos envies : notre système vous proposera les modèles qui correspondent le mieux à vos critères.')
    st.image(Path(__file__).parent / "assets" / "botimg.png")
    if st.button("ChatBot", use_container_width=True):
        st.switch_page("pages/chatbot.py")

with left:
    st.write('Avec la recherche par filtres, explorez les modèles selon les caractéristiques, pour trouver l’ordinateur qui vous convient.')
    st.image(Path(__file__).parent / "assets" / "filterimg.png")
    if st.button("Filters", use_container_width=True):
        st.switch_page("pages/filters.py")

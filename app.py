import streamlit  as st
import pandas as pd
from pathlib import Path


# --------------------------- Bar naviagation ----------------------------------
from streamlit_option_menu import option_menu

with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Home", "Filtre", "ChatBot"],
        icons=[],  # No icons
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "#05335F",
                "class": "navbar-fixed",  # Add fixed class
            },
            "nav-link": {
                "color": "white",
                "font-size": "16px",
                "margin": "0px",
                "padding": "10px",
            },
            "nav-link-selected": {
                "background-color": "#1B4F72"
            },
        }
    )
if selected == "Home":
    selected =  "Home"
if selected == "Filtre":
    st.switch_page("pages/filtre.py")
if selected == "ChatBot":
    st.switch_page("pages/chatbot.py")
#if selected == "Contact":
#    st.switch_page("pages/Contact.py")




# ----------------------------------------------------

# Logo Site
logoright, logomid, logoleft = st.columns([0.5,2,0.5])

imgpc_reco = Path(__file__).parent / "assets" / "logo_pngv2.png"
logomid.image(imgpc_reco)

st.set_page_config(page_title="Trouve le PC adapté à tes besoins", page_icon="💻",)

st.markdown("""
<style>
    .st-emotion-cache-1jicfl2 {
        display: none;
    }
    
    .st-emotion-cache-1y4p8pa {
        display: none;
    }
    
    .st-emotion-cache-10trblm {
        display: none;
    }
    
    [data-testid="stSidebarNav"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

def load_page(page_path):
    try:
        with open(page_path, 'r', encoding='utf-8') as f:
            exec(f.read())
    except FileNotFoundError:
        st.error(f"Pagina non trovata: {page_path}")
    except Exception as e:
        st.error(f"Errore nel caricamento della pagina: {e}")

st.sidebar.title("Navigation")

menu_option = {
    "🏠 Homepage": "app",
    "💻 Recherche PC": "filtre", 
    "🧠 ChatBot": "chatbot"
}


selected = st.sidebar.selectbox(
    "Sélectionnez une page:",
    list(menu_option.keys())
)


if selected == "🏠 Homepage":
    st.title("HomePage")
elif selected == "💻 Recherche PC":
    load_page("pages/filtre.py")
elif selected == "🧠 ChatBot":
    load_page("pages/chatbot.py")

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
        st.switch_page("pages/filtre.py")
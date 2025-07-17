import streamlit as st 

st.set_page_config(page_title="Find your PC", page_icon="💻",)

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
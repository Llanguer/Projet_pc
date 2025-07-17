import streamlit as st 

# --------------------------- Bar naviagation ----------------------------------
from streamlit_option_menu import option_menu

with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Home", "Filtre", "ChatBot"],
        icons=[],  # No icons
        default_index=2,
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
    st.switch_page("app.py")
if selected == "Filtre":
    st.switch_page("pages/filtre.py")
if selected == "ChatBot":
    selected =  "ChatBot"
#if selected == "Contact":
#    st.switch_page("pages/Contact.py")




# ----------------------------------------------------



def show_chatbot_page():
    import pandas as pd 
    import time
    from google import genai
    from google.genai import types
    from google.genai.types import HttpOptions, ModelContent, Part, UserContent
    
    
    # Google Api key to use Gemini
    api_key = st.secrets["GOOGLE_API_KEY"]

    # Defining client

    client = genai.Client(api_key)

    system_prompt = """Vous êtes un spécialiste de tout ce qui touche l'informatique et les ordinateurs portables. Vous donnez des réponses précises et cohérentes avec l'argumentation.
    Vous donnez des suggestions basées sur ce que l'utilisateur demande, mais sur la base des ensembles de données fournis, tels que le dataframe 'pc_score_cpu_gpu.csv' téléchargées sur cette page, sans mentionner où vous avez obtenu l'information. Si la question n'est pas en rapport avec le sujet, dites à l'utilisateur que vous n'êtes spécialisé que dans cette branche.
    Fournissez ensuite à l'utilisateur le lien Streamlit de ce site vers l'ordinateur portable que vous lui avez suggéré, en fonction de ses besoins. Ce lien est basé sur 'http://localhost:8501/filtre?pc=' suivi de l'index de l'ordinateur portable que vous lui avez suggéré.
    Veuillez d’abord indiquer le lien, puis fournir une explication détaillée des raisons pour lesquelles vous l’avez choisi.
    Ta reponse sera en format Markdown."""

    chat = client.chats.create(
        model = "gemini-2.5-flash-preview-05-20",
        history= [
            UserContent(parts=[Part(text="Hello")]),
            ModelContent(parts=[Part(text="Great to meet you. What would you like to know?")])
        ]
    )

    chat.send_message(system_prompt)

    st.title("🧠Le spécialiste de la Tech🧠")

    st.markdown(
        """
            Bienvenue ! Je suis un spécialiste de l'informatique.
            Posez-moi vos questions sur la **Tech**, **Ordinateurs Portable** et les **Mac**.
            """
    )

    st.markdown("---")

    user_question = st.text_area("Votre question : ", height= 100, placeholder="Quel ordinateur portable recommanderiez-vous à un passionné de jeux vidéo ?")

    if st.button("Poser la question", help="Cliquez pour obtenir une réponse"):
        if user_question:
            with st.spinner("Analyse de votre question et préparation de la réponse..."):
                time.sleep(5)
                response = chat.send_message_stream(user_question)
            for chunk in response:
                st.write(chunk.text, end="")    

if __name__ == "__main__":
    show_chatbot_page()
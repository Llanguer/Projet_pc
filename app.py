import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

# ──────────── Config ────────────
st.set_page_config(page_title="PC Finder", layout="wide")

# ──────────── Data ────────────
csv_path = Path(__file__).parent / "Data" / "pc_score_cpu_gpu.csv"
df = pd.read_csv(csv_path)

req = {"img_url", "Désignation", "Bureautique", "Gamer", "Graphisme"}
if not req.issubset(df.columns):
    st.error(f"Colonnes manquantes : {', '.join(req - set(df.columns))}")
    st.stop()

if "selected_type" not in st.session_state:
    st.session_state.selected_type = None
if "selected_pc" not in st.session_state:
    st.session_state.selected_pc = None

# ──────────── Check paramètre URL (clic image) ────────────
query_params = st.query_params
if "pc" in query_params:
    try:
        pc_idx = int(query_params["pc"])
        if 0 <= pc_idx < len(df):
            st.session_state.selected_pc = pc_idx
    except:
        pass

# ──────────── Page principale : liste des PC ────────────
def show_pc_list():
    st.title("Trouve le PC adapté à tes besoins")

    st.markdown("""
    <style>
    div.stButton > button {width:100%; height:90px; font-size:1.2rem; border-radius:12px;}
    </style>
    """, unsafe_allow_html=True)

    types = ["Bureautique", "Gamer", "Graphisme"]
    btn_cols = st.columns(3)
    for i, act in enumerate(types):
        with btn_cols[i % 3]:
            if st.button(act, key=f"btn_{i}"):
                st.session_state.selected_type = act
                st.session_state.selected_pc = None
                st.query_params.clear()  # reset l'URL

    if not st.session_state.selected_type:
        st.warning("Veuillez sélectionner une catégorie pour voir les résultats.")
        return

    filtered = df[df[st.session_state.selected_type] == 1]

    # ───── Sidebar : filtres ─────
    st.sidebar.header("Filtres avancés")
    filter_cols = [
        "Processeur", "GPU series",
        "Type d'écran", "Type de Dalle", "Clavier rétroéclairé", "Office fourni",
        "Fréquence CPU", "Nombre de core", "Taille de la mémoire",
        "Capacité", "Taille de l'écran", "Résolution Max",
        "Taux de rafraîchissement", "Autonomie",
        "Poids", "Largeur", "Profondeur", "Epaisseur",
        "CPU_benchmark_single_core", "CPU_benchmark_multi_core", "3d_mark", "geekbench",
        "price"
    ]
    filter_cols = [c for c in filter_cols if c in filtered.columns]

    for col in filter_cols:
        col_clean = filtered[col].dropna()
        if col_clean.empty:
            continue
        if col_clean.dtype == object or col_clean.nunique() <= 20:
            options = sorted(col_clean.unique())
            selected = st.sidebar.multiselect(col, options, default=options)
            filtered = filtered[filtered[col].isin(selected)]
        elif np.issubdtype(col_clean.dtype, np.number):
            mn, mx = float(col_clean.min()), float(col_clean.max())
            low, high = st.sidebar.slider(col, mn, mx, (mn, mx))
            filtered = filtered[(filtered[col] >= low) & (filtered[col] <= high)]

    # ───── Affichage résultats ─────
    if filtered.empty:
        st.warning("Aucun PC ne correspond aux filtres sélectionnés.")
        return

    st.caption(f"{len(filtered)} PC trouvé(s)")
    img_cols = st.columns(4)

    for idx, row in filtered.reset_index().iterrows():
        with img_cols[idx % 4]:
            pc_index = row["index"]
            img_html = f"""
            <a href="?pc={pc_index}" target="_self">
                <img src="{row['img_url']}" style="width:100%; border-radius:8px;" />
            </a>
            """
            st.markdown(img_html, unsafe_allow_html=True)
            label = str(row["Désignation"]) if pd.notna(row["Désignation"]) else "Sans nom"
            st.caption(label)

# ──────────── Page détails PC ────────────
def show_pc_details():
    pc = df.loc[st.session_state.selected_pc]
    st.title(pc["Désignation"] if pd.notna(pc["Désignation"]) else "Fiche PC")

    st.image(pc["img_url"], width=300)
    st.markdown("### Détails techniques")

    exclude_cols = {"img_url", "Désignation", "Bureautique", "Gamer", "Graphisme"}
    for col in df.columns:
        if col in exclude_cols:
            continue
        val = pc[col]
        if pd.isna(val):
            continue
        st.write(f"**{col} :** {val}")

    if st.button("← Retour"):
        st.session_state.selected_pc = None
        st.query_params.clear()  # nettoyer l'URL

# ──────────── Navigation ────────────
if st.session_state.selected_pc is None:
    show_pc_list()
else:
    show_pc_details()

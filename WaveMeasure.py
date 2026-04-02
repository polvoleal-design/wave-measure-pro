import streamlit as st
import os
import base64
from PIL import Image, ImageEnhance
import math
import io

# --- 1. CONFIGURAÇÃO SHARP (SEM PASTAS) ---
st.set_page_config(page_title="WAVE MEASURE PRO", layout="wide", initial_sidebar_state="collapsed")

def find_file(filename):
    # Procura o ficheiro no diretório principal
    if os.path.exists(filename):
        return filename
    # Procura na pasta assets se ela existir
    assets_path = os.path.join("assets", filename)
    if os.path.exists(assets_path):
        return assets_path
    return None

# --- 2. INJETAR O FUNDO ---
hero_path = find_file("hero7.png")
if hero_path:
    with open(hero_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(11,14,17,0.75), rgba(11,14,17,0.95)), url(data:image/png;base64,{b64});
            background-size: cover; background-attachment: fixed;
        }}
        .stTabs [data-baseweb="tab-list"] {{ justify-content: center; gap: 30px; }}
        .stTabs [data-baseweb="tab"] {{ color: #ffffff; font-weight: bold; text-transform: uppercase; border: none; font-size: 14px; }}
        .stTabs [aria-selected="true"] {{ color: #00ccff !important; border-bottom: 2px solid #00ccff !important; }}
        h1, h2, h3, p, label {{ color: #e1e4e8 !important; }}
        </style>
        """, unsafe_allow_html=True)

# --- 3. LOGOTIPO ---
logo_path = find_file("logo.png")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if logo_path:
        st.image(logo_path, use_container_width=True)
    st.markdown("<h1 style='text-align: center;'>WAVE MEASURE PRO</h1>", unsafe_allow_html=True)

st.divider()
t_home, t_sub, t_analysis, t_gold = st.tabs(["🏠 HOME", "📂 SUBMISSIONS", "🔬 ANALYSIS", "✨ GOLDEN MOMENTS"])

with t_home:
    st.write("### Witness the Truth.")
    st.write("Ensuring scientific truth in the world's most dangerous arena.")
    st.write("© Jorge Leal | Pioneer Committee")

with t_sub:
    st.header("Submission Portal")
    st.file_uploader("Upload Original Photo", type=['jpg','png','jpeg'])

with t_analysis:
    st.header("The VAR Room")
    st.info("Awaiting Submissions for Forensic Scan.")

with t_gold:
    st.header("The Golden Gallery")
    st.write("The Top 7 and Artistic Highlights will appear here.")

import streamlit as st
import base64
import os

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="WAVE MEASURE PRO", layout="wide")

def img_to_b64(name):
    if os.path.exists(name):
        with open(name, "rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
    return ""

# Carregar as peças do teu design
hero_b64 = img_to_b64("hero7.png")
logo_b64 = img_to_b64("logo.png")
btn1 = img_to_b64("btn_athletes.png")
btn2 = img_to_b64("btn_explore.png")
btn3 = img_to_b64("btn_photo_video.png")

# --- 2. CSS "BLINDADO" (PARA MATAR O MOSAICO E PARTIDAS DO BROWSER) ---
st.markdown(f"""
    <style>
    /* Remove todo o lixo do Streamlit */
    [data-testid="stHeader"], [data-testid="stSidebar"], footer {{display: none !important;}}
    .block-container {{padding: 0 !important; max-width: 100% !important;}}
    
    /* FIXA O FUNDO: SEM MOSAICO, SEM REPETIÇÃO */
    .stApp {{
        background-image: url("{hero_b64}");
        background-size: cover !important;
        background-position: center center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }}

    /* CRIA A MOLDURA DO TELEMÓVEL NO CENTRO DO MAC PRO */
    .mobile-wrapper {{
        width: 100%;
        max-width: 450px; /* Largura de um telemóvel */
        min-height: 100vh;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        background: rgba(0,0,0,0.3); /* Overlay suave para o design respirar */
        padding: 40px 20px;
    }}

    .logo-main {{ width: 180px; margin-bottom: 60px; }}

    /* BOTÕES COM EFEITO DE ESCURECER (50% BRIGHTNESS) */
    .btn-wrap {{ width: 100%; margin-bottom: 15px; cursor: pointer; }}
    .btn-wrap img {{ width: 100%; display: block; transition: 0.3s; }}
    .btn-wrap img:hover {{ filter: brightness(0.5); transform: scale(0.98); }}

    .copy {{ color: rgba(255,255,255,0.3); font-size: 10px; margin-top: auto; letter-spacing: 1px; }}
    </style>

    <div class="mobile-wrapper">
        <img src="{logo_b64}" class="logo-main">
        <div class="btn-wrap"><img src="{btn1}"></div>
        <div class="btn-wrap"><img src="{btn2}"></div>
        <div class="btn-wrap"><img src="{btn3}"></div>
        <div class="copy">© 2026 JORGE LEAL | WAVE MEASURE</div>
    </div>
    """, unsafe_allow_html=True)

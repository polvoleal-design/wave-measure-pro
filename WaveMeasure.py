import streamlit as st
import base64
import os
import time

# --- CONFIGURAÇÃO SHARP ---
st.set_page_config(page_title="WAVE MEASURE PRO", layout="centered")

def img_to_b64(name):
    if os.path.exists(name):
        with open(name, "rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
    return ""

# Carregar Peças do Teu Design (que estão soltas no GitHub)
hero_b64 = img_to_b64("hero7.png")
logo_b64 = img_to_b64("logo.png")
btn1 = img_to_b64("btn_athletes.png")
btn2 = img_to_b64("btn_explore.png")
btn3 = img_to_b64("btn_photo_video.png")

# --- CSS DE DESIGNER (OVERRIDE PARA MOBILE) ---
st.markdown(f"""
    <style>
    [data-testid="stHeader"], [data-testid="stSidebar"], footer {{display: none !important;}}
    .block-container {{padding: 0 !important; max-width: 100% !important;}}
    
    .stApp {{
        background: url("{hero_b64}") no-repeat center center fixed !important;
        background-size: cover !important;
    }}

    .mobile-screen {{
        width: 420px;
        height: 100vh;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: start;
        position: relative;
        background: rgba(0,0,0,0.4); /* Overlay para dar contraste */
    }}

    .logo-main {{ width: 160px; margin-top: 80px; margin-bottom: 60px; }}

    .btn-container {{ width: 100%; margin-bottom: 10px; cursor: pointer; }}
    .btn-container img {{ width: 100%; display: block; transition: 0.3s; }}
    .btn-container img:hover {{ filter: brightness(0.5); transform: scale(0.98); }}

    .copyright {{ position: absolute; bottom: 30px; color: rgba(255,255,255,0.4); font-size: 10px; letter-spacing: 1px; }}
    </style>

    <div class="mobile-screen">
        <img src="{logo_b64}" class="logo-main">
        <div class="btn-container"><img src="{btn1}"></div>
        <div class="btn-container"><img src="{btn2}"></div>
        <div class="btn-container"><img src="{btn3}"></div>
        <div class="copyright">© 2026 JORGE LEAL | WAVE MEASURE</div>
    </div>
    """, unsafe_allow_html=True)

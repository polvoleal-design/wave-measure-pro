import streamlit as st
import base64
import os

# --- 1. CONFIGURAÇÃO DE PÁGINA ---
st.set_page_config(page_title="WAVE MEASURE PRO", layout="wide")

def get_base64(file_name):
    """Lê o ficheiro e converte para código para o fundo não falhar"""
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

# Carregar imagens (Garante que os nomes no GitHub são estes e em minúsculas)
hero = get_base64("hero7.png")
logo = get_base64("logo.png")
btn1 = get_base64("btn_athletes.png")
btn2 = get_base64("btn_explore.png")
btn3 = get_base64("btn_photo_video.png")

# --- 2. CSS "THE GAME CHANGER" (PARA MATAR O MOSAICO) ---
st.markdown(f"""
    <style>
    /* Esconder tudo o que é do Streamlit */
    header, footer, [data-testid="stHeader"], [data-testid="stSidebar"] {{display: none !important;}}
    
    /* FORÇAR O FUNDO ÚNICO E FIXO */
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{hero}") !important;
        background-size: cover !important;
        background-position: center center !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }}

    /* REMOVER O FUNDO CINZENTO DO STREAMLIT */
    .stApp {{ background: transparent !important; }}

    /* CONTENTOR VERTICAL (A TUA APP) */
    .mobile-ui {{
        width: 100%;
        max-width: 420px;
        margin: 0 auto;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 80px 20px;
        background: rgba(0,0,0,0.2); /* Sombra muito leve */
    }}

    .logo-img {{ width: 180px; margin-bottom: 60px; }}
    
    .button-container {{ width: 100%; margin-bottom: 12px; cursor: pointer; }}
    .button-container img {{ 
        width: 100%; 
        display: block; 
        transition: filter 0.3s, transform 0.2s; 
    }}
    .button-container img:hover {{ 
        filter: brightness(0.5); 
        transform: scale(0.98); 
    }}

    .copy {{ color: rgba(255,255,255,0.4); font-size: 10px; margin-top: auto; letter-spacing: 1px; }}
    </style>

    <div class="mobile-ui">
        <img src="data:image/png;base64,{logo}" class="logo-img">
        <div class="button-container"><img src="data:image/png;base64,{btn1}"></div>
        <div class="button-container"><img src="data:image/png;base64,{btn2}"></div>
        <div class="button-container"><img src="data:image/png;base64,{btn3}"></div>
        <div class="copy">© 2026 JORGE LEAL | WAVE MEASURE</div>
    </div>
    """, unsafe_allow_html=True)

# Mensagem de erro caso os ficheiros não existam (Só aparece se faltar algo no GitHub)
if not hero or not logo:
    st.error("ERRO CRÍTICO: Verifica se os ficheiros 'hero7.png' e 'logo.png' estão na raiz do GitHub.")

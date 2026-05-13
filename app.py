import streamlit as st
import streamlit.components.v1 as components
import os

# Configuración básica
st.set_page_config(
    page_title="Respira, Mamá", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 1. El Camuflaje Definitivo: Destruimos el banner rojo y la cabecera
st.markdown("""
    <style>
        /* Ocultar la cabecera y el menú superior */
        [data-testid="stHeader"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        #MainMenu {display: none !important;}
        
        /* Ocultar el banner rojo de Hosted with Streamlit */
        .viewerBadge_container {display: none !important;}
        
        /* Ocultar el footer */
        footer {display: none !important;}
        
        /* Ajustar los márgenes para que la App ocupe toda la pantalla */
        .block-container { 
            padding: 0px !important; 
            max-width: 100% !important;
        }
        
        /* Forzar la caja del HTML */
        iframe {
            border: none !important;
            width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# 2. Cargamos tu App
ruta = os.path.join(os.path.dirname(__file__), "index.html")

if os.path.exists(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        html_puro = f.read()
        
    # Lanzamos el código
    components.html(html_puro, height=900, scrolling=False)

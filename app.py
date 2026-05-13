import streamlit as st
import streamlit.components.v1 as components
import os

# Configuración básica en modo colapsado
st.set_page_config(
    page_title="Respira, Mamá", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# 1. El Camuflaje: Ocultamos logos, menús, padding y forzamos el alto al 100% de la pantalla
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Quitamos las márgenes blancas de Streamlit y limitamos el ancho al tamaño de un celular */
        .block-container { 
            padding: 0px !important; 
            max-width: 430px !important;
            margin: 0 auto !important;
        }
        
        /* Forzamos que la caja de la app ocupe el 100% de la pantalla sin bordes */
        iframe {
            border: none !important;
            height: 100vh !important; 
            width: 100% !important;
        }
        
        /* Fondo gris para los bordes si lo abren en PC */
        .stApp {
            background-color: #D3CEC4;
        }
    </style>
""", unsafe_allow_html=True)

# 2. Cargamos tu App
ruta = os.path.join(os.path.dirname(__file__), "index.html")

if os.path.exists(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        html_puro = f.read()
        
    # Lanzamos tu código. 
    # scrolling=False es el truco para que la navegación fluida de tu código original tome el control.
    components.html(html_puro, height=850, scrolling=False)

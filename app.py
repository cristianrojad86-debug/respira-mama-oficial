import streamlit as st
import streamlit.components.v1 as components
import os

# Configuración básica
st.set_page_config(page_title="Respira, Mamá", layout="centered")

# Solo ajustamos los márgenes, dejamos los menús visibles por ahora para ver errores
st.markdown("""
    <style>
        .block-container { padding: 0px !important; }
    </style>
""", unsafe_allow_html=True)

# Buscar y leer el archivo HTML
ruta = os.path.join(os.path.dirname(__file__), "index.html")

if os.path.exists(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        html_puro = f.read()
        
    # Verificamos que el archivo no se haya subido vacío por error
    if len(html_puro) < 100:
        st.warning("⚠️ El archivo 'index.html' parece estar vacío. Vuelve a subir tus 676 líneas a GitHub.")
    else:
        # Si todo está bien, lanzamos la app
        components.html(html_puro, height=900, scrolling=True)
else:
    st.error("❌ No encuentro el archivo 'index.html'. Asegúrate de haberlo subido al repositorio.")

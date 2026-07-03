import streamlit as st
import pathlib

st.set_page_config(
    page_title="Emplacamentos Brasil",
    page_icon="🚗",
    layout="wide",
)

# Remove Streamlit padding so o HTML ocupa toda a área
st.markdown("""
<style>
    .block-container { padding: 0 !important; }
    #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

html = pathlib.Path(__file__).parent.joinpath("assets", "emplacamentos_mapa.html").read_text(encoding="utf-8")
st.components.v1.html(html, height=920, scrolling=True)

import streamlit as st
import pathlib

st.set_page_config(
    page_title="SCR - Crédito Pessoal e Consignado",
    page_icon="💳",
    layout="wide",
)

# Remove Streamlit padding so o HTML ocupa toda a área
st.markdown("""
<style>
    .block-container { padding: 0 !important; }
    #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

html = pathlib.Path(__file__).parent.parent.joinpath("assets", "scr_dashboard.html").read_text(encoding="utf-8")
st.components.v1.html(html, height=3000, scrolling=True)

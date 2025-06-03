import streamlit as st
import json

# Carregar previsões
with open("previsoes_semanais.json", "r") as f:
    previsoes = json.load(f)

with open("previsoes_veronica.json", "r") as f:
    previsoes_veronica = json.load(f)

st.set_page_config(page_title="Previsão de Matrículas", layout="wide")

st.title("Previsão de Matrículas")
st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Geral")
    semana_escolhida = st.selectbox("Selecione a semana:", list(previsoes.keys()))
    if semana_escolhida:
        st.success(f"Previsão: {previsoes[semana_escolhida]} matrículas")

with col2:
    st.subheader("Previsão Verônica")
    semana_veronica = st.selectbox("Semana (Verônica):", list(previsoes_veronica.keys()), key="veronica")
    if semana_veronica:
        st.info(f"Previsão Verônica: {previsoes_veronica[semana_veronica]} matrículas")
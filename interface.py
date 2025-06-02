import streamlit as st
import json

# Carregar previsões salvas
with open("previsoes_semanais.json", "r") as f:
    previsoes = json.load(f)

st.set_page_config(page_title="Previsão de Matrículas", layout="centered")
st.title("Previsão de Matrículas")
st.markdown("---")

semana_escolhida = st.selectbox("Selecione a semana:", list(previsoes.keys()))

if semana_escolhida:
    st.success(f"Previsão: {previsoes[semana_escolhida]} matrículas")
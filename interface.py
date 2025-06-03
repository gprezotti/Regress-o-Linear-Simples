import streamlit as st

st.set_page_config(layout="wide", page_title="Dashboard de Matrículas")

# Exemplo de dados
semana_opcoes = ["03/06/25 - 09/06/25", "10/06/25 - 16/06/25"]
semana_selecionada = st.selectbox("Previsão de Matrículas", semana_opcoes, label_visibility="collapsed")

# CSS customizado
st.markdown("""
    <style>
    .card {
        background-color: #1B3929;
        border-radius: 16px;
        padding: 10px 0;
        text-align: center;
        color: #A8FFE0;
        font-weight: bold;
        font-size: 34px;
        margin-bottom: 0;
    }
    .label {
        font-size: 17px;
        font-weight: 600;
        color: white;
        margin-bottom: 4px;
    }
    .percent {
        font-size: 24px;
        margin-top: 4px;
        font-weight: bold;
        color: #A8FFE0;
    }
    .percent-yellow {
        background-color: #FFD447;
        color: #1B3929;
        padding: 6px 0;
        border-radius: 0 0 16px 16px;
    }
    </style>
""", unsafe_allow_html=True)

# LINHA 1 - Total e Meta
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="label">Previsão de Matrículas</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">80</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="label">Previsão de Atingimento da Meta</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">104%</div>', unsafe_allow_html=True)

# LINHA 2 - Verônica, Thiago, Danielly
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="label">Previsão de Matrículas Verônica</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">15</div>', unsafe_allow_html=True)
    st.markdown('<div class="percent">83%</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="label">Previsão de Matrículas Thiago</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">14</div>', unsafe_allow_html=True)
    st.markdown('<div class="percent">80%</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="label">Previsão de Matrículas Danielly</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">11</div>', unsafe_allow_html=True)
    st.markdown('<div class="percent percent-yellow">75%</div>', unsafe_allow_html=True)
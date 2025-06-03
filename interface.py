import streamlit as st

st.set_page_config(layout="wide", page_title="Dashboard de Matrículas")

# CSS para personalização
st.markdown("""
    <style>
    .card {
        background-color: #1B3929;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        color: #A8FFE0;
        font-weight: bold;
        font-size: 32px;
    }
    .subcard {
        border-radius: 0 0 16px 16px;
        padding: 10px;
        font-size: 24px;
    }
    .subcard-yellow {
        background-color: #FFD447;
        color: #1B3929;
    }
    .label {
        font-size: 18px;
        font-weight: 600;
        color: white;
        margin-bottom: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# Linha 1
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="label">Previsão de Matrículas</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">80</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="label">Previsão de Atingimento da Meta</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">104%</div>', unsafe_allow_html=True)

# Linha 2
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="label">Previsão de Matrículas Verônica</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">15</div>', unsafe_allow_html=True)
    st.markdown('<div class="subcard subcard-green">83%</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="label">Previsão de Matrículas Thiago</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">14</div>', unsafe_allow_html=True)
    st.markdown('<div class="subcard subcard-green">80%</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="label">Previsão de Matrículas Danielly</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">11</div>', unsafe_allow_html=True)
    st.markdown('<div class="subcard subcard-yellow">75%</div>', unsafe_allow_html=True)
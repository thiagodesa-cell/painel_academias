import streamlit as st

# Configuração da página em formato vertical (apropriado para dispositivos móveis)
st.set_page_config(page_title="App de Treinos", page_icon="💪", layout="centered")

# Estilo personalizado com foco em visual de mini aplicativo mobile
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffe6f0; /* Fundo rosa suave estilo app */
        max-width: 480px;        /* Limita a largura para parecer uma tela de celular */
        margin: 0 auto;          /* Centraliza na tela do computador se aberto no PC */
    }
    
    /* Cores gerais dos textos */
    h1, h2, h3, p, span, label {
        color: #4a2b38 !important;
    }

    /* Estilização da Barra Lateral */
    [data-testid="stSidebar"] {
        background-color: #ffb3d1 !important;
    }

    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span, 
    [data-testid="stSidebar"] label {
        color: #3b1d28 !important;
        font-weight: bold;
    }

    /* Estilização dos botões expansíveis para parecerem cartões de app */
    .streamlit-expanderHeader {
        background-color: #ffffff !important;
        border-radius: 12px !important;
        color: #4a2b38 !important;
        font-weight: bold !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; font-size: 24px;'>💪 Meu App de Treinos</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px;'>Séries e Escalas na Palma da Mão</p>", unsafe_allow_html=True)

# Menu lateral para escolher o dia
st.sidebar.header("📅 Navegação")
dia_selecionado = st.sidebar.selectbox("Escolha o Dia:", ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"])

st.divider()

st.markdown(f"### 📍 Escala: {dia_selecionado}")

# Exemplo de blocos verticais (perfeito para telas de celular)
st.markdown("### 🏋️ Séries do Dia")

# Exercício 1
with st.expander("📌 Supino Reto com Halteres"):
    st.write("**Séries:** 4 de 12 repetições")
    st.write("**Foco:** Peitoral e Tríceps")
    st.write("**Dica:** Manter os cotovelos levemente flexionados.")
    st.image("https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?q=80&w=400", caption="Ilustração do Movimento")

# Exercício 2
with st.expander("📌 Agachamento Livre"):
    st.write("**Séries:** 3 de 15 repetições")
    st.write("**Foco:** Pernas e Glúteos")
    st.write("**Dica:** Coluna reta e força nos calcanhares.")
    st.image("https://images.unsplash.com/photo-1574680096145-d05b474e2155?q=80&w=400", caption="Postura Correta")
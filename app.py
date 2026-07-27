import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="App de Treinos",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS para destacar a setinha ---
st.markdown("""
    <style>
        [data-testid="collapsedControl"] svg, 
        [data-testid="collapsedControl"] svg path {
            fill: white !important;
            stroke: white !important;
        }
        [data-testid="collapsedControl"] {
            background-color: rgba(255, 255, 255, 0.1) !important;
            border-radius: 50% !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- Conteúdo do App ---
st.sidebar.title("Navegação")
dia_escolhido = st.sidebar.selectbox("Escolha o Dia:", ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"])

st.title("💪 Meu App de Treinos")
st.write("Séries e Escalas na Palma da Mão")

if dia_escolhido == "Segunda-feira":
    st.header("Treino de Segunda-feira")
    
    with st.expander("🏋️ Supino Reto"):
        st.write("**Séries:** 3 de 12 repetições")
        st.write("**Foco:** Peitoral e Tríceps")
        st.write("**Dica:** Manter os cotovelos levemente flexionados.")
        # GIF CORRETO: Execução de Supino Reto
        st.image("https://i.pinimg.com/originals/02/a6/9e/02a69e2d8a7230e93002d63994f8b0fd.gif", caption="Demonstração: Supino Reto")
        
    with st.expander("🏃 Agachamento Livre"):
        st.write("**Séries:** 3 de 15 repetições")
        st.write("**Foco:** Pernas e Glúteos")
        st.write("**Dica:** Coluna reta e força nos calcanhares.")
        # GIF CORRETO: Execução de Agachamento Livre
        st.image("https://fitnessprogramer.com/wp-content/uploads/2021/02/Barbell-Squat.gif", caption="Demonstração: Agachamento Livre")
else:
    st.header(f"Treino de {dia_escolhido}")
    st.write("Configure os exercícios deste dia no seu painel.")

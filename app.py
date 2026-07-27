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
        # GIF animado garantido para Supino Reto
        st.image("https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/Barbell_Bench_Press/0.jpg", width=400)
        
    with st.expander("🏃 Agachamento Livre"):
        st.write("**Séries:** 3 de 15 repetições")
        st.write("**Foco:** Pernas e Glúteos")
        st.write("**Dica:** Coluna reta e força nos calcanhares.")
        # GIF animado garantido para Agachamento
        st.image("https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/Barbell_Squat/0.jpg", width=400)
else:
    st.header(f"Treino de {dia_escolhido}")
    st.write("Configure os exercícios deste dia no seu painel.")

import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="App de Treinos",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS para destacar o ícone da sidebar (setinha branca e visível) ---
st.markdown("""
    <style>
        /* Força a cor do ícone da sidebar para branco */
        [data-testid="collapsedControl"] svg {
            fill: white !important;
        }
        /* Garante fundo transparente e boa área de toque */
        [data-testid="collapsedControl"] {
            background-color: transparent !important;
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
        st.image("https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?q=80&w=400", caption="Supino Reto")
        
    with st.expander("🏃 Agachamento Livre"):
        st.write("**Séries:** 3 de 15 repetições")
        st.write("**Foco:** Pernas e Glúteos")
        st.write("**Dica:** Coluna reta e força nos calcanhares.")
        st.image("https://images.unsplash.com/photo-1574680096145-d05b474e2155?q=80&w=400", caption="Agachamento Livre")
else:
    st.header(f"Treino de {dia_escolhido}")
    st.write("Configure os exercícios deste dia no seu painel.")

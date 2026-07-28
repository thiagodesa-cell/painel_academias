import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="App de Treinos",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS com força máxima para a setinha ficar branca ---
st.markdown("""
    <style>
        /* Força a cor do ícone e dos traços da setinha da sidebar para branco */
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
        # Exemplo com foto normal
        st.image("https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?q=80&w=400", caption="Supino Reto")
        
    with st.expander("🏃 Agachamento Livre"):
        st.write("**Séries:** 3 de 15 repetições")
        st.write("**Foco:** Pernas e Glúteos")
        st.write("**Dica:** Coluna reta e força nos calcanhares.")
        # Exemplo com GIF animado (basta colocar o link de um GIF válido aqui)
        st.image("https://media.giphy.com/media/l0HlHFRbmaZtBRhXG/giphy.gif", caption="Agachamento (Exemplo Animado)")
else:
    st.header(f"Treino de {dia_escolhido}")
    st.write("Configure os exercícios deste dia no seu painel.")

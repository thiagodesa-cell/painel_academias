import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="App de Treinos",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS customizado para botões e cards de alto impacto visual ---
st.markdown("""
    <style>
        /* Força a cor do ícone e traços da setinha da sidebar para branco */
        [data-testid="collapsedControl"] svg, 
        [data-testid="collapsedControl"] svg path {
            fill: white !important;
            stroke: white !important;
        }
        [data-testid="collapsedControl"] {
            background-color: rgba(255, 255, 255, 0.15) !important;
            border-radius: 50% !important;
        }
        
        /* Estilização moderna para os expanders de treino */
        .streamlit-expanderHeader {
            font-weight: bold;
            font-size: 1.1rem;
            color: #FF007F !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- Conteúdo do App ---
st.sidebar.title("🔥 Menu de Treinos")
dias_semana = [
    "Segunda-feira", "Terça-feira", "Quarta-feira", 
    "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"
]
dia_escolhido = st.sidebar.selectbox("Escolha o Dia:", dias_semana)

st.title("💪 Meu App de Treinos")
st.write("Séries completas de segunda a domingo na palma da mão")

# --- Lógica de Exibição por Dia da Semana com GIFs Animados ---

if dia_escolhido == "Segunda-feira":
    st.header("💥 Segunda-feira: Membros Superiores (Peito e Tríceps)")
    
    with st.expander("🏋️ 1. Supino Reto com Halteres"):
        st.write("**Séries:** 4 de 10 a 12 repetições")
        st.write("**Foco:** Peitoral e Tríceps")
        st.write("**Dica:** Mantenha os ombros firmes no banco e desça controlando.")
        st.image("https://fitnessprogramer.com/wp-content/uploads/2021/02/Barbell-Bench-Press.gif", width=400, caption="Animação: Supino Reto")
        
    with st.expander("🔥 2. Tríceps Pulley"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Tríceps")
        st.write("**Dica:** Cotovelos colados ao lado do corpo.")
        st.image("https://fitnessprogramer.com/wp-content/uploads/2021/02/Cable-Pushdown.gif", width=400, caption="Animação: Tríceps Pulley")

elif dia_escolhido == "Terça-feira":
    st.header("🦵 Terça-feira: Membros Inferiores (Foco em Quadríceps)")
    
    with st.expander("🏋️ 1. Agachamento Livre"):
        st.write("**Séries:** 4 de 8 a 10 repetições")
        st.write("**Foco:** Pernas e Glúteos")
        st.write("**Dica:** Coluna reta e força nos calcanhares.")
        st.image("https://fitnessprogramer.com/wp-content/uploads/2021/02/Barbell-Squat.gif", width=400, caption="Animação: Agachamento Livre")
        
    with st.expander("🔥 2. Cadeira Extensora"):
        st.write("**Séries:** 3 de 12 repetições (com Drop-set)")
        st.write("**Foco:** Quadríceps isolado")
        st.image("https://fitnessprogramer.com/wp-content/uploads/2021/02/Leg-Extension.gif", width=400, caption="Animação: Cadeira Extensora")

elif dia_escolhido == "Quarta-feira":
    st.header("🦾 Quarta-feira: Costas, Bíceps e Antebraço")
    
    with st.expander("🏋️ 1. Puxada Alta Frontal"):
        st.write("**Séries:** 4 de 10 repetições")
        st.write("**Foco:** Dorsal e Bíceps")
        st.write("**Dica:** Estufe o peito ao puxar a barra em direção à clavícula.")
        st.image("https://fitnessprogramer.com/wp-content/uploads/2021/02/Lat-Pulldown.gif", width=400, caption="Animação: Puxada Alta")
        
    with st.expander("🔥 2. Rosca Directa com Barra W"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Bíceps")
        st.image("https://fitnessprogramer.com/wp-content/uploads/2021/02/Barbell-Curl.gif", width=400, caption="Animação: Rosca Direta")

elif dia_escolhido == "Quinta-feira":
    st.header("🛡️ Quinta-feira: Ombros e Abdômen")
    
    with st.expander("🏋️ 1. Desenvolvimento com Halteres"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Deltoides (Ombros)")
        st.image("https://fitnessprogramer.com/wp-content/uploads/2021/02/Dumbbell-Overhead-Press.gif", width=400, caption="Animação: Desenvolvimento")
        
    with st.expander("🔥 2. Prancha Abdominal"):
        st.write("**Séries:** 3 séries de 45 segundos")
        st.write("**Foco:** Core e Abdômen")
        st.image("https://fitnessprogramer.com/wp-content/uploads/2021/02/Plank.gif", width=400, caption="Animação: Prancha")

elif dia_escolhido == "Sexta-feira":
    st.header("🍑 Sexta-feira: Membros Inferiores (Posteriores e Glúteos)")
    
    with st.expander("🏋️ 1. Stiff com Barra"):
        st.write("**Séries:** 4 de 10 repetições")
        st.write("**Foco:** Posterior de coxa e glúteos")
        st.write("**Dica:** Mantenha os joelhos semi-flexionados e empurre o quadril para trás.")
        st.image("https://fitnessprogramer.com/wp-content/uploads/2021/02/Barbell-Stiff-Legged-Deadlift.gif", width=400, caption="Animação: Stiff")
        
    with st.expander("🔥 2. Cadeira Flexora"):
        st.write("**Séries:** 3 de 12 repetições")
        st.write("**Foco:** Posterior de coxa")
        st.image("https://fitnessprogramer.com/wp-content/uploads/2021/02/Lying-Leg-Curl.gif", width=400, caption="Animação: Cadeira Flexora")

elif dia_escolhido == "Sábado":
    st.header("⚡ Sábado: Full Body / Condicionamento (HIIT)")
    
    with st.expander("🏃 1. Burpees"):
        st.write("**Séries:** 4 blocos de 45 segundos")
        st.write("**Foco:** Condicionamento físico geral e queima calórica")
        st.image("https://fitnessprogramer.com/wp-content/uploads/2021/02/Burpee.gif", width=400, caption="Animação: Burpee")
        
    with st.expander("🔥 2. Pular Corda"):
        st.write("**Séries:** 4 rounds de 1 minuto")
        st.write("**Foco:** Resistência e Panturrilhas")
        st.image("https://fitnessprogramer.com/wp-content/uploads/2021/06/Jump-Rope.gif", width=400, caption="Animação: Pular Corda")

elif dia_escolhido == "Domingo":
    st.header("🌿 Domingo: Recuperação Ativa e Mobilidade")
    
    with st.expander("🧘 1. Alongamento Global"):
        st.write("**Duração:** 15 a 20 minutos")
        st.write("**Foco:** Soltura muscular e prevenção de lesões")
        st.image("https://fitnessprogramer.com/wp-content/uploads/2021/02/Hamstring-Stretch.gif", width=400, caption="Animação: Alongamento")
        
    with st.expander("🚶 2. Caminhada Leve (Opcional)"):
        st.write("**Duração:** 30 minutos em ritmo leve")
        st.write("**Foco:** Circulação e descanso ativo")
        st.image("https://fitnessprogramer.com/wp-content/uploads/2021/02/Walking.gif", width=400, caption="Animação: Caminhada")

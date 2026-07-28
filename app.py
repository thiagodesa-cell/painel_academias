import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="App de Treinos",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS customizado ---
st.markdown("""
    <style>
        [data-testid="collapsedControl"] svg, 
        [data-testid="collapsedControl"] svg path {
            fill: white !important;
            stroke: white !important;
        }
        [data-testid="collapsedControl"] {
            background-color: rgba(255, 255, 255, 0.15) !important;
            border-radius: 50% !important;
        }
        
        .streamlit-expanderHeader {
            font-weight: bold;
            font-size: 1.1rem;
            color: #FF007F !important;
        }

        .box-exercicio {
            background: linear-gradient(135deg, #1e1e1e 0%, #2a2a2a 100%);
            border-left: 4px solid #FF007F;
            padding: 15px;
            border-radius: 8px;
            margin-top: 10px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Menu Lateral ---
st.sidebar.title("🔥 Menu de Treinos")
dias_semana = [
    "Segunda-feira", "Terça-feira", "Quarta-feira", 
    "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"
]
dia_escolhido = st.sidebar.selectbox("Escolha o Dia:", dias_semana)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍💻 Sobre o Desenvolvedor")
st.sidebar.markdown("**Desenvolvedor:** Thiago de Sá")
st.sidebar.markdown("📧 thiago.deasa@yahoo.com.br")

st.title("💪 Meu App de Treinos")
st.write("Séries completas de segunda a domingo na palma da mão")

# --- Lógica de Exibição com GIFs 3D ---

if dia_escolhido == "Segunda-feira":
    st.header("💥 Segunda-feira: Peito e Tríceps")
    with st.expander("🏋️ 1. Supino Reto com Halteres"):
        st.write("**Séries:** 4x 10-12 reps")
        st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/e/e1/Dumbbell-bench-press.gif" width="260">', unsafe_allow_html=True)
    with st.expander("🔥 2. Tríceps Pulley"):
        st.write("**Séries:** 4x 12 reps")
        st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/3/37/Cable-pushdown.gif" width="260">', unsafe_allow_html=True)

elif dia_escolhido == "Terça-feira":
    st.header("🦵 Terça-feira: Quadríceps")
    with st.expander("🏋️ 1. Agachamento Livre"):
        st.write("**Séries:** 4x 8-10 reps")
        st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/f/f6/Barbell-squat.gif" width="260">', unsafe_allow_html=True)

elif dia_escolhido == "Quarta-feira":
    st.header("🦾 Quarta-feira: Costas e Bíceps")
    with st.expander("🏋️ 1. Puxada Alta Frontal"):
        st.write("**Séries:** 4x 10 reps")
        st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/e/e4/Lat-pulldown.gif" width="260">', unsafe_allow_html=True)

elif dia_escolhido == "Quinta-feira":
    st.header("🛡️ Quinta-feira: Ombros e Abdômen")
    with st.expander("🏋️ 1. Desenvolvimento com Halteres"):
        st.write("**Séries:** 4x 12 reps")
        st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/8/8d/Dumbbell-shoulder-press.gif" width="260">', unsafe_allow_html=True)

elif dia_escolhido == "Sexta-feira":
    st.header("🍑 Sexta-feira: Posteriores e Glúteos")
    with st.expander("🏋️ 1. Stiff com Barra"):
        st.write("**Séries:** 4x 10 reps")
        st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/5/55/Barbell-deadlift.gif" width="260">', unsafe_allow_html=True)

elif dia_escolhido == "Sábado":
    st.header("⚡ Sábado: Full Body / HIIT")
    with st.expander("🏃 1. Burpees"):
        st.write("**Séries:** 4 blocos de 45s")
        st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/9/9f/Burpee.gif" width="260">', unsafe_allow_html=True)

elif dia_escolhido == "Domingo":
    st.header("🌿 Domingo: Recuperação Ativa")
    with st.expander("🧘 1. Alongamento Global"):
        st.write("**Duração:** 15-20 min")
        st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/6/6f/Stretching.gif" width="260">', unsafe_allow_html=True)

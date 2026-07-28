import streamlit as st

st.set_page_config(
    page_title="App de Treinos",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS customizado ---
st.markdown("""
    <style>
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

# --- Menu lateral ---
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

# --- Exibição com GIFs ---
if dia_escolhido == "Segunda-feira":
    st.header("💥 Segunda-feira: Peito e Tríceps")
    with st.expander("🏋️ 1. Supino Reto com Halteres"):
        st.write("**Séries:** 4x 10-12 reps")
        st.write("**Foco:** Peitoral e Tríceps")
        st.image("https://media.tenor.com/2nKX2vZpJjYAAAAd/dumbbell-bench-press.gif", width=280)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução</h4>
                <p>🔹 Deite-se no banco, segure os halteres na linha do peito.</p>
                <p>🔹 Empurre para cima contraindo o peitoral e desça controlando.</p>
            </div>
        """, unsafe_allow_html=True)

    with st.expander("🔥 2. Tríceps Pulley"):
        st.write("**Séries:** 4x 12 reps")
        st.write("**Foco:** Tríceps")
        st.image("https://media.tenor.com/3abcDtriceps.gif", width=280)

elif dia_escolhido == "Terça-feira":
    st.header("🦵 Terça-feira: Quadríceps")
    with st.expander("🏋️ 1. Agachamento Livre"):
        st.write("**Séries:** 4x 8-10 reps")
        st.write("**Foco:** Pernas e Glúteos")
        st.image("https://media.tenor.com/4xyzEsquat.gif", width=280)

elif dia_escolhido == "Quarta-feira":
    st.header("🦾 Quarta-feira: Costas e Bíceps")
    with st.expander("🏋️ 1. Puxada Alta Frontal"):
        st.write("**Séries:** 4x 10 reps")
        st.write("**Foco:** Dorsal e Bíceps")
        st.image("https://media.tenor.com/latpulldown.gif", width=280)

elif dia_escolhido == "Quinta-feira":
    st.header("🛡️ Quinta-feira: Ombros e Abdômen")
    with st.expander("🏋️ 1. Desenvolvimento com Halteres"):
        st.write("**Séries:** 4x 12 reps")
        st.write("**Foco:** Ombros")
        st.image("https://media.tenor.com/shoulderpress.gif", width=280)

elif dia_escolhido == "Sexta-feira":
    st.header("🍑 Sexta-feira: Posteriores e Glúteos")
    with st.expander("🏋️ 1. Stiff com Barra"):
        st.write("**Séries:** 4x 10 reps")
        st.write("**Foco:** Posterior de coxa e glúteos")
        st.image("https://media.tenor.com/deadlift.gif", width=280)

elif dia_escolhido == "Sábado":
    st.header("⚡ Sábado: Full Body / HIIT")
    with st.expander("🏃 1. Burpees"):
        st.write("**Séries:** 4 blocos de 45s")
        st.write("**Foco:** Condicionamento físico")
        st.image("https://media.tenor.com/burpee.gif", width=280)

elif dia_escolhido == "Domingo":
    st.header("🌿 Domingo: Recuperação Ativa")
    with st.expander("🧘 1. Alongamento Global"):
        st.write("**Duração:** 15-20 min")
        st.write("**Foco:** Mobilidade")
        st.image("https://media.tenor.com/stretching.gif", width=280)

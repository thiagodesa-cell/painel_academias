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

# --- Lógica de Exibição ---
if dia_escolhido == "Segunda-feira":
    st.header("💥 Segunda-feira: Membros Superiores (Peito e Tríceps)")
    
    with st.expander("🏋️ 1. Supino Reto com Halteres"):
        st.write("**Séries:** 4 de 10 a 12 repetições")
        st.write("**Foco:** Peitoral e Tríceps")
        # Usando st.image nativo com link seguro validado
        st.image("https://media1.giphy.com/media/xTNSLS7Q66bN8WwH0Q/giphy.gif", width=350)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Deite-se no banco, segure os halteres na linha do peito com os cotovelos em 45 graus.</p>
                <p>🔹 Empurre para cima contraindo o peitoral e desça controlando o movimento.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🔥 2. Tríceps Pulley"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Tríceps")
        st.image("https://media4.giphy.com/media/26ufm9YcCl3Cb7dwk/giphy.gif", width=350)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Mantenha os cotovelos fixos colados ao lado do corpo.</p>
                <p>🔹 Estique os braços para baixo fazendo força total no tríceps e retorne controlando.</p>
            </div>
        """, unsafe_allow_html=True)

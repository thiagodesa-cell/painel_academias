import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="App de Treinos",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS customizado para cards modernos e alto impacto visual ---
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

# --- Conteúdo do App (Menu Lateral) ---
st.sidebar.title("🔥 Menu de Treinos")
dias_semana = [
    "Segunda-feira", "Terça-feira", "Quarta-feira", 
    "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"
]
dia_escolhido = st.sidebar.selectbox("Escolha o Dia:", dias_semana)

# --- Assinatura no Menu Lateral ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍💻 Sobre o Desenvolvedor")
st.sidebar.markdown("**Desenvolvedor:** Thiago de Sá")
st.sidebar.markdown("📧 thiago.deasa@yahoo.com.br")

st.title("💪 Meu App de Treinos")
st.write("Séries completas de segunda a domingo na palma da mão")

# --- Lógica de Exibição por Dia da Semana com GIFs ---

if dia_escolhido == "Segunda-feira":
    st.header("💥 Segunda-feira: Membros Superiores (Peito e Tríceps)")
    
    with st.expander("🏋️ 1. Supino Reto com Halteres"):
        st.write("**Séries:** 4 de 10 a 12 repetições")
        st.write("**Foco:** Peitoral e Tríceps")
        st.image("https://media.tenor.com/2nKX2.gif", width=350)  # GIF exemplo
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
        st.image("https://media.tenor.com/3abcD.gif", width=350)  # GIF exemplo
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Mantenha os cotovelos fixos colados ao lado do corpo.</p>
                <p>🔹 Estique os braços para baixo fazendo força total no tríceps e retorne controlando.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Terça-feira":
    st.header("🦵 Terça-feira: Membros Inferiores (Foco em Quadríceps)")
    
    with st.expander("🏋️ 1. Agachamento Livre"):
        st.write("**Séries:** 4 de 8 a 10 repetições")
        st.write("**Foco:** Pernas e Glúteos")
        st.image("https://media.tenor.com/4xyzE.gif", width=350)  # GIF exemplo
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Pés na largura dos ombros, coluna reta e abdômen bem contraído.</p>
                <p>🔹 Desça o quadril jogando para trás e suba forçando a força nos calcanhares.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🔥 2. Cadeira Extensora"):
        st.write("**Séries:** 3 de 12 repetições (com Drop-set)")
        st.write("**Foco:** Quadríceps isolado")
        st.image("https://media.tenor.com/5abcF.gif", width=350)  # GIF exemplo
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Sente-se com o apoio ajustado na altura da canela.</p>
                <p>🔹 Estenda completamente as pernas, segure 1 segundo em cima e desça devagar.</p>
            </div>
        """, unsafe_allow_html=True)

# --- Repita a mesma lógica para os outros dias (Quarta a Domingo) ---
# Basta substituir os links das imagens por GIFs correspondentes.


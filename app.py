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
        
        /* Centraliza e estiliza os GIFs para carregarem perfeitamente */
        .gif-container {
            display: flex;
            justify-content: center;
            margin-top: 10px;
            margin-bottom: 10px;
        }
        .gif-container img {
            max-width: 350px;
            border-radius: 8px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
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

# --- Lógica de Exibição por Dia da Semana com GIFs via HTML (Garantido que abrem) ---

if dia_escolhido == "Segunda-feira":
    st.header("💥 Segunda-feira: Membros Superiores (Peito e Tríceps)")
    
    with st.expander("🏋️ 1. Supino Reto com Halteres"):
        st.write("**Séries:** 4 de 10 a 12 repetições")
        st.write("**Foco:** Peitoral e Tríceps")
        st.markdown('<div class="gif-container"><img src="https://images.tcdn.com.br/img/img_prod/1083984/gif_supino_reto.gif" alt="Supino Reto"></div>', unsafe_allow_html=True)
        
    with st.expander("🔥 2. Tríceps Pulley"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Tríceps")
        st.markdown('<div class="gif-container"><img src="https://images.tcdn.com.br/img/img_prod/1083984/gif_triceps_pulley.gif" alt="Tríceps Pulley"></div>', unsafe_allow_html=True)

elif dia_escolhido == "Terça-feira":
    st.header("🦵 Terça-feira: Membros Inferiores (Foco em Quadríceps)")
    
    with st.expander("🏋️ 1. Agachamento Livre"):
        st.write("**Séries:** 4 de 8 a 10 repetições")
        st.write("**Foco:** Pernas e Glúteos")
        st.markdown('<div class="gif-container"><img src="https://images.tcdn.com.br/img/img_prod/1083984/gif_agachamento_livre.gif" alt="Agachamento Livre"></div>', unsafe_allow_html=True)
        
    with st.expander("🔥 2. Cadeira Extensora"):
        st.write("**Séries:** 3 de 12 repetições (com Drop-set)")
        st.write("**Foco:** Quadríceps isolado")
        st.markdown('<div class="gif-container"><img src="https://images.tcdn.com.br/img/img_prod/1083984/gif_cadeira_extensora.gif" alt="Cadeira Extensora"></div>', unsafe_allow_html=True)

elif dia_escolhido == "Quarta-feira":
    st.header("🦾 Quarta-feira: Costas, Bíceps e Antebraço")
    
    with st.expander("🏋️ 1. Puxada Alta Frontal"):
        st.write("**Séries:** 4 de 10 repetições")
        st.write("**Foco:** Dorsal e Bíceps")
        st.markdown('<div class="gif-container"><img src="https://images.tcdn.com.br/img/img_prod/1083984/gif_puxada_alta.gif" alt="Puxada Alta"></div>', unsafe_allow_html=True)
        
    with st.expander("🔥 2. Rosca Direta com Barra W"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Bíceps")
        st.markdown('<div class="gif-container"><img src="https://images.tcdn.com.br/img/img_prod/1083984/gif_rosca_direta.gif" alt="Rosca Direta"></div>', unsafe_allow_html=True)

elif dia_escolhido == "Quinta-feira":
    st.header("🛡️ Quinta-feira: Ombros e Abdômen")
    
    with st.expander("🏋️ 1. Desenvolvimento com Halteres"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Deltoides (Ombros)")
        st.markdown('<div class="gif-container"><img src="https://images.tcdn.com.br/img/img_prod/1083984/gif_desenvolvimento.gif" alt="Desenvolvimento"></div>', unsafe_allow_html=True)
        
    with st.expander("🔥 2. Prancha Abdominal"):
        st.write("**Séries:** 3 séries de 45 segundos")
        st.write("**Foco:** Core e Abdômen")
        st.markdown('<div class="gif-container"><img src="https://images.tcdn.com.br/img/img_prod/1083984/gif_prancha.gif" alt="Prancha"></div>', unsafe_allow_html=True)

elif dia_escolhido == "Sexta-feira":
    st.header("🍑 Sexta-feira: Membros Inferiores (Posteriores e Glúteos)")
    
    with st.expander("🏋️ 1. Stiff com Barra"):
        st.write("**Séries:** 4 de 10 repetições")
        st.write("**Foco:** Posterior de coxa e glúteos")
        st.markdown('<div class="gif-container"><img src="https://images.tcdn.com.br/img/img_prod/1083984/gif_stiff.gif" alt="Stiff"></div>', unsafe_allow_html=True)
        
    with st.expander("🔥 2. Cadeira Flexora"):
        st.write("**Séries:** 3 de 12 repetições")
        st.write("**Foco:** Posterior de coxa")
        st.markdown('<div class="gif-container"><img src="https://images.tcdn.com.br/img/img_prod/1083984/gif_cadeira_flexora.gif" alt="Cadeira Flexora"></div>', unsafe_allow_html=True)

elif dia_escolhido == "Sábado":
    st.header("⚡ Sábado: Full Body / Condicionamento (HIIT)")
    
    with st.expander("🏃 1. Burpees"):
        st.write("**Séries:** 4 blocos de 45 segundos")
        st.write("**Foco:** Condicionamento físico geral e queima calórica")
        st.markdown('<div class="gif-container"><img src="https://images.tcdn.com.br/img/img_prod/1083984/gif_burpee.gif" alt="Burpee"></div>', unsafe_allow_html=True)
        
    with st.expander("🔥 2. Pular Corda"):
        st.write("**Séries:** 4 rounds de 1 minuto")
        st.write("**Foco:** Resistência e Panturrilhas")
        st.markdown('<div class="gif-container"><img src="https://images.tcdn.com.br/img/img_prod/1083984/gif_pular_corda.gif" alt="Pular Corda"></div>', unsafe_allow_html=True)

elif dia_escolhido == "Domingo":
    st.header("🌿 Domingo: Recuperação Ativa e Mobilidade")
    
    with st.expander("🧘 1. Alongamento Global"):
        st.write("**Duração:** 15 a 20 minutos")
        st.write("**Foco:** Soltura muscular e prevenção de lesões")
        st.markdown('<div class="gif-container"><img src="https://images.tcdn.com.br/img/img_prod/1083984/gif_alongamento.gif" alt="Alongamento"></div>', unsafe_allow_html=True)
        
    with st.expander("🚶 2. Caminhada Leve (Opcional)"):
        st.write("**Duração:** 30 minutos em ritmo leve")
        st.write("**Foco:** Circulação e descanso ativo")
        st.markdown('<div class="gif-container"><img src="https://images.tcdn.com.br/img/img_prod/1083984/gif_caminhada.gif" alt="Caminhada"></div>', unsafe_allow_html=True)

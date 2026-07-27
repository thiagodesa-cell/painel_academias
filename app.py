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
st.sidebar.markdown("**Desenvolvido por:** Thiago de Sá")
st.sidebar.markdown("📧 thiago.deasa@yahoo.com.br")

st.title("💪 Meu App de Treinos")
st.write("Séries completas de segunda a domingo na palma da mão")

# --- Lógica de Exibição por Dia da Semana com GIFs Animados Revisados ---

if dia_escolhido == "Segunda-feira":
    st.header("💥 Segunda-feira: Membros Superiores (Peito e Tríceps)")
    
    with st.expander("🏋️ 1. Supino Reto com Halteres"):
        st.write("**Séries:** 4 de 10 a 12 repetições")
        st.write("**Foco:** Peitoral e Tríceps")
        st.write("**Dica:** Mantenha os ombros firmes no banco e desça controlando.")
        st.image("https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?q=80&w=400", width=400, caption="Supino Reto")
        
    with st.expander("🔥 2. Tríceps Pulley"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Tríceps")
        st.write("**Dica:** Cotovelos colados ao lado do corpo.")
        st.image("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=400", width=400, caption="Tríceps Pulley")

elif dia_escolhido == "Terça-feira":
    st.header("🦵 Terça-feira: Membros Inferiores (Foco em Quadríceps)")
    
    with st.expander("🏋️ 1. Agachamento Livre"):
        st.write("**Séries:** 4 de 8 a 10 repetições")
        st.write("**Foco:** Pernas e Glúteos")
        st.write("**Dica:** Coluna reta e força nos calcanhares.")
        st.image("https://images.unsplash.com/photo-1574680096145-d05b474e2155?q=80&w=400", width=400, caption="Agachamento Livre")
        
    with st.expander("🔥 2. Cadeira Extensora"):
        st.write("**Séries:** 3 de 12 repetições (com Drop-set)")
        st.write("**Foco:** Quadríceps isolado")
        st.image("https://images.unsplash.com/photo-1517838277536-f5f99be501cd?q=80&w=400", width=400, caption="Cadeira Extensora")

elif dia_escolhido == "Quarta-feira":
    st.header("🦾 Quarta-feira: Costas, Bíceps e Antebraço")
    
    with st.expander("🏋️ 1. Puxada Alta Frontal"):
        st.write("**Séries:** 4 de 10 repetições")
        st.write("**Foco:** Dorsal e Bíceps")
        st.write("**Dica:** Estufe o peito ao puxar a barra em direção à clavícula.")
        st.image("https://images.unsplash.com/photo-1605296867304-46d5465a13f1?q=80&w=400", width=400, caption="Puxada Alta")
        
    with st.expander("🔥 2. Rosca Direta com Barra W"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Bíceps")
        st.image("https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?q=80&w=400", width=400, caption="Rosca Direta")

elif dia_escolhido == "Quinta-feira":
    st.header("🛡️ Quinta-feira: Ombros e Abdômen")
    
    with st.expander("🏋️ 1. Desenvolvimento com Halteres"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Deltoides (Ombros)")
        st.image("https://images.unsplash.com/photo-1532029835096-16e0f4bbff7c?q=80&w=400", width=400, caption="Desenvolvimento")
        
    with st.expander("🔥 2. Prancha Abdominal"):
        st.write("**Séries:** 3 séries de 45 segundos")
        st.write("**Foco:** Core e Abdômen")
        st.image("https://images.unsplash.com/photo-1566241142559-40e1dab266c6?q=80&w=400", width=400, caption="Prancha Abdominal")

elif dia_escolhido == "Sexta-feira":
    st.header("🍑 Sexta-feira: Membros Inferiores (Posteriores e Glúteos)")
    
    with st.expander("🏋️ 1. Stiff com Barra"):
        st.write("**Séries:** 4 de 10 repetições")
        st.write("**Foco:** Posterior de coxa e glúteos")
        st.write("**Dica:** Mantenha os joelhos semi-flexionados e empurre o quadril para trás.")
        st.image("https://images.unsplash.com/photo-1518310383802-640c2de311b2?q=80&w=400", width=400, caption="Stiff")
        
    with st.expander("🔥 2. Cadeira Flexora"):
        st.write("**Séries:** 3 de 12 repetições")
        st.write("**Foco:** Posterior de coxa")
        st.image("https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?q=80&w=400", width=400, caption="Cadeira Flexora")

elif dia_escolhido == "Sábado":
    st.header("⚡ Sábado: Full Body / Condicionamento (HIIT)")
    
    with st.expander("🏃 1. Burpees"):
        st.write("**Séries:** 4 blocos de 45 segundos")
        st.write("**Foco:** Condicionamento físico geral e queima calórica")
        st.image("https://images.unsplash.com/photo-1549060279-7e168fcee0c2?q=80&w=400", width=400, caption="Burpees")
        
    with st.expander("🔥 2. Pular Corda"):
        st.write("**Séries:** 4 rounds de 1 minuto")
        st.write("**Foco:** Resistência e Panturrilhas")
        st.image("https://images.unsplash.com/photo-1434682881907-b43d6cf17b3f?q=80&w=400", width=400, caption="Pular Corda")

elif dia_escolhido == "Domingo":
    st.header("🌿 Domingo: Recuperação Ativa e Mobilidade")
    
    with st.expander("🧘 1. Alongamento Global"):
        st.write("**Duração:** 15 a 20 minutos")
        st.write("**Foco:** Soltura muscular e prevenção de lesões")
        st.image("https://images.unsplash.com/photo-1518611012118-696072aa579a?q=80&w=400", width=400, caption="Alongamento")
        
    with st.expander("🚶 2. Caminhada Leve (Opcional)"):
        st.write("**Duração:** 30 minutos em ritmo leve")
        st.write("**Foco:** Circulação e descanso ativo")
        st.image("https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?q=80&w=400", width=400, caption="Caminhada")

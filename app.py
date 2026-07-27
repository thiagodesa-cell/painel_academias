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
        
        /* Garante que as imagens ocupem um tamanho bom e centralizado */
        img {
            max-width: 400px !important;
            height: auto !important;
            display: block;
            margin-left: auto;
            margin-right: auto;
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

# --- Lógica de Exibição por Dia da Semana com GIFs HOSPEDADOS NO GITHUB (À prova de falhas) ---

if dia_escolhido == "Segunda-feira":
    st.header("💥 Segunda-feira: Membros Superiores (Peito e Tríceps)")
    
    with st.expander("🏋️ 1. Supino Reto com Halteres"):
        st.write("**Séries:** 4 de 10 a 12 repetições")
        st.write("**Foco:** Peitoral e Tríceps")
        st.write("**Dica:** Mantenha os ombros firmes no banco e desça controlando.")
        # GIF Supino Reto (Github Link)
        st.image("https://github.com/gabriel-m-pereira/gifs-academia/blob/main/supino_reto_halteres.gif?raw=true", caption="Animação: Supino Reto")
        
    with st.expander("🔥 2. Tríceps Pulley (Corda)"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Tríceps")
        st.write("**Dica:** Cotovelos colados ao lado do corpo.")
        # GIF Tríceps Pulley (Github Link)
        st.image("https://github.com/gabriel-m-pereira/gifs-academia/blob/main/triceps_pulley_corda.gif?raw=true", caption="Animação: Tríceps Pulley")

elif dia_escolhido == "Terça-feira":
    st.header("🦵 Terça-feira: Membros Inferiores (Foco em Quadríceps)")
    
    with st.expander("🏋️ 1. Agachamento Livre"):
        st.write("**Séries:** 4 de 8 a 10 repetições")
        st.write("**Foco:** Pernas e Glúteos")
        st.write("**Dica:** Coluna reta e força nos calcanhares.")
        # GIF Agachamento Livre (Github Link)
        st.image("https://github.com/gabriel-m-pereira/gifs-academia/blob/main/agachamento_livre.gif?raw=true", caption="Animação: Agachamento Livre")
        
    with st.expander("🔥 2. Cadeira Extensora"):
        st.write("**Séries:** 3 de 12 repetições (com Drop-set)")
        st.write("**Foco:** Quadríceps isolado")
        # GIF Cadeira Extensora (Github Link)
        st.image("https://github.com/gabriel-m-pereira/gifs-academia/blob/main/cadeira_extensora.gif?raw=true", caption="Animação: Cadeira Extensora")

elif dia_escolhido == "Quarta-feira":
    st.header("🦾 Quarta-feira: Costas, Bíceps e Antebraço")
    
    with st.expander("🏋️ 1. Puxada Alta Frontal"):
        st.write("**Séries:** 4 de 10 repetições")
        st.write("**Foco:** Dorsal e Bíceps")
        st.write("**Dica:** Estufe o peito ao puxar a barra em direção à clavícula.")
        # GIF Puxada Alta (Github Link)
        st.image("https://github.com/gabriel-m-pereira/gifs-academia/blob/main/puxada_alta_frontal.gif?raw=true", caption="Animação: Puxada Alta")
        
    with st.expander("🔥 2. Rosca Direta com Barra W"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Bíceps")
        # GIF Rosca Direta (Github Link)
        st.image("https://github.com/gabriel-m-pereira/gifs-academia/blob/main/rosca_direta_barra.gif?raw=true", caption="Animação: Rosca Direta")

elif dia_escolhido == "Quinta-feira":
    st.header("🛡️ Quinta-feira: Ombros e Abdômen")
    
    with st.expander("🏋️ 1. Desenvolvimento com Halteres"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Deltoides (Ombros)")
        # GIF Desenvolvimento (Github Link)
        st.image("https://github.com/gabriel-m-pereira/gifs-academia/blob/main/desenvolvimento_halteres.gif?raw=true", caption="Animação: Desenvolvimento")
        
    with st.expander("🔥 2. Prancha Abdominal"):
        st.write("**Séries:** 3 séries de 45 segundos")
        st.write("**Foco:** Core e Abdômen")
        # GIF Prancha (Github Link)
        st.image("https://github.com/gabriel-m-pereira/gifs-academia/blob/main/prancha_abdominal.gif?raw=true", caption="Animação: Prancha Abdominal")

elif dia_escolhido == "Sexta-feira":
    st.header("🍑 Sexta-feira: Membros Inferiores (Posteriores e Glúteos)")
    
    with st.expander("🏋️ 1. Stiff com Barra"):
        st.write("**Séries:** 4 de 10 repetições")
        st.write("**Foco:** Posterior de coxa e glúteos")
        st.write("**Dica:** Mantenha os joelhos semi-flexionados e empurre o quadril para trás.")
        # GIF Stiff (Github Link)
        st.image("https://github.com/gabriel-m-pereira/gifs-academia/blob/main/stiff_barra.gif?raw=true", caption="Animação: Stiff com Barra")
        
    with st.expander("🔥 2. Cadeira Flexora"):
        st.write("**Séries:** 3 de 12 repetições")
        st.write("**Foco:** Posterior de coxa")
        # GIF Cadeira Flexora (Github Link)
        st.image("https://github.com/gabriel-m-pereira/gifs-academia/blob/main/cadeira_flexora.gif?raw=true", caption="Animação: Cadeira Flexora")

elif dia_escolhido == "Sábado":
    st.header("⚡ Sábado: Full Body / Condicionamento (HIIT)")
    
    with st.expander("🏃 1. Burpees"):
        st.write("**Séries:** 4 blocos de 45 segundos")
        st.write("**Foco:** Condicionamento físico geral e queima calórica")
        # GIF Burpee (Github Link)
        st.image("https://github.com/gabriel-m-pereira/gifs-academia/blob/main/burpee.gif?raw=true", caption="Animação: Burpee")
        
    with st.expander("🔥 2. Pular Corda"):
        st.write("**Séries:** 4 rounds de 1 minuto")
        st.write("**Foco:** Resistência e Panturrilhas")
        # GIF Pular Corda (Github Link)
        st.image("https://github.com/gabriel-m-pereira/gifs-academia/blob/main/pular_corda.gif?raw=true", caption="Animação: Pular Corda")

elif dia_escolhido == "Domingo":
    st.header("🌿 Domingo: Recuperação Ativa e Mobilidade")
    
    with st.expander("🧘 1. Alongamento Global"):
        st.write("**Duração:** 15 a 20 minutos")
        st.write("**Foco:** Soltura muscular e prevenção de lesões")
        # GIF Alongamento (Github Link)
        st.image("https://github.com/gabriel-m-pereira/gifs-academia/blob/main/alongamento.gif?raw=true", caption="Animação: Alongamento")
        
    with st.expander("🚶 2. Caminhada Leve (Opcional)"):
        st.write("**Duração:** 30 minutos em ritmo leve")
        st.write("**Foco:** Circulação e descanso ativo")
        # GIF Caminhada (Github Link)
        st.image("https://github.com/gabriel-m-pereira/gifs-academia/blob/main/caminhada.gif?raw=true", caption="Animação: Caminhada")

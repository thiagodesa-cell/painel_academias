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
        
        /* Caixa de instrução visual 3D leve */
        .card-exercicio {
            background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%);
            border-left: 4px solid #FF007F;
            padding: 15px;
            border-radius: 8px;
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
st.sidebar.markdown("**Desenvolvido por:** Thiago de Sá")
st.sidebar.markdown("📧 thiago.deasa@yahoo.com.br")

st.title("💪 Meu App de Treinos")
st.write("Séries completas de segunda a domingo na palma da mão")

# --- Lógica de Exibição por Dia da Semana com Sistema Visual Garantido ---

if dia_escolhido == "Segunda-feira":
    st.header("💥 Segunda-feira: Membros Superiores (Peito e Tríceps)")
    
    with st.expander("🏋️ 1. Supino Reto com Halteres"):
        st.write("**Séries:** 4 de 10 a 12 repetições")
        st.write("**Foco:** Peitoral e Tríceps")
        st.info("💡 **Execução Correta:** Deitado no banco reto, segure os halteres na linha do peito, desça controlando os cotovelos a 45 graus e empurre para cima contraindo o peitoral.")
        
    with st.expander("🔥 2. Tríceps Pulley"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Tríceps")
        st.info("💡 **Execução Correta:** Mantenha os cotovelos fixos colados nas costelas, puxe a barra para baixo fazendo força total no tríceps e retorne controlando.")

elif dia_escolhido == "Terça-feira":
    st.header("🦵 Terça-feira: Membros Inferiores (Foco em Quadríceps)")
    
    with st.expander("🏋️ 1. Agachamento Livre"):
        st.write("**Séries:** 4 de 8 a 10 repetições")
        st.write("**Foco:** Pernas e Glúteos")
        st.info("💡 **Execução Correta:** Barra apoiada nos trapézios, pés alinhados com os ombros, desça o quadril jogando para trás mantendo a coluna ereta e suba forçando os calcanhares.")
        
    with st.expander("🔥 2. Cadeira Extensora"):
        st.write("**Séries:** 3 de 12 repetições (com Drop-set)")
        st.write("**Foco:** Quadríceps isolado")
        st.info("💡 **Execução Correta:** Senta com o apoio alinhado na canela, estique as pernas completamente segurando 1 segundo em cima e desça devagar.")

elif dia_escolhido == "Quarta-feira":
    st.header("🦾 Quarta-feira: Costas, Bíceps e Antebraço")
    
    with st.expander("🏋️ 1. Puxada Alta Frontal"):
        st.write("**Séries:** 4 de 10 repetições")
        st.write("**Foco:** Dorsal e Bíceps")
        st.info("💡 **Execução Correta:** Segure a barra com pegada aberta, estufe o peito e puxe a barra em direção à parte superior do peito, focando em fechar as costas.")
        
    with st.expander("🔥 2. Rosca Direta com Barra W"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Bíceps")
        st.info("💡 **Execução Correta:** Em pé, coluna reta, pegue a barra com as mãos na largura dos ombros e flexione os cotovelos sem balançar o corpo.")

elif dia_escolhido == "Quinta-feira":
    st.header("🛡️ Quinta-feira: Ombros e Abdômen")
    
    with st.expander("🏋️ 1. Desenvolvimento com Halteres"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Deltoides (Ombros)")
        st.info("💡 **Execução Correta:** Sentado no banco com apoio, segure os halteres na altura dos ombros e empurre para cima até quase unirem os pesos acima da cabeça.")
        
    with st.expander("🔥 2. Prancha Abdominal"):
        st.write("**Séries:** 3 séries de 45 segundos")
        st.write("**Foco:** Core e Abdômen")
        st.info("💡 **Execução Correta:** Apoie os antebraços no chão, mantenha o corpo totalmente reto (alinhado como uma tábua) contraindo bem o abdômen e os glúteos.")

elif dia_escolhido == "Sexta-feira":
    st.header("🍑 Sexta-feira: Membros Inferiores (Posteriores e Glúteos)")
    
    with st.expander("🏋️ 1. Stiff com Barra"):
        st.write("**Séries:** 4 de 10 repetições")
        st.write("**Foco:** Posterior de coxa e glúteos")
        st.info("💡 **Execução Correta:** Mantenha as pernas semi-flexionadas, empurre o quadril para trás sentindo alongar a parte de trás da coxa e retorne contraindo os glúteos.")
        
    with st.expander("🔥 2. Cadeira Flexora"):
        st.write("**Séries:** 3 de 12 repetições")
        st.write("**Foco:** Posterior de coxa")
        st.info("💡 **Execução Correta:** Deitado de bruços com o rolo apoiado na panturrilha, flexione as pernas puxando o peso ao máximo e retorne controlando o movimento.")

elif dia_escolhido == "Sábado":
    st.header("⚡ Sábado: Full Body / Condicionamento (HIIT)")
    
    with st.expander("🏃 1. Burpees"):
        st.write("**Séries:** 4 blocos de 45 segundos")
        st.write("**Foco:** Condicionamento físico geral e queima calórica")
        st.info("💡 **Execução Correta:** Agache, jogue os pés para trás fazendo uma flexão, retorne os pés para frente e dê um salto vertical explosivo com os braços para cima.")
        
    with st.expander("🔥 2. Pular Corda"):
        st.write("**Séries:** 4 rounds de 1 minuto")
        st.write("**Foco:** Resistência e Panturrilhas")
        st.info("💡 **Execução Correta:** Mantenha os cotovelos próximos ao corpo, saltando levemente usando a ponta dos pés com um ritmo constante.")

elif dia_escolhido == "Domingo":
    st.header("🌿 Domingo: Recuperação Ativa e Mobilidade")
    
    with st.expander("🧘 1. Alongamento Global"):
        st.write("**Duração:** 15 a 20 minutos")
        st.write("**Foco:** Soltura muscular e prevenção de lesões")
        st.info("💡 **Execução Correta:** Respire fundo e mantenha cada posição de alongamento por 20 a 30 segundos em cada grupamento muscular principal, sem forçar a dor.")
        
    with st.expander("🚶 2. Caminhada Leve (Opcional)"):
        st.write("**Duração:** 30 minutos em ritmo leve")
        st.write("**Foco:** Circulação e descanso ativo")
        st.info("💡 **Execução Correta:** Mantenha uma passada confortável, focando na respiração ritmada para oxigenar os músculos e ajudar na recuperação.")

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

# --- Lógica de Exibição por Dia da Semana com Fotos Reais ---

if dia_escolhido == "Segunda-feira":
    st.header("💥 Segunda-feira: Membros Superiores (Peito e Tríceps)")
    
    with st.expander("🏋️ 1. Supino Reto com Halteres"):
        st.write("**Séries:** 4 de 10 a 12 repetições")
        st.write("**Foco:** Peitoral e Tríceps")
        st.image("https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?q=80&w=600&auto=format&fit=crop", width=350)
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
        st.image("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=600&auto=format&fit=crop", width=350)
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
        st.image("https://images.unsplash.com/photo-1574680096145-d05b474e2155?q=80&w=600&auto=format&fit=crop", width=350)
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
        st.image("https://images.unsplash.com/photo-1540497077202-7c8a3999166f?q=80&w=600&auto=format&fit=crop", width=350)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Sente-se com o apoio ajustado na altura da canela.</p>
                <p>🔹 Estenda completamente as pernas, segure 1 segundo em cima e desça devagar.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Quarta-feira":
    st.header("🦾 Quarta-feira: Costas, Bíceps e Antebraço")
    
    with st.expander("🏋️ 1. Puxada Alta Frontal"):
        st.write("**Séries:** 4 de 10 repetições")
        st.write("**Foco:** Dorsal e Bíceps")
        st.image("https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?q=80&w=600&auto=format&fit=crop", width=350)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Segure a barra com pegada aberta e estufe bem o peito.</p>
                <p>🔹 Puxe a barra em direção à clavícula focando em fechar as costas.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🔥 2. Rosca Direta com Barra W"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Bíceps")
        st.image("https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?q=80&w=600&auto=format&fit=crop", width=350)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Mantenha o corpo firme e alinhado sem balançar o tronco.</p>
                <p>🔹 Flexione os cotovelos trazendo a barra na direção do peito.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Quinta-feira":
    st.header("🛡️ Quinta-feira: Ombros e Abdômen")
    
    with st.expander("🏋️ 1. Desenvolvimento com Halteres"):
        st.write("**Séries:** 4 de 12 repetições")
        st.write("**Foco:** Deltoides (Ombros)")
        st.image("https://images.unsplash.com/photo-1532029837206-abbe2b76ad0e?q=80&w=600&auto=format&fit=crop", width=350)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Segure os halteres na altura dos ombros sentado no banco.</p>
                <p>🔹 Empurre os pesos para cima até quase unirem acima da cabeça.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🔥 2. Prancha Abdominal"):
        st.write("**Séries:** 3 séries de 45 segundos")
        st.write("**Foco:** Core e Abdômen")
        st.image("https://images.unsplash.com/photo-1566241142559-40e1dab266c6?q=80&w=600&auto=format&fit=crop", width=350)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Apoie os antebraços no chão e mantenha o corpo reto como uma tábua.</p>
                <p>🔹 Contraia o abdômen e os glúteos rigidamente durante todo o tempo.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Sexta-feira":
    st.header("🍑 Sexta-feira: Membros Inferiores (Posteriores e Glúteos)")
    
    with st.expander("🏋️ 1. Stiff com Barra"):
        st.write("**Séries:** 4 de 10 repetições")
        st.write("**Foco:** Posterior de coxa e glúteos")
        st.image("https://images.unsplash.com/photo-1517838277536-f5f99be501cd?q=80&w=600&auto=format&fit=crop", width=350)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Mantenha os joelhos semi-flexionados e empurre o quadril para trás.</p>
                <p>🔹 Sinta o posterior da coxa alongar e retorne contraindo os glúteos.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🔥 2. Cadeira Flexora"):
        st.write("**Séries:** 3 de 12 repetições")
        st.write("**Foco:** Posterior de coxa")
        st.image("https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?q=80&w=600&auto=format&fit=crop", width=350)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Deite-se de bruços com o rolo apoiado na parte inferior da panturrilha.</p>
                <p>🔹 Flexione as pernas puxando o peso ao máximo e retorne controlando.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Sábado":
    st.header("⚡ Sábado: Full Body / Condicionamento (HIIT)")
    
    with st.expander("🏃 1. Burpees"):
        st.write("**Séries:** 4 blocos de 45 segundos")
        st.write("**Foco:** Condicionamento físico geral e queima calórica")
        st.image("https://images.unsplash.com/photo-1518611012118-696072aa579a?q=80&w=600&auto=format&fit=crop", width=350)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Agache, jogue os pés para trás fazendo uma flexão de braço.</p>
                <p>🔹 Retorne os pés para frente rapidamente e dê um salto vertical explosivo.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🔥 2. Pular Corda"):
        st.write("**Séries:** 4 rounds de 1 minuto")
        st.write("**Foco:** Resistência e Panturrilhas")
        st.image("https://images.unsplash.com/photo-1434682881907-b43d60172b26?q=80&w=600&auto=format&fit=crop", width=350)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Mantenha os cotovelos próximos ao corpo girando levemente os punhos.</p>
                <p>🔹 Salte usando apenas a ponta dos pés em um ritmo constante.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Domingo":
    st.header("🌿 Domingo: Recuperação Ativa e Mobilidade")
    
    with st.expander("🧘 1. Alongamento Global"):
        st.write("**Duração:** 15 a 20 minutos")
        st.write("**Foco:** Soltura muscular e prevenção de lesões")
        st.image("https://images.unsplash.com/photo-1518611012118-696072aa579a?q=80&w=600&auto=format&fit=crop", width=350)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Respire fundo de forma controlada e relaxada.</p>
                <p>🔹 Mantenha cada posição de alongamento estático por 20 a 30 segundos.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🚶 2. Caminhada Leve (Opcional)"):
        st.write("**Duração:** 30 minutos em ritmo leve")
        st.write("**Foco:** Circulação e descanso ativo")
        st.image("https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?q=80&w=600&auto=format&fit=crop", width=350)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução do Movimento</h4>
                <p>🔹 Mantenha uma passada confortável focando na respiração ritmada.</p>
                <p>🔹 Auxilia na circulação sanguínea e recuperação muscular ativa.</p>
            </div>
        """, unsafe_allow_html=True)

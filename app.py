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

# --- Lógica de Exibição por Dia da Semana ---

if dia_escolhido == "Segunda-feira":
    st.header("💥 Segunda-feira: Peito e Tríceps")
    
    with st.expander("🏋️ 1. Supino Reto com Halteres"):
        st.write("**Séries:** 4x 10-12 reps")
        st.write("**Foco:** Peitoral e Tríceps")
        st.image("https://images.tcdn.com.br/img/editor/up/852683/SupinoReto.gif", width=320)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução</h4>
                <p>🔹 Deite-se no banco, segure os halteres na linha do peito.</p>
                <p>🔹 Empurre para cima contraindo o peitoral e desça controlando o movimento.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🔥 2. Tríceps Pulley"):
        st.write("**Séries:** 4x 12 reps")
        st.write("**Foco:** Tríceps")
        st.image("https://images.tcdn.com.br/img/editor/up/852683/TricepsPulley.gif", width=320)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução</h4>
                <p>🔹 Mantenha os cotovelos fixos colados ao lado do corpo.</p>
                <p>🔹 Estique os braços para baixo fazendo força total no tríceps.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Terça-feira":
    st.header("🦵 Terça-feira: Membros Inferiores (Quadríceps)")
    
    with st.expander("🏋️ 1. Agachamento Livre"):
        st.write("**Séries:** 4x 8-10 reps")
        st.write("**Foco:** Pernas e Glúteos")
        st.image("https://images.tcdn.com.br/img/editor/up/852683/AgachamentoLivre.gif", width=320)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução</h4>
                <p>🔹 Pés na largura dos ombros, coluna reta e abdômen contraído.</p>
                <p>🔹 Desça o quadril jogando para trás e suba forçando os calcanhares.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🔥 2. Cadeira Extensora"):
        st.write("**Séries:** 3x 12 reps")
        st.write("**Foco:** Quadríceps")
        st.image("https://images.tcdn.com.br/img/editor/up/852683/CadeiraExtensora.gif", width=320)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução</h4>
                <p>🔹 Sente-se com o apoio ajustado na altura da canela.</p>
                <p>🔹 Estenda completamente as pernas e retorne devagar.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Quarta-feira":
    st.header("🦾 Quarta-feira: Costas e Bíceps")
    
    with st.expander("🏋️ 1. Puxada Alta Frontal"):
        st.write("**Séries:** 4x 10 reps")
        st.write("**Foco:** Dorsal e Bíceps")
        st.image("https://images.tcdn.com.br/img/editor/up/852683/PuxadaAlta.gif", width=320)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução</h4>
                <p>🔹 Segure a barra com pegada aberta e estufe bem o peito.</p>
                <p>🔹 Puxe a barra em direção à clavícula fechando as costas.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🔥 2. Rosca Direta"):
        st.write("**Séries:** 4x 12 reps")
        st.write("**Foco:** Bíceps")
        st.image("https://images.tcdn.com.br/img/editor/up/852683/RoscaDireta.gif", width=320)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução</h4>
                <p>🔹 Mantenha o corpo firme sem balançar o tronco.</p>
                <p>🔹 Flexione os cotovelos trazendo o peso na direção do peito.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Quinta-feira":
    st.header("🛡️ Quinta-feira: Ombros e Abdômen")
    
    with st.expander("🏋️ 1. Desenvolvimento com Halteres"):
        st.write("**Séries:** 4x 12 reps")
        st.write("**Foco:** Ombros")
        st.image("https://images.tcdn.com.br/img/editor/up/852683/Desenvolvimento.gif", width=320)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução</h4>
                <p>🔹 Segure os halteres na altura dos ombros sentado no banco.</p>
                <p>🔹 Empurre para cima até quase unirem acima da cabeça.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🔥 2. Prancha Abdominal"):
        st.write("**Séries:** 3x 45 segundos")
        st.write("**Foco:** Core")
        st.image("https://images.tcdn.com.br/img/editor/up/852683/Prancha.gif", width=320)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução</h4>
                <p>🔹 Apoie os antebraços no chão mantendo o corpo reto.</p>
                <p>🔹 Contraia o abdômen rigidamente durante todo o tempo.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Sexta-feira":
    st.header("🍑 Sexta-feira: Posteriores e Glúteos")
    
    with st.expander("🏋️ 1. Stiff com Barra"):
        st.write("**Séries:** 4x 10 reps")
        st.write("**Foco:** Posterior e Glúteos")
        st.image("https://images.tcdn.com.br/img/editor/up/852683/Stiff.gif", width=320)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução</h4>
                <p>🔹 Joelhos semi-flexionados, empurre o quadril para trás.</p>
                <p>🔹 Sinta o posterior alongar e retorne contraindo os glúteos.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🔥 2. Cadeira Flexora"):
        st.write("**Séries:** 3x 12 reps")
        st.write("**Foco:** Posterior de coxa")
        st.image("https://images.tcdn.com.br/img/editor/up/852683/CadeiraFlexora.gif", width=320)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução</h4>
                <p>🔹 Deite-se de bruços com o rolo apoiado na panturrilha.</p>
                <p>🔹 Flexione as pernas puxando o peso ao máximo.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Sábado":
    st.header("⚡ Sábado: Full Body / HIIT")
    
    with st.expander("🏃 1. Burpees"):
        st.write("**Séries:** 4x 45 segundos")
        st.write("**Foco:** Condicionamento")
        st.image("https://images.tcdn.com.br/img/editor/up/852683/Burpee.gif", width=320)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução</h4>
                <p>🔹 Agache, jogue os pés para trás fazendo uma flexão.</p>
                <p>🔹 Retorne os pés para frente e dê um salto explosivo.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🔥 2. Pular Corda"):
        st.write("**Séries:** 4x 1 minuto")
        st.write("**Foco:** Resistência")
        st.image("https://images.tcdn.com.br/img/editor/up/852683/PularCorda.gif", width=320)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução</h4>
                <p>🔹 Cotovelos próximos ao corpo girando os punhos.</p>
                <p>🔹 Salte usando a ponta dos pés em ritmo constante.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Domingo":
    st.header("🌿 Domingo: Recuperação e Mobilidade")
    
    with st.expander("🧘 1. Alongamento Global"):
        st.write("**Duração:** 15-20 minutos")
        st.write("**Foco:** Soltura muscular")
        st.image("https://images.tcdn.com.br/img/editor/up/852683/Alongamento.gif", width=320)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução</h4>
                <p>🔹 Respire fundo de forma controlada e relaxada.</p>
                <p>🔹 Mantenha cada posição estática por 20 a 30 segundos.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🚶 2. Caminhada Leve"):
        st.write("**Duração:** 30 minutos")
        st.write("**Foco:** Descanso ativo")
        st.image("https://images.tcdn.com.br/img/editor/up/852683/Caminhada.gif", width=320)
        st.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução</h4>
                <p>🔹 Mantenha uma passada confortável focando na respiração.</p>
                <p>🔹 Auxilia na circulação e recuperação ativa.</p>
            </div>
        """, unsafe_allow_html=True)

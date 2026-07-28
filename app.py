import streamlit as str_app

# --- Configuração da Página ---
str_app.set_page_config(
    page_title="App de Treinos",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS customizado para cards modernos e alto impacto visual ---
str_app.markdown("""
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
        
        .badge-card {
            background-color: #252525;
            color: #FF007F;
            padding: 8px 15px;
            border-radius: 6px;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 10px;
            border: 1px solid #333;
        }
    </style>
""", unsafe_allow_html=True)

# --- Conteúdo do App (Menu Lateral) ---
str_app.sidebar.title("🔥 Menu de Treinos")
dias_semana = [
    "Segunda-feira", "Terça-feira", "Quarta-feira", 
    "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"
]
dia_escolhido = str_app.sidebar.selectbox("Escolha o Dia:", dias_semana)

# --- Assinatura no Menu Lateral ---
str_app.sidebar.markdown("---")
str_app.sidebar.markdown("### 👨‍💻 Sobre o Desenvolvedor")
str_app.sidebar.markdown("**Desenvolvedor:** Thiago de Sá")
str_app.sidebar.markdown("📧 thiago.deasa@yahoo.com.br")

str_app.title("💪 Meu App de Treinos")
str_app.write("Séries completas de segunda a domingo na palma da mão com fotos ilustrativas de execução")

# --- Lógica de Exibição por Dia da Semana com Fotos Ilustrativas ---

if dia_escolhido == "Segunda-feira":
    str_app.header("💥 Segunda-feira: Peito e Tríceps")
    
    with str_app.expander("🏋️ 1. Supino Reto com Halteres"):
        str_app.markdown('<div class="badge-card">⚡ Séries: 4x 10-12 reps | Foco: Peitoral e Tríceps</div>', unsafe_allow_html=True)
        col1, col2 = str_app.columns(2)
        with col1:
            str_app.image("https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?w=500&auto=format&fit=crop&q=60", caption="Fase Inicial (Subida/Contração)")
        with col2:
            str_app.image("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500&auto=format&fit=crop&q=60", caption="Fase Final (Descida/Alongamento)")
        str_app.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução Correta</h4>
                <p>🔹 Deite-se firmemente no banco, segurando os halteres na linha do peito.</p>
                <p>🔹 Empurre para cima contraindo o peitoral e desça controlando bem o movimento.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with str_app.expander("🔥 2. Tríceps Pulley"):
        str_app.markdown('<div class="badge-card">⚡ Séries: 4x 12 reps | Foco: Tríceps</div>', unsafe_allow_html=True)
        col1, col2 = str_app.columns(2)
        with col1:
            str_app.image("https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?w=500&auto=format&fit=crop&q=60", caption="Posição Inicial (Cotovelos Fixos)")
        with col2:
            str_app.image("https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=500&auto=format&fit=crop&q=60", caption="Contração Total em Baixo")
        str_app.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução Correta</h4>
                <p>🔹 Mantenha os cotovelos fixos e colados ao lado do corpo.</p>
                <p>🔹 Estique os braços para baixo fazendo força total no tríceps, sem balançar o tronco.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Terça-feira":
    str_app.header("🦵 Terça-feira: Membros Inferiores (Quadríceps)")
    
    with str_app.expander("🏋️ 1. Agachamento Livre"):
        str_app.markdown('<div class="badge-card">⚡ Séries: 4x 8-10 reps | Foco: Pernas e Glúteos</div>', unsafe_allow_html=True)
        col1, col2 = str_app.columns(2)
        with col1:
            str_app.image("https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=500&auto=format&fit=crop&q=60", caption="Postura Inicial (Coluna Reta)")
        with col2:
            str_app.image("https://images.unsplash.com/photo-1566241142559-40e1dab266c6?w=500&auto=format&fit=crop&q=60", caption="Flexão Completa do Quadril")
        str_app.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução Correta</h4>
                <p>🔹 Posicione os pés na largura dos ombros, mantenha a coluna reta e o abdômen contraído.</p>
                <p>🔹 Desça o quadril projetando para trás e suba forçando a base dos calcanhares.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with str_app.expander("🔥 2. Cadeira Extensora"):
        str_app.markdown('<div class="badge-card">⚡ Séries: 3x 12 reps | Foco: Quadríceps</div>', unsafe_allow_html=True)
        col1, col2 = str_app.columns(2)
        with col1:
            str_app.image("https://images.unsplash.com/photo-1534367507873-d2d7e24c797f?w=500&auto=format&fit=crop&q=60", caption="Início do Movimento")
        with col2:
            str_app.image("https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=500&auto=format&fit=crop&q=60", caption="Extensão Máxima das Pernas")
        str_app.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução Correta</h4>
                <p>🔹 Sente-se com o apoio ajustado exatamente na altura da canela.</p>
                <p>🔹 Estenda completamente as pernas em cima e retorne controlando o peso devagar.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Quarta-feira":
    str_app.header("🦾 Quarta-feira: Costas e Bíceps")
    
    with str_app.expander("🏋️ 1. Puxada Alta Frontal"):
        str_app.markdown('<div class="badge-card">⚡ Séries: 4x 10 reps | Foco: Dorsal e Bíceps</div>', unsafe_allow_html=True)
        col1, col2 = str_app.columns(2)
        with col1:
            str_app.image("https://images.unsplash.com/photo-1605296867304-46d5465a13f1?w=500&auto=format&fit=crop&q=60", caption="Pegada Aberta e Peito Estufado")
        with col2:
            str_app.image("https://images.unsplash.com/photo-1541534741688-6078c6bfb5c5?w=500&auto=format&fit=crop&q=60", caption="Barra na Direção da Clavícula")
        str_app.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução Correta</h4>
                <p>🔹 Segure a barra com pegada aberta e estufe bem o peito.</p>
                <p>🔹 Puxe a barra em direção à clavícula fechando bem as costas.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with str_app.expander("🔥 2. Rosca Direta"):
        str_app.markdown('<div class="badge-card">⚡ Séries: 4x 12 reps | Foco: Bíceps</div>', unsafe_allow_html=True)
        col1, col2 = str_app.columns(2)
        with col1:
            str_app.image("https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?w=500&auto=format&fit=crop&q=60", caption="Início com Braços Estendidos")
        with col2:
            str_app.image("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500&auto=format&fit=crop&q=60", caption="Flexão Máxima do Bíceps")
        str_app.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução Correta</h4>
                <p>🔹 Mantenha o corpo firme sem balançar o tronco ou usar impulso.</p>
                <p>🔹 Flexione os cotovelos trazendo o peso na direção do peito de forma controlada.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Quinta-feira":
    str_app.header("🛡️ Quinta-feira: Ombros e Abdômen")
    
    with str_app.expander("🏋️ 1. Desenvolvimento com Halteres"):
        str_app.markdown('<div class="badge-card">⚡ Séries: 4x 12 reps | Foco: Ombros</div>', unsafe_allow_html=True)
        col1, col2 = str_app.columns(2)
        with col1:
            str_app.image("https://images.unsplash.com/photo-1532029835096-16e0369c4f7b?w=500&auto=format&fit=crop&q=60", caption="Halteres na Altura dos Ombros")
        with col2:
            str_app.image("https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=500&auto=format&fit=crop&q=60", caption="Empurrão para Cima")
        str_app.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução Correta</h4>
                <p>🔹 Segure os halteres na altura dos ombros sentado no banco com apoio.</p>
                <p>🔹 Empurre para cima até quase unirem acima da cabeça sem travar os cotovelos.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with str_app.expander("🔥 2. Prancha Abdominal"):
        str_app.markdown('<div class="badge-card">⚡ Séries: 3x 45 segundos | Foco: Core</div>', unsafe_allow_html=True)
        col1, col2 = str_app.columns(2)
        with col1:
            str_app.image("https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=500&auto=format&fit=crop&q=60", caption="Antebraços Apoiados e Corpo Reto")
        with col2:
            str_app.image("https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=500&auto=format&fit=crop&q=60", caption="Abdômen Contraído")
        str_app.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução Correta</h4>
                <p>🔹 Apoie os antebraços no chão mantendo o corpo totalmente alinhado e reto.</p>
                <p>🔹 Contraia o abdômen rigidamente durante todo o tempo de execução.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Sexta-feira":
    str_app.header("🍑 Sexta-feira: Posteriores e Glúteos")
    
    with str_app.expander("🏋️ 1. Stiff com Barra"):
        str_app.markdown('<div class="badge-card">⚡ Séries: 4x 10 reps | Foco: Posterior e Glúteos</div>', unsafe_allow_html=True)
        col1, col2 = str_app.columns(2)
        with col1:
            str_app.image("https://images.unsplash.com/photo-1566241142559-40e1dab266c6?w=500&auto=format&fit=crop&q=60", caption="Postura Inicial com Barra")
        with col2:
            str_app.image("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500&auto=format&fit=crop&q=60", caption="Quadril para Trás e Alongamento")
        str_app.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução Correta</h4>
                <p>🔹 Joelhos semi-flexionados, empurre o quadril para trás mantendo a coluna neutra.</p>
                <p>🔹 Sinta o posterior alongar ao máximo e retorne contraindo os glúteos.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with str_app.expander("🔥 2. Cadeira Flexora"):
        str_app.markdown('<div class="badge-card">⚡ Séries: 3x 12 reps | Foco: Posterior de coxa</div>', unsafe_allow_html=True)
        col1, col2 = str_app.columns(2)
        with col1:
            str_app.image("https://images.unsplash.com/photo-1534367507873-d2d7e24c797f?w=500&auto=format&fit=crop&q=60", caption="Deitado com Apoio na Panturrilha")
        with col2:
            str_app.image("https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=500&auto=format&fit=crop&q=60", caption="Flexão Completa das Pernas")
        str_app.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução Correta</h4>
                <p>🔹 Deite-se de bruços com o rolo de apoio posicionado na altura da panturrilha.</p>
                <p>🔹 Flexione as pernas puxando o peso totalmente e retorne desacelerando.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Sábado":
    str_app.header("⚡ Sábado: Full Body / HIIT")
    
    with str_app.expander("🏃 1. Burpees"):
        str_app.markdown('<div class="badge-card">⚡ Séries: 4x 45 segundos | Foco: Condicionamento</div>', unsafe_allow_html=True)
        col1, col2 = str_app.columns(2)
        with col1:
            str_app.image("https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=500&auto=format&fit=crop&q=60", caption="Fase de Apoio e Flexão")
        with col2:
            str_app.image("https://images.unsplash.com/photo-1574680096145-d05b474e2155?w=500&auto=format&fit=crop&q=60", caption="Salto Explosivo Vertical")
        str_app.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução Correta</h4>
                <p>🔹 Agache, jogue os pés para trás fazendo uma flexão completa de braço.</p>
                <p>🔹 Retorne os pés rapidamente para frente e dê um salto explosivo vertical.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with str_app.expander("🔥 2. Pular Corda"):
        str_app.markdown('<div class="badge-card">⚡ Séries: 4x 1 minuto | Foco: Resistência</div>', unsafe_allow_html=True)
        col1, col2 = str_app.columns(2)
        with col1:
            str_app.image("https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?w=500&auto=format&fit=crop&q=60", caption="Cotovelos Próximos ao Corpo")
        with col2:
            str_app.image("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500&auto=format&fit=crop&q=60", caption="Salto Leve na Ponta dos Pés")
        str_app.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução Correta</h4>
                <p>🔹 Mantenha os cotovelos próximos ao corpo girando apenas os punhos.</p>
                <p>🔹 Salte levemente usando a ponta dos pés em um ritmo constante.</p>
            </div>
        """, unsafe_allow_html=True)

elif dia_escolhido == "Domingo":
    str_app.header("🌿 Domingo: Recuperação e Mobilidade")
    
    with str_app.expander("🧘 1. Alongamento Global"):
        str_app.markdown('<div class="badge-card">⚡ Duração: 15-20 minutos | Foco: Soltura muscular</div>', unsafe_allow_html=True)
        col1, col2 = str_app.columns(2)
        with col1:
            str_app.image("https://images.unsplash.com/photo-1518611012118-696072aa579a?w=500&auto=format&fit=crop&q=60", caption="Relaxamento e Respiração")
        with col2:
            str_app.image("https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=500&auto=format&fit=crop&q=60", caption="Posição Estática de Soltura")
        str_app.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução Correta</h4>
                <p>🔹 Respire fundo de forma controlada, relaxando a musculatura trabalhada na semana.</p>
                <p>🔹 Mantenha cada posição estática de alongamento por 20 a 30 segundos.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with str_app.expander("🚶 2. Caminhada Leve"):
        str_app.markdown('<div class="badge-card">⚡ Duração: 30 minutos | Foco: Descanso ativo</div>', unsafe_allow_html=True)
        col1, col2 = str_app.columns(2)
        with col1:
            str_app.image("https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=500&auto=format&fit=crop&q=60", caption="Ritmo Confortável ao Ar Livre")
        with col2:
            str_app.image("https://images.unsplash.com/photo-1502680390469-be75c86b636f?w=500&auto=format&fit=crop&q=60", caption="Recuperação Ativa")
        str_app.markdown("""
            <div class="box-exercicio">
                <h4>🎯 Execução Correta</h4>
                <p>🔹 Mantenha uma passada confortável e constante, focando em uma boa respiração.</p>
                <p>🔹 Excelente para auxiliar na circulação sanguínea e recuperação ativa dos músculos.</p>
            </div>
        """, unsafe_allow_html=True)

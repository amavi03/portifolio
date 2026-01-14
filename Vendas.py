import streamlit as st
import streamlit.components.v1 as components

# Configurações da página
st.set_page_config(
    page_title="Vendas AMV Sistemas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="auto"
)

# CSS personalizado para melhorar a visualização
st.markdown("""
    <style>
        .main > div {
            padding-top: 1rem;
        }
        iframe {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .stMarkdown h1 {
            color: #2c3e50;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Cabeçalho da aplicação
st.markdown("<h1 style='text-align: center;'>📊 Dashboard Vendas AMV Sistemas</h1>", unsafe_allow_html=True)

# Descrição explicativa
with st.expander("ℹ️ Sobre este dashboard", expanded=False):
    st.markdown("""
        Este painel interativo exibe em tempo real as principais métricas financeiras da AMV Sistemas.
        - Utilize os filtros no próprio dashboard para explorar os dados
        - Visualize diferentes perspectivas financeiras
        - Dados atualizados automaticamente
    """)

# Espaçamento
st.write("")

# Container principal para o iframe
with st.container():
    components.html(
        """
        <iframe 
            title="Dashboard Vendas AMV" 
            width="100%" 
            height="1060" 
            src="https://app.powerbi.com/view?r=eyJrIjoiZGJmODc4MzgtZjEwNC00YWNiLWI4MWUtMGUxZmU5MjU2MDEzIiwidCI6IjZhNzQxMjUxLTA0ZWMtNDA1YS1hMDE2LWZmZWNjNTlkYjg5YyJ9" 
            frameborder="0" 
            allowFullScreen="true">
        </iframe>
        """,
        height=1060,
        scrolling=True
    )

# Rodapé informativo
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Acesso rápido**")
    st.markdown("""
    - [Portal AMV](https://www.amvsistemas.com.br)
    - [Suporte Vendas](mailto:Vendas@amvsistemas.com.br)
    """)

with col2:
    st.markdown("**Informações técnicas**")
    st.markdown("""
    - Última atualização: Automática
    - Fonte: Sistemas corporativos AMV
    - Versão do dashboard: 2.4.1
    """)
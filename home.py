import streamlit as st

pages = {
    "": [
        st.Page("pages/Pagina inicial.py"),
    ],
    "📈 Power BI": [
        st.Page("pages/Financeiro.py"),
        st.Page("pages/RH.py"),
        st.Page("pages/Vendas.py"),
    ]
}

pg = st.navigation(pages) 

pg.run()


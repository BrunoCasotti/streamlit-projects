import streamlit as st;
from login import page_login;

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

st.set_page_config(page_title="Inventory", layout="wide")

if not st.session_state.authenticated:
    # Exibe a página de login
    page_login()

else:
    # Interface principal do app
    productInsert_page = st.Page(
        page="productInsert.py",
        title="Register"
    )

    productConsult_page = st.Page(
        page="productConsult.py",
        title="Consult"
    )

    inventory_page = st.Page(
        page="inventory.py",
        title="Inventory"
    )

    with st.sidebar:
        st.logo("gm-logo-azul.png", size="large")

        pg = st.navigation(
            {
                "Inventory": [inventory_page],
                "Product": [productInsert_page, productConsult_page],
            }
        )

         # Botão de Logout
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.rerun()

    pg.run()

    # Rodapé
    st.markdown("""
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            padding: 10px;
            text-align: right;
            background-color: transparent;
            font-size: 14px;
        }
        
        .footer-divider {
            width: 78%;
            margin-left: auto;
            margin-right: 2%;
            border-top: 2px solid #ccc; 
        }
                
        .footer-text {
            margin-right: 2%;
        }
                
        </style>
        
        <div class="footer">
            <div class="footer-divider"></div> 
            <p class="footer-text">Created by - Bruno O. Casotti</p>
        </div>
    """, unsafe_allow_html=True)
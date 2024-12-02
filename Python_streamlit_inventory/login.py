import streamlit as st;
import loginController;



def page_login():

    st.logo("gm-logo-azul.png", size="large")

    # Insert a form in the container
    with st.container(border=True):
        st.markdown("#### Enter your credentials")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):

            if loginController.authenticate_user(username,password) == True:
                st.session_state.authenticated = True
                st.success("Login successful!")
                st.rerun()

            else:
                st.error("Credentials are incorrect.")
                
    return st.session_state.authenticated
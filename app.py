import streamlit as st

# ===============================
# Inicialização do estado de sessão
# ===============================

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "current_page" not in st.session_state:
    st.session_state.current_page = "login"

if "user" not in st.session_state:
    st.session_state.user = None


# ===============================
# Proteção de acesso
# ===============================

if not st.session_state.authenticated and st.session_state.current_page == "dashboard":
    st.session_state.current_page = "login"


# ===============================
# Orquestração de páginas
# ===============================

if st.session_state.current_page == "login":
    import pages.login as login


elif st.session_state.current_page == "register":
    import pages.register as register


elif st.session_state.current_page == "dashboard":
    import pages.dashboard as dashboard

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user_id = None
    st.session_state.user_name = None

st.switch_page("pages/login.py")


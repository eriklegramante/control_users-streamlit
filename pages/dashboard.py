import streamlit as st


st.title("Dashboard")
st.write(f"Welcome, {st.session_state.user_name}")

if st.session_state.get("user_role") == "admin":
    if st.button("Admin Panel"):
        st.switch_page("pages/admin_users.py")

if not st.session_state.get("authenticated"):
    st.switch_page("pages/login.py")
    st.stop()
if st.button("Logout"):
    st.session_state.authenticated = False
    st.session_state.user_id = None
    st.session_state.user_name = None
    st.switch_page("pages/login.py")

if not st.session_state.get("authenticated"):
    st.switch_page("pages/login.py")
    st.stop()



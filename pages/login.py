import streamlit as st
from db.database import get_connection
import hashlib

st.session_state.get("user_role")

st.title("Login")

email = st.text_input("E-mail")
password = st.text_input("Password", type="password")

def hash_password(p):
    return hashlib.sha256(p.encode()).hexdigest()

if st.button("Login"):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, email, role FROM users WHERE email = ? AND password = ?",
        (email.strip(), hash_password(password))
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        st.session_state.authenticated = True
        st.session_state.user_id = user[0]
        st.session_state.user_name = user[1]
        st.session_state.user_email = user[2]
        st.session_state.user_role = user[3]  # VEM DO BANCO

        if st.session_state.user_role == "admin":
            st.switch_page("pages/admin_users.py")
        else:
            st.switch_page("pages/dashboard.py")


st.write("Don't have an account?")
if st.button("Register"):
    st.switch_page("pages/register.py")

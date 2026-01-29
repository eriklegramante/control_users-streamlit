import streamlit as st
from db.database import get_connection, create_table
import hashlib

from scripts.session import init_session
init_session()

create_table()

if st.session_state.get("authenticated"):
    st.switch_page("pages/dashboard.py")
    st.stop()

st.title("Welcome to Register users.py")

name = st.text_input("Name")
email = st.text_input("E-mail")
confirm_email = st.text_input("Confirm your E-mail")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm your Password", type="password")

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

if "registered" not in st.session_state:
    st.session_state.registered = False

if st.button("Register") and not st.session_state.registered:
    if not all([name, email, confirm_email, password, confirm_password]):
        st.error("Fill in all fields.")
    
    elif email != confirm_email:
        st.error("Emails do not match.")
    
    elif password != confirm_password:
        st.error("Passwords do not match.")
    
    else:
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                (name.strip(), email.strip(), hash_password(password))
            )
            conn.commit()

            st.session_state.registered = True
            st.success("User registered successfully!")
            st.switch_page("pages/login.py")

        except Exception:
            st.error("This email is already registered.")

        finally:
            conn.close()


if st.button("Already have an account? Login"):
    st.switch_page("pages/login.py")

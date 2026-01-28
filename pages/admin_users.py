import streamlit as st
from db.database import get_connection
from utils.security import hash_password 

if not st.session_state.get("authenticated"):
    st.error("You must be logged in.")
    st.stop()

if st.session_state.get("user_role") != "admin":
    st.error("Admins only.")
    st.stop()

st.title("Admin – User Management")

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT id, name, email, role FROM users")
users = cursor.fetchall()
conn.close()

st.subheader("Create user")

name = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
role = st.selectbox("Role", ["user", "admin"])

if st.button("Create user"):
    if not all([name, email, password]):
        st.error("Fill all fields.")
        st.stop()

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
            (name.strip(), email.strip(), hash_password(password), role)
        )
        conn.commit()
        st.success("User created")
        st.rerun()

    except Exception:
        st.error("Email already exists.")

    finally:
        conn.close()

st.divider()

for user in users:
    user_id, name, email, role = user
    st.write(user_id, name, email, role)

    if st.button(f"Delete {name}", key=f"del_{user_id}"):
        if role == "admin":
            st.error("Cannot delete admin users.")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()

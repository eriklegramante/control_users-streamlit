import streamlit as st
from db.database import get_connection
from utils.security import hash_password 

from scripts.session import init_session
init_session()


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

    col1, col2, col3, col4, col5 = st.columns([1, 3, 4, 2, 2])

    col1.write(user_id)
    col2.write(name)
    col3.write(email)
    col4.write(role)

    if col5.button("✏️ Edit", key=f"edit_{user_id}"):
        st.session_state.edit_user_id = user_id
        st.rerun()

    if col5.button("🗑 Delete", key=f"del_{user_id}"):
        if role == "admin":
            st.error("Cannot delete admin users.")
            continue

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()

        st.success(f"User {name} deleted")
        st.rerun()

st.divider()

if "edit_user_id" in st.session_state:
    user_id = st.session_state.edit_user_id

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, email, role FROM users WHERE id = ?",
        (user_id,)
    )
    user = cursor.fetchone()
    conn.close()

    st.subheader("Edit User")

    with st.form("edit_user_form"):
        if user_id == st.session_state.user_id:
            st.warning("You are editing your own account.")
            
        name = st.text_input("Name", value=user[0])
        email = st.text_input("Email", value=user[1])
        role = st.selectbox(
            "Role",
            ["user", "admin"],
            index=0 if user[2] == "user" else 1
        )

        col1, col2 = st.columns(2)

        save = col1.form_submit_button("Save")
        cancel = col2.form_submit_button("Cancel")

    if save:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE users
            SET name = ?, email = ?, role = ?
            WHERE id = ?
            """,
            (name.strip(), email.strip(), role, user_id)
        )

        conn.commit()
        conn.close()

        del st.session_state.edit_user_id
        st.success("User updated")
        st.rerun()

    if cancel:
        del st.session_state.edit_user_id
        st.rerun()

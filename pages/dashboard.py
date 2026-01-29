import streamlit as st
from db.database import get_connection
import pandas as pd


from scripts.session import init_session
init_session()

st.title("Dashboard")
st.write(f"Welcome, {st.session_state.user_name}")

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


conn = get_connection()
df = pd.read_sql("SELECT * FROM users", conn)
conn.close()

total_users = len(df)
admins = len(df[df["role"] == "admin"])
common_users = len(df[df["role"] == "user"])

col1, col2, col3 = st.columns(3)
col1.metric("Total Users", total_users)
col2.metric("Admins", admins)
col3.metric("Common Users", common_users)

st.divider()

# =========================
# Gráficos
# =========================
st.subheader("Users by Role")

role_counts = df["role"].value_counts()
st.bar_chart(role_counts)

st.subheader("User Distribution")

st.line_chart(df.index + 1)

st.divider()

# =========================
# Widgets
# =========================
st.subheader("Quick Actions")

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Register User"):
        st.switch_page("pages/register.py")

with col2:
    if st.session_state.user_role == "admin":
        if st.button("🛠 Admin Panel"):
            st.switch_page("pages/admin_users.py")

st.divider()

# =========================
# Info
# =========================
st.info(f"Logged in as: {st.session_state.user_name} ({st.session_state.user_role})")
import streamlit as st

def init_session():
    defaults = {
        "authenticated": False,
        "user_id": None,
        "user_name": None,
        "user_email": None,
        "user_role": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

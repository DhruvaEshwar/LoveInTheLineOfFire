import streamlit as st

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Journey of a Young Mind",
    layout="centered"
)

# ------------------ Session State ------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# 🔐 auto logout on refresh
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ------------------ PASSWORD ------------------
HOME_PASSWORD = "14022010"   # 🔑 change password here

# ------------------ PASSWORD PAGE ------------------
if not st.session_state.authenticated:
    st.markdown("### 🔒 Enter Passcode to access the website")
    password = st.text_input("Passcode", type="password")

    if st.button("Enter"):
        if password == HOME_PASSWORD:
            st.session_state.authenticated = True
            st.success("✅ Access granted!")
        else:
            st.error("❌ Incorrect passcode")

    # Stop rendering until authenticated
    st.stop()

# ------------------ SIDEBAR (ONLY AFTER PASSWORD) ------------------
with st.sidebar:
    st.title("Menu")

    if st.button("🏠 Home"):
        st.session_state.page = "Home"

    if st.button("📖 Journey of a Young Mind"):
        st.session_state.page = "Journey"

# ------------------ PAGES ------------------
if st.session_state.page == "Home":
    st.markdown(
        "<h1 style='text-align:center;'>Journey of a Young Mind</h1>",
        unsafe_allow_html=True
    )

elif st.session_state.page == "Journey":
    st.markdown("<h1>Journey of a Young Mind</h1>", unsafe_allow_html=True)
    st.write("📅 **Will be uploaded on 14th Feb, 2026**")

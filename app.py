import streamlit as st

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Love in the Line of Fire",
    layout="centered"
)

# ------------------ Session State ------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ------------------ Sidebar Menu (Streamlit default) ------------------
with st.sidebar:
    st.title("Menu")

    if st.button("🏠 Home"):
        st.session_state.page = "Home"

    if st.button("📖 Journey of a Young Mind"):
        st.session_state.page = "Journey"

# ------------------ Pages ------------------
if st.session_state.page == "Home":
    st.markdown(
        "<h1 style='text-align:center;'>Love in the Line of Fire</h1>",
        unsafe_allow_html=True
    )

elif st.session_state.page == "Journey":
    st.markdown("<h1>Journey of a Young Mind</h1>", unsafe_allow_html=True)
    st.write("📅 **Will be uploaded on 14th Feb, 2026**")

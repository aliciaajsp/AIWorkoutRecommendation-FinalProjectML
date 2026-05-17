import streamlit as st

from utils.style import load_css

st.set_page_config(
    page_title="FitAI Workout Recommender",
    page_icon="💪",
    layout="wide"
)
load_css()
st.markdown("""
<style>

[data-testid="stSidebar"] {
    background-color: #151B54 !important;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.sidebar-title {
    color: white !important;
    font-weight: 800;
    font-size: 26px;
    text-align: center;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("<div class='sidebar-title'>FitAI</div>", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Choose Feature :",
    [
        "Introduction",
        "Exploratory Data Analysis",
        "User Input",
        "Result",
        "Evaluation"
    ]
)

st.sidebar.markdown("---")

# navigation buttons
if page == "Introduction":
    from Streamlit.introduction_page import show_page
    show_page()

elif page == "Exploratory Data Analysis":
    from Streamlit.eda_page import show_page
    show_page()

elif page == "User Input":
    from Streamlit.user_input_page import show_page
    show_page()

elif page == "Result":
    from Streamlit.result_page import show_page
    show_page()

elif page == "Evaluation":
    from Streamlit.evaluation_page import show_page
    show_page()

st.sidebar.markdown("""
<div>
    <h3 style="color:#9C7B57;">
        Group - 4
    </h3>
    <p style="font-size:14px; color:#666;">
        
1. Adisca Gandawidjaja
2. Alicia Angelina Jusup
3. Mathilda Rafaela Christy Nugroho
    </p>
</div>
""", unsafe_allow_html=True)
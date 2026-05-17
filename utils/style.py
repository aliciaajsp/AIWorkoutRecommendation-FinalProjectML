import streamlit as st

def load_css():
    st.markdown("""
    <style>

    .stApp {
        background-color: #F6F9FF;
        color: #0F172A;
        font-family: 'Inter', sans-serif;
    }

    section[data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E2E8F0;
    }

    .sidebar-title {
        font-size: 28px;
        font-weight: 800;
        color: #2563EB;
        text-align: center;
        padding: 12px;
    }

    .title {
        font-size: 36px;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 16px;
        color: #64748B;
        margin-bottom: 20px;
    }

    .card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.08);
        transition: 0.2s ease-in-out;
    }

    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.15);
    }

    .metric-card {
        background: #FFFFFF;
        border-left: 5px solid #2563EB;
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }

    .stButton > button {
        background-color: #2563EB;
        color: white;
        border-radius: 10px;
        padding: 10px 18px;
        font-weight: 600;
        border: none;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background-color: #1D4ED8;
        transform: scale(1.02);
    }

    .stDataFrame {
        border-radius: 12px;
    }

    </style>
    """, unsafe_allow_html=True)
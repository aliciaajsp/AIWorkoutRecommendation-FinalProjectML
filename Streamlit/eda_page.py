import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from utils.style import load_css

BASE_DIR = Path(__file__).resolve().parents[2]

def load_model():
    model_dir = BASE_DIR / "Models"
    exercise_df = model_dir / "exercise_df.pkl"
    tfidf = model_dir / "tfidf.pkl"
    tfidf_matrix = model_dir / "tfidf_matrix.pkl"
    fitness_df = model_dir / "fitness_df.pkl"
    return exercise_df, tfidf, tfidf_matrix, fitness_df

    
def show_page():
    load_css()
    exercise_df, tfidf, tfidf_matrix, fitness_df = load_model()
    exercise_df = pd.read_csv(
        "datasets/exercise.csv"
    )
    fitness_df = pd.read_csv(
        "datasets/fitness.csv"
    )
    
    st.markdown("""
    <div style="padding:10px 0 20px 0;">
        <h1 style="
            font-size:38px;
            font-weight:800;
            color:#0F172A;
        ">
            📊 Exploratory Data Analysis
        </h1>
        <p style="
            color:#64748B;
            font-size:15px;
        ">
            Overview of dataset structure, patterns, and distributions for FitAI recommendation system.
        </p>
    </div>
    """, unsafe_allow_html=True)

# dataset overview
    st.markdown("### 📌 Dataset Overview")

    c1, c2, c3, c4 = st.columns(4)

    def kpi(label, value):
        return f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E8F0;
            padding:18px;
            border-radius:14px;
            text-align:center;
        ">
            <div style="font-size:26px;font-weight:800;color:#2563EB;">
                {value}
            </div>
            <div style="font-size:13px;color:#64748B;">
                {label}
            </div>
        </div>
        """
    with c1:
        st.markdown(kpi("Exercises", f"{exercise_df.shape[0]:,}"), unsafe_allow_html=True)

    with c2:
        st.markdown(kpi("Body Parts", exercise_df["BodyPart"].nunique()), unsafe_allow_html=True)

    with c3:
        st.markdown(kpi("Equipment Types", exercise_df["Equipment"].nunique()), unsafe_allow_html=True)

    with c4:
        st.markdown(kpi("Fitness Levels", exercise_df["Level"].nunique()), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(kpi("Users", f"{fitness_df.shape[0]:,}"), unsafe_allow_html=True)

    with c2:
        st.markdown(kpi("Avg BMI", round(fitness_df["BMI"].mean(), 1)), unsafe_allow_html=True)

    with c3:
        st.markdown(kpi("Avg Age", round(fitness_df["Age"].mean(), 1)), unsafe_allow_html=True)

    with c4:
        st.markdown(kpi("Gender Types", fitness_df["Gender"].nunique()), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 📂 Dataset Preview")

    tab1, tab2 = st.tabs(["Exercise Dataset", "Fitness Dataset"])

    with tab1:
        st.dataframe(exercise_df, use_container_width=True)

    with tab2:
        st.dataframe(fitness_df, use_container_width=True)

    st.markdown("### 📈 Statistical Summary")

    tab1, tab2 = st.tabs(["Exercise Stats", "Fitness Stats"])

    with tab1:
        st.dataframe(exercise_df.describe(), use_container_width=True)

    with tab2:
        st.dataframe(fitness_df.describe(), use_container_width=True)

    st.markdown("### 📉 Missing Values")

    tab1, tab2 = st.tabs(["Exercise Dataset", "Fitness Dataset"])

    with tab1:
        st.dataframe(exercise_df.isnull().sum(), use_container_width=True)

    with tab2:
        st.dataframe(fitness_df.isnull().sum(), use_container_width=True)

    st.markdown("### 📊 Data Visualization")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Workout Type Distribution")
        st.bar_chart(exercise_df["Type"].value_counts())

    with col2:
        st.markdown("#### Top Body Parts")
        st.bar_chart(exercise_df["BodyPart"].value_counts().head(10))

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("#### Fitness Level Distribution")
        st.bar_chart(exercise_df["Level"].value_counts())

    with col4:
        st.markdown("#### Equipment Usage")
        st.bar_chart(exercise_df["Equipment"].value_counts().head(8))

    col5, col6 = st.columns(2)

    with col5:
        st.markdown("#### BMI Distribution")
        st.bar_chart(fitness_df["BMI"].round().value_counts().sort_index())

    with col6:
        st.markdown("#### Age Distribution")
        st.bar_chart(fitness_df["Age"].value_counts().sort_index())

    st.markdown("""
    <div style="
        text-align:center;
        padding:30px;
        color:#94A3B8;
        font-size:13px;
    ">
        Created by Group 4 - Machine Learning - Final Project
    </div>
    """, unsafe_allow_html=True)
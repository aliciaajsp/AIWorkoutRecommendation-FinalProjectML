import streamlit as st
from utils.style import load_css
from utils.recommender import (
    recommend_workout,
    precision_at_k,
)
from pathlib import Path
import pickle

BASE_DIR = Path(__file__).resolve().parents[1]

def load_model():
    model_dir = BASE_DIR / "Models"

    tfidf = pickle.load(open(model_dir / "tfidf.pkl", "rb"))
    tfidf_matrix = pickle.load(open(model_dir / "tfidf_matrix.pkl", "rb"))
    exercise_df = pickle.load(open(model_dir / "exercise_df.pkl", "rb"))

    return tfidf, tfidf_matrix, exercise_df

def show_page():
    load_css()

    st.markdown("""
    <div style="padding:10px 0 25px 0;">
        <h1 style="
            font-size:38px;
            font-weight:800;
            color:#0F172A;
        ">
            📈 Model Evaluation
        </h1>
        <p style="
            color:#64748B;
            font-size:15px;
        ">
            Evaluate the performance of the FitAI recommendation system using Precision@K and similarity scoring.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    query = "strength chest beginner dumbbell"
    tfidf, tfidf_matrix, exercise_df = load_model()

    result = recommend_workout(query, tfidf, tfidf_matrix, exercise_df)
    query_features = query.split()

    precision = precision_at_k(query_features, result, k=5)
    avg_similarity = result["Similarity Score"].mean()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E8F0;
            padding:20px;
            border-radius:14px;
            text-align:center;
        ">
            <div style="font-size:26px;font-weight:800;color:#2563EB;">
                Precision@5
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.metric(label="", value=precision)

    with col2:
        st.markdown("""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E8F0;
            padding:20px;
            border-radius:14px;
            text-align:center;
        ">
            <div style="font-size:26px;font-weight:800;color:#2563EB;">
                Avg Similarity
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.metric(label="", value=round(avg_similarity, 3))

    with col3:
        st.markdown("""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E8F0;
            padding:20px;
            border-radius:14px;
            text-align:center;
        ">
            <div style="font-size:26px;font-weight:800;color:#2563EB;">
                Query Type
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="
            background:#2563EB;
            color:white;
            padding:10px;
            border-radius:10px;
            text-align:center;
            font-weight:600;
        ">
            Rule-based Test Query
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    ### 📌 Evaluation Method

    FitAI recommendation system is evaluated using:

    - **Precision@K** → measures how many recommended workouts match query features  
    - **Average Similarity Score** → measures overall relevance of recommendations  

    The system uses:
    - TF-IDF Vectorization  
    - Cosine Similarity  
    - Content-Based Filtering  
    """)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 🏋 Sample Recommendations")

    st.dataframe(result, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
        text-align:center;
        padding:30px;
        color:#94A3B8;
        font-size:13px;
    ">
        FitAI • Model Evaluation Dashboard • Machine Learning Project
    </div>
    """, unsafe_allow_html=True)
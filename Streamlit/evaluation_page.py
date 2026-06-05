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

    query = "strength chest beginner dumbbell"

    tfidf, tfidf_matrix, exercise_df = load_model()

    result = recommend_workout(
        query,
        tfidf,
        tfidf_matrix,
        exercise_df
    )

    query_features = query.split()

    precision = precision_at_k(
        query_features,
        result,
        k=5
    )

    avg_similarity = result["Similarity Score"].mean()

    st.markdown("""
    <div style="
        background:linear-gradient(
            135deg,
            #2563EB,
            #4F46E5
        );
        padding:35px;
        border-radius:24px;
        color:white;
        margin-bottom:25px;
        box-shadow:0 8px 24px rgba(37,99,235,0.25);
    ">
        <h1 style="
            margin:0;
            font-size:42px;
            font-weight:800;
        ">
            📈 FitAI Model Evaluation
        </h1>
        <p style="
            margin-top:12px;
            font-size:16px;
            opacity:0.95;
        ">
            Analyze recommendation quality using
            Precision@K, Similarity Score,
            TF-IDF Vectorization,
            and Content-Based Filtering.
        </p>
    </div>
    """, unsafe_allow_html=True)

    def metric_card(title, value, color):
        st.markdown(f"""
        <div style="
            background:white;
            border:1px solid #E2E8F0;
            border-radius:22px;
            padding:25px;
            text-align:center;
            height:180px;
            box-shadow:
                0 4px 15px rgba(0,0,0,0.05);
        ">
            <div style="
                color:#64748B;
                font-size:14px;
                font-weight:600;
            ">
                {title}
            </div>
            <div style="
                margin-top:20px;
                font-size:42px;
                font-weight:800;
                color:{color};
            ">
                {value}
            </div>
        </div>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        metric_card(
            "Precision@5",
            f"{precision:.2f}",
            "#2563EB"
        )

    with col2:
        metric_card(
            "Avg Similarity",
            f"{avg_similarity:.3f}",
            "#7C3AED"
        )

    with col3:
        metric_card(
            "Query Type",
            "Rule-Based",
            "#0EA5E9"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
        background:white;
        border-radius:20px;
        padding:25px;
        border:1px solid #E2E8F0;
        margin-bottom:20px;
    ">
        <h3 style="margin-top:0;">
            Recommendation Performance
        </h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("Precision Score")
    st.progress(min(float(precision), 1.0))

    st.write("Average Similarity Score")
    st.progress(min(float(avg_similarity), 1.0))

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
        background:#EFF6FF;
        border-left:7px solid #2563EB;
        padding:25px;
        border-radius:18px;
        margin-bottom:25px;
    ">
        <h3 style="
            margin-top:0;
            color:#1E40AF;
        ">
            AI Insight
        </h3>
        <p style="
            font-size:15px;
            line-height:1.8;
            color:#334155;
        ">
            The recommendation engine achieved a
            <b>Precision@5 score of {precision:.2f}</b>
            and an average similarity score of
            <b>{avg_similarity:.3f}</b>.
            This indicates that the retrieved
            workouts are highly aligned with
            the user's input query and relevant
            exercise attributes.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        background:white;
        border:1px solid #E2E8F0;
        border-radius:22px;
        padding:28px;
        margin-bottom:25px;
        box-shadow:
            0 4px 12px rgba(0,0,0,0.04);
    ">
        <h3 style="
            margin-top:0;
            color:#0F172A;
        ">
            Evaluation Methodology
        </h3>
        <ul style="
            color:#475569;
            line-height:2;
        ">
            <li>
                <b>Precision@K</b> measures
                how many recommended workouts
                are relevant to the query.
            </li>
            <li>
                <b>Average Similarity Score</b>
                evaluates overall recommendation
                relevance.
            </li>
            <li>
                <b>TF-IDF Vectorization</b>
                converts exercise text into
                numerical feature vectors.
            </li>
            <li>
                <b>Cosine Similarity</b>
                computes similarity between
                user queries and exercises.
            </li>
            <li>
                <b>Content-Based Filtering</b>
                retrieves exercises sharing
                similar characteristics.
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.dataframe(
        result,
        use_container_width=True,
        height=450
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
        text-align:center;
        padding:35px;
        color:#94A3B8;
        font-size:13px;
    ">
        Created by Group 4 - Machine Learning - Final Project
    </div>
    """, unsafe_allow_html=True)
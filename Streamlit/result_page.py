import streamlit as st
import pandas as pd
import pickle
from utils.style import load_css
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parents[1]

def load_model():
    model_dir = BASE_DIR / "Models"

    tfidf = pickle.load(open(model_dir / "tfidf.pkl", "rb"))
    tfidf_matrix = pickle.load(open(model_dir / "tfidf_matrix.pkl", "rb"))
    exercise_df = pickle.load(open(model_dir / "exercise_df.pkl", "rb"))

    return tfidf, tfidf_matrix, exercise_df

def recommend_workout(user_input, top_n=5):
    tfidf, tfidf_matrix, exercise_df = load_model()
    user_vector = tfidf.transform([user_input])
    similarity = cosine_similarity(user_vector, tfidf_matrix)

    scores = similarity.flatten()
    sorted_idx = scores.argsort()[::-1]

    results = []
    seen = set()

    for idx in sorted_idx:

        title = exercise_df.iloc[idx]["Title"]

        if title in seen:
            continue

        seen.add(title)

        row = exercise_df.iloc[idx].copy()
        row["Similarity Score"] = round(scores[idx], 3)

        results.append(row)

        if len(results) == top_n:
            break

    return pd.DataFrame(results)[
        ["Title", "Type", "BodyPart", "Equipment", "Level", "Similarity Score"]
    ]

def show_page():
    load_css()
    st.markdown("""
    <div style="padding:10px 0 25px 0;">
        <h1 style="
            font-size:38px;
            font-weight:800;
            color:#0F172A;
        ">
            🎯 Workout Recommendations
        </h1>
        <p style="
            color:#64748B;
            font-size:15px;
        ">
            AI-powered personalized workout suggestions based on your profile.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if "user_profile" not in st.session_state:

        st.warning("⚠ Please complete User Input first to generate recommendations.")
        return

    user_profile = st.session_state["user_profile"]

    st.markdown("### 🧠 Your Profile")

    st.markdown(f"""
    <div style="
        background:#FFFFFF;
        border:1px solid #E2E8F0;
        padding:16px;
        border-radius:12px;
        color:#2563EB;
        font-weight:600;
    ">
        {user_profile}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    top_n = st.slider("Number of Recommendations", 1, 10, 5)

    st.markdown("<br>", unsafe_allow_html=True)

    results = recommend_workout(user_profile, top_n)

    st.markdown("### 🏋 Recommended Workouts")

    for _, row in results.iterrows():

        score = round(row["Similarity Score"] * 100, 1)

        st.markdown(f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E8F0;
            border-radius:14px;
            padding:18px;
            margin-bottom:14px;
        ">
            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
                gap:20px;
            ">
                <div>
                    <div style="
                        font-size:18px;
                        font-weight:700;
                        color:#0F172A;
                    ">
                        🏋 {row["Title"]}
                    </div>
                    <div style="
                        margin-top:8px;
                        font-size:13px;
                        color:#64748B;
                        line-height:1.6;
                    ">
                        Type: {row["Type"].title()} •
                        Body: {row["BodyPart"].title()} •
                        Equipment: {row["Equipment"].title()} •
                        Level: {row["Level"].title()}
                    </div>
                </div>
                <div style="
                    background:#2563EB;
                    color:white;
                    padding:12px 16px;
                    border-radius:12px;
                    text-align:center;
                    min-width:110px;
                ">
                    <div style="font-size:12px;opacity:0.8;">
                        Match
                    </div>
                    <div style="font-size:20px;font-weight:700;">
                        {score}%
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 📊 Full Results Table")
    st.dataframe(results, use_container_width=True)

    st.markdown("---")

    st.markdown("""
    ### 🧠 How Recommendation Works

    FitAI uses a **Content-Based Filtering system**:

    - TF-IDF Vectorization
    - Cosine Similarity
    - Feature Matching (Type, BodyPart, Equipment, Level)

    to find the most relevant workouts for your profile.
    """)

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
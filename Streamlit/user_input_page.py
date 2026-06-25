import streamlit as st
from utils.style import load_css
from pathlib import Path
import pickle

BASE_DIR = Path(__file__).resolve().parents[1]

def load_model():

    model_dir = BASE_DIR / "Models"

    exercise_df = pickle.load(open(model_dir / "exercise_df.pkl", "rb"))
    tfidf = pickle.load(open(model_dir / "tfidf.pkl", "rb"))
    tfidf_matrix = pickle.load(open(model_dir / "tfidf_matrix.pkl", "rb"))
    fitness_df = pickle.load(open(model_dir / "fitness_df.pkl", "rb"))

    return exercise_df, tfidf, tfidf_matrix, fitness_df


def show_page():
    load_css();
    exercise_df, tfidf, tfidf_matrix, fitness_df = load_model()

    st.markdown("""
    <div style="padding:10px 0 25px 0;">
        <h1 style="
            font-size:38px;
            font-weight:800;
            color:#0F172A;
        ">
            🧍 User Input
        </h1>
        <p style="
            color:#64748B;
            font-size:15px;
        ">
            Generate your personalized workout profile using manual selection or AI auto-generation.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs([
        "🎯 Manual Profile",
        "🤖 Auto Generate"
    ])

    with tab1:

        st.markdown("### 🎯 Build Your Workout Profile")

        col1, col2 = st.columns(2)

        with col1:
            workout_type = st.selectbox(
                "Workout Type",
                [
                    "strength",
                    "cardio",
                    "stretching",
                    "plyometrics",
                    "powerlifting",
                    "strongman",
                    "olympic weightlifting"
                ]
            )

            body_part = st.selectbox(
                "Target Body Part",
                [
                    "chest",
                    "back",
                    "legs",
                    "shoulders",
                    "arms",
                    "abdominals",
                    "full body"
                ]
            )

        with col2:
            equipment = st.selectbox(
                "Equipment",
                [
                    "body only",
                    "dumbbell",
                    "barbell",
                    "machine",
                    "kettlebells",
                    "bands",
                    "medicine ball"
                ]
            )

            level = st.selectbox(
                "Difficulty Level",
                ["beginner", "intermediate", "expert"]
            )

        user_profile = f"{workout_type} {body_part} {equipment} {level}"

        st.markdown("---")

        st.markdown("#### 🧠 Generated Profile")

        st.markdown(f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E8F0;
            padding:16px;
            border-radius:12px;
            font-size:15px;
            color:#2563EB;
            font-weight:600;
        ">
            {user_profile}
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("✨ Find Recommendation"):

            st.session_state["user_profile"] = user_profile
            st.success("Profile created successfully!")

    with tab2:

        st.markdown("### 🤖 AI Profile Generator")

        col1, col2 = st.columns(2)

        with col1:
            bmi = st.number_input(
                "BMI",
                min_value=10.0,
                max_value=50.0,
                value=22.0,
                step=0.1
            )

        with col2:
            intensity = st.slider(
                "Workout Intensity",
                1, 10, 5
            )

        if bmi < 18.5:

            if intensity <= 3:
                workout_type = "stretching"
            elif intensity <= 7:
                workout_type = "strength"
            else:
                workout_type = "strength"

        elif bmi < 25:

            if intensity <= 3:
                workout_type = "stretching"
            elif intensity <= 7:
                workout_type = "strength"
            else:
                workout_type = "powerlifting"

        elif bmi < 30:

            if intensity <= 3:
                workout_type = "cardio"
            elif intensity <= 7:
                workout_type = "cardio"
            else:
                workout_type = "plyometrics"

        else:
            if intensity <= 3:
                workout_type = "cardio"
            elif intensity <= 7:
                workout_type = "cardio"
            else:
                workout_type = "cardio"


        if intensity <= 3:
            level = "beginner"

        elif intensity <= 7:
            level = "intermediate"

        else:
            level = "expert"

        if workout_type == "strength":
            body_part = "chest"

        elif workout_type == "cardio":
            body_part = "legs"

        elif workout_type == "stretching":
            body_part = "full body"

        elif workout_type == "plyometrics":
            body_part = "legs"

        elif workout_type == "powerlifting":
            body_part = "back"

        if workout_type in ["cardio", "stretching"]:
            equipment = "body only"

        elif workout_type == "strength":
            equipment = "dumbbell" if intensity <= 5 else "barbell"

        elif workout_type == "plyometrics":
            equipment = "medicine ball"

        elif workout_type == "powerlifting":
            equipment = "barbell"

        generated_profile = (
            f"{workout_type} "
            f"{body_part} "
            f"{equipment} "
            f"{level}"
        )

        st.markdown("---")

        st.markdown("#### 🤖 AI Generated Profile")

        st.markdown(f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E2E8F0;
            padding:16px;
            border-radius:12px;
            font-size:15px;
            color:#2563EB;
            font-weight:600;
        ">
            {generated_profile}
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("✨ Generate Recommendation"):

            st.session_state["user_profile"] = generated_profile
            st.success("AI profile generated successfully!")

    st.markdown("---")

    st.markdown("""
    ### 📌 How It Works

    FitAI converts your input into a **feature-based profile**
    and matches it with similar workouts using:

    - TF-IDF Vectorization
    - Cosine Similarity
    - Content-Based Filtering

    This ensures personalized workout recommendations
    based on your fitness characteristics.
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
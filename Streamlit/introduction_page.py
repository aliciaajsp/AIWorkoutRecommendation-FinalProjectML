import streamlit as st
from utils.style import load_css

def show_page():
    load_css()

    st.markdown("""
    <div>
        <h1>
            Fit<span style="color:#4169E1;">AI</span>
        </h1>
        <p>
            Discover the perfect workout plan tailored to your body goals,
            fitness level, and preferences using intelligent recommendation systems.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Introduction
    st.markdown("## 📌 Introduction")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">
            <h3 style="color:#2563EB;">👥 Group Members</h3>
            <ul style="color:#0F172A; line-height:1.8;">
                <li>2802415744 - Mathilda Rafaela Christy Nugroho</li>
                <li>2802420315 - Adisca Gandawidjaja</li>
                <li>2802420334 - Alicia Angelina Jusup</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <h3 style="color:#2563EB;">📊 Project Overview</h3>
            <p style="color:#64748B; line-height:1.7;">
                FitAI is a machine learning-based workout recommender system that helps users
                discover personalized exercises based on fitness profile, workout type,
                body part, equipment, and difficulty level.
                <br><br>
                The system uses TF-IDF and cosine similarity to match user preferences
                with the most relevant workouts.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">
            <h3 style="color:#2563EB;">📍 Project Background</h3>
            <p style="color:#64748B; line-height:1.7;">
                Many users struggle to find suitable workouts that match their goals and physical conditions.
                Beginners often feel overwhelmed when choosing exercises.
                <br><br>
                FitAI solves this by providing intelligent, data-driven workout recommendations
                that improve consistency and fitness experience.
                <br><br>
                This project demonstrates how AI can be applied in fitness personalization.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Objectives
    st.markdown("## 🎯 Objectives")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
            <h4 style="color:#2563EB;">Personalized Training</h4>
            <p style="color:#64748B;">
                Build AI system that recommends workouts based on user profile.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <h4 style="color:#2563EB;">Smart Recommendation</h4>
            <p style="color:#64748B;">
                Match users with exercises based on similarity of features.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <h4 style="color:#2563EB;">AI Application</h4>
            <p style="color:#64748B;">
                Demonstrate AI usage in real-world fitness domain.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # About Project
    st.markdown("## 📂 Datasets")

    left, right = st.columns(2)

    with left:

        st.markdown("""
        <div class="card">
            <h3 style="color:#2563EB;">Dataset 1 - Fitness Metrics</h3>
            <p style="color:#64748B;">
                Source: Kaggle Exercise and Fitness Metrics Dataset
            </p>
            <b>Attributes:</b>
            <ul style="color:#64748B;">
                <li>Age</li>
                <li>Gender</li>
                <li>BMI</li>
                <li>Duration</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <h3 style="color:#2563EB;">TF-IDF Method</h3>
            <p style="color:#64748B;">
                TF-IDF converts text features into numerical vectors
                to compute similarity between workouts using cosine similarity.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with right:

        st.markdown("""
        <div class="card">
            <h3 style="color:#2563EB;">Dataset 2 - Exercise Data</h3>
            <b>Attributes:</b>
            <ul style="color:#64748B;">
                <li>Title</li>
                <li>Type</li>
                <li>BodyPart</li>
                <li>Equipment</li>
                <li>Level</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <h3 style="color:#2563EB;">System Info</h3>
            <p style="color:#64748B;">
                Model: Content-Based Filtering <br>
                Framework: Streamlit + Scikit-Learn <br>
                Features: Recommendation, EDA, Evaluation
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("## ⚠️ Limitations")

    st.markdown("""
    <div class="card">
        <ul style="color:#64748B; line-height:1.8;">
            <li><b>Limited physiological understanding</b> – only uses structured features.</li>
            <li><b>No injury/pain awareness</b> – cannot detect user health conditions.</li>
            <li><b>Basic personalization</b> – no deep behavioral modeling.</li>
            <li><b>Similarity-based learning only</b> – no causal reasoning like human trainers.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# footer
    st.markdown("""
    <div style="
        text-align:center;
        padding:25px;
        color:#8A8A8A;
        font-size:14px;
    ">
        Created by Group 4 - Machine Learning - Final Project 
    </div>
    """, unsafe_allow_html=True)
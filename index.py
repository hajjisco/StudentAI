
import streamlit as st

st.title("Student Performance Predictor 🎓")
st.write("Welcome to my first AI project!")

hours = st.number_input(
    "How many hours do you study daily?",
    min_value=0.0,
    max_value=24.0,
    value=2.0
)

attendance = st.slider(
    "Your attendance percentage",
    min_value=0,
    max_value=100,
    value=80
)

if st.button("Predict Performance"):
    score = min(100, (hours / 8) * 70 + attendance * 0.3)

    if score >= 70:
        result = "Excellent"
    elif score >= 50:
        result = "Good"
    else:
        result = "Needs Improvement"

    st.subheader(f"Predicted result: {result}")
    st.write(f"Estimated score: {score:.1f}%")
    st.caption("This is a demonstration, not a trained AI model.")

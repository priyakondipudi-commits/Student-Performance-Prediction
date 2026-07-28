import streamlit as st
import joblib

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

model = joblib.load("student_model.pkl")
st.sidebar.title("📚 Student Dashboard")

st.sidebar.markdown("""
### About Project

This project predicts whether a student will **PASS** or **FAIL** using Machine Learning.

### Technologies Used
- 🐍 Python
- 📊 Pandas
- 🤖 Scikit-Learn
- 🎨 Streamlit
- 💾 Joblib
""")
st.title("🎓 AI Powered Student Performance Prediction System")
st.markdown(
    "<p style='font-size:12px; color:#A9A9A9; margin-top:-10px;'>AI-based prediction of student academic performance.</p>",
    unsafe_allow_html=True
)
st.divider()
st.markdown("### Enter Student Details")

student_name = st.text_input("👤 Student Name")
roll_number = st.text_input("🆔 Roll Number")

department = st.selectbox(
    "🏫 Department",
    ["CSE", "ECE", "EEE", "MECH", "CIVIL", "AI&DS", "AI&ML"]
)
study_hours = st.slider("📚 Study Hours", 0, 12, 5)

attendance = st.slider("📅 Attendance (%)", 0, 100, 75)

previous_marks = st.slider("📝 Previous Marks", 0, 100, 60)

assignment = st.selectbox(
    "📂 Assignment Submitted",
    ["Yes", "No"]
)

assignment = 1 if assignment == "Yes" else 0

if st.button("🔍 Predict Result"):

    prediction = model.predict([[study_hours, attendance, previous_marks, assignment]])
    probability = model.predict_proba([[study_hours, attendance, previous_marks, assignment]])
    confidence = max(probability[0]) * 100

    if prediction[0] == 1:
        st.success("🎉 Student Will PASS")
        st.balloons()
        st.info(f"🎯 Confidence Score: {confidence:.2f}%")
    else:
        st.error("❌ Student Will FAIL")
        st.info(f"🎯 Confidence Score: {confidence:.2f}%")

    if previous_marks >= 85:
        st.success("⭐⭐⭐⭐⭐ Performance Level: Excellent")
    elif previous_marks >= 70:
        st.success("⭐⭐⭐⭐ Performance Level: Good")
    elif previous_marks >= 50:
        st.warning("⭐⭐⭐ Performance Level: Average")
    else:
        st.error("⭐⭐ Performance Level: Needs Improvement")

    st.subheader("💡 Suggestions")

    if attendance < 75:
        st.warning("📅 Improve attendance above 75%.")

    if study_hours < 4:
        st.warning("📚 Increase study hours.")

    if previous_marks < 50:
        st.warning("📝 Focus on improving previous marks.")

    if assignment == 0:
        st.warning("📂 Submit assignments regularly.")  

    st.subheader("📊 Performance Summary")

    st.write("📚 Study Hours")
    st.progress(study_hours / 12)

    st.write("📅 Attendance")
    st.progress(attendance / 100)

    st.write("📝 Previous Marks")
    st.progress(previous_marks / 100)

st.markdown("---")
st.markdown("👩‍💻 Developed by **KONDIPUDI DURGA BHAVANI**")
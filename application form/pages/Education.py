import streamlit as st

if 'page' not in st.session_state:
    st.session_state.page = "intro"

if st.session_state.page != "education":
    st.warning("Please start from the beginning.")
    if st.button("Go to Start"):
        st.session_state.page = "intro"
        st.rerun()
    st.stop()

st.title("Step 1: Personal & Educational Details")

with st.form("education_form"):
    st.subheader("Personal Info")
    name = st.text_input("Full Name *")
    email = st.text_input("Email *")
    phone = st.text_input("Phone Number *")
    age = st.number_input("Age", min_value=16, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])

    st.subheader("Education")
    degree = st.selectbox("Highest Degree", ["High School", "Bachelor's", "Master's", "PhD", "Other"])
    institution = st.text_input("Institution Name")
    year = st.number_input("Graduation Year", min_value=1950, max_value=2030)
    gpa = st.number_input("GPA / Percentage (optional)", min_value=0.0, max_value=100.0, step=0.1)

    submitted = st.form_submit_button("Next → Skills")
    if submitted:
        if not name or not email or not phone:
            st.error("Please fill all required fields.")
        else:
            st.session_state.app_data = {
                'name': name, 'email': email, 'phone': phone, 'age': age, 'gender': gender,
                'degree': degree, 'institution': institution, 'year': year, 'gpa': gpa
            }
            st.session_state.page = "skills"
            st.success("Saved! Moving to next step...")
            st.rerun()

if st.button("← Back to Intro"):
    st.session_state.page = "intro"
    st.rerun()

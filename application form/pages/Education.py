import streamlit as st

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "intro"
if 'app_data' not in st.session_state:
    st.session_state.app_data = {}

if st.session_state.current_page != "education":
    st.warning("Please start from the main page.")
    if st.button("Go to Start"):
        st.session_state.current_page = "intro"
        st.rerun()
    st.stop()

st.title("Step 1: Personal & Educational Details")

with st.form("education_form"):
    st.subheader("Personal Info")
    name = st.text_input("Full Name *", value=st.session_state.app_data.get('name', ''))
    email = st.text_input("Email *", value=st.session_state.app_data.get('email', ''))
    phone = st.text_input("Phone Number *", value=st.session_state.app_data.get('phone', ''))
    age = st.number_input("Age", min_value=16, max_value=100, value=st.session_state.app_data.get('age', 18))
    gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"], 
                          index=["Male", "Female", "Other", "Prefer not to say"].index(st.session_state.app_data.get('gender', "Male")) if st.session_state.app_data.get('gender') in ["Male", "Female", "Other", "Prefer not to say"] else 0)

    st.subheader("Education")
    degree = st.selectbox("Highest Degree", ["High School", "Bachelor's", "Master's", "PhD", "Other"], 
                          index=["High School", "Bachelor's", "Master's", "PhD", "Other"].index(st.session_state.app_data.get('degree', "Bachelor's")) if st.session_state.app_data.get('degree') else 1)
    institution = st.text_input("Institution Name", value=st.session_state.app_data.get('institution', ''))
    year = st.number_input("Graduation Year", min_value=1950, max_value=2030, value=st.session_state.app_data.get('year', 2023))
    gpa = st.number_input("GPA / Percentage (optional)", min_value=0.0, max_value=100.0, step=0.1, value=st.session_state.app_data.get('gpa', 0.0))

    submitted = st.form_submit_button("Next → Skills")
    if submitted:
        if not name or not email or not phone:
            st.error("Please fill all required fields.")
        else:
            st.session_state.app_data.update({
                'name': name, 'email': email, 'phone': phone, 'age': age, 'gender': gender,
                'degree': degree, 'institution': institution, 'year': year, 'gpa': gpa
            })
            st.session_state.current_page = "skills"
            st.success("Saved! Moving to Skills...")
            st.rerun()

if st.button("← Back to Intro"):
    st.session_state.current_page = "intro"
    st.rerun()

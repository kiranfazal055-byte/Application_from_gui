import streamlit as st

st.set_page_config(page_title="Application Form", page_icon="📋", layout="centered")

st.title("Welcome to the Application Form")
st.markdown("""
### For Job / Digital Course Enrollment

This form has 5 steps:
1. Personal Information
2. Educational Details
3. Skills
4. Experience
5. Upload Photo & Submit

Please fill all sections carefully.
""")

st.info("Click 'Start Application' to begin")

if st.button("Start Application →"):
    st.session_state.current_page = "education"
    st.session_state.app_data = {}  # Initialize data
    st.rerun()

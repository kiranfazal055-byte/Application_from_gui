import streamlit as st

st.title("Step 3: Experience")

with st.form("experience_form"):
    exp_level = st.selectbox("Experience Level", ["Fresher", "0-1 year", "1-3 years", "3-5 years", "5+ years"])
    job_title = st.text_input("Current/Most Recent Job Title")
    company = st.text_input("Company Name")
    years = st.slider("Years of Experience", 0, 30, 0)
    description = st.text_area("Briefly describe your experience")

    submitted = st.form_submit_button("Next → Upload Photo")
    if submitted:
        st.session_state['app_data'].update({
            'exp_level': exp_level, 'job_title': job_title, 'company': company,
            'years_exp': years, 'exp_desc': description
        })
        st.success("Experience saved!")
        st.switch_page("pages/5_Upload_Photo.py")

if st.button("← Back"):
    st.switch_page("pages/3_Skills.py")
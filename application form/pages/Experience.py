import streamlit as st

if st.session_state.current_page != "experience":
    st.warning("Please complete previous steps.")
    st.stop()

st.title("Step 3: Experience")

with st.form("experience_form"):
    exp_level = st.selectbox("Experience Level", ["Fresher", "0-1 year", "1-3 years", "3-5 years", "5+ years"],
                             index=["Fresher", "0-1 year", "1-3 years", "3-5 years", "5+ years"].index(st.session_state.app_data.get('exp_level', "Fresher")))
    job_title = st.text_input("Current/Most Recent Job Title", value=st.session_state.app_data.get('job_title', ''))
    company = st.text_input("Company Name", value=st.session_state.app_data.get('company', ''))
    years = st.slider("Years of Experience", 0, 30, st.session_state.app_data.get('years_exp', 0))
    description = st.text_area("Briefly describe your experience", value=st.session_state.app_data.get('exp_desc', ''))

    submitted = st.form_submit_button("Next → Upload Photo")
    if submitted:
        st.session_state.app_data.update({
            'exp_level': exp_level, 'job_title': job_title, 'company': company,
            'years_exp': years, 'exp_desc': description
        })
        st.session_state.current_page = "upload"
        st.success("Experience saved!")
        st.rerun()

if st.button("← Back"):
    st.session_state.current_page = "skills"
    st.rerun()

import streamlit as st

st.title("Step 2: Skills")

if 'app_data' not in st.session_state:
    st.error("Please start from the beginning.")
    st.stop()

with st.form("skills_form"):
    st.subheader("Technical Skills")
    skills = st.multiselect("Select your skills", 
                            ["Python", "JavaScript", "Excel", "Data Analysis", "Machine Learning", 
                             "Graphic Design", "Marketing", "Communication", "Leadership", "Other"])

    other_skill = st.text_input("Other skills (comma separated)")

    st.subheader("Certifications")
    certs = st.text_area("List certifications (optional)")

    submitted = st.form_submit_button("Next → Experience")
    if submitted:
        st.session_state['app_data'].update({
            'skills': skills + [s.strip() for s in other_skill.split(',') if s.strip()],
            'certs': certs
        })
        st.success("Skills saved!")
        st.switch_page("pages/4_Experience.py")

if st.button("← Back"):
    st.switch_page("pages/2_Education.py")
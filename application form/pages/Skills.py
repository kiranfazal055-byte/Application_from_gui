import streamlit as st

if st.session_state.get("page") != "skills":
    st.warning("Please complete previous steps.")
    if st.button("Go Back"):
        st.session_state.page = "education"
        st.rerun()
    st.stop()

st.title("Step 2: Skills")

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
        all_skills = skills + [s.strip() for s in other_skill.split(',') if s.strip()]
        st.session_state.app_data.update({'skills': all_skills, 'certs': certs})
        st.session_state.page = "experience"
        st.success("Skills saved!")
        st.rerun()

if st.button("← Back"):
    st.session_state.page = "education"
    st.rerun()

import streamlit as st

if st.session_state.current_page != "skills":
    st.warning("Please complete previous steps.")
    if st.button("Go Back to Education"):
        st.session_state.current_page = "education"
        st.rerun()
    st.stop()

st.title("Step 2: Skills")

with st.form("skills_form"):
    skills = st.multiselect("Select your skills", 
                            ["Python", "JavaScript", "Excel", "Data Analysis", "Machine Learning", 
                             "Graphic Design", "Marketing", "Communication", "Leadership", "Other"],
                            default=st.session_state.app_data.get('skills', []))

    other_skill = st.text_input("Other skills (comma separated)", value=", ".join(st.session_state.app_data.get('other_skills', [])))

    certs = st.text_area("List certifications (optional)", value=st.session_state.app_data.get('certs', ''))

    submitted = st.form_submit_button("Next → Experience")
    if submitted:
        all_skills = skills + [s.strip() for s in other_skill.split(',') if s.strip()]
        st.session_state.app_data.update({
            'skills': all_skills,
            'certs': certs
        })
        st.session_state.current_page = "experience"
        st.success("Skills saved!")
        st.rerun()

if st.button("← Back"):
    st.session_state.current_page = "education"
    st.rerun()

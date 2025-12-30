import streamlit as st
import pandas as pd
from datetime import datetime

if st.session_state.current_page != "upload":
    st.warning("Please complete previous steps.")
    st.stop()

st.title("Step 4: Upload Photo & Submit")

uploaded_photo = st.file_uploader("Upload your recent photo (JPG/PNG)", type=["jpg", "jpeg", "png"])
uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_photo:
    st.image(uploaded_photo, caption="Photo Preview", width=200)

if st.button("Submit Application"):
    data = st.session_state.app_data.copy()
    data.update({
        'photo_uploaded': uploaded_photo is not None,
        'resume_uploaded': uploaded_resume is not None,
        'submitted_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    st.success("Application Submitted Successfully! 🎉")
    st.balloons()
    st.json(data)

    # Save to CSV
    df = pd.DataFrame([data])
    df.to_csv("applications.csv", mode='a', header=not st.file_exists("applications.csv"), index=False)

    if st.button("Start New Application"):
        st.session_state.clear()
        st.session_state.current_page = "intro"
        st.rerun()

if st.button("← Back"):
    st.session_state.current_page = "experience"
    st.rerun()

import streamlit as st
import pandas as pd
from datetime import datetime

if st.session_state.get("page") != "upload":
    st.warning("Please complete previous steps.")
    st.stop()

st.title("Step 4: Upload Photo & Submit")

uploaded_photo = st.file_uploader("Upload your recent photo (JPG/PNG)", type=["jpg", "jpeg", "png"])
uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"], help="Optional")

if uploaded_photo:
    st.image(uploaded_photo, caption="Preview", width=200)

if st.button("Submit Application"):
    data = st.session_state.app_data
    data.update({
        'photo': uploaded_photo.name if uploaded_photo else "Not uploaded",
        'resume': uploaded_resume.name if uploaded_resume else "Not uploaded",
        'submitted_at': datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    st.success("Application Submitted Successfully!")
    st.balloons()
    st.json(data)

    # Save to CSV
    df = pd.DataFrame([data])
    df.to_csv("applications.csv", mode='a', header=not st.file_exists("applications.csv"), index=False)

    if st.button("Start New Application"):
        st.session_state.clear()
        st.session_state.page = "intro"
        st.rerun()

if st.button("← Back"):
    st.session_state.page = "experience"
    st.rerun()

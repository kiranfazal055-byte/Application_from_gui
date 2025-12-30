import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Step 4: Upload Photo & Submit")

uploaded_photo = st.file_uploader("Upload your recent photo (JPG/PNG)", type=["jpg", "jpeg", "png"])
uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"], help="Optional")

if uploaded_photo:
    st.image(uploaded_photo, caption="Preview", width=200)

if st.button("Submit Application"):
    if 'app_data' not in st.session_state:
        st.error("No data found. Please start again.")
    else:
        data = st.session_state['app_data']
        data.update({
            'photo': uploaded_photo.name if uploaded_photo else "Not uploaded",
            'resume': uploaded_resume.name if uploaded_resume else "Not uploaded",
            'submitted_at': datetime.now().strftime("%Y-%m-%d %H:%M")
        })

        # Show summary
        st.success("Application Submitted Successfully!")
        st.balloons()
        st.write("### Summary")
        st.json(data)

        # Optional: Save to CSV (for your records)
        df = pd.DataFrame([data])
        df.to_csv("applications.csv", mode='a', header=not pd.io.common.file_exists("applications.csv"), index=False)

        if st.button("Start New Application"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.switch_page("streamlit_app.py")
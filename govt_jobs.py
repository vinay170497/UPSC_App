import streamlit as st
import pandas as pd
from utils.job_scraper import fetch_govt_jobs

def show_govt_jobs():
    st.title("📌 Govt. Job Openings")
    st.write("📢 **Feature Overview:**")
    st.markdown("- Fetch and display the latest government job notifications.")
    st.markdown("- Get updates from official sources (UPSC, SSC, etc.).")

    df = fetch_govt_jobs()

    if df.empty:
        st.warning("No job listings found at the moment. Please check again later.")
    else:
        st.dataframe(df)

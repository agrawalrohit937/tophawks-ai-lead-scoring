import streamlit as st
import pandas as pd
from lead_scoring import process_data

st.set_page_config(page_title="AI Lead Scoring Tool", layout="wide")

st.title("🚀 AI Lead Scoring Tool")
st.info("High Score = High conversion probability 🚀")

st.write("Upload your lead data CSV file to get conversion scores.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("### 📊 Original Data")
    st.dataframe(df)

    # Process data
    result = process_data(df)

    # Sort by score (highest first)
    result = result.sort_values(by="score", ascending=False)

    st.write("### 🔥 Top Priority Leads")
    st.dataframe(result.head(3))

    st.write("### 📈 All Scored Leads")
    st.dataframe(result)

    st.download_button(
        label="📥 Download Results",
        data=result.to_csv(index=False),
        file_name="scored_leads.csv",
        mime="text/csv"
    )
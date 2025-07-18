import streamlit as st
import pandas as pd

st.set_page_config(page_title="KPTCL Dashboard", page_icon="⚡", layout="wide", initial_sidebar_state="expanded")
st.title("GESCOM Dashboard")

# ✅ Typo fixed: file_uploader, not file_uploder
data_file = st.file_uploader("Upload CSV File", type=["csv"])

if data_file is not None:
    df = pd.read_csv(data_file)

    st.subheader("Data Preview")
    st.dataframe(df)

    st.subheader("📈 Basic Statistics")
    st.write(df.describe())

    if "Division" in df.columns:
        st.subheader("Division Wise Consumer Count")
        Division_Count = df.groupby("Division")["Account ID"].value_counts()
        st.bar_chart(Division_Count)
 






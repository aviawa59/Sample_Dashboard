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

    if "Division" in df.columns and "Account ID" in df.columns:
        st.subheader("Division Wise Consumer Count")
        Division_Count_df = (df.groupby("Division")["Account ID"].nunique.reset_index())
        st.write(division_count_df)
        st.bar_chart(data = Division_Count_df, x = "Division", y = "Account ID")
    
    else:
        st.warning("Required columns 'Division' or 'Account ID' not found in the uploaded file")
 






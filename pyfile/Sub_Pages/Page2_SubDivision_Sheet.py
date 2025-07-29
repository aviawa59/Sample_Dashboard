import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt 
import seaborn as sns 

st.title("GESCOM Dashboard - SubDivision")

data_file = st.file_uploader("Upload CSV File", type=['csv'])

if data_file is not None:
    df1 = pd.read_csv(data_file)
    df1.columns = df1.columns.str.strip()

    st.subheader("Basic Stats")
    st.write(df1.describe())

    st.subheader("Divisions and Sub-Divisions")
    grouped = df1.groupby(["Division", "Subdivision"]).size().reset_index(name='Count')

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=grouped, x="Subdivision", y="Count", hue="Division", ax=ax)
    plt.xticks(rotation=45)

    st.pyplot(fig)


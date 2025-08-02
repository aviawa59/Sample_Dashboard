import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import streamlit as st

st.set_page_config(page_title = "KPTCL Dashboard" , layout = 'wide')
st.title("GESCOM DASHBOARD")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #87CEEB; /* sky blue */
    }
    </style>
    """,
    unsafe_allow_html = True
)

data_file = st.file_uploader("Upload CSV FIle", type = ['csv'])

if data_file is not None:
    df = pd.read_csv(data_file)
    df.columns = df.columns.str.strip()

    st.subheader("🧾 Data Preview")
    st.dataframe(df)

    st.subheader("📈 Basic Statistics")
    st.write(df.describe())


    #Grouping Data in order to get counts per Division

    grp_data = df.groupby("Division")["Account ID"].count().reset_index()
    grp_data = grp_data.sort_values(by="Account ID", ascending = True)


    #for plotting
    cmap_graph = cm.get_cmap('plasma', len(grp_data))
    colours = [cmap_graph(i) for i in range(len(grp_data))]
    
    #plotting using matplotlib in streamlit is bit different - synatx and all needs to be changed
    fig, ax = plt.subplots(figsize = (10, 6))
    ax.barh(grp_data["Division"], grp_data["Account ID"], color=colours)
    ax.set_xlabel("No. of Consumers")
    ax.set_ylabel("Divisions")
    ax.set_title("Division wise Consumer Meter Installation Details")
    ax.grid(axis='x', linestyle='--', alpha=0.7)

    st.pyplot(fig)


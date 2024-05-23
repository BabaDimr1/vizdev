import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load custom CSS
css_file_path = os.path.join(os.path.dirname(__file__), "..", "styles.css")
with open(css_file_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the data
data = pd.read_csv('./cleaned_data.csv')
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Load the predicted data
data2 = pd.read_csv("./predicted_data_2024.csv")
data2['timestamp'] = pd.to_datetime(data2['timestamp'])

# Page title
st.title("Comparison between 2023 and 2024")

# Select factor
factor1 = st.selectbox("Select First Factor:", ["TC", "HUM", "PRES", "US", "SOIL1"])
factor2 = st.selectbox("Select second Factor:", ["TC_predicted", "HUM_predicted", "PRES_predicted", "US_predicted", "SOIL1_predicted"])

# Filter the dataframes based on the selected factor
select_data = data[['timestamp', factor1]]
select_data2 = data2[['timestamp', factor2]]

if st.button("calculate the comparison!"):
    # Line Chart
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(select_data['timestamp'], select_data[factor1], label='2023')
    ax.plot(select_data2['timestamp'], select_data2[factor2], label='2024')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel(factor1)
    ax.set_title(f'Visualization of {factor1}')
    ax.legend()
    st.pyplot(fig)

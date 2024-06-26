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

# Filter for Temperature (TC)
temp_data = data[['timestamp', 'TC']]

# Page title
st.title("Temperature (TC) Visualizations")

# Line Chart
st.markdown("<div class='card'><h3>Temperature Over Time</h3></div>", unsafe_allow_html=True)
st.line_chart(temp_data.set_index('timestamp')['TC'])

st.area_chart(temp_data.set_index('timestamp')['TC'])

# Bar Chart
st.markdown("<div class='card'><h3>Temperature Distribution</h3></div>", unsafe_allow_html=True)
st.bar_chart(temp_data.set_index('timestamp')['TC'])

# Pie Chart
st.markdown("<div class='card'><h3>Temperature Proportions</h3></div>", unsafe_allow_html=True)
temp_bins = pd.cut(temp_data['TC'], bins=5)
temp_pie_data = temp_bins.value_counts().reset_index()
temp_pie_data.columns = ['Temperature Range', 'Count']  # Rename columns
fig, ax = plt.subplots()
ax.pie(temp_pie_data['Count'], labels=temp_pie_data['Temperature Range'], autopct='%1.1f%%')
st.pyplot(fig)

# Scatter Plot
st.markdown("<div class='card'><h3>Temperature Scatter Plot</h3></div>", unsafe_allow_html=True)
fig, ax = plt.subplots()
sns.scatterplot(x='timestamp', y='TC', data=temp_data, ax=ax)
st.pyplot(fig)

st.markdown("<footer>Smart Agriculture Dashboard © 2024</footer>", unsafe_allow_html=True)

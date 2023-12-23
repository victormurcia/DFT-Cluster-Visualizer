import streamlit as st
import streamlit.components.v1 as components
import requests

plot_url = 'https://drive.google.com/uc?export=download&id=1uczhuw8go5I-d0NpJbcQ2vDj4O8pzo5q'

# For HTML Plotly plot
html_content = requests.get(plot_url).text
#components.html(html_content, height=800)

# Load the HTML file
#html_file = open('dft_clusters.html', 'r', encoding='utf-8')
#source_code = html_file.read() 

# Set up the title and description for the Streamlit app
st.title('Interactive Visualization of DFT Clustering Algorithm')
st.write('This interactive plot demonstrates the clustering visualization. Hover over the plot to see more details about each transition pair like the percent overlap and the cluster it belongs to.')
st.write('This was made using Plotly, unfortunately, encoding the coloring algorithm I made was not possible to implement at the moment. But maybe in the future...')

# Use Streamlit's components.html to display the plot
components.html(html_content , width=700, height=800)

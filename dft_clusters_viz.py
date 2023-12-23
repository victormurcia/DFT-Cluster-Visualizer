import streamlit as st
import streamlit.components.v1 as components

# Load the HTML file
html_file = open('dft_clusters.html', 'r', encoding='utf-8')
source_code = html_file.read() 

# Use Streamlit's components.html to display the plot
components.html(source_code, width=700, height=800)

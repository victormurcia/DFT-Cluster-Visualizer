# DFT-Cluster-Visualizer

This repo contains the methods used to create the visualization for the DFT clustering algorithm. The plot shows the Overlap Matrix such that each transition pair is color coded by cluster. Furthermore, the color intensity represents the percent overlap. The brighter the color the higher the overlap and viceversa.

![Cluster Visualization](https://github.com/victormurcia/DFT-Cluster-Visualizer/blob/main/cluster%20viz%202.png)

# Making Visualization More Interactive

I also started playing with making this visualization interactive by using Plotly and deploying the figure in Streamlit. Encoding the same information as in the static image doesn't seem currently possible with Plotly, or at the very least, it'll be challenging. I'll maybe play more with that later. 

You can find the app here: 
![Interactive Demo](https://dft-cluster-visualizer-5paa583li2mtzeskmztwzk.streamlit.app/)

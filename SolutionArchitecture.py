import streamlit as st
import graphviz

st.set_page_config(page_title="High-Level Solution Architecture", layout="wide")

st.title("High-Level Solution Architecture")

dot = graphviz.Digraph()

# Nodes
dot.node("NI", "New Incident", shape="box", style="filled", color="lightblue")
dot.node("CA", "Classification Agent", shape="box", style="filled", color="lightgray")
dot.node("RA", "Retrieval Agent", shape="box", style="filled", color="lightgray")
dot.node("LLM", "LLM\n(Large Language Model)", shape="ellipse", style="filled", color="lightyellow")
dot.node("ResA", "Resolution Agent", shape="box", style="filled", color="lightgray")
dot.node("PR", "Possible Resolution", shape="box", style="filled", color="lightgreen")

# External Data Sources
dot.node("KB", "Knowledge Base", shape="cylinder", style="filled", color="pink")
dot.node("ID", "Incident Dump", shape="cylinder", style="filled", color="lightblue")
dot.node("LOGS", "Logs", shape="cylinder", style="filled", color="orange")

# Edges
dot.edge("NI", "CA", label="")
dot.edge("CA", "RA", label="Incident Title\nIncident Description\nCategory")
dot.edge("RA", "LLM", label="Context")
dot.edge("LLM", "ResA", label="")
dot.edge("ResA", "PR", label="")

# External Data Connections
dot.edge("RA", "KB", dir="both")
dot.edge("RA", "ID", dir="both")
dot.edge("RA", "LOGS", dir="both")

st.graphviz_chart(dot)

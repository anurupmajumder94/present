import streamlit as st
import graphviz

st.set_page_config(page_title="Data Ingestion", layout="wide")

st.title("Data Ingestion")

# Graphviz Digraph
dot = graphviz.Digraph()

# Nodes
dot.node("KB", "Knowledge Base", shape="cylinder", style="filled", color="pink")
dot.node("ID", "Incident Dumps", shape="cylinder", style="filled", color="lightblue")
dot.node("CH", "Chunks", shape="box", style="filled", color="lightgray")
dot.node("VEC", "Vectors", shape="ellipse", style="filled", color="lightyellow")
dot.node("DB", "Vector Database", shape="cylinder", style="filled", color="lightgreen")

# Edges
dot.edge("KB", "CH", label="Split")
dot.edge("CH", "VEC", label="Vectorization")
dot.edge("ID", "VEC", label="Vectorization")
dot.edge("VEC", "DB")

# Render in Streamlit
st.graphviz_chart(dot)

# Right side explanation
st.markdown("""
### Beyond Simple Split
Documents can be complex and contain tables, images, etc.  
Hence, simple splitting techniques might fail.  
Using **unstructured** or **Azure Document Intelligence** might help.

### Choice of Vectorization Technique and Vector DB
- Major LLM and aggregator companies provide multiple vectorization techniques  
- Free open-source alternatives exist as well  
- Same applies to database selection  
- The choice must be made based on **use case and budget**
""")

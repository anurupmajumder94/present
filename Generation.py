import streamlit as st
import graphviz

st.set_page_config(page_title="Generation", layout="wide")

st.title("Generation")

# Two columns: Graph (left) + Text (right)
col1, col2 = st.columns([2, 1])

with col1:
    dot = graphviz.Digraph()

    # Nodes
    dot.node("NI", "New Incident", shape="box", style="filled", color="lightblue")
    dot.node("KB", "Related Knowledge Base", shape="cylinder", style="filled", color="pink")
    dot.node("ID", "Incident Details", shape="box", style="filled", color="lightgray")
    dot.node("LS", "Log Statement", shape="note", style="filled", color="lightyellow")
    dot.node("PII", "PII FILTER", shape="diamond", style="filled", color="lightcoral")
    dot.node("LLM", "LLM", shape="ellipse", style="filled", color="lightcyan")
    dot.node("PR", "Possible Resolution", shape="box", style="filled", color="lightgreen")

    # Edges (dashed for supporting context)
    dot.edge("NI", "PII", style="dashed")
    dot.edge("KB", "PII", style="dashed")
    dot.edge("ID", "PII", style="dashed")
    dot.edge("LS", "PII", style="dashed")

    dot.edge("PII", "LLM", label="")
    dot.edge("LLM", "PR", label="")

    # Render
    st.graphviz_chart(dot, use_container_width=True)

with col2:
    st.subheader("PII Filtration")
    st.markdown("""
    PII filtration can be done using **Natural Language Processing (NLP)**  
    and **Named Entity Recognition (NER)** to identify PII elements such as:  

    - Names  
    - Phone numbers  
    - Email addresses  
    - Custom entities (e.g., employee ID, internal tags)  
    """)

    st.subheader("Self Reflective Generation")
    st.markdown("""
    This allows measuring the **correctness of responses on the go**  
    and enables **query rewriting** for better accuracy.
    """)

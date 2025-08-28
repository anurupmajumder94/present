import streamlit as st
import graphviz

st.set_page_config(page_title="Data Retrieval", layout="wide")

st.title("Data Retrieval")

# Two columns: Graph on left, Text on right
col1, col2 = st.columns([2, 1])

with col1:
    dot = graphviz.Digraph()

    # Nodes
    dot.node("NI", "New Incident", shape="box", style="filled", color="lightblue")
    dot.node("VEC", "Vectors", shape="ellipse", style="filled", color="lightyellow")
    dot.node("DB", "Vector Database", shape="cylinder", style="filled", color="lightgreen")
    dot.node("SIM", "Similar Vectors\n& Associated Documents/Incidents", shape="box", style="filled", color="lightgray")
    dot.node("LOGS", "Logs", shape="cylinder", style="filled", color="orange")
    dot.node("LS", "Log Statement", shape="note", style="filled", color="lightpink")

    # Edges
    dot.edge("NI", "VEC", label="Vectorization")
    dot.edge("VEC", "DB", label="Query")
    dot.edge("DB", "SIM", label="Return")
    dot.edge("SIM", "NI", style="dashed")
    dot.edge("NI", "LOGS", style="dashed")
    dot.edge("LOGS", "LS", style="dashed")

    # Render graph
    st.graphviz_chart(dot, use_container_width=True)

with col2:
    st.subheader("Connectivity of Agents and Tools")
    st.markdown("""
    - **New Incident** is vectorized and sent to the **Vector Database**.  
    - **Database query** retrieves similar vectors and associated incidents/documents.  
    - **Logs** are analyzed and linked to the incident.  
    - **Log Statements** are generated for further context.  
    - Agent connection can be made using **secure APIs** or even **MCP servers**.  
    """)

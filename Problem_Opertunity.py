import streamlit as st

st.set_page_config(page_title="Problem & Opportunity", layout="wide")

st.title("Problem Statement & Opportunity")

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.header("Problem Statement")
    st.write("""
    Incident resolution in large enterprises is a time-consuming, manual, and error-prone process. 
    IT teams and support engineers often spend hours triaging incidents, analyzing logs, identifying root causes, 
    and searching through fragmented documentation or runbooks. When initial efforts fail, the issue is escalated 
    across multiple teams, further increasing resolution time.

    This traditional approach results in:
    - High Mean Time to Resolution (MTTR)  
    - SLA breaches and compliance penalties  
    - Customer dissatisfaction and service disruptions  
    - Increased operational costs due to manual effort  
    - Repetitive handling of similar or recurring issues  
    """)

with col2:
    st.header("Opportunity")
    st.write("""
    Many of these tasks — particularly in Level 1 and Level 2 support workflows — are partially or fully automatable.  

    This approach enables:  
    - Ticket classification and triage automated using AI-based classifiers  
    - Contextual data gathering (logs, metrics, historical tickets) via intelligent retrieval agents  
    - Root cause analysis leveraging GenAI with contextual reasoning  
    - Resolution suggestions auto-generated from knowledge bases or past fixes  
    - Execution of remediation scripts or commands via agents (with human-in-the-loop validation if needed)  
    """)

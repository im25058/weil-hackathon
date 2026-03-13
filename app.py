import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent.agent_graph import run_agent
from blockchain.weilchain_client import store_on_chain
from utils.replay import load_audit_logs
from utils.verification import verify_report
from utils.graph_visualizer import draw_agent_graph
from utils.pdf_generator import create_pdf
from utils.trust_score import calculate_trust_score
from utils.analytics import credibility_chart
st.set_page_config(page_title="Fantastic WEB4 AI", layout="wide")
st.markdown("""
### Agents in the System

Planner Agent 🤖  
Research Agent 🔎  
Validator Agent ✔  
""")

st.title("Fantastic WEB4 AI")

tab1, tab2, tab3 = st.tabs(["Research Agent", "Audit Logs", "Verification"])
st.subheader("Research Comparison Mode")

query1 = st.text_input("Research Topic A")

query2 = st.text_input("Research Topic B")

if st.button("Compare Research", key="compare_button"):

    report1, _ = run_agent(query1)
    report2, _ = run_agent(query2)

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Topic A Report")
        st.write(report1)

    with col2:
        st.write("### Topic B Report")
        st.write(report2)
    score = calculate_trust_score()

    st.metric("Research Credibility Score", f"{score}%")

# ---------------- TAB 1 ----------------

with tab1:

    st.header("Agent Workflow")

    graph = draw_agent_graph()
    st.graphviz_chart(graph)

    query = st.text_input("Enter research topic")

    if st.button("Run Agent", key="run_agent_button1"):

        report, hash_value = run_agent(query)

        st.session_state["report"] = report
        st.session_state["hash"] = hash_value

        st.write("### Generated Report")
        st.write(report)

        st.write("### Hash")
        st.write(hash_value)
        st.subheader("Research Analytics Dashboard")

score = calculate_trust_score()

chart = credibility_chart(score)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Credibility Score", f"{score}%")

with col2:
    st.metric("Agent Steps Executed", len(load_audit_logs()))

with col3:
    if "report" in st.session_state:

     report = st.session_state["report"]

     st.metric("Report Length", f"{len(report.split())} words")

st.pyplot(chart)

if "report" in st.session_state:

        if st.button("Approve and Store on Blockchain", key="approve_button"):

            tx = store_on_chain(st.session_state["hash"])

            st.success("Stored on Weilchain")

            st.write(tx)

        pdf_file = create_pdf(st.session_state["report"])

        st.download_button(
            label="Download Report as PDF",
            data=pdf_file,
            file_name="research_report.pdf"
        )

# ---------------- TAB 2 ----------------

with tab2:

    st.header("Execution Replay")

    logs = load_audit_logs()

    for log in logs:

        st.write("Step:", log["step_id"])
        st.write("Action:", log["action"])
        st.write("Input:", log["input"])
        st.write("Output:", log["output"])
        st.write("Timestamp:", log["timestamp"])

        st.divider()

# ---------------- TAB 3 ----------------

with tab3:

    st.header("Verify Research Report")

    report_text = st.text_area("Paste Report")

    hash_text = st.text_input("Enter Hash")

    if st.button("Run Agent", key="run_agent_button2"):

     with st.spinner("AI Agents researching..."):

        report, hash_value = run_agent(query)

        result = verify_report(report_text, hash_text)

        if result:

            st.success("Report Verified")

        else:

            st.error("Report Invalid")
st.subheader("AI Reasoning Explanation")

logs = load_audit_logs()

for log in logs:

    st.write(f"Step {log['step_id']} — {log['action']}")      
    st.subheader("Execution Timeline")
    st.markdown(f"""
    **Step {log['step_id']}**

    Action: {log['action']}

    Timestamp: {log['timestamp']}
    """)  
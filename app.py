import streamlit as st
import time
import os
from src.crew import run_research

# --- Page Config ---
st.set_page_config(page_title="Agentic Researcher", page_icon="🕵️", layout="wide")

# --- Hide Streamlit Header (GitHub icon) ---
hide_header = """
<style>
header[data-testid="stHeader"] {
    display: none;
}
</style>
"""
st.markdown(hide_header, unsafe_allow_html=True)

st.title("🕵️ Agentic Researcher")
st.markdown("Give me a topic, and my AI agents will search the web, read the top articles, and write a cited report.")

# --- Input Area ---
topic = st.text_input("What do you want to research?", placeholder="e.g., The future of solid-state batteries")

if st.button("Generate Report", type="primary"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner(f"Agents are researching '{topic}'... This takes about 30-60 seconds."):
            try:
                # Run the crew
                report = run_research(topic)
                
                st.success("Research Complete!")
                
                # Display the report
                st.markdown("---")
                st.markdown(report)
                
                # Add a download button
                st.download_button(
                    label="📥 Download Report as Markdown",
                    data=str(report),
                    file_name=f"research_{topic.replace(' ', '_')}.md",
                    mime="text/markdown"
                )
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

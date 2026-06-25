import streamlit as st
from agents import run_research
import os

# Set up sleek page configuration (collapsed sidebar by default)
st.set_page_config(
    page_title="Agentic Deep Researcher", 
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Premium CSS Styling
st.markdown("""
    <style>
        /* Main background and font styling */
        .main {
            background-color: #0d1117;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        
        /* Modern Header styling */
        .header-title {
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(45deg, #1f6feb, #58a6ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.2rem;
        }
        .header-subtitle {
            color: #8b949e;
            font-size: 1rem;
            margin-bottom: 2rem;
        }
        
        /* Chat Input Adjustment */
        .stChatInputContainer {
            padding-bottom: 20px;
        }
        
        /* Clean divider line */
        hr {
            border-top: 1px solid #30363d;
            margin-top: 10px;
            margin-bottom: 25px;
        }
        
        /* Hide sidebar toggle if it completely empty */
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state variables safely
if "messages" not in st.session_state:
    st.session_state.messages = []

def reset_chat():
    st.session_state.messages = []

# --- MAIN INTERFACE ---
# Title Header with gradient effect
col1, col2 = st.columns([6, 1])
with col1:
    st.markdown('<div class="header-title">🔍 Agentic Deep Researcher</div>', unsafe_allow_html=True)
    st.markdown('<div class="header-subtitle">Powered by DeepSeek-R1 local models and Linkup internet intelligence agents</div>', unsafe_allow_html=True)
with col2:
    # Placed the clear action natively on the main view dashboard to keep layout functional
    st.button("Clear History ↺", on_click=reset_chat, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Display active chat layout
if not st.session_state.messages:
    # Onboarding view
    with st.container():
        st.markdown("""
        <div style='background-color: #161b22; padding: 30px; border-radius: 12px; border: 1px solid #30363d; margin-top: 20px;'>
            <h4 style='color: #c9d1d9; margin-top: 0;'>Welcome to the Deep Research Assistant!</h4>
            <p style='color: #8b949e; font-size: 0.95rem;'>
                This application coordinates local reasoning models with real-time web execution graphs to provide complex, exhaustive answers.
            </p>
            <ul style='color: #8b949e; font-size: 0.9rem; padding-left: 20px;'>
                <li>Deep multi-tier web searches and information extraction</li>
                <li>Comprehensive cross-referencing and objective verification</li>
                <li>Markdown formatted dynamic reports with full structures</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

else:
    # Display message components sequentially
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Accept user prompt and process
if prompt := st.chat_input("Enter your research objective or query here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Validate that system variable is set before executing
    if not os.environ.get("LINKUP_API_KEY", ""):
        response = "⚠️ **Configuration Error:** Please ensure the `LINKUP_API_KEY` environment variable is exported in your terminal before running the application."
    else:
        with st.spinner("🤖 Coordinating agents and researching internet data... Please wait..."):
            try:
                result = run_research(prompt)
                response = result
            except Exception as e:
                response = f"❌ **An execution error occurred:** `{str(e)}`"

    with st.chat_message("assistant"):
        st.markdown(response)
        
    st.session_state.messages.append({"role": "assistant", "content": response})
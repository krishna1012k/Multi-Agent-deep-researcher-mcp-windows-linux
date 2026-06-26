import os
import streamlit as st
from agents import run_research

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Agentic Deep Researcher",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS STYLING ---
st.markdown("""
    <style>
        /* Dark theme backgrounds */
        .stApp {
            background-color: #0d1117;
            color: #c9d1d9;
        }
        
        /* Header styling */
        .header-title {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(45deg, #1f6feb, #58a6ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            padding-bottom: 20px;
        }
        
        /* Clean divider line */
        hr {
            border-top: 1px solid #30363d;
            margin-top: 10px;
            margin-bottom: 25px;
        }
        
        /* Hide sidebar toggle if completely empty */
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
with col2:
    st.button("Clear History ↺", on_click=reset_chat, use_container_width=True)

st.markdown("##### Powered by DeepSeek-R1 local models and Linkup internet intelligence agents")
st.markdown("---")

# --- CONFIGURATION & API CHECK ---
# Check Streamlit secrets first, then fall back to terminal environment variables
linkup_key = st.secrets.get("LINKUP_API_KEY") or os.environ.get("LINKUP_API_KEY")

if not linkup_key:
    st.error("⚠️ Configuration Error: Please ensure the LINKUP_API_KEY environment variable is exported or added to Streamlit secrets.")
    st.stop()
else:
    # Ensure it's injected into the environment so underlying agents can find it
    os.environ["LINKUP_API_KEY"] = linkup_key

# --- CHAT HISTORY DISPLAY ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- USER INPUT & AGENT COORDINATION ---
if prompt := st.chat_input("Enter your research objective or query here..."):
    # Accept user prompt and process
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.spinner("🤖 Coordinating agents and researching internet data... Please wait..."):
        try:
            # Execute the research pipeline via agents.py logic
            result = run_research(prompt)
            response = result
        except Exception as e:
            response = f"❌ **An execution error occurred:** `{str(e)}`"
            
    with st.chat_message("assistant"):
        st.markdown(response)
        
    st.session_state.messages.append({"role": "assistant", "content": response})
import streamlit as st

# MUST be the first Streamlit command
st.set_page_config(page_title="AI Data Agent V2 (Chat UI)", layout="wide")

st.title("🤖 AI Data Agent - Chat UI (v2)")

# ------------------------------- 
# Context Toggle (NEW) 
# ------------------------------- 
use_context = st.toggle("🧠 Use Conversation Context", value=True)

# ------------------------------- 
# Session State (Chat History) 
# ------------------------------- 
if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------------------- 
# Lazy Load Agent 
# ------------------------------- 
@st.cache_resource 
def get_agent():
    from app.agents.orchestrator_agent import OrchestratorAgent
    return OrchestratorAgent()

agent = get_agent()

# ------------------------------- 
# Display Chat History 
# ------------------------------- 
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ------------------------------- 
# Chat Input 
# ------------------------------- 
user_input = st.chat_input("Ask your data question...")

if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user", 
        "content": user_input
    })
    
    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    # Get response
    with st.spinner("Thinking..."):
        if use_context:
            # Pass history if context is enabled
            response = agent.route(user_input, chat_history=st.session_state.messages)
        else:
            # Route without context
            response = agent.route(user_input)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant", 
        "content": response
    })
    
    # Show assistant response
    with st.chat_message("assistant"):
        st.write(response)
import streamlit as st

# ✅ MUST be first Streamlit command
st.set_page_config(page_title="AI Data Agent", layout="wide")

st.title("🤖 AI Data Agent")

# ✅ Lazy load orchestrator (IMPORTANT FIX)
@st.cache_resource
def get_agent():
    from app.agents.orchestrator_agent import OrchestratorAgent
    return OrchestratorAgent()

agent = get_agent()

# Input
user_query = st.text_input("Ask your data question:")

if st.button("Run Agent"):
    if user_query:
        with st.spinner("Thinking..."):
            # This line must be indented to stay inside the spinner block
            result = agent.route(user_query)

        # These lines must be indented to stay inside the 'if st.button' block
        st.subheader("💡 Response")
        st.write(result)
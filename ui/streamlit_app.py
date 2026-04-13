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

def detect_agent(query: str) -> str:
    query_lower = query.lower()

    if any(keyword in query_lower for keyword in [
        "job", "retry", "fail", "error", "log"
    ]):
        return "Tool Agent"
    else:
        return "RAG Agent"
    
# Input
user_query = st.text_input("Ask your data question:")

if st.button("Run Agent"):
    if user_query:
        agent_type = detect_agent(user_query)

        with st.spinner("Thinking..."):
            result = agent.route(user_query)

        st.subheader("🧭 Routed Agent")
        st.write(agent_type)

        st.subheader("💡 Response")
        st.write(result)
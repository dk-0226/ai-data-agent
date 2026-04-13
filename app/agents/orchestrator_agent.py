"""
Module: orchestrator_agent.py

Purpose:
--------
This module acts as the central brain of the AI system.

It combines:
1. Tool-based Agent (LangChain)  → for operational workflows
2. RAG-based Agent               → for data intelligence

Why this design?
----------------
- Keeps agents independent (modular design)
- Enables scalability (can add more agents later)
- Maintains backward compatibility (existing code untouched)

Flow:
-----
User Query
   ↓
Orchestrator decides:
   ├── Tool Agent → for actions (retry jobs, logs, failures)
   └── RAG Agent  → for data-related queries

Future Enhancements:
-------------------
- Replace rule-based routing with LLM-based routing
- Add memory-aware routing
- Add multiple domain-specific agents
"""

# -------------------------------
# Imports
# -------------------------------
from app.agents.data_agent import run_agent  # Existing tool-based agent
from app.agents.rag_agent import RAGAgent


class OrchestratorAgent:
    """
    Orchestrator that routes queries to appropriate agents.
    """

    def __init__(self):
        """
        Initialize both agents.

        NOTE:
        - Tool Agent is function-based (run_agent)
        - RAG Agent is class-based
        """

        print("🚀 Initializing Orchestrator...")

        # Initialize RAG Agent
        self.rag_agent = RAGAgent("app/data_lake/silver/data.parquet")

        print("✅ Orchestrator Ready")

    def route(self, query: str) -> str:
        """
        Route query to appropriate agent.

        Parameters:
        -----------
        query : str
            User query

        Returns:
        --------
        str
            Response from selected agent
        """

        query_lower = query.lower()

        # -------------------------------
        # Rule-Based Routing Logic
        # -------------------------------
        # Tool Agent → operational queries
        if any(keyword in query_lower for keyword in [
            "job", "retry", "fail", "error", "log"
        ]):
            print(" Routing to Tool Agent...")
            
            # Existing tool agent does not take query dynamically
            # It runs a predefined task
            return run_agent()

        # -------------------------------
        # RAG Agent → data queries
        # -------------------------------
        else:
            print("📊 Routing to RAG Agent...")
            return self.rag_agent.answer(query)
"""
Module: rag_agent.py

Purpose:
--------
Handles data related queries using Retrieval Augmented Generation.

This agent:
- Retrieves relevant data using embeddings + FAISS
- Uses LLM to generate intelligent responses
"""

import os
from openai import OpenAI

from app.rag.retriever import Retriever

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

class RAGAgent:
    def __init__(self, data_path: str):
        self.retriever = Retriever(data_path)
        self.retriever.prepare_embeddings()
        print("Preparing embeddings...")
        self.retriever.prepare_embeddings()
        print("RAG ready")
    
    def answer(self, query: str) -> str:
        results = self.retriever.retrieve(query)
        context = "\n".join([str(r) for r in results])
        prompt = f"""
You are a data analyst.
Use the following data:
{context}
Answer:
{query}
"""
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
                {"role" : "system", "content": "You are a helpful data analyst."},
                {"role" : "user", "content" : prompt}
            ],
            temperature = 0.2
        )
        return response.choices[0].message.content
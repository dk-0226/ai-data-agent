"""
Module: retriever.py

Purpose:
--------
This module connects data + embeddings + vector store.

It is responsible for:
- Preparing data (convert records to embeddings)
- Storing embeddings in vector store
- Retrieving relevant records for a query

Why is this important?
----------------------
Retriever is the core of RAG:
It ensures that the LLM gets only relevant context instead of entire dataset.

Flow:
-----
1. Load data (from silver/gold layer)
2. Convert each record → text
3. Generate embeddings
4. Store in FAISS
5. On query:
   - Convert query → embedding
   - Search FAISS
   - Return top matches
"""

import pandas as pd

from app.rag.embedder import get_embedding
from app.rag.vector_store import VectorStore


class Retriever:
    """
    Retriever class for RAG pipeline.
    """

    def __init__(self, data_path: str):
        """
        Initialize retriever with data source.
        """
        self.data_path = data_path
        self.vector_store = None

    def load_data(self):
        """
        Load dataset from parquet file.
        """
        df = pd.read_parquet(self.data_path)
        return df

    def prepare_embeddings(self):
        """
        Convert dataset into embeddings and store in FAISS.
        """

        df = self.load_data()   # ✅ FIXED

        # Convert each row into text format
        records = df.to_dict(orient="records")
        texts = [str(record) for record in records]

        # Generate embeddings
        embeddings = [get_embedding(text) for text in texts]

        # Initialize vector store
        dimension = len(embeddings[0])
        self.vector_store = VectorStore(dimension)   # ✅ FIXED

        # Store embeddings
        self.vector_store.add_embeddings(embeddings, records)

    def retrieve(self, query: str, top_k: int = 3):
        """
        Retrieve relevant records for a given query.
        """

        if self.vector_store is None:
            raise ValueError("Embeddings not prepared. Call prepare_embeddings() first.")

        # Convert query to embedding
        query_embedding = get_embedding(query)

        # Search in vector store
        results = self.vector_store.search(query_embedding, top_k)

        return results
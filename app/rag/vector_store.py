"""
Module: vector_store.py

Purpose:
--------
Stores embeddings using FAISS for fast similarity search.

Responsibilities:
- Initialize FAISS index
- Add embeddings with metadata
- Perform similarity search
"""

import faiss
import numpy as np


class VectorStore:
    """
    FAISS-based vector store
    """

    def __init__(self, dimension: int):
        """
        Initialize FAISS index
        """
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.records = []  # Store original data

    def add_embeddings(self, embeddings, records):
        """
        Add embeddings to FAISS index
        """

        vectors = np.array(embeddings).astype("float32")

        self.index.add(vectors)
        self.records.extend(records)

    def search(self, query_embedding, top_k=3):
        """
        Search similar embeddings
        """

        query_vector = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_vector, top_k)

        results = []
        for idx in indices[0]:
            if idx < len(self.records):
                results.append(self.records[idx])

        return results
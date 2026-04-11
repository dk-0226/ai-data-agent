"""
Module: embedder.py

Purpose:
--------
This module is responsible for converting text into numerical vectors (embeddings)
using OpenAI embedding models.

Why Embeddings?
---------------
Machine learning models and vector databases cannot understand raw text.
So we convert text into vectors (lists of numbers) that capture semantic meaning.

Example:
--------
"High value transaction" ≈ "Large transaction"

Both will have similar embeddings → enabling similarity search.

Used In:
--------
- Query embedding (user input)
- Data embedding (stored records)
- Semantic search (RAG pipeline)
"""

import os
from openai import OpenAI

# Initialize OpenAI client using API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_embedding(text: str) -> list:
    """
    Generate embedding for given text.

    Parameters:
    -----------
    text : str
        Input text that needs to be converted into vector representation

    Returns:
    --------
    list
        A high-dimensional vector representing the semantic meaning of the text

    Example:
    --------
    Input: "High value transaction"
    Output: [0.12, -0.44, 0.98, ...]

    Notes:
    ------
    - Uses OpenAI embedding model
    - This vector is later used in similarity search (FAISS)
    """

    # Call OpenAI embedding API
    response = client.embeddings.create(
        model="text-embedding-3-small",  # fast + cost-effective model
        input=text
    )

    # Extract embedding vector
    embedding = response.data[0].embedding

    return embedding
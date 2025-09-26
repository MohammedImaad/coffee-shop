import chromadb
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

persist_directory = "../data/vector_store"
collection_name = "pdf_documents"
client = chromadb.PersistentClient(path=persist_directory)
collection = client.get_collection(name=collection_name)

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_answer(query_text):
    query_embedding = model.encode([query_text]) 
    results = collection.query(
        query_embeddings=query_embedding.tolist(),  
        n_results=3
    )
    context=results["documents"][0]
    return context


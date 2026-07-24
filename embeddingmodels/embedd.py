from langchain_community.embeddings import HuggingFaceEmbeddings
embedding_model=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
sentence=[
    "I love machine learning",
    "sentence Transformers are useful for semantic search.",
    "Natural language processing is fascinating."
]
embeddings=embedding_model.embed_documents(sentence)
print(len(embeddings))
print(len(embeddings[0]))
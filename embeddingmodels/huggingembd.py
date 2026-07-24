from langchain_huggingface import HuggingFaceEmbeddings
embedding=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
texts=["hello this is Jayaprakash",
       "hello your name is youtube",
       "and you all are my fav"
       ]
vector=embedding.embed_documents(texts)
print(vector)
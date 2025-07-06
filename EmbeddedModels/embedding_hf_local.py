from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "AI is the broader concept of machines being able to carry out tasks in a way that we would consider “smart.”",
    "ML is a subset of AI that enables machines to learn from data and improve their performance without being explicitly programmed.",
    "DL is a specialized subset of ML that uses neural networks with many layers to model complex patterns in large datasets."
]

vector = embedding.embed_documents(documents)

print(str(vector))
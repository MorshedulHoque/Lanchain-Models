from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "AI is the broader concept of machines being able to carry out tasks in a way that we would consider “smart.”",
    "ML is a subset of AI that enables machines to learn from data and improve their performance without being explicitly programmed.",
    "DL is a specialized subset of ML that uses neural networks with many layers to model complex patterns in large datasets."
]

result = embedding.embed_documents(documents)

print(str(result))
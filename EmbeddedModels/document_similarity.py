from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "AI is the broader concept of machines being able to carry out tasks in a way that we would consider “smart.”",
    "ML is a subset of AI that enables machines to learn from data and improve their performance without being explicitly programmed.",
    "DL is a specialized subset of ML that uses neural networks with many layers to model complex patterns in large datasets."
]


query = 'tell me about DL'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)
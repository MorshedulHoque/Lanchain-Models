from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="tiiuae/falcon-7b-instruct",  # or google/flan-t5-small
    task="text-generation",
    huggingfacehub_api_token=api_key
)

response = llm.invoke("What is the capital of France?")
print(response)

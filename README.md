# LangChain: ChatModels and EmbeddingModels

LangChain is a powerful framework that simplifies the creation of applications using large language models (LLMs). It provides modular components to build intelligent, context-aware systems such as chatbots, document Q&A tools, and more.

This document covers two key components of LangChain:

- **ChatModels** – for conversational interaction with LLMs  
- **EmbeddingModels** – for transforming text into vector representations

---

## 🔹 ChatModels

**ChatModels** are used to interact with language models through a conversational interface. They are ideal for building chatbots, agents, and any system that requires natural, back-and-forth communication.

### 🧩 Types of ChatModels

#### 1. Open Source ChatModels
- Examples: `LLaMA`, `Mistral`, `phi-2`, `ChatGLM`
- Can be self-hosted and fine-tuned
- Useful for custom applications or offline use

#### 2. Closed Source ChatModels
- Examples: `GPT-3.5`, `GPT-4`, `Claude`, `Gemini`
- Accessed via APIs from providers like OpenAI, Anthropic, Google
- Known for powerful performance and ease of use

### 🧪 Example Usage

```python
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(temperature=0)
response = chat.predict("What is LangChain?")
print(response)
```

---

## 🔹 EmbeddingModels

**EmbeddingModels** are used to convert text into numerical vector representations. These embeddings capture semantic meaning and are essential for tasks like similarity search, retrieval, clustering, and document ranking.

### 🧩 Types of EmbeddingModels

#### 1. Open Source EmbeddingModels
- Examples: `all-MiniLM`, `GTE`, `Instructor`, `BGE`
- Run locally and are free to use
- Suitable for privacy-focused or low-cost deployments

#### 2. Closed Source EmbeddingModels
- Examples: `text-embedding-ada-002` (OpenAI), `Cohere`, `VertexAI Embeddings`
- Require API access via providers
- Offer strong performance and integration with cloud ecosystems

### 🧪 Example Usage

```python
from langchain.embeddings import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings()
vector = embedding_model.embed_query("LangChain enables LLM-powered applications.")
print(vector)
```

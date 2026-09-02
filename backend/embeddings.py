from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_embedding(val: str) -> list[float]:
    embeddings = client.embeddings.create(input=val, model="nomic-embed-text-v1_5")
    return embeddings.data[0].embedding

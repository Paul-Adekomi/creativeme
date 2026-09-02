import ollama


def get_embedding(val: str) -> list[float]:
    embeddings = ollama.embed(input=val, model="nomic-embed-text:latest")
    return embeddings.embeddings[0]

import json
from embeddings import get_embedding

with open("profilesData/profiles.json", "r") as f:
    profiles = json.load(f)

    for profile in profiles:
        words = (
            profile["title"] + " " + profile["category"] + " " + profile["description"]
        )
        result = get_embedding(words)
        profile["embedding"] = result
with open("profilesData/profiles.json", "w") as f:
    json.dump(profiles, f)

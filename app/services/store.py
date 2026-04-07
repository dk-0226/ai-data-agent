import json
import os

def save_memory(data):
    os.makedirs("app/memory", exist_ok=True)

    with open("app/memory/history.json", "a") as f:
        f.write(json.dumps(data) + "\n")
import json

def save_memory(data):
    with open("memory/history.json","a") as f:
        f.write(json.dumps(data) + "\n")
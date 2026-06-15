import json

# Save data to file
data = {"username": "admin", "password": "123"}
with open("users.json", "w") as f:
    json.dump(data, f)

# Read it back
with open("users.json", "r") as f:
    loaded = json.load(f)
    print("Loaded:", loaded)

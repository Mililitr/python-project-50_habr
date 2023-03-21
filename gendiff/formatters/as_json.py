import json

data = {
    "Ducks": ["added", "Are cool creatures"],
    "I_like": ["added", "big ducks and I cannot lie"],
    "author": [
        "deleted",
        {
            "name": "Duck",
            "email": "duck@example.com (this is a fake email)",
        },
    ],
    "favorite_color": ["added", "yellow"],
    "language": ["deleted", "Why Python? Why not Sssssssssssnake+?"],
    "number_of_ducks": ["added", 99],
    "repository": ["deleted", "myrepo (not to be confused with trash)"],
    "version": ["deleted", "3.8 (eat five)"],
}

json_output = json.dumps(data, indent=2)
print(json_output)

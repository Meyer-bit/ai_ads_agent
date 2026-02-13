import json

def save_decisions(decisions):
    with open("outputs/decisions.json", "w") as f:
        json.dump(decisions, f, indent=2)

    return True
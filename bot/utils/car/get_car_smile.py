import random


def get_car_smile() -> str:
    smiles = ["🚕", "🚖", "🚗", "🚘", "🚙", "🛻", "🏎️"]
    return random.choice(smiles)

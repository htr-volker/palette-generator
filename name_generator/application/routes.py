from application import app
import random
from flask import jsonify

@app.route('/name', methods=['GET'])
def generate_name():
    words = [
        "Cerulean", "Lavender", "Azure", "Sky", "Crab", "Jungle", "Wave", "Dream", "Grey", "Night", "Garden",
        "Vanta", "Malta", "Christmas", "Tea", "Green", "Yellow", "Muse", "Blossom", "Sunset", "Day", "Hour",
        "Minute", "Calm", "Coffee", "Whiskey", "Grass", "Red", "Aloe", "Russet", "Rust", "Tree", "Despair",
        "Sleep", "Candle", "Trite", "Kale", "Jaffa", "Vera", "Terra", "Agave", "Plant", "Reality", "Tear",
        "Story", "Mountain", "Dusk", "Fountain", "Foundation", "Twilight", "Snow", "Rain", "Sun", "Wood"
    ]

    palette_name = { "name" : [random.choice(words)] }
    
    if random.randint(0,10) > 1:
        palette_name["name"].append(random.choice(words))
        if random.randint(0,10) == 0: 
            palette_name["name"].append(random.choice(words))

    return jsonify(palette_name)

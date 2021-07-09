from application import app
from random import randint
from flask import jsonify

@app.route('/palette', methods=['GET'])
def generate_palette():
    num_of_colours = randint(3,5)
    palette = { "palette" : [] }
    for _ in range(num_of_colours):
        colour = []
        for _ in range(3):
            colour.append(randint(0,255))
        palette["palette"].append(colour)
    
    return jsonify(palette)

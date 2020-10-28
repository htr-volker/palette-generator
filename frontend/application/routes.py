from application import app
from flask import render_template, url_for, redirect, request
import requests

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html", title="Home")

@app.route('/palette', methods=['GET', 'POST'])
def get_palette():
    if request.method == "GET":
        return redirect(url_for("home"))
    palette = requests.get("http://colour-generator:5001/palette")
    palette_rgb = []
    for colour in palette.json()["palette"]:
        palette_rgb.append(f"({colour[0]}, {colour[1]}, {colour[2]})")
    name = requests.get("http://name-generator:5002/name")
    name = " ".join(name.json()["name"])
    return render_template("index.html", title=name, palette=palette_rgb)

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html", title="About")

    
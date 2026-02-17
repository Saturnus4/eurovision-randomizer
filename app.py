from flask import Flask, render_template, redirect, session
import json
import random

app = Flask(__name__)
app.secret_key = "secretkey"

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "songs.json")

with open(json_path, "r", encoding="utf-8") as f:
    songs = json.load(f)

def calculate_weight(song):
    weight = song["base"]

    if song["ranking"] <= 3:
        weight += 10
    elif song["ranking"] <= 10:
        weight += 5
    elif song["ranking"] <= 26:
        weight += 2

    weight += song["personal_bonus"]

    return weight

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate")
def generate():
    weights = [calculate_weight(song) for song in songs]
    selected = random.choices(songs, weights=weights, k=1)[0]
    session["song"] = selected
    # Redirect to the embedded video page instead
    return render_template("play.html", song=selected)

@app.route("/reveal")
def reveal():
    song = session.get("song")
    return render_template("reveal.html", song=song)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

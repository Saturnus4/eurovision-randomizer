from flask import Flask, render_template, session, request
import random

app = Flask(__name__)
app.secret_key = "secretkey"

# -------------------------------------------
# Songs list (Java-style)
# Format: ("description string", total_weight, youtube_link)
# Copy-paste new songs here
# ------------------------------------------


Pohja = 5
Finaali = 5
Top10 = 7
Top3 = 9
Suosikki = 6
Suosikkitop = 4
Extra = 9


songs = [
    ("Wasted Love \nMaa: Austria\nVuosi: 2025 \nSija: Top3, 1", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=onOex2WXjbA"),
    ("New Day Will Rise \nMaa: Israel\nVuosi: 2025 \nSija: Top3, 2", Pohja + Top3, "https://www.youtube.com/watch?v=_7zHp51j2WM&list=RD_7zHp51j2WM&start_radio=1"),
    ("Espresso Macchiato \nMaa: Estonia\nVuosi: 2025 \nSija: Top3, 3", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=F3wsy8bywXQ&list=RDF3wsy8bywXQ&start_radio=1"),
    ("Code \nMaa: Switzerland\nVuosi: 2024 \nSija: Top3, 1", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=CO_qJf-nW0k&list=RDCO_qJf-nW0k&start_radio=1"),

]

# -------------------------------------------
# Routes
# -------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate")
def generate():
    # Weighted random choice
    weights = [song[1] for song in songs]
    selected = random.choices(songs, weights=weights, k=1)[0]

    description, weight, youtube_link = selected
    session["song"] = {"description": description, "youtube": youtube_link}

    # Optional: detect mobile for separate YouTube link if you want
    user_agent = request.headers.get('User-Agent', "")

    return f'''
        <script>
            window.open("{youtube_link}", "_blank");
            window.location.href = "/reveal";
        </script>
    '''


@app.route("/reveal")
def reveal():
    song = session.get("song")
    return render_template("reveal.html", song=song)


# -------------------------------------------
# Run the app
# -------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



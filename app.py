from flask import Flask, render_template, session, request
import random

app = Flask(__name__)
app.secret_key = "secretkey"

# -------------------------------------------
# git add .
# git commit -m "Test1"
# git push origin master
# ------------------------------------------


Pohja = 5
Finaali = 5
Top10 = 7
Top3 = 9
Suosikki = 6
Suosikkitop = 4
Extra = 9


songs = [
("Wasted Love \nMaa: Austria\nVuosi: 2025 \nSija: Top3, 1", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=onOex2WXjbA&list=RDonOex2WXjbA&start_radio=1"),
("New Day Will Rise \nMaa: Israel\nVuosi: 2025 \nSija: Top3, 2", Pohja + Top3, "https://www.youtube.com/watch?v=_7zHp51j2WM&list=RD_7zHp51j2WM&start_radio=1"),
("Espresso Macchiato \nMaa: Estonia\nVuosi: 2025 \nSija: Top3, 3", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=F3wsy8bywXQ&list=RDF3wsy8bywXQ&start_radio=1"),
("Code \nMaa: Switzerland\nVuosi: 2024 \nSija: Top3, 1", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=CO_qJf-nW0k&list=RDCO_qJf-nW0k&start_radio=1"),
("Rim Tim Tagi Dim \nMaa: Croatia\nVuosi: 2024 \nSija: Top3, 2", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=YIBjarAiAVc&list=RDYIBjarAiAVc&start_radio=1"),
("Teresa & Maria \nMaa: Ukraine\nVuosi: 2024 \nSija: Top3, 3", Pohja + Top3, "https://www.youtube.com/watch?v=d4N82wPpdg8&list=RDd4N82wPpdg8&start_radio=1"),
("Tattoo \nMaa: Sweden\nVuosi: 2023 \nSija: Top3, 1", Pohja + Top3, "https://www.youtube.com/watch?v=BE2Fj0W4jP4&list=RDBE2Fj0W4jP4&start_radio=1"),
("Cha Cha Cha \nMaa: Finland\nVuosi: 2023 \nSija: Top3, 2", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=l6rS8Dv5g-8&list=RDl6rS8Dv5g-8&start_radio=1"),
("Unicorn \nMaa: Israel\nVuosi: 2023 \nSija: Top3, 3", Pohja + Top3, "https://www.youtube.com/watch?v=Z3mIcCllJXY&list=RDZ3mIcCllJXY&start_radio=1"),
("Stefania \nMaa: Ukraine\nVuosi: 2022 \nSija: Top3, 1", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=F1fl60ypdLs&list=RDF1fl60ypdLs&start_radio=1"),
("Space Man \nMaa: United Kingdom\nVuosi: 2022 \nSija: Top3, 2", Pohja + Top3, "https://www.youtube.com/watch?v=RZ0hqX_92zI&list=RDRZ0hqX_92zI&start_radio=1"),
("SloMo \nMaa: Spain\nVuosi: 2022 \nSija: Top3, 3", Pohja + Top3, "https://www.youtube.com/watch?v=jSQYTt4xg3I&list=RDjSQYTt4xg3I&start_radio=1"),
("Zitti e buoni \nMaa: Italy\nVuosi: 2021 \nSija: Top3, 1", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=RVH5dn1cxAQ&list=RDRVH5dn1cxAQ&start_radio=1"),
("Voilà \nMaa: France\nVuosi: 2021 \nSija: Top3, 2", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=3kiyXRhIXWU&list=RD3kiyXRhIXWU&start_radio=1"),
("Tout l'univers \nMaa: Switzerland\nVuosi: 2021 \nSija: Top3, 3", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=jznH_fltcYA&list=RDjznH_fltcYA&start_radio=1"),
("Arcade \nMaa: Netherlands\nVuosi: 2019 \nSija: Top3, 1", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=R3D-r4ogr7s&list=RDR3D-r4ogr7s&start_radio=1"),
("Soldi \nMaa: Italy\nVuosi: 2019 \nSija: Top3, 2", Pohja + Top3, "https://www.youtube.com/watch?v=M-aoyPa41Ic&list=RDM-aoyPa41Ic&start_radio=1"),
("Scream \nMaa: Russia\nVuosi: 2019 \nSija: Top3, 3", Pohja + Top3, "https://www.youtube.com/watch?v=eNzlxEZ_JG4&list=RDeNzlxEZ_JG4&start_radio=1"),
("Toy \nMaa: Israel\nVuosi: 2018 \nSija: Top3, 1", Pohja + Top3, "https://www.youtube.com/watch?v=84LBjXaeKk4&list=RD84LBjXaeKk4&start_radio=1"),
("Fuego \nMaa: Cyprus\nVuosi: 2018 \nSija: Top3, 2", Pohja + Top3, "https://www.youtube.com/watch?v=vyDTbJ4wenY&list=RDvyDTbJ4wenY&start_radio=1"),
("Nobody but You \nMaa: Austria\nVuosi: 2018 \nSija: Top3, 3", Pohja + Top3, "https://www.youtube.com/watch?v=a8Yvzo1puoE&list=RDa8Yvzo1puoE&start_radio=1"),
("Amar pelos dois \nMaa: Portugal\nVuosi: 2017 \nSija: Top3, 1", Pohja + Top3, "https://www.youtube.com/watch?v=Qotooj7ODCM&list=RDQotooj7ODCM&start_radio=1"),
("Beautiful Mess \nMaa: Bulgaria\nVuosi: 2017 \nSija: Top3, 2", Pohja + Top3, "https://www.youtube.com/watch?v=OMmm-G078LM&list=RDOMmm-G078LM&start_radio=1"),
("Hey Mamma \nMaa: Moldova\nVuosi: 2017 \nSija: Top3", Pohja + Top3, "https://www.youtube.com/watch?v=SWaQdHoCvYk&list=RDSWaQdHoCvYk&start_radio=1"),
("1944 \nMaa: Ukraine\nVuosi: 2016 \nSija: Top3, 1", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=B-rnM-MwRHY&list=RDB-rnM-MwRHY&start_radio=1"),
("Sound of Silence \nMaa: Australia\nVuosi: 2016 \nSija: Top3, 2", Pohja + Top3, "https://www.youtube.com/watch?v=5ymFX91HwM0&list=RD5ymFX91HwM0&start_radio=1"),
("You Are the Only One \nMaa: Russia\nVuosi: 2016 \nSija: Top3, 3", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=e94dst20C9Y&list=RDe94dst20C9Y&start_radio=1"),
("Heroes \nMaa: Sweden\nVuosi: 2015 \nSija: Top3, 1", Pohja + Top3, "https://www.youtube.com/watch?v=5sGOwFVUU0I&list=RD5sGOwFVUU0I&start_radio=1"),
("A Million Voices \nMaa: Russia\nVuosi: 2015 \nSija: Top3, 2", Pohja + Top3, "https://www.youtube.com/watch?v=Q2gbKglCL5s&list=RDQ2gbKglCL5s&start_radio=1"),
("Grande amore \nMaa: Italy\nVuosi: 2015 \nSija: Top3, 3", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=1TOMqZV2jA8&list=RD1TOMqZV2jA8&start_radio=1"),
("Rise Like a Phoenix \nMaa: Austria\nVuosi: 2014 \nSija: Top3, 1", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=SaolVEJEjV4&list=RDSaolVEJEjV4&start_radio=1"),
("Calm After the Storm \nMaa: Netherlands\nVuosi: 2014 \nSija: Top3, 2", Pohja + Top3, "https://www.youtube.com/watch?v=bWe8PRsW4T0&list=RDbWe8PRsW4T0&start_radio=1"),
("Undo \nMaa: Sweden\nVuosi: 2014 \nSija: Top3, 3", Pohja + Top3, "https://www.youtube.com/watch?v=5PQJI-3LW-8&list=RD5PQJI-3LW-8&start_radio=1"),
("Only Teardrops \nMaa: Denmark\nVuosi: 2013 \nSija: Top3, 1", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=k59E7T0H-Us&list=RDk59E7T0H-Us&start_radio=1"),
n("Hold Me \nMaa: Azerbaijan\nVuosi: 2013 \nSija: Top3, 2", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=iN3d_V7KVLE&list=RDiN3d_V7KVLE&start_radio=1"),
("Gravity \nMaa: Ukraine\nVuosi: 2013 \nSija: Top3, 3", Pohja + Top3, "https://www.youtube.com/watch?v=Eo5H62mCIsg&list=RDEo5H62mCIsg&start_radio=1"),
("Euphoria \nMaa: Sweden\nVuosi: 2012 \nSija: Top3, 1", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=Pfo-8z86x80&list=RDPfo-8z86x80&start_radio=1"),
("Party for Everybody \nMaa: Russia\nVuosi: 2012 \nSija: Top3, 2", Pohja + Top3, "https://www.youtube.com/watch?v=BgUstrmJzyc&list=RDBgUstrmJzyc&start_radio=1"),
("Nije ljubav stvar \nMaa: Serbia\nVuosi: 2012 \nSija: Top3, 3", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=R9x9VbJzaDQ&list=RDR9x9VbJzaDQ&start_radio=1"),
("Running Scared \nMaa: Azerbaijan\nVuosi: 2011 \nSija: Top3, 1", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=_0tlQUW5X0U&list=RD_0tlQUW5X0U&start_radio=1"),
("Madness of Love \nMaa: Italy\nVuosi: 2011 \nSija: Top3, 2", Pohja + Top3, "https://www.youtube.com/watch?v=TE0uNLp3LuU&list=RDTE0uNLp3LuU&start_radio=1"),
("Popular \nMaa: Sweden\nVuosi: 2011 \nSija: Top3, 3", Pohja + Top3, "https://www.youtube.com/watch?v=-04pUETT7oI&list=RD-04pUETT7oI&start_radio=1"),
("Satellite \nMaa: Germany\nVuosi: 2010 \nSija: Top3, 1", Pohja + Top3, "https://www.youtube.com/watch?v=7pL9vdpSvnY&list=RD7pL9vdpSvnY&start_radio=1"),
("We Could Be the Same \nMaa: Turkey\nVuosi: 2010 \nSija: Top3, 2", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=HB_GnnhNz-8&list=RDHB_GnnhNz-8&start_radio=1"),
("Playing with Fire \nMaa: Romania\nVuosi: 2010 \nSija: Top3, 3", Pohja + Top3 + Suosikkitop, "https://www.youtube.com/watch?v=J9EtMZXeQZw&list=RDJ9EtMZXeQZw&start_radio=1"),
("Fairytale \nMaa: Norway\nVuosi: 2009 \nSija: Top3, 1", Pohja + Top3, "https://www.youtube.com/watch?v=WXwgZL4zx9o&list=RDWXwgZL4zx9o&start_radio=1"),
("Believe \nMaa: Russia\nVuosi: 2008 \nSija: Top3, 1", Pohja + Top3, "https://www.youtube.com/watch?v=-72s4WzUcKI&list=RD-72s4WzUcKI&start_radio=1"),
("Molitva \nMaa: Serbia\nVuosi: 2007 \nSija: Top3, 1", Pohja + Top3, "https://www.youtube.com/watch?v=FSueQN1QvV4&list=RDFSueQN1QvV4&start_radio=1"),
("Dancing Lasha Tumbai \nMaa: Ukraine\nVuosi: 2007 \nSija: Top3, 2", Pohja + Top3, "https://www.youtube.com/watch?v=hfjHJneVonE&list=RDhfjHJneVonE&start_radio=1"),
("Hard Rock Hallelujah \nMaa: Finland\nVuosi: 2006 \nSija: Top3, 1", Pohja + Top3, "https://www.youtube.com/watch?v=gAh9NRGNhUU&list=RDgAh9NRGNhUU&start_radio=1")

]

# -------------------------------------------
# Routes
# -------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


from flask import redirect

@app.route("/generate")
def generate():
    weights = [song[1] for song in songs]
    selected = random.choices(songs, weights=weights, k=1)[0]

    description, weight, youtube_link = selected
    session["song"] = {"description": description, "youtube": youtube_link}

    return redirect("/reveal")



@app.route("/reveal")
def reveal():
    song = session.get("song")
    return render_template("reveal.html", song=song)


# -------------------------------------------
# Run the app
# -------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



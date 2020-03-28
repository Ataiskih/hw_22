from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/medicallist")
def medicallist():
    lst = ["Парацетамол","Линкас", "Антигриппин", "Кавинтон", "Канефирон"]
    return render_template("medlist.html", lst = lst)

@app.route("/recommendations")
@app.route("/recommendations/<name>")
def recommendations(name = ""):
    return render_template("recommend.html", name = name)

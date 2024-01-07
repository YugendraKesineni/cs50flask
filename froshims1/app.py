from flask import Flask, render_template, request, redirect

from cs50 import SQL 

app = Flask(__name__)

db = SQL("sqlite:///froshims.db")

REGISTRANTS = {}

SPORTS = ["BasketBall", "Soccer", "Ultimate Frisbee"]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/deregister", methods=["POST"])
def deregister():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM registrants WHERE id = ?", id)
    return redirect("/registrants")

@app.route("/register", methods=["POST", "GET"])
def register():
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")
    
    for sport in request.form.getlist("sport"):
        if sport not in SPORTS:
            return render_template("failure.html")
        
    name = request.form.get("name")
    sport = request.form.get("sport")
    db.execute("INSERT INTO registrants (name,sport) VALUES (?,?)", name,sport)
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)
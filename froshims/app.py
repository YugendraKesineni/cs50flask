from flask import Flask, render_template, request

app = Flask(__name__)

REGISTRANTS = {}

SPORTS = ["BasketBall", "Soccer", "Ultimate Frisbee"]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST", "GET"])
def register():
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")
    
    for sport in request.form.getlist("sport"):
        if sport not in SPORTS:
            return render_template("failure.html")
        
    name = request.form.get("name")
    sport = request.form.get("sport")
    REGISTRANTS[name] = sport
    return render_template("registrants.html", registrants=REGISTRANTS)
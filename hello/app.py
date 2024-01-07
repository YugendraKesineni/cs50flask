from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    # if "name" in request.args:
    #     name = request.args["name"]
    # else:
    #     name = "World"
    if request.method == "POST":
        name = request.form.get("name")
        # return render_template("index.html", name=name)
        return render_template("greet.html", name=name)
    return render_template("index.html")

# @app.route("/greet", methods=["GET","POST"])
# def greet():

#     name = request.form.get("name", "world")
#     # name = request.args.get("name", "world")

#     return render_template("greet.html", name=name)
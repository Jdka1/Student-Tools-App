from flask import *

app = Flask(__name__)
app.secret_key = "abc"  


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/tools", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        flash("you are successfuly logged in")
        return render_template("base.html")
    else:
        return render_template("tools.html")



if __name__ == "__main__":
	app.run(debug=True)
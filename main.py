from flask import *

app = Flask(__name__)
app.secret_key = "abc"  


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/tools")
def tools():
    return render_template("tools.html")


@app.route("/tools/<tool>")
def tool(tool):
    return render_template(f"{tool}.html")


if __name__ == "__main__":
	app.run(debug=True)
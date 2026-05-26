from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hazards")
def hazards():
    return render_template("hazards.html")

if __name__ == "__main__":
    app.run(debug=True)